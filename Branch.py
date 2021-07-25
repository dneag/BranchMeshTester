# Branch.py
# defines the Branch class

import maya.cmds as cmds
from functools import partial

import SegmentControls
reload(SegmentControls)
from SegmentControls import SegmentControls

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