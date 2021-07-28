# Branch.py
# defines the Branch class

import maya.cmds as cmds
from functools import partial

class Branch:

    # represents a chain of connected segments
    
    def __init__(self, rootSegNum, parentBranch, theGUI):
    
        theGUI.branchCount += 1
        
        self.theGUI = theGUI
        self.rootSegNum = rootSegNum
        self.parentBranch = parentBranch
        self.segmentControls = []
        self.childBranches = []
        
        cmds.setParent(theGUI.mainColumn_LO)
        self.segmentScroll_LO_Name = "segmentScroll_LO_" + str(theGUI.branchCount)
        self.segmentScroll_LO = cmds.scrollLayout(self.segmentScroll_LO_Name, w=300,h=500, bgc=[.2,.2,.2], vis=False)
    
    def collectSegmentAttributes(self, allBranches, segsPerBranch, indicesOfSegsOnParent, pols, azis, dists, rads, offsets):
        
        segsOnThisBranch = 0
        
        for sc in self.segmentControls:
            
            pols.append(cmds.intField(sc.pol_FLD, q=True, v=True))
            azis.append(cmds.intField(sc.azi_FLD, q=True, v=True))
            dists.append(cmds.floatField(sc.distance_FLD, q=True, v=True))
            rads.append(cmds.floatField(sc.radius_FLD, q=True, v=True))
            offsets.append(cmds.floatField(sc.offSet_FLD, q=True, v=True))
            
            if (sc.lateralBranch is not None):
            
                allBranches.append(sc.lateralBranch)
                indicesOfSegsOnParent.append(len(pols) - 1)

            segsOnThisBranch += 1
            
        segsPerBranch.append(segsOnThisBranch)
        
    def activateBranchUI(self):
        
        cmds.scrollLayout(self.segmentScroll_LO, e=True, vis=True)
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
                cmds.scrollLayout(self.segmentScroll_LO, e=True, vis=False)# hide this branch's layout before turning another on
                cb.activateBranchUI()
                
    def makeSegmentControls(self, *_):
    
        cmds.setParent(self.segmentScroll_LO)       
        segmentNumber = len(self.segmentControls) + 1
        self.segmentControls.append(SegmentControls(self, segmentNumber))
    
    def deleteSegmentControls(self, *_):
    
        cmds.setParent(self.segmentScroll_LO)

        if (len(self.segmentControls) > 0):
        
            # deleting SegmentControls also means deleting the segment's lateral branch if it has one
            if (self.segmentControls[-1].lateralBranch is not None):
                self.segmentControls[-1].deleteLateralBranch(self)
                
            # del does NOT call the destructor so we will delete the controls here
            cmds.deleteUI(self.segmentControls[-1].controlRowCol_LO_Name)
                
            del self.segmentControls[-1] 
    
    def toParentBranch(self, *_):
    
        cmds.scrollLayout(self.segmentScroll_LO, e=True, vis=False)
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
    
        self.segmentNumber = segmentNumber # the index + 1 of this segment on the branch
        self.lateralBranch = None
        
        homeBranch.theGUI.segmentControlsCount += 1
        totalSegs = homeBranch.theGUI.segmentControlsCount
        
        # segment control UI elements
        self.controlRowCol_LO_Name = "controlRowCol_LO_" + str(totalSegs)
        self.controlRowCol_LO = cmds.rowColumnLayout(self.controlRowCol_LO_Name, nc=8, cw=[ (1,40), (2,40), (3,40), (4,40), (5,20), (6,30), (7,45), (8,30) ], rs=[1,5])
        self.pol_FLD = cmds.intField(v=0, min=0, max=359)
        self.azi_FLD = cmds.intField(v=0, min=0, max=359)
        self.distance_FLD = cmds.floatField(v=.3, pre=2, min=.01, max=3)
        self.radius_FLD = cmds.floatField(v=.3, pre=2, min=.01, max=3)
        self.separator = cmds.separator(style="none")
        self.checkBox = cmds.checkBox(l="", onc=partial(self.lateralBranch_On, homeBranch), ofc=partial(self.lateralBranch_Off, homeBranch))
        self.offSet_FLD = cmds.floatField(v=.15, pre=2, min=.01, max=3, en=False)
        self.toBranchButton = cmds.button(l="->",en=False, bgc=[.4,.4,.4], command=partial(homeBranch.locateAndActivate, self.segmentNumber))
        
    def lateralBranch_On(self, homeBranch, checkBoxState):
    
        # turns on lateral branch controls and creates a new branch
        
        # enable the offset and toBranch button controls
        cmds.floatField(self.offSet_FLD, e=True, en=checkBoxState)
        cmds.button(self.toBranchButton, e=True, en=checkBoxState)
        
        # create a new Branch and appends it to the homeBranch's list of childBranches
        # childBranches is always in ascending order by the Branch's rootSegNum
        self.lateralBranch = Branch(self.segmentNumber, homeBranch, homeBranch.theGUI)
        homeBranch.childBranches.append(self.lateralBranch)
        homeBranch.childBranches[-1].makeSegmentControls()
        homeBranch.childBranches.sort(key=lambda branch: branch.rootSegNum)
        
        # for cb in homeBranch.childBranches:
        
            # print cb.rootSegNum
        
        # print " "
        
    def lateralBranch_Off(self, homeBranch, checkBoxState):
    
        # turns off lateral branch controls and removes the branch located on the segment
        
        # disable the offset and toBranch button controls
        cmds.floatField(self.offSet_FLD, e=True, en=checkBoxState)
        cmds.button(self.toBranchButton, e=True, en=checkBoxState)
          
        self.deleteLateralBranch(homeBranch)
                
        # for cb in homeBranch.childBranches:
        
            # print cb.rootSegNum
        
        # print " "
        
    def deleteLateralBranch(self, homeBranch):
    
        # removes the branch rooted at the segment corresponding to rootSegNum
        for i, cb in enumerate(homeBranch.childBranches):
            if cb.rootSegNum == self.segmentNumber:
                self.lateralBranch = None
                cmds.deleteUI(homeBranch.childBranches[i].segmentScroll_LO_Name)
                del homeBranch.childBranches[i]
                break