# BranchMeshTester_GUI.py
# defines GUI() class which creates the GUI for the BranchMesh Tester

import maya.cmds as cmds
from functools import partial

class GUI():

    def __init__(self):
        
        self.winName = "bmtWindow"
        self.dockName = "bmtDock"
    
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
        
        self.allBranches = []
        self.allBranches.append(Branch(0, None))
        self.makeBranchControls(self.mainColumn_LO, self.allBranches[0])
        
        cmds.rowColumnLayout(nc=7, cw=[ (1,40), (2,40), (3,40), (4,40), (5,20), (6,30), (7,45), (8,30) ])
        cmds.text(l="pol", bgc=[.4,.4,.4], h=20)
        cmds.text(l="azi", bgc=[.35,.35,.35], h=20)
        cmds.text(l="dist", bgc=[.4,.4,.4], h=20)
        cmds.text(l="rad", bgc=[.35,.35,.35], h=20)
        cmds.separator(style="none")
        cmds.text(l="Br", bgc=[.4,.4,.4], h=20)
        cmds.text(l="offset", bgc=[.35,.35,.35], h=20)
        cmds.separator(style="none")
        cmds.setParent(self.mainColumn_LO)
        
        cmds.separator(style="double",h=4,w=300,hr=True)
        
        
        self.segmentScroll_LO = cmds.scrollLayout(w=300,h=500, bgc=[.2,.2,.2])
        self.segmentRowCol_LO = cmds.rowColumnLayout(nc=8, cw=[ (1,40), (2,40), (3,40), (4,40), (5,20), (6,30), (7,45), (8,30) ], rs=[1,5])

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
        
    def makeBranchControls(self, startingLayout, currentBranch):

        cmds.separator(style="none",h=5)
        cmds.rowColumnLayout(nc=3, cw=[ (1,100), (2,100), (3,100) ])
        self.currentBranchLabel = cmds.text(l="Branch 1")
        cmds.button(l="Add Seg", command=partial(self.makeSegmentControls, currentBranch))
        #cmds.button(l="Remove Seg", command=self.deleteSegmentControls)
        cmds.setParent(startingLayout)
        cmds.separator(style="none",h=5)
        
    def makeSegmentControls(self, currentBranch, *_):
        
        cmds.setParent(self.segmentRowCol_LO)
        segmentNumber = len(currentBranch.segmentControls) + 1
        currentBranch.segmentControls.append(SegmentControls(self, currentBranch, segmentNumber))
    
    def startNewBranch(self, parentBranch, rootSegNum, *_):
    
        # creates a new Branch and appends it to the parentBranch's list of childBranches
        # childBranches is always in ascending order by the Branch's rootSegNum
        
        parentBranch.childBranches.append(Branch(rootSegNum, parentBranch))
        parentBranch.childBranches.sort(key=lambda branch: branch.rootSegNum)
        
            
class Branch:

    # represents a chain of connected segments
    
    def __init__(self, rootSegNum, prnt):
    
        self.rootSegNum = rootSegNum
        self.segmentControls = []
        self.prnt = prnt
        self.childBranches = []
        
class SegmentControls:

    # represents the controls used for defining a segment
    
    def __init__(self, theGUI, homeBranch, segmentNumber):
    
        self.pol_FLD = cmds.intField(v=0, min=0, max=359)
        self.azi_FLD = cmds.intField(v=0, min=0, max=359)
        self.distance_FLD = cmds.floatField(v=.3, pre=2, min=.01, max=3)
        self.radius_FLD = cmds.floatField(v=.3, pre=2, min=.01, max=3)
        self.separator1 = cmds.separator(style="none")
        self.checkBox = cmds.checkBox(l="", onc=partial(theGUI.startNewBranch, homeBranch, segmentNumber), ofc=partial(theGUI.startNewBranch, homeBranch, segmentNumber))
        self.offSet_FLD = cmds.floatField(v=.3, pre=2, min=.01, max=3)
        self.toBranchButton = cmds.button()
        
    
        
        
        