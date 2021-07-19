//
// Copyright (C)  
// 
// File: pluginMain.cpp
//
// Author: Maya Plug-in Wizard 2.0
//

/*
edited from the Maya Plug-in Wizard 2.0 template
defines methods called when loading and unloading the BranchMeshTester plugin
*/

#include <maya/MFnPlugin.h>

#include "BMTCommand.h"

MStatus initializePlugin(MObject obj)
//
//	Description:
//		this method is called when the plug-in is loaded into Maya.  It 
//		registers all of the services that this plug-in provides with 
//		Maya.
//
//	Arguments:
//		obj - a handle to the plug-in object (use MFnPlugin to access it)
//
{
	MStatus   status;
	MFnPlugin plugin(obj, "", "2018", "Any");

	status = plugin.registerCommand("makeBranchMeshes", BMTCommand::creator, BMTCommand::newSyntax);
	CHECK_MSTATUS_AND_RETURN_IT(status);

	return status;
}

MStatus uninitializePlugin(MObject obj)
//
//	Description:
//		this method is called when the plug-in is unloaded from Maya. It 
//		deregisters all of the services that it was providing.
//
//	Arguments:
//		obj - a handle to the plug-in object (use MFnPlugin to access it)
//
{
	MStatus   status;
	MFnPlugin plugin(obj);

	status = plugin.deregisterCommand("makeBranchMeshes");
	CHECK_MSTATUS_AND_RETURN_IT(status);

	return status;
}
