/*
BranchMesh.h

*/

#pragma once
#ifndef BranchMesh_h
#define BranchMesh_h

#include <vector>
#include <queue>

#include "Segment.h"
#include "Operators.h"
#include "BMTMath.h"

class BranchMesh
{
	int sides;
	double initialRadius;
	std::vector< Point > verts;
	std::vector<int> faceCounts;
	std::vector<double> us;
	std::vector<double> vs;
	std::vector<int> faceConnects;

public:

	BranchMesh(Segment *firstseg, const int sides);

	Segment * findNextSegOnPath(Segment *currentSeg);

	void completePath(Segment *lastSeg, const int sides, const std::vector<double> &preadjusts);

	double findDividerIfAny(const double currentSegRadius, Segment *nextSegOnPath);

	std::vector<double> createNextRing(Segment *currentSeg, Segment *nextSeg, const int currentOrderSides, const std::vector<double> &preadjusts);

	// creates and finalizes the positions of the ring of vertices between the top rings of the current seg and next seg
	void createDividerRing(const double halfDividerWidth, Segment *currentSeg, Segment *nextSeg,
		const int currentOrderSides, const std::vector<double> &preadjusts);

	// Traverses all segments until there is no seg above the current seg with the same meristem as the current seg
	// At each segment we check for connected segs with different meristems, adding those segs as new firstSegsOfBMeshes
	// At each segment we set the positions for the ring of vertices at its end, and if there is a divider above it, we set that ring too
	// For each ring of vertices added, a corresponding set of faceConnects and faceCounts is also added
	// When the last segment of the mesh is found, a single cap vertex is added along with a corresponding set of faceConnects and faceCounts
	void go(Segment *seg, const int currentOrderSides, const std::vector<double> &preadjusts, std::queue<Segment*> &firstSegsOfBMeshes);

	int numVerts() { return verts.size(); }
	void addVert(Point newVert) { verts.push_back(newVert); }
	void insertVert(Point newVert, int index) { verts.insert(verts.begin() + index, newVert); }
	Point& vertex(int index) { return verts[index]; }
	Point getVert(int index) { return verts[index]; }
	void setVert(int index, Point value) { verts[index] = value; }
	void addVectToVert(int index, CVect vect) { verts[index] += vect; }
	double distBetween(int a, int b) { return distance(verts[a], verts[b]); }

	int numFaces() { return faceCounts.size(); }
	int numUs() { return us.size(); }
	int numVs() { return vs.size(); }
	void addFaceCount(int newFC) { faceCounts.push_back(newFC); }
	double getU(int index) { return us[index]; }
	double getV(int index) { return vs[index]; }
	int getFaceCount(int index) { return faceCounts[index]; }

	int numFaceConnects() { return faceConnects.size(); }
	void addFaceConnect(int newFCN) { faceConnects.push_back(newFCN); }
	int getFaceConnect(int index) { return faceConnects[index]; }

	void addNextFaceConnectsAndCounts(const int sides);

	void addCapFaceConnectsAndCounts(const int sides);

	void calculateUVs();
};

#endif /* BranchMesh_h */
