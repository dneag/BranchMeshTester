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

	void sendMeshesToMaya(std::vector<BranchMesh*> treeMesh);
}

MStatus BMTCommand::doIt(const MArgList &argList) {

	MStatus status;

	MArgDatabase argData(syntax(), argList, &status);
	CHECK_MSTATUS_AND_RETURN_IT(status);

	std::vector<BranchMesh*> treeMesh;

	// there will always be a root segment regardless of user input
	Meristem *rootMeri = new Meristem(.01, 8);
	Segment *rootSeg = new Segment(CVect(0., .3, 0.), Point(0., -.3, 0.), .05, rootMeri);

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

	sendMeshesToMaya(treeMesh);

	return MS::kSuccess;
}

namespace {

	void sendMeshesToMaya(std::vector<BranchMesh*> treeMesh) {

		// dagFn.create("transform", groupName) will create a Maya group that we can assign each BranchMesh to
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
}
