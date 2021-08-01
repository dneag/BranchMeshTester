/*
	BMTCommand_newSyntax.cpp

	Defines the newSyntax() method of BMTCommand
	This method adds flags (much like arguments) to the custom command (makeBranchMeshes) we are creating, allowing us
	to pass information from the python script to the API
*/

#include "BMTCommand.h"

#include <maya/MSyntax.h>

MSyntax BMTCommand::newSyntax() {

	MSyntax syntax;

	// As far as I'm aware, we cannot pass objects nor lists of lists through the command flags, we can only pass
	// lists of a single built in data type (makeFlagMultiUse() enables passing of lists), so we will use an arbitrary code to parse the received lists:
	
	// The lengths of -spb and -iop are the same and correspond to the number of branches
	// Each entry in -spb is an integer indicating the number of segments on the corresponding branch
	// Each entry in -iop is an integer indicating the index on the corresponding branch's parent branch
	syntax.addFlag("-spb", "-segments per branch", MSyntax::kLong);
	syntax.makeFlagMultiUse("-spb");
	syntax.addFlag("-iop", "-index on parent", MSyntax::kLong);
	syntax.makeFlagMultiUse("-iop");

	// The lengths of the following flags correspond to the total number of segments in the mesh
	// Each represents a physical dimension of a segment
	// -p, -a, and -d are the spherical coordinates
	// -r is the radius of the segment cross-section (segments are cylindrical)
	// -o is the offset of the segment along its parent branch, starting from bottom of the segment from which it is lateral
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
