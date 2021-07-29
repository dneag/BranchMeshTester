#include <maya/MStreamUtils.h>

#include "BranchMesh.h"
#include "Segment.h"
#include "BMTMath.h"
#include "Operators.h"

// creates the object and its first ring of vertices
BranchMesh::BranchMesh(Segment *firstSeg, const int sides) {

	//MStreamUtils::stdOutStream() << "ENTER FUNCTION - BranchMesh::BranchMesh() " << "\n";

	initialRadius = firstSeg->getRadius();

	if (sides > 2) {

		Space meshSpace(findVectorAngles(firstSeg->getVect()));
		double polarAngleToNextVert = 0., polarIncrement = MM::PIM2 / sides;

		for (int i = 0; i < sides; i++)
		{
			CVect vectorToVert = meshSpace.makeVector(polarAngleToNextVert, MM::PID2, initialRadius);

			Point newVert = firstSeg->getStartPoint() + vectorToVert;
			verts.push_back(newVert);

			polarAngleToNextVert -= polarIncrement;
		}
	}
	else {

		double distTimesSinAzi = initialRadius * MM::sinPID2;
		CVect vectorToStartVert;
		double polarAngleToNextVert = findVectorAngles(firstSeg->getVect()).pol + MM::PID2;

		for (int i = 0; i<sides; i++)
		{
			vectorToStartVert.x = distTimesSinAzi*std::cos(polarAngleToNextVert);
			vectorToStartVert.y = initialRadius * MM::cosPID2;
			vectorToStartVert.z = distTimesSinAzi*std::sin(polarAngleToNextVert);

			Point newVert = firstSeg->getStartPoint() + vectorToStartVert;
			verts.push_back(newVert);

			polarAngleToNextVert -= MM::PI;
		}
	}
}

void BranchMesh::go(Segment *seg, const int currentOrderSides, const std::vector<double> &preadjusts, std::queue<Segment*> &firstSegsOfBMeshes) {

	//MStreamUtils::stdOutStream() << "ENTER FUNCTION - BranchMesh::go()" << "\n";
	
	// first check for the beginnings of any new branch meshes
	std::vector<Segment*> potentialFirstSegs = seg->getConnectedUpperSegs();
	for (auto connectedSeg : potentialFirstSegs) {

		if (connectedSeg->getMeri() != seg->getMeri())
			firstSegsOfBMeshes.push(connectedSeg);
	}

	Segment *nextSegOnPath = findNextSegOnPath(seg);
	if (!nextSegOnPath) {

		// this should mean this is the last segment for this mesh
		MStreamUtils::stdOutStream() << "last seg..." << "\n\n";

		this->completePath(seg, currentOrderSides, preadjusts);

		//MStreamUtils::stdOutStream() << "path completed.  verts: " << verts.size() << ", faceConnects: " << faceConnects.size() <<
		//	", faceCounts: " << faceCounts.size() << "\n\n";

		return;
	}

	std::vector<double> nextPreadjusts = this->createNextRing(seg, nextSegOnPath, currentOrderSides, preadjusts);

	this->addNextFaceConnectsAndCounts(currentOrderSides);

	double halfDividerWidth = findDividerIfAny(seg->getRadius(), nextSegOnPath);

	if (halfDividerWidth > 0.) {

		this->createDividerRing(halfDividerWidth, seg, nextSegOnPath, currentOrderSides, nextPreadjusts);
		this->addNextFaceConnectsAndCounts(currentOrderSides);
		// the preadjusts are applied to the divider ring, so we reset them to 0. for the next go()
		std::fill(nextPreadjusts.begin(), nextPreadjusts.end(), 0.);
	}

	this->go(nextSegOnPath, currentOrderSides, nextPreadjusts, firstSegsOfBMeshes);
}

Segment * BranchMesh::findNextSegOnPath(Segment *currentSeg) {

	//MStreamUtils::stdOutStream() << "ENTER FUNCTION - BranchMesh::findNextSegOnPath()" << "\n";

	for (auto segAbove : currentSeg->getSegsAbove()) {

		//MStreamUtils::stdOutStream() << "checking meri of seg in segsAbove" << "\n";

		if (segAbove->getMeri() == currentSeg->getMeri()) {
			//MStreamUtils::stdOutStream() << "found next seg on path" << "\n";
			//MStreamUtils::stdOutStream() << "EXIT FUNCTION - BranchMesh::findNextSegOnPath()" << "\n";
			return segAbove;
		}
	}

	//MStreamUtils::stdOutStream() << "EXIT FUNCTION - BranchMesh::findNextSegOnPath()" << "\n";
	return nullptr;
}

void BranchMesh::completePath(Segment *lastSeg, const int sides, const std::vector<double> &preadjusts) {

	MStreamUtils::stdOutStream() << "ENTER FUNCTION - BranchMesh::completePath() " << "\n";

	std::size_t lowerRingFirstVert = verts.size() - sides;
	for (int i = 0; i < sides; ++i)
	{
		CVect resizedVector = lastSeg->getVect().resized(lastSeg->getVect().getMag() + preadjusts[i]);
		verts.push_back(verts[lowerRingFirstVert + i] + resizedVector);
	}

	this->addNextFaceConnectsAndCounts(sides);

	CVect vectorToLastVert = lastSeg->getVect().resized(lastSeg->getRadius());
	Point capVert = lastSeg->getStartPoint() + lastSeg->getVect() + vectorToLastVert;
	verts.push_back(capVert);

	this->addCapFaceConnectsAndCounts(sides);

	//MStreamUtils::stdOutStream() << "EXIT FUNCTION - BranchMesh::completePath()" << "\n";
}

std::vector<double> BranchMesh::createNextRing(Segment *currentSeg, Segment *nextSeg, const int currentOrderSides, const std::vector<double> &preadjusts) {

	//MStreamUtils::stdOutStream() << "ENTER FUNCTION - BranchMesh::createNextRing()" << "\n";

	std::vector<double> newPreadjusts;
	const double angBetweenSegments = findAngBetween(currentSeg->getVect(), nextSeg->getVect());

	//MStreamUtils::stdOutStream() << "angBetweenSegments: " << angBetweenSegments << "\n";

	if (angBetweenSegments > .0001 || angBetweenSegments < -.0001) {

		// even if the two segments have different radii, only use the current seg's radius for calculating the first ring
		const double currentRadius = currentSeg->getRadius();
		const double angBetweenOut90 = MM::PID2 - angBetweenSegments;
		const double sinAngBetween = std::sin(angBetweenOut90);

		const double largeOppSideLength = sinAngBetween * nextSeg->getVect().getMag(); // SOH
		const Point nextSegEndPoint = nextSeg->getStartPoint() + nextSeg->getVect();
		const CVect currentVectResized = currentSeg->getVect().resized(largeOppSideLength);
		const Point rightAnglePoint = nextSegEndPoint - currentVectResized;
		const Point currentSegEndPoint = currentSeg->getStartPoint() + currentSeg->getVect();
		CVect rightAngleVector = rightAnglePoint - currentSegEndPoint;
		rightAngleVector.resize(currentRadius);
		const Point pointUnderAngle = currentSegEndPoint + rightAngleVector;
		const Point pointBehindAngle = currentSegEndPoint - rightAngleVector;
		rightAngleVector = pointBehindAngle - pointUnderAngle;

		const double topTriangleHSide = sinAngBetween * currentRadius; //SOH
		const double topTriangleVSide = std::cos(angBetweenOut90) * currentRadius; //CAH
		const double bottomTriangleVSide = std::tan(angBetweenOut90) * (currentRadius - topTriangleHSide); //TOA
		double maxAdjust = bottomTriangleVSide - topTriangleVSide;

		if (std::fabs(maxAdjust) >= currentSeg->getVect().getMag())
			MStreamUtils::stdOutStream() << "WARNING: angle between segments is too big.  Your mesh probably looks funny. " << "\n";

		const int topRingFirstVert = verts.size() - currentOrderSides;
		for (int s = 0; s < currentOrderSides; ++s) {

			// preadjusts must be added to create a tentative Point. this point lies on the plane at the end of and perpendicular to the 
			// current segment's vector. its position is needed to calculate the next adjustment
			Point vertPosWithPreAdjust = verts[topRingFirstVert + s] + currentSeg->getVect().resized(currentSeg->getLength() + preadjusts[s]);
			CVect vectorToPUA = vertPosWithPreAdjust - pointUnderAngle;
			double vectorToPUAMag = vectorToPUA.getMag();
			double adjust = maxAdjust;

			if (vectorToPUAMag > 0.) {
				double angBetween = findAngBetween(rightAngleVector, vectorToPUA);
				double distAlongRightAngleVector = std::cos(angBetween) * vectorToPUAMag; //CAH
				adjust = (1. - (distAlongRightAngleVector / currentRadius)) * maxAdjust;
			}

			// add the new adjustment then save it as a preadjust for the next ring
			Point finalVertPos = vertPosWithPreAdjust + currentSeg->getVect().resized(adjust);
			verts.push_back(finalVertPos);
			newPreadjusts.push_back(adjust);
		}
	}
	else {

		const int topRingFirstVert = verts.size() - currentOrderSides;
		for (int s = 0; s < currentOrderSides; ++s) {

			verts.push_back(verts[topRingFirstVert + s] + currentSeg->getVect().resized(currentSeg->getLength() + preadjusts[s]));
			newPreadjusts.push_back(0.);
		}
	}

	//MStreamUtils::stdOutStream() << "EXIT FUNCTION - BranchMesh::createNextRing()" << "\n";

	return newPreadjusts;
}

