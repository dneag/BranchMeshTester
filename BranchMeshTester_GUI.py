# BranchMeshTester_GUI.py
# defines GUI() class which creates the GUI for the BranchMesh Tester

import maya.cmds as cmds
from functools import partial

class GUI():

    def __init__(self):
        
        # Creates and displays the window and establishes all interface elements
        
        self.winName = "bmtWindow"
        self.dockName = "bmtDock"
    
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
        
        self.segmentScroll_LO = cmds.scrollLayout(w=300,h=500, bgc=[.2,.2,.2])
        
        self.allBranches = []
        self.allBranches.append(Branch(0, None, self))
        self.allBranches[0].activateBranchUI()
        
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
        
    def makeBranchControls(self, startingLayout):

        cmds.separator(style="none",h=5)
        cmds.rowColumnLayout(nc=3, cw=[ (1,100), (2,100), (3,100) ])
        self.branchLabel = cmds.text(l="Branch 1")
        self.addSegButton = cmds.button(l="Add Seg", command=self.doNothing)
        #cmds.button(l="Remove Seg", command=self.deleteSegmentControls)
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
        
    # def makeSegmentControls(self, currentBranch, *_):
        
        # cmds.setParent(self.segmentRowCol_LO)
        # segmentNumber = len(currentBranch.segmentControls) + 1
        # currentBranch.segmentControls.append(SegmentControls(currentBranch, segmentNumber))
    
    def doNothing(self):
    
        pass
        
class Branch:

    # represents a chain of connected segments
    
    def __init__(self, rootSegNum, prnt, theGUI):
    
        self.theGUI = theGUI
        self.rootSegNum = rootSegNum
        self.segmentControls = []
        self.prnt = prnt
        self.childBranches = []
        
        # we should always be on the parent branch's rowColumnLayout here, so we need to switch and switch back parent layouts when creating 
        # the rowColumnLayout for this new branch
        cmds.setParent(theGUI.segmentScroll_LO)
        self.segmentRowCol_LO = cmds.rowColumnLayout(nc=8, cw=[ (1,40), (2,40), (3,40), (4,40), (5,20), (6,30), (7,45), (8,30) ], rs=[1,5], vis=False)
        
    def activateBranchUI(self):
        
        cmds.rowColumnLayout(self.segmentRowCol_LO, e=True, vis=True)
        branchNumber = self.calculateBranchNumber()
        cmds.text(self.theGUI.branchLabel, e=True, l=branchNumber)
        cmds.button(self.theGUI.addSegButton, e=True, command=self.makeSegmentControls)
    
    def locateAndActivate(self, rootSegNum, *_):
    
        for cb in self.childBranches:
            if (cb.rootSegNum == rootSegNum):
                cmds.rowColumnLayout(self.segmentRowCol_LO, e=True, vis=False) # hide this branch's layout before turning another on
                cb.activateBranchUI()
                
    def makeSegmentControls(self, *_):
    
        cmds.setParent(self.segmentRowCol_LO)
        segmentNumber = len(self.segmentControls) + 1
        self.segmentControls.append(SegmentControls(self, segmentNumber))
    
    def calculateBranchNumber(self):
        
        branchNumber = []
        self.getIndexInParentList(branchNumber)
        branchNumber.reverse()
        branchNumberAsString = "Branch "
        for n in branchNumber:
            branchNumberAsString += str(n)
            
        return branchNumberAsString
       
    def getIndexInParentList(self, branchNumber):
     
       if (self.prnt is not None):
           for i, childBranch in enumerate(self.prnt.childBranches):
               if (childBranch.rootSegNum == self.rootSegNum):
                   branchNumber.append(i)
                   self.prnt.getIndexInParentList(branchNumber)
                   break
       else:
           branchNumber.append(1)
                    
class SegmentControls:

    # represents the controls used for defining a segment
    
    def __init__(self, homeBranch, segmentNumber):
    
        self.segmentNumber = segmentNumber
        self.pol_FLD = cmds.intField(v=0, min=0, max=359)
        self.azi_FLD = cmds.intField(v=0, min=0, max=359)
        self.distance_FLD = cmds.floatField(v=.3, pre=2, min=.01, max=3)
        self.radius_FLD = cmds.floatField(v=.3, pre=2, min=.01, max=3)
        self.separator1 = cmds.separator(style="none")
        self.checkBox = cmds.checkBox(l="", onc=partial(self.lateralBranch_On, homeBranch), ofc=partial(self.lateralBranch_Off, homeBranch))
        self.offSet_FLD = cmds.floatField(v=.15, pre=2, min=.01, max=3, en=False)
        self.toBranchButton = cmds.button(l="->",en=False, bgc=[.4,.4,.4], command=partial(homeBranch.locateAndActivate, self.segmentNumber))
        
        
    def lateralBranch_On(self, parentBranch, checkBoxState):
    
        # turns on lateral branch controls and creates a new branch
        
        # enable the offset and toBranch button controls
        cmds.floatField(self.offSet_FLD, e=True, en=checkBoxState)
        cmds.button(self.toBranchButton, e=True, en=checkBoxState)
        
        # create a new Branch and appends it to the parentBranch's list of childBranches
        # childBranches is always in ascending order by the Branch's rootSegNum
        parentBranch.childBranches.append(Branch(self.segmentNumber, parentBranch, parentBranch.theGUI))
        parentBranch.childBranches.sort(key=lambda branch: branch.rootSegNum)
        
        # for cb in parentBranch.childBranches:
        
            # print cb.rootSegNum
        
        # print " "
        
    def lateralBranch_Off(self, parentBranch, checkBoxState):
    
        # turns off lateral branch controls and removes the branch located on the segment
        
        # disable the offset and toBranch button controls
        cmds.floatField(self.offSet_FLD, e=True, en=checkBoxState)
        cmds.button(self.toBranchButton, e=True, en=checkBoxState)
        
        # removes the branch rooted at the segment corresponding to rootSegNum
        for i, cb in enumerate(parentBranch.childBranches):
            if cb.rootSegNum == self.segmentNumber:
                del parentBranch.childBranches[i]
                break
                
        # for cb in parentBranch.childBranches:
        
            # print cb.rootSegNum
        
        # print " "
        