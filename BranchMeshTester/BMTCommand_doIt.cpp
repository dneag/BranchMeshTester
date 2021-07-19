/*
	BMTCommand_doIt.cpp

	defines doIt() method of BMTCommand
*/

#include <iostream>
#include <stdlib.h>

#include <maya/MArgDatabase.h>
#include <maya/MSyntax.h>

#include "BMTCommand.h"

MStatus BMTCommand::doIt(const MArgList &argList) {

	MStatus status;

	MArgDatabase argData(syntax(), argList, &status);
	CHECK_MSTATUS_AND_RETURN_IT(status);


	return MS::kSuccess;
}