// returns the width of the divider
// returns 0. if there is no divider
// pre: all segment radii are already calculated
double BranchMesh::findDividerIfAny(const double currentSegRadius, Segment *nextSegOnPath) {

	//MStreamUtils::stdOutStream() << "ENTER FUNCTION - BranchMesh::findDividerIfAny()" << "\n";

	double radiusMinPercentDiff = 1.15;
	double radiusOfSegAbove = nextSegOnPath->getRadius();

	//MStreamUtils::stdOutStream() << "this radius: " << currentSegRadius << ", last radius: " << radiusOfSegAbove << "\n";

	if (currentSegRadius > radiusOfSegAbove * radiusMinPercentDiff) {

		double largestRadius = 0.;

		for (auto lateralSeg : nextSegOnPath->getLateralSegs())
		{
			double skinThickness = lateralSeg->getMeri()->skinThickness;

			double thisRadius = lateralSeg->getRadius() + skinThickness;
			if (thisRadius > largestRadius) { largestRadius = thisRadius; }
		}

		if (largestRadius == 0. || largestRadius >= nextSegOnPath->getLength())
			MStreamUtils::stdOutStream() << "WARNING: creating divider with funny width" << "\n";

		//MStreamUtils::stdOutStream() << "largestRadius: " << largestRadius << "\n";

		return largestRadius;
	}
	else {

		return 0.;
	}
}

void BranchMesh::createDividerRing(const double halfDividerWidth, Segment *currentSeg, Segment *nextSeg,
	const int currentOrderSides, const std::vector<double> &preadjusts) {

	//MStreamUtils::stdOutStream() << "ENTER FUNCTION - BranchMesh::createDividerRing()" << "\n";

	int topRingFirstVert = verts.size() - currentOrderSides;
	for (int s = 0; s < currentOrderSides; ++s) {

		// first add the preadjust from the previous ring so that the vertex sits on the perpendicular plane at the beginning of nextSeg
		Point tempVertPos = verts[topRingFirstVert + s] + nextSeg->getVect().resized(preadjusts[s]);
		// then using the start point of the nextSeg, shrink the vertex position inward according to the new radius
		CVect vectorTowardsCenter = nextSeg->getStartPoint() - tempVertPos;
		vectorTowardsCenter.resize(currentSeg->getRadius() - nextSeg->getRadius());
		MStreamUtils::stdOutStream() << "radius difference: " << currentSeg->getRadius() - nextSeg->getRadius() << "\n";
		// add vectorTowardsCenter to tempVertPos to shrink its position inward, then add nextSeg's vector at a length of halfDividerWidth
		// to finalize the position of the new vertex
		verts.push_back(tempVertPos + vectorTowardsCenter + nextSeg->getVect().resized(halfDividerWidth));

		// now that we are done with the vertex in the previous ring, we can slide it down according to the divider width
		verts[topRingFirstVert + s] -= currentSeg->getVect().resized(halfDividerWidth);
	}

	//MStreamUtils::stdOutStream() << "EXIT FUNCTION - BranchMesh::createDividerRing()" << "\n";
}

// adds faceConnects for the faces between the last and second-to-last rings of verts created 
// pre: must have two rings for which faceconnects have not been created
void BranchMesh::addNextFaceConnectsAndCounts(const int sides) {

	// for each 4 sided face added we have to specify the indices of the verts that make up its 4 corners - these indices are the faceConnects
	// for each face, they start on the lower left and move counter-clockwise
	int initialIndex = verts.size() - sides * 2;
	if (sides > 2) {

		int nextVertIndex = initialIndex;
		for (nextVertIndex; nextVertIndex < verts.size() - sides - 1; ++nextVertIndex) {

			faceConnects.push_back(nextVertIndex);
			faceConnects.push_back(nextVertIndex + 1);
			faceConnects.push_back(nextVertIndex + 1 + sides);
			faceConnects.push_back(nextVertIndex + sides);
		}

		//The pattern for faceConnects is a bit different for the last side in every ring of sides
		faceConnects.push_back(nextVertIndex);
		faceConnects.push_back(initialIndex);
		faceConnects.push_back(initialIndex + sides);
		faceConnects.push_back(nextVertIndex + sides);

		for (int i = 0; i < sides; ++i)
			faceCounts.push_back(4);
	}
	else
	{
		// this is for 2 siders (one face)
		faceConnects.push_back(initialIndex);
		faceConnects.push_back(initialIndex + 1);
		faceConnects.push_back(initialIndex + 1 + sides);
		faceConnects.push_back(initialIndex + sides);

		faceCounts.push_back(4);
	}
}

