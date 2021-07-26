# SegmentControls.py
# defines the SegmentControls class

import maya.cmds as cmds
from functools import partial

import Branch
reload(Branch)
from Branch import Branch

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