# BranchMeshTester_GUI.py
# defines GUI() class which creates the GUI for the BranchMesh Tester

import maya.cmds as cmds
from functools import partial

import Branch
reload(Branch)
from Branch import Branch

class GUI():

    def __init__(self):
        
        # Creates and displays the window and establishes all interface elements
        
        self.winName = "bmtWindow"
        self.dockName = "bmtDock"
        
        # counts are needed for creating unique names for object ui elements
        self.branchCount = 0
        self.segmentControlsCount = 0
        
        # Make sure the window or dock doesn't exist before creating a new one.  Delete it if it does
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
        
        self.makeBranchControls(self.mainColumn_LO)
        
        self.makeSegmentControlLabels(self.mainColumn_LO)
        
        cmds.separator(style="double",h=4,w=300,hr=True)

        self.rootBranch = Branch(0, None, self)
        self.rootBranch.activateBranchUI()
        
        cmds.showWindow()
        #cmds.dockControl(dockName, l="BranchMesh Tester Dock", area="right",content=mainWindow)

    def callMainCommand(self, *_):

        self.branchReport(self.rootBranch, "1")
        
        segmentAttributes = []
        self.rootBranch.collectSegmentAttributes(segmentAttributes)
        print segmentAttributes
        
        cmds.makeBranchMeshes()
        
    def branchReport(self, branch, branchNumber):
        
        # print information about branches 
        
        print "Branch " + branchNumber + " has " + str(len(branch.childBranches)) + " child branches and " + str(len(branch.segmentControls)) + " segments."
        
        for i, cb in enumerate(branch.childBranches):
        
            nextBranchNumber = branchNumber + ":" + str(i + 1)
            self.branchReport(cb, nextBranchNumber)
            
    def makeMainCommandButton(self, startingLayout):

        cmds.separator(style="none",h=5)
        cmds.rowColumnLayout(nc=3, cw=[ (1,80), (2,140), (3,80) ])
        cmds.separator(style="none")
        cmds.button(l="Make Branch Meshes", command=self.callMainCommand)
        cmds.separator(style="none")
        cmds.setParent(startingLayout)
        cmds.separator(style="none",h=5)
        
    def makeBranchControls(self, startingLayout):

        cmds.separator(style="none",h=5)
        cmds.rowColumnLayout(nc=4, cw=[ (1,100), (2,60), (3,80), (4,60) ])
        self.branchLabel = cmds.text(l="Branch 1")
        self.addSegButton = cmds.button(l="Add Seg", command=self.doNothing)
        self.removeSegButton = cmds.button(l="Remove Seg", command=self.doNothing)
        self.toParentBranchButton = cmds.button(l="To Parent", command=self.doNothing, vis=False)
        cmds.setParent(startingLayout)
        cmds.separator(style="none",h=5)
    
    def makeSegmentControlLabels(self, startingLayout):
    
        cmds.rowColumnLayout(nc=7, cw=[ (1,40), (2,40), (3,40), (4,40), (5,20), (6,30), (7,45), (8,30) ])
        cmds.text(l="pol", bgc=[.4,.4,.4], h=20)
        cmds.text(l="azi", bgc=[.35,.35,.35], h=20)
        cmds.text(l="dist", bgc=[.4,.4,.4], h=20)
        cmds.text(l="rad", bgc=[.35,.35,.35], h=20)
        cmds.separator(style="none")
        cmds.text(l="Br", bgc=[.4,.4,.4], h=20)
        cmds.text(l="offset", bgc=[.35,.35,.35], h=20)
        cmds.separator(style="none")
        cmds.setParent(startingLayout)
    
    def doNothing(self):
    
        pass
                       