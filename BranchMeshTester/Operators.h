/*
Operators.h

overloads operators for CVect and Point math
*/

#pragma once
#ifndef Operators_h
#define Operators_h

#include "BMTMath.h"

Point& operator+=(Point &lhs, const CVect &rhs);

Point& operator-=(Point &lhs, const CVect &rhs);

Point operator+(Point const &lhs, CVect const &rhs);

Point operator-(Point const &lhs, CVect const &rhs);

CVect operator+(CVect const &lhs, CVect const &rhs);

CVect operator-(Point const &lhs, Point const &rhs);

CVect operator-(CVect const &lhs, CVect const &rhs);

CVect& operator+=(CVect &lhs, const CVect &rhs);

CVect& operator*=(CVect &lhs, const double multiplier);

CVect operator*(CVect const &lhs, const double multiplier);

CVect operator/(CVect const &lhs, const double divisor);

#endif /* Operators_h */
