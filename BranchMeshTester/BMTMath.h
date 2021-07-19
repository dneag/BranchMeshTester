#pragma once
#ifndef BMTMath_h
#define BMTMath_h

#include <cmath>
#include <iostream>

namespace MM {

	const double PI = 3.14159265358979;
	const double PID2 = 1.5707963267949;
	const double PID4 = PI / 4.;
	const double PIM2 = 6.28318530717959;
	const double PIANDAHALF = PI + PID2;
	const double sinPID2 = std::sin(PID2);
	const double cosPID2 = std::cos(PID2);
}

struct PolAngles
{
	double pol = 0.;
	double azi = 0.;

	PolAngles() {}

	PolAngles(double POL, double AZI) : pol(POL), azi(AZI) {}

	void operator=(const PolAngles &rhs) {

		pol = rhs.pol;
		azi = rhs.azi;
	}
};

struct Point
{
	double x = 0.;
	double y = 0.;
	double z = 0.;

	Point() {}

	Point(double X, double Y, double Z) : x(X), y(Y), z(Z) {}

	void operator=(const Point &rhs) {

		x = rhs.x;
		y = rhs.y;
		z = rhs.z;
	}
};

struct CVect
{
	double x = 0.;
	double y = 0.;
	double z = 0.;

	CVect() {}

	CVect(double X, double Y, double Z) : x(X), y(Y), z(Z) {}

	CVect(double v[3]) : x(v[0]), y(v[1]), z(v[2]) {}

	CVect(const CVect &rhs) : x(rhs.x), y(rhs.y), z(rhs.z) {}

	void operator=(const CVect &rhs) {

		x = rhs.x;
		y = rhs.y;
		z = rhs.z;
	}

	double getMag() const { return std::sqrt(x*x + y*y + z*z); }

	void resize(double newLength) {

		double length = std::sqrt(x * x + y * y + z * z);
		if (length == 0.)
			std::cout << "WARNING! Vector length is zero (in CVect::resize())" << std::endl;

		double normalizer = newLength / length;
		x *= normalizer;
		y *= normalizer;
		z *= normalizer;
	}

	CVect resized(double newLength) const {

		double length = std::sqrt(x * x + y * y + z * z);
		if (length == 0.)
			std::cout << "WARNING! Vector length is zero (in CVect::resized())" << std::endl;

		CVect v;
		double normalizer = newLength / length;
		v.x = x * normalizer;
		v.y = y * normalizer;
		v.z = z * normalizer;

		return v;
	}
};

class Space
{
	double aziMatrix[3][3];
	double iAziMatrix[3][3];
	double matrixFromVectors[3][3];
	double polarOrientation = 0.;
	double aziOrientation = 0.;
	double u[3];

public:

	Space() {}

	// create an object oriented to the angles parameter
	Space(PolAngles angles);

	CVect makeVector(double polar, double azimuth, double distance) const;
};

PolAngles findVectorAngles(const CVect &v);

double distance(const Point &p, const Point &q);

double findAngBetween(const CVect &p, const CVect &q);

#endif /* BMTMath_h */
