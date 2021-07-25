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
    
        self.segmentNumber = segmentNumber # the index + 1 of the segment on the branch
        
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
        
        # UI elements
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