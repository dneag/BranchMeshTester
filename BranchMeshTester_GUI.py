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
        print 'deleted existing ' + dockName

    mainWindow = cmds.window(winName, title="BranchMesh Tester", resizeToFitChildren=True)
    cmds.columnLayout(w=300)
    cmds.separator(style="none",h=5)
    cmds.rowColumnLayout(nc=3, cw=[ (1,80), (2,140), (3,80) ])
    cmds.separator(style="none")
    cmds.button(l="Make Branch Meshes", command=callMainCommand)
    cmds.separator(style="none")
    cmds.setParent("..")
    cmds.separator(style="none",h=5)
    cmds.separator(style="in",h=4,w=300,hr=True)
    cmds.scrollLayout(w=300,h=500)
    cmds.showWindow()
    #cmds.dockControl(dockName, l="BranchMesh Tester Dock", area="right",content=mainWindow)


def callMainCommand(*args):

    cmds.makeBranchMeshes()