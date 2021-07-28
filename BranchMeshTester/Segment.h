/*
Segment.h

The Segment class.  Segments are the virtual building blocks of a BranchMesh
*/

#pragma once
#ifndef Segment_h
#define Segment_h

#include <vector>

#include "BMTMath.h"

// in the larger program, a Meristem class determines much of what happens to Segments
// in this program it does not at all, we just need two attributes to mimic its usage in BranchMesh
struct Meristem
{
	double skinThickness;
	int sides;

	Meristem(double SKINTHICKNESS, int SIDES) : skinThickness(SKINTHICKNESS), sides(SIDES) {}
};

class Segment
{
	CVect vect;
	Point startPoint;
	double radius;

	// segsAbove are Segments whose start points are at the end point of this one
	std::vector<Segment*> segsAbove;

	// lateralSegs are Segments whose start points are along the length of this one
	std::vector<Segment*> lateralSegs;

	Meristem *meri = nullptr;

public:

	Segment(CVect VECT, Point STARTPOINT, double RADIUS, Meristem *MERI)
		: vect(VECT), startPoint(STARTPOINT), radius(RADIUS), meri(MERI) {}

	double getRadius() const { return radius; }

	CVect getVect() const { return vect; }

	double getLength() const { return vect.getMag(); }

	void setStartPoint(const Point &sp) { startPoint = sp; }

	Point getStartPoint() const { return startPoint; }

	void addSegAbove(Segment *seg) { segsAbove.push_back(seg); }

	std::vector<Segment*> getSegsAbove() const { return segsAbove; }

	void addLateralSeg(Segment *seg) { lateralSegs.push_back(seg); }

	std::vector<Segment*> getLateralSegs() const { return lateralSegs; }

	std::vector<Segment*> getConnectedUpperSegs() const {

		std::vector<Segment*> connectedUpperSegs;
		connectedUpperSegs = lateralSegs;
		connectedUpperSegs.insert(std::end(connectedUpperSegs), std::begin(segsAbove), std::end(segsAbove));
		return connectedUpperSegs;
	}

	Meristem * getMeri() const { return meri; }
};
#endif /* Segment_h */