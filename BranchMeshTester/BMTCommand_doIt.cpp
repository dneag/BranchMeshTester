/*
	BMTCommand_doIt.cpp

	defines doIt() method of BMTCommand

	this is sort of a driver file for the program
	doIt() is the method called when the user executes the command "makeBranchMeshes"
*/

#include <iostream>
#include <stdlib.h>
#include <string>

#include <maya/MStreamUtils.h>
#include <maya/MArgDatabase.h>
#include <maya/MArgList.h>
#include <maya/MSyntax.h>
#include <maya/MFnDagNode.h>
#include <maya/MFloatPointArray.h>
#include <maya/MFloatPoint.h>
#include <maya/MFloatArray.h>
#include <maya/MIntArray.h>
#include <maya/MFnMesh.h>

#include "BMTCommand.h"
#include "BranchMesh.h"

namespace {

	Segment * createSegments(MStatus &status, const MArgDatabase &argData);

	std::vector<BranchMesh*> makeManyBMesh(Segment *rootSeg);

	void sendMeshesToMaya(std::vector<BranchMesh*> treeMesh);

	void checkBranches(Segment * seg, int &segIndex);
}

MStatus BMTCommand::doIt(const MArgList &argList) {

	MStatus status;

	MArgDatabase argData(syntax(), argList, &status);
	CHECK_MSTATUS_AND_RETURN_IT(status);

	Segment *rootSeg = createSegments(status, argData);

	int segIndex = 0;
	//checkBranches(rootSeg, segIndex);

	std::vector<BranchMesh*> treeMesh = makeManyBMesh(rootSeg);

	sendMeshesToMaya(treeMesh);

	return MS::kSuccess;
}

namespace {

	Segment * createSegments(MStatus &status, const MArgDatabase &argData) {

		uint totalBranches = argData.numberOfFlagUses("-spb");
		std::vector<int> segmentsPerBranch;
		std::vector<int> segIndicesOnParent;

		for (int i = 0; i < totalBranches; ++i) {

			MArgList branchArgList;
			status = argData.getFlagArgumentList("-spb", i, branchArgList);
			segmentsPerBranch.push_back(branchArgList.asInt(0, &status));

			status = argData.getFlagArgumentList("-iop", i, branchArgList);
			segIndicesOnParent.push_back(branchArgList.asInt(1, &status));
		}

		// the uses should be the same for any segment attribute flag, so those from -p should represent the length of 
		// all other incoming attribute lists
		uint segmentAttributesCount = argData.numberOfFlagUses("-p");
		std::vector<double>  pols(segmentAttributesCount);
		std::vector<double>  azis(segmentAttributesCount);
		std::vector<double>  dists(segmentAttributesCount);
		std::vector<double>  rads(segmentAttributesCount);
		std::vector<double>  offsets(segmentAttributesCount);

		for (int i = 0; i < segmentAttributesCount; ++i) {

			int argIndex = 0;
			MArgList argSegmentAttributes;

			status = argData.getFlagArgumentList("-p", i, argSegmentAttributes);
			pols[i] = argSegmentAttributes.asDouble(argIndex++, &status) * (MM::PI / 180.); // convert to radians

			status = argData.getFlagArgumentList("-a", i, argSegmentAttributes);
			azis[i] = argSegmentAttributes.asDouble(argIndex++, &status) * (MM::PI / 180.); // convert to radians

			status = argData.getFlagArgumentList("-d", i, argSegmentAttributes);
			dists[i] = argSegmentAttributes.asDouble(argIndex++, &status);

			status = argData.getFlagArgumentList("-r", i, argSegmentAttributes);
			rads[i] = argSegmentAttributes.asDouble(argIndex++, &status);

			status = argData.getFlagArgumentList("-o", i, argSegmentAttributes);
			offsets[i] = argSegmentAttributes.asDouble(argIndex++, &status);
		}

		Space worldSpace({ 0.,0. });

		// Make the first segment separately to establish its startPoint and the first meristem
		CVect rootSegVect = worldSpace.makeVector(pols[0], azis[0], dists[0]);
		Meristem *rootMeri = new Meristem(.01, 8);
		Segment *rootSeg = new Segment(rootSegVect, { 0.,0.,0. }, rads[0] + rootMeri->skinThickness, rootMeri);
		Segment *previousSeg = rootSeg;
		
		std::vector<Segment*> allNewSegs;

		// do the first branch separately because it will not have a parent segment nor offset
		for (int s = 1; s < segmentsPerBranch[0]; ++s) {

			CVect newSegVect = worldSpace.makeVector(pols[s], azis[s], dists[s]);
			Point newSegStartPoint = previousSeg->getStartPoint() + previousSeg->getVect();
			Segment *newSeg = new Segment(newSegVect, newSegStartPoint, rads[s] + rootMeri->skinThickness, rootSeg->getMeri());
			previousSeg->addSegAbove(newSeg);
			allNewSegs.push_back(newSeg);
			previousSeg = newSeg;
		}

		int branchFirstSegIndex = 0;
		branchFirstSegIndex += segmentsPerBranch[0];

		for (int bi = 1; bi < totalBranches; ++bi) {

			// This loop iterates once for each branch, with segmentsPerBranch[bi] indicating the number of segments on the branch
			// The first seg's start point is calculated from its parent seg's offset and start point, with the exception of 
			//    the first seg on the first branch. Thus we start at bi = 1

			int iop = segIndicesOnParent[bi];
			Point newSegStartPoint = allNewSegs[iop]->getStartPoint() + allNewSegs[iop]->getVect().resized(offsets[iop]);
			CVect newSegVect = worldSpace.makeVector(pols[branchFirstSegIndex], azis[branchFirstSegIndex], dists[branchFirstSegIndex]);
			Meristem *branchMeri = new Meristem(.01, 8);
			Segment *newSeg = new Segment(newSegVect, newSegStartPoint, rads[branchFirstSegIndex] + branchMeri->skinThickness, branchMeri);
			allNewSegs[iop]->addLateralSeg(newSeg);
			allNewSegs.push_back(newSeg);
			previousSeg = newSeg;

			for (int s = branchFirstSegIndex + 1; s < branchFirstSegIndex + segmentsPerBranch[bi]; ++s) {

				CVect newSegVect = worldSpace.makeVector(pols[s], azis[s], dists[s]);
				Point newSegStartPoint = previousSeg->getStartPoint() + previousSeg->getVect();
				Segment *newSeg = new Segment(newSegVect, newSegStartPoint, rads[s] + branchMeri->skinThickness, branchMeri);
				previousSeg->addSegAbove(newSeg);
				allNewSegs.push_back(newSeg);
				previousSeg = newSeg;
			}

			branchFirstSegIndex += segmentsPerBranch[bi];
		}

		return rootSeg;
	}

