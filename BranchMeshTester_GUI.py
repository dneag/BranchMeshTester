# BranchMeshTester_GUI.py
# defines GUI() function which creates the GUI for the BranchMesh Tester

import maya.cmds as cmds

def GUI():

    winName = "bmtWindow"
    dockName = "bmtDock"

    if (cmds.window(winName, exists=True)):
        cmds.deleteUI(winName)
        print 'deleted existing ' + winName

    if(cmds.dockControl(dockName, exists=True)):
        cmds.deleteUI(dockName)
        print 'deleted existing' + dockName

    mainWindow = cmds.window(winName, title="BranchMesh Tester", w=350, h=300)
    cmds.scrollLayout(w=420)
    #cmds.showWindow()
    dockCtrl = cmds.dockControl(dockName, l="BranchMesh Tester Dock", area="right",content=mainWindow)
