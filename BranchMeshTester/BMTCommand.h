/*
	BMTCommand.h

	Creates user defined Maya commands
*/

#pragma once
#ifndef BMTCommand_h
#define BMTCommand_h

#include <maya/MPxCommand.h>

class BMTCommand : public MPxCommand
{
public:

	BMTCommand() {}

	virtual MStatus doIt(const MArgList& argList);

	static void* creator() {

		return new BMTCommand;
	}

	static MSyntax newSyntax();
};

#endif /* BMTCommand_h */