	std::vector<BranchMesh*> makeManyBMesh(Segment *rootSeg) {

		// treeMesh is the collection of BranchMeshes
		std::vector<BranchMesh*> treeMesh;

		std::queue<Segment*> firstSegsOfNewBMeshes;
		firstSegsOfNewBMeshes.push(rootSeg);

		// Each iteration declares a BranchMesh and the go() method completes it.  
		// The go() method also finds any segments that mark the beginning of what will be a new BranchMesh, and adds them to the queue
		while (!firstSegsOfNewBMeshes.empty()) {

			const int orderSides = firstSegsOfNewBMeshes.front()->getMeri()->sides;
			BranchMesh *bMesh = new BranchMesh(firstSegsOfNewBMeshes.front(), orderSides);
			treeMesh.push_back(bMesh);
			std::vector<double> initialPreadjusts(orderSides, 0.);
			bMesh->go(firstSegsOfNewBMeshes.front(), orderSides, initialPreadjusts, firstSegsOfNewBMeshes);
			firstSegsOfNewBMeshes.pop();
		}

		return treeMesh;
	}

	void sendMeshesToMaya(std::vector<BranchMesh*> treeMesh) {

		// MFnDagNode's create() will create a Maya group that we can assign each BranchMesh to
		std::string groupName_str = "BranchMesh Tree";
		char groupName_c[18];
		strcpy(groupName_c, groupName_str.c_str());
		MString groupName = groupName_c;
		MFnDagNode dagFn;
		MObject grpTransform = dagFn.create("transform", groupName);

		for (auto bMesh : treeMesh)
		{
			MFloatPointArray fpaVertices;
			for (int i = 0; i < bMesh->numVerts(); i++)
			{
				Point vert = bMesh->getVert(i);
				fpaVertices.append(MFloatPoint(vert.x, vert.y, vert.z));
			}

			MIntArray iaUVCounts;
			MIntArray iaFaceCounts;
			for (int i = 0; i < bMesh->numFaces(); i++)
			{
				iaFaceCounts.append(bMesh->getFaceCount(i));
				iaUVCounts.append(bMesh->getFaceCount(i));
			}

			MFloatArray faU;
			MFloatArray faV;

			bMesh->calculateUVs();

			if (bMesh->numUs() != bMesh->numFaceConnects()) { std::cout << "NUMBER OF U's != NUMBER OF FACECONNECTS" << std::endl; }
			if (bMesh->numVs() != bMesh->numFaceConnects()) { std::cout << "NUMBER OF V's != NUMBER OF FACECONNECTS" << std::endl; }

			MIntArray iaUVIDs;
			MIntArray iaFaceConnects;
			for (int i = 0; i < bMesh->numFaceConnects(); i++)
			{
				iaFaceConnects.append(bMesh->getFaceConnect(i));
				iaUVIDs.append(i);
				faU.append(bMesh->getU(i));
				faV.append(bMesh->getV(i));
			}

			MFnMesh fnMesh;
			MObject newTransform = fnMesh.create(bMesh->numVerts(), bMesh->numFaces(), fpaVertices,
				iaFaceCounts, iaFaceConnects, faU, faV);
			fnMesh.assignUVs(iaUVCounts, iaUVIDs);
			dagFn.addChild(newTransform);
		}
	}

	void checkBranches(Segment * seg, int &segIndex) {

		for (auto s : seg->getLateralSegs()) {

			MStreamUtils::stdOutStream() << "New branch at segment index " << segIndex << "\n";
			int newBranchSegIndex = 0;
			checkBranches(s, newBranchSegIndex);
		}

		for (auto s : seg->getSegsAbove()) {

			checkBranches(s, ++segIndex);
		}
	}
}