// pre: the cap is a single vertex and it is the last in the list for this mesh
void BranchMesh::addCapFaceConnectsAndCounts(const int sides) {

	int initialIndex = verts.size() - sides - 1;
	if (sides > 2) {

		// first do (sides - 1) loops because the pattern changes for the last face in the ring
		int nextVertIndex = initialIndex;
		for (nextVertIndex; nextVertIndex < verts.size() - 2; ++nextVertIndex) {

			faceConnects.push_back(nextVertIndex);
			faceConnects.push_back(nextVertIndex + 1);
			faceConnects.push_back(verts.size() - 1);
		}

		//The pattern for faceConnects is a bit different for the last face in every ring
		faceConnects.push_back(nextVertIndex);
		faceConnects.push_back(initialIndex);
		faceConnects.push_back(verts.size() - 1);

		for (int i = 0; i < sides; ++i)
			faceCounts.push_back(3);
	}
	else {

		//this means we have a 2-sider, so only making one face
		faceConnects.push_back(initialIndex);
		faceConnects.push_back(initialIndex + 1);
		faceConnects.push_back(verts.size() - 1);

		faceCounts.push_back(3);
	}
}

void BranchMesh::calculateUVs()
{
	double wedgeAngle = MM::PIM2 / sides;
	double radSqu = initialRadius*initialRadius;

	double baseFaceWidth = std::sqrt((radSqu + radSqu) - (2 * radSqu*std::cos(wedgeAngle)));//law of cosines

	int numTextureColumns = 1;
	int faces = sides;
	if (sides == 2) { faces = 1; }

	double uvFaceWidth = 1. / (numTextureColumns * faces);
	double uvScaler = uvFaceWidth / baseFaceWidth;

	int sideInd = 0;
	int cnctInd = 0;

	sideInd = 0;
	cnctInd = 0;
	int ring = 1;
	int indexDiffOfVertBelow;

	for (int i = 0; i<faceCounts.size(); i++)
	{
		if (faceCounts[i] == 4)
		{
			us.push_back(1. - (sideInd * uvFaceWidth));
			us.push_back(1. - ((sideInd + 1) * uvFaceWidth));
			us.push_back(1. - ((sideInd + 1) * uvFaceWidth));
			us.push_back(1. - (sideInd * uvFaceWidth));

			if (ring > 1)
			{
				int matchingCnctInd = (cnctInd - indexDiffOfVertBelow) + 3;
				vs.push_back(vs[matchingCnctInd]);
				matchingCnctInd = ((cnctInd + 1) - indexDiffOfVertBelow) + 1;
				vs.push_back(vs[matchingCnctInd]);
				double distFromVertBelow = distBetween(faceConnects[cnctInd + 1], faceConnects[cnctInd + 2]);
				vs.push_back(vs.back() + (distFromVertBelow * uvScaler));
				distFromVertBelow = distBetween(faceConnects[cnctInd], faceConnects[cnctInd + 3]);
				vs.push_back(vs[cnctInd] + (distFromVertBelow * uvScaler));
			}
			else
			{
				vs.push_back(0.);
				vs.push_back(0.);

				double distFromVertBelow = distBetween(faceConnects[cnctInd + 1], faceConnects[cnctInd + 2]);
				vs.push_back(distFromVertBelow * uvScaler);
				distFromVertBelow = distBetween(faceConnects[cnctInd], faceConnects[cnctInd + 3]);
				vs.push_back(distFromVertBelow * uvScaler);
			}
		}
		else if (faceCounts[i] == 3)
		{
			indexDiffOfVertBelow = 0;

			for (int j = 1; j <= sides; j++)
			{
				indexDiffOfVertBelow += faceCounts[i - j];
			}

			us.push_back(1. - (sideInd * uvFaceWidth));
			us.push_back(1. - ((sideInd + 1) * uvFaceWidth));
			us.push_back(1. - ((sideInd + 1) * uvFaceWidth) + (uvFaceWidth * .5));

			//here we can assume ring > 1 because only cap faces should have 3 sides
			int matchingCnctInd = (cnctInd - indexDiffOfVertBelow) + 3;
			vs.push_back(vs[matchingCnctInd]);
			matchingCnctInd = ((cnctInd + 1) - indexDiffOfVertBelow) + 1;
			vs.push_back(vs[matchingCnctInd]);
			double distFromVertBelow = distBetween(faceConnects[cnctInd + 1], faceConnects[cnctInd + 2]);
			vs.push_back(vs.back() + (distFromVertBelow * uvScaler));
		}

		cnctInd += faceCounts[i];
		if (sides > 2) { sideInd++; }

		if (sideInd == sides) {
			sideInd = 0;
			indexDiffOfVertBelow = sides * (faceCounts[(i + 1) - sides]);
			ring++;
		}
	}
}
