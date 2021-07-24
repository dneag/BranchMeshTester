# BranchMeshTester_GUI.py
# defines GUI() class which creates the GUI for the BranchMesh Tester

import maya.cmds as cmds
from functools import partial

class GUI():

    def __init__(self):
        
        # Creates and displays the window and establishes all interface elements
        
        self.winName = "bmtWindow"
        self.dockName = "bmtDock"
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
        
        self.segmentScroll_LO = cmds.scrollLayout(w=300,h=500, bgc=[.2,.2,.2])
        
        self.rootBranch = Branch(0, None, self)
        self.rootBranch.activateBranchUI()
        
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
        
class Branch:

    # represents a chain of connected segments
    
    def __init__(self, rootSegNum, parentBranch, theGUI):
    
        self.theGUI = theGUI
        self.rootSegNum = rootSegNum
        self.segmentControls = []
        self.parentBranch = parentBranch
        self.childBranches = []
        cmds.setParent(theGUI.segmentScroll_LO)
        self.segmentRowCol_LO = cmds.rowColumnLayout(nc=8, cw=[ (1,40), (2,40), (3,40), (4,40), (5,20), (6,30), (7,45), (8,30) ], rs=[1,5], vis=False)
        
    def activateBranchUI(self):
        
        cmds.rowColumnLayout(self.segmentRowCol_LO, e=True, vis=True)
        branchNumber = self.calculateBranchNumber()
        cmds.text(self.theGUI.branchLabel, e=True, l=branchNumber)
        cmds.button(self.theGUI.addSegButton, e=True, command=self.makeSegmentControls)
        cmds.button(self.theGUI.removeSegButton, e=True, command=self.deleteSegmentControls)
        
        if (self.parentBranch is not None):
            cmds.button(self.theGUI.toParentBranchButton, e=True, vis=True)
        else:
            cmds.button(self.theGUI.toParentBranchButton, e=True, vis=False)
            
        cmds.button(self.theGUI.toParentBranchButton, e=True, command=self.toParentBranch)
        
    def locateAndActivate(self, rootSegNum, *_):
    
        for cb in self.childBranches:
            if (cb.rootSegNum == rootSegNum):
                cmds.rowColumnLayout(self.segmentRowCol_LO, e=True, vis=False) # hide this branch's layout before turning another on
                cb.activateBranchUI()
                
    def makeSegmentControls(self, *_):
    
        cmds.setParent(self.segmentRowCol_LO)        
        segmentNumber = len(self.segmentControls) + 1
        self.segmentControls.append(SegmentControls(self, segmentNumber))
    
    def deleteSegmentControls(self, *_):
    
        cmds.setParent(self.segmentRowCol_LO)

        if (len(self.segmentControls) > 0):
        
            # del does NOT call the destructor so we will delete the controls here
            seg = self.segmentControls[-1]
            cmds.deleteUI(seg.pol_FLD_Name, seg.azi_FLD_Name, seg.distance_FLD_Name, seg.radius_FLD_Name,
                seg.separator_Name, seg.checkBox_Name, seg.offSet_FLD_Name, seg.toBranchButton_Name)
                
            del self.segmentControls[-1] 
    
    def toParentBranch(self, *_):
    
        cmds.rowColumnLayout(self.segmentRowCol_LO, e=True, vis=False)
        self.parentBranch.activateBranchUI()
        
    def calculateBranchNumber(self):
        
        branchNumber = []
        self.getIndexInParentList(branchNumber)
        branchNumber.reverse()
        branchNumberAsString = "Branch " + str(branchNumber[0])
        for n in branchNumber[1:]:
            branchNumberAsString += ":" + str(n)
        
        return branchNumberAsString
       
    def getIndexInParentList(self, branchNumber):
     
       # each recursive iteration adds the index value of an ancestor branch to the branchNumber list, starting with the youngest
       
       if (self.parentBranch is not None):
           for i, childBranch in enumerate(self.parentBranch.childBranches):
               if (childBranch.rootSegNum == self.rootSegNum):
                   branchNumber.append(i + 1)
                   self.parentBranch.getIndexInParentList(branchNumber)
                   break
       else:
           branchNumber.append(1)
                    
class SegmentControls:

    # represents the controls used for defining a segment
    
    def __init__(self, homeBranch, segmentNumber):
    
        self.segmentNumber = segmentNumber
        homeBranch.theGUI.segmentControlsCount += 1
        totalSegs = homeBranch.theGUI.segmentControlsCount
        
        # names needed for cmds.deleteUI()
        self.pol_FLD_Name = "pol_FLD_" + str(totalSegs)
        self.azi_FLD_Name = "azi_FLD_" + str(totalSegs)
        self.distance_FLD_Name = "distance_FLD_" + str(totalSegs)
        self.radius_FLD_Name = "radius_FLD_" + str(totalSegs)
        self.separator_Name = "separator_" + str(totalSegs)
        self.checkBox_Name = "checkBox_" + str(totalSegs)
        self.offSet_FLD_Name = "offSet_FLD_" + str(totalSegs)
        self.toBranchButton_Name = "toBranchButton_" + str(totalSegs)
        
        self.pol_FLD = cmds.intField(self.pol_FLD_Name, v=0, min=0, max=359)
        self.azi_FLD = cmds.intField(self.azi_FLD_Name, v=0, min=0, max=359)
        self.distance_FLD = cmds.floatField(self.distance_FLD_Name, v=.3, pre=2, min=.01, max=3)
        self.radius_FLD = cmds.floatField(self.radius_FLD_Name, v=.3, pre=2, min=.01, max=3)
        self.separator = cmds.separator(self.separator_Name, style="none")
        self.checkBox = cmds.checkBox(self.checkBox_Name, l="", onc=partial(self.lateralBranch_On, homeBranch), ofc=partial(self.lateralBranch_Off, homeBranch))
        self.offSet_FLD = cmds.floatField(self.offSet_FLD_Name, v=.15, pre=2, min=.01, max=3, en=False)
        self.toBranchButton = cmds.button(self.toBranchButton_Name, l="->",en=False, bgc=[.4,.4,.4], command=partial(homeBranch.locateAndActivate, self.segmentNumber))
        
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
        