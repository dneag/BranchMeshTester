/*
	BMTCommand_newSyntax.cpp

	defines the newSyntax() method of BMTCommand
*/

#include "BMTCommand.h"

#include <maya/MSyntax.h>

MSyntax BMTCommand::newSyntax() {

	MSyntax syntax;

	// As far as I'm aware, we cannot pass objects nor lists of lists through the command flags, we can only pass
	// lists of a single data type, so we will use an arbitrary code to parse the received lists:
	
	syntax.addFlag("-spb", "-segments per branch", MSyntax::kLong);
	syntax.makeFlagMultiUse("-spb");
	syntax.addFlag("-iop", "-index on parent", MSyntax::kLong);
	syntax.makeFlagMultiUse("-iop");
	syntax.addFlag("-p", "-polars", MSyntax::kDouble);
	syntax.makeFlagMultiUse("-p");
	syntax.addFlag("-a", "-azimuths", MSyntax::kDouble);
	syntax.makeFlagMultiUse("-a");
	syntax.addFlag("-d", "-distances", MSyntax::kDouble);
	syntax.makeFlagMultiUse("-d");
	syntax.addFlag("-r", "-radii", MSyntax::kDouble);
	syntax.makeFlagMultiUse("-r");
	syntax.addFlag("-o", "-offsets", MSyntax::kDouble);
	syntax.makeFlagMultiUse("-o");

	syntax.enableEdit(false);
	syntax.enableQuery(false);

	return syntax;
}