# BranchMeshTester_GUI.py
# defines GUI() function which creates the GUI for the BranchMesh Tester

import maya.cmds as cmds

class GUI():


    winName = "bmtWindow"
    dockName = "bmtDock"

    def __init__(self):
    
        if (cmds.window(self.winName, exists=True)):
            cmds.deleteUI(self.winName)
            print 'deleted existing ' + self.winName

        if(cmds.dockControl(self.dockName, exists=True)):
            cmds.deleteUI(self.dockName)
            print 'deleted existing ' + self.dockName
        
        self.mainWindow = cmds.window(self.winName, title="BranchMesh Tester", resizeToFitChildren=True)
        
        self.mainColumn_LO = cmds.columnLayout(w=300)
        
        self.makeMainCommandButton(self.mainColumn_LO)
        
        cmds.separator(style="in",h=4,w=300,hr=True)
        
        self.makeCurrentBranchLabel(self.mainColumn_LO)
        
        self.makeAddSegmentButton(self.mainColumn_LO)
        
        cmds.separator(style="double",h=4,w=300,hr=True)
        
        self.segmentScroll_LO = cmds.scrollLayout(w=300,h=500, bgc=[.2,.2,.2])
        self.segmentRowCol_LO = cmds.rowColumnLayout(nc=3, cw=[ (1,100), (2,100), (3,100) ])
        cmds.setParent(self.mainColumn_LO)
        cmds.button()
        cmds.showWindow()
        #cmds.dockControl(dockName, l="BranchMesh Tester Dock", area="right",content=mainWindow)


    def callMainCommand(self, *_):

        cmds.makeBranchMeshes()
        
    def makeMainCommandButton(self, startingLayout):

        cmds.separator(style="none",h=5)
        cmds.rowColumnLayout(nc=3, cw=[ (1,80), (2,140), (3,80) ])
        cmds.separator(style="none")
        cmds.button(l="Make Branch Meshes", command=self.callMainCommand)
        cmds.separator(style="none")
        cmds.setParent(startingLayout)
        cmds.separator(style="none",h=5)
        
    def makeCurrentBranchLabel(self, startingLayout):

        cmds.separator(style="none",h=5)
        cmds.rowColumnLayout(nc=3, cw=[ (1,40), (2,220), (3,40) ])
        cmds.separator(style="none")
        cmds.text(l="Branch 1")
        cmds.separator(style="none")
        cmds.setParent(startingLayout)
        cmds.separator(style="none",h=5)
        
    def makeAddSegmentButton(self, startingLayout):

        cmds.separator(style="none",h=5)
        cmds.rowColumnLayout(nc=3, cw=[ (1,100), (2,100), (3,100) ])
        cmds.separator(style="none")
        cmds.button(l="Add Segment", command=self.makeSegmentControls)
        cmds.separator(style="none")
        cmds.setParent(startingLayout)
        cmds.separator(style="none",h=5)
        
    def makeSegmentControls(self, *_):
        
        cmds.setParent(self.segmentRowCol_LO)
        cmds.separator(style="none")
        cmds.button(l="Dummy")
        cmds.separator(style="none")