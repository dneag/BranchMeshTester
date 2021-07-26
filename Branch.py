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
    
        theGUI.branchCount += 1
        
        self.theGUI = theGUI
        self.rootSegNum = rootSegNum
        self.parentBranch = parentBranch
        self.segmentControls = []
        self.childBranches = []
        
        cmds.setParent(theGUI.mainColumn_LO)
        self.segmentScroll_LO_Name = "segmentScroll_LO_" + str(theGUI.branchCount)
        self.segmentScroll_LO = cmds.scrollLayout(self.segmentScroll_LO_Name, w=300,h=500, bgc=[.2,.2,.2], vis=False)
    
    def collectSegmentInfo(self):
    
        # makes a depth first traversal of the segments, collecting attributes at each
        
        for sc in self.segmentControls:
        
            if (sc.lateralBranch is not None):
            
                sc.lateralBranch.collectSegmentInfo()
        
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