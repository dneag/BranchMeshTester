/*
	BMTCommand_newSyntax.cpp

	defines the newSyntax() method of BMTCommand
*/

#include "BMTCommand.h"

#include <maya/MSyntax.h>

MSyntax BMTCommand::newSyntax() {

	MSyntax syntax;

	syntax.addFlag("-sa", "-segment attributes", MSyntax::kDouble);
	syntax.makeFlagMultiUse("-sa");

	syntax.enableEdit(false);
	syntax.enableQuery(false);

	return syntax;
}