import maya.cmds as cmds
import math
import random
import time
from collections import deque
from functools import partial
import os, os.path
# import angleFinder
# reload (angleFinder)
# import spaceRotator
# reload (spaceRotator)
# import lightVectors
# reload (lightVectors)
# import makinShaders
# reload (makinShaders)
# import blockPointGrid
# reload (blockPointGrid)

class GUI_Names :

    winName = "treeMaker_window"
    dockName = "treeMaker_dock"
        
#winName = "treeMaker_v29Window"
#dockName = "treeMaker_v29Dock"

global PI, PId2, PIm2, PHI
PI = 3.1415926
PId2 = 1.5707963
PIm2 = 6.2831853
PIandAHalf = 4.7123889
PHI = 1.6180339

# class A_Meristem:
#
#     def __init__(self, loc, vectorSum, pol, azi, branchAzi, pathSegs, orderParents, axialParent, rootSegIndx, lengthFromRoot, branchLength,
#                  segmentProgress, newSegs, lightCheck, orderChildren, axialChildren, nodeSiblings, descendants, ancestors, order, vigor, lightMult, orderInfluence,
#                  randomPullMult, randomPullChangeTime, xAreaAdded, baseOffSet, linkedPoints, lastSegLength, parentProximity, parentLengthAtRoot,
#                  age, budPolar, lsBudPolar, rootRelativePolar, collarReach, collarStrength, collarReachGain, collarStrengthGain, collarLimiters,
#                  collarStrengthenees, limiterSegments, pullForceVector, suppression, suppLimit, bakedSuppressedVigor, suppressionApplied, suppressionLevel,
#                  timeGradReach, nodeFreq, lsNodeFreq, lengthAtNextNode, lengthAtNextLSNode, merisIndebtedTo, hasGrowthDebt, timeOwed,
#                  cloneInfo, delay, lsShedLength, selfShedLength):
#
#         self.loc = loc
#         self.vectorSum = vectorSum
#         self.pol = pol
#         self.azi = azi
#         self.branchAzi = branchAzi
#         self.pathSegs = pathSegs
#         self.orderParents = orderParents
#         self.axialParent = axialParent
#         self.rootSegIndx = rootSegIndx
#         self.lengthFromRoot = lengthFromRoot
#         self.branchLength = branchLength
#         self.segmentProgress = segmentProgress
#         self.newSegs = newSegs
#         self.lightCheck = lightCheck
#         self.orderChildren = orderChildren
#         self.axialChildren = axialChildren
#         self.nodeSiblings = nodeSiblings
#         self.descendants = descendants
#         self.ancestors = ancestors
#         self.order = order
#         self.vigor = vigor
#         self.lightMult = lightMult
#         self.orderInfluence = orderInfluence
#         self.randomPullMult = randomPullMult
#         self.randomPullChangeTime = randomPullChangeTime
#         self.xAreaAdded = xAreaAdded
#         self.baseOffSet = baseOffSet
#         self.linkedPoints = linkedPoints
#         self.lastSegLength = lastSegLength
#         self.parentProximity = parentProximity
#         self.parentLengthAtRoot = parentLengthAtRoot
#         self.age = age
#         self.budPolar = budPolar
#         self.lsBudPolar = lsBudPolar
#         self.rootRelativePolar = rootRelativePolar
#         self.collarReach = collarReach
#         self.collarStrength = collarStrength
#         self.collarReachGain = collarReachGain
#         self.collarStrengthGain = collarStrengthGain
#         self.collarLimiters = collarLimiters
#         self.collarStrengthenees = collarStrengthenees
#         self.limiterSegments = limiterSegments
#         self.pullForceVector = pullForceVector
#         self.suppression = suppression
#         self.suppLimit = suppLimit
#         self.bakedSuppressedVigor = bakedSuppressedVigor
#         self.suppressionApplied = suppressionApplied
#         self.suppressionLevel = suppressionLevel
#         self.timeGradReach = timeGradReach
#         self.nodeFreq = nodeFreq
#         self.lsNodeFreq = lsNodeFreq
#         self.lengthAtNextNode = lengthAtNextNode
#         self.lengthAtNextLSNode = lengthAtNextLSNode
#         self.merisIndebtedTo = merisIndebtedTo
#         self.hasGrowthDebt = hasGrowthDebt
#         self.timeOwed = timeOwed
#         self.cloneInfo = cloneInfo
#         self.delay = delay
#         self.lsShedLength = lsShedLength
#         self.selfShedLength = selfShedLength

# class Segment:
#
#     def __init__(self, startPoint, vector, length, pol, azi, xArea, distalLength, distalWeight, modulus, pullForce, lengthFromRoot, basalLength, split, merisOnSeg,
#                  vectorSnapShot, prevAngsBtwnLmtrs, pathModIncrease, bpgIndices, bpLoc):
#
#         self.startPoint = startPoint
#         self.vector = vector
#         self.length = length
#         self.pol = pol
#         self.azi = azi
#         self.xArea = xArea
#         self.distalLength = distalLength
#         self.distalWeight = distalWeight
#         self.modulus = modulus
#         self.pullForce = pullForce
#         self.lengthFromRoot = lengthFromRoot
#         self.basalLength = basalLength
#         self.split = split
#         self.merisOnSeg = merisOnSeg
#         self.vectorSnapShot = vectorSnapShot
#         self.prevAngsBtwnLmtrs = prevAngsBtwnLmtrs
#         self.pathModIncrease = pathModIncrease
#         self.bpgIndices = bpgIndices
#         self.bpLoc = bpLoc

# class B_Segment:
#
#     def __init__(self, points, radius, topSegment, bottomSegment, shrinkPoints):
#
#         self.points = points
#         self.radius = radius
#         self.topSegment = topSegment
#         self.bottomSegment = bottomSegment
#         self.shrinkPoints = shrinkPoints

class Order:

    def __init__(self, earlyDelay, lateDelay, delayBlend, vigorTimeGradient, vGradientReach, rndVigorRng, selfSustained, lightInfluence, shadeTolerance, healthLossRate,
                 parentGrowthTillShed, suppressionGradient, suppReach, suppEffectGradient, nodeFreq, nodeFreqFluct, nfVigorLink, shootsPerNode, SPNFluct, nodeRotation,
                 nodeRotFluct, lsTgl, lsNodeFreqMin, lsNodeFreqMax, lsSPNMin, lsSPNMax, lsNodeRotMin, lsNodeRotMax, lsShedAge, lsShedLengthMin, lsShedLengthMax, lsShedFallOff,
                 lsISTime, lsISAge, cloneFreqMin, cloneFreqMax, cloneOrdInfl, cloneDelay, abortFreqMin, abortFreqMax, numTransfMeris, transfRng, DGT, DGTSides, xAreaAdded,
                 acGradientsReach, overallACGradReach, pullACGradient, weightACGradient, pullMult, pullSuppLink, PSStart, PSRange, pLossSuppLink, weightMult, gravitropism,
                 backRotation, straightenerStr, backRotationDelay, backRotationOffset, collarReach, collarStrength, collarReachGain, collarStrengthGain, collarLimitReach,
                 collarLimitAngle, sproutAzimuth, sproutToBase, baseAzimuth, collarJitter, pdDroop, pddPeak, pddEnd, windStrength, rippleStrength, blockPointsTgl, ignoreBPsTgl,
                 bpRes, bpSize, bpDensity, branchMeshTgl, skinRadius, segmentLength, sides, stripsTgl, stripWidth, stripTextureTgl, maturityRange, maturityGradient, bacMtrLink,
                 srMtrLink):

        self.earlyDelay = earlyDelay
        self.lateDelay = lateDelay
        self.delayBlend = delayBlend
        self.vigorTimeGradient = vigorTimeGradient
        self.vGradientReach = vGradientReach
        self.rndVigorRng = rndVigorRng
        self.selfSustained = selfSustained
        self.lightInfluence = lightInfluence
        self.shadeTolerance = shadeTolerance
        self.healthLossRate = healthLossRate
        self.parentGrowthTillShed = parentGrowthTillShed
        self.suppressionGradient = suppressionGradient
        self.suppReach = suppReach
        self.suppEffectGradient = suppEffectGradient
        self.nodeFreq = nodeFreq
        self.nodeFreqFluct = nodeFreqFluct
        self.nfVigorLink = nfVigorLink
        self.shootsPerNode = shootsPerNode
        self.SPNFluct = SPNFluct
        self.nodeRotation = nodeRotation
        self.nodeRotFluct = nodeRotFluct
        self.lsTgl = lsTgl
        self.lsNodeFreqMin = lsNodeFreqMin
        self.lsNodeFreqMax = lsNodeFreqMax
        self.lsSPNMin = lsSPNMin
        self.lsSPNMax = lsSPNMax
        self.lsNodeRotMin = lsNodeRotMin
        self.lsNodeRotMax = lsNodeRotMax
        self.lsShedAge = lsShedAge
        self.lsShedLengthMin = lsShedLengthMin
        self.lsShedLengthMax = lsShedLengthMax
        self.lsShedFallOff = lsShedFallOff
        self.lsISTime = lsISTime
        self.lsISAge = lsISAge
        self.cloneFreqMin = cloneFreqMin
        self.cloneFreqMax = cloneFreqMax
        self.cloneOrdInfl = cloneOrdInfl
        self.cloneDelay = cloneDelay
        self.abortFreqMin = abortFreqMin
        self.abortFreqMax = abortFreqMax
        self.numTransfMeris = numTransfMeris
        self.transfRng = transfRng
        self.DGT = DGT
        self.DGTSides = DGTSides
        self.xAreaAdded = xAreaAdded
        self.acGradientsReach = acGradientsReach
        self.overallACGradReach = overallACGradReach
        self.pullACGradient = pullACGradient
        self.weightACGradient = weightACGradient
        self.pullMult = pullMult
        self.pullSuppLink = pullSuppLink
        self.PSStart = PSStart
        self.PSRange = PSRange
        self.pLossSuppLink = pLossSuppLink
        self.weightMult = weightMult
        self.gravitropism = gravitropism
        self.backRotation = backRotation
        self.straightenerStr = straightenerStr
        self.backRotationDelay = backRotationDelay
        self.backRotationOffset = backRotationOffset
        self.collarReach = collarReach
        self.collarStrength = collarStrength
        self.collarReachGain = collarReachGain
        self.collarStrengthGain = collarStrengthGain
        self.collarLimitReach = collarLimitReach
        self.collarLimitAngle = collarLimitAngle
        self.sproutAzimuth = sproutAzimuth
        self.sproutToBase = sproutToBase
        self.baseAzimuth = baseAzimuth
        self.collarJitter = collarJitter
        self.pdDroop = pdDroop
        self.pddPeak = pddPeak
        self.pddEnd = pddEnd
        self.windStrength = windStrength
        self.rippleStrength = rippleStrength
        self.blockPointsTgl = blockPointsTgl
        self.ignoreBPsTgl = ignoreBPsTgl
        self.bpRes = bpRes
        self.bpSize = bpSize
        self.bpDensity = bpDensity
        self.branchMeshTgl = branchMeshTgl
        self.skinRadius = skinRadius
        self.segmentLength = segmentLength
        self.sides = sides
        self.stripsTgl = stripsTgl
        self.stripWidth = stripWidth
        self.stripTextureTgl = stripTextureTgl
        self.maturityRange = maturityRange
        self.maturityGradient = maturityGradient
        self.bacMtrLink = bacMtrLink
        self.srMtrLink = srMtrLink

# class CloneInfo:
#
#     def __init__(self, isClone, vigorPercent, original):
#
#         self.isClone = isClone
#         self.vigorPercent = vigorPercent
#         self.original = original

# def initiateLightVectors(*args):
#
#     global angleMatrix, lvInfoMatrix
#     #lightVectorInfo = lightVectors.initiate(1.,0.05,0.7,0.15) #old settings with close wall and ground
#     lightVectorInfo = lightVectors.initiate(1.,3.,3.,0.15) #parameters are radius, ground distance, wall distance, and wall height
#     angleMatrix = lightVectorInfo[0]
#     lvInfoMatrix = lightVectorInfo[1]

# def initiateBlockPointGrid(*args):
#
#     global BPG
#
#     BPG = blockPointGrid.create(16,24,16)

class GUI:

    def __init__(self):

        self.totalTime = 2
        
        guiNames = GUI_Names()
        if(cmds.window(guiNames.winName, exists=True)):
            cmds.deleteUI(guiNames.winName)
            print("Deleted existing main treeMaker window")
        if(cmds.dockControl(guiNames.dockName, exists=True)):
            cmds.deleteUI(guiNames.dockName)
            print("Deleted existing dock")

        self.mainWindow = cmds.window(guiNames.winName, title="treeMaker_v29", w=350, h=300)
        cmds.scrollLayout(w=420)
        self.LO1 = cmds.columnLayout(rs=5)
        cmds.rowColumnLayout(nc=3)
        #cmds.button(label="Initiate Light Vectors", w=100, command = initiateLightVectors)
        #cmds.button(label="Initiate Block Point Grid", w=200, command = initiateBlockPointGrid)
        #cmds.rowLayout(nc=2)
        cmds.button(label="Make Tree", w=100, h=30,command=self.prepareToBluePrint)
        cmds.button(label="Scale Man", w=80, h=20,command=self.makeScaleMan)
        cmds.rowColumnLayout(nc=2)
        cmds.button(label="Save Settings",w=80,h=20,command = self.saveSettings)
        self.presetNameFLD = cmds.textField()
        cmds.button(label="Load Settings",w=80,h=20)
        self.loadPresetButton = cmds.popupMenu(button=1)
        for presetFile in os.listdir('C:/Users/13308/Documents/maya/scripts/TreeMaker_Interface_Presets'):
            if presetFile.endswith(".txt"):
                cmds.menuItem(presetFile, l=presetFile,command=partial(self.loadSettings, presetFile))

        cmds.setParent("..")
        cmds.setParent("..")
        self.totalTimeFLD = cmds.intSliderGrp(v=self.totalTime, min=1,max=1000,field=True, label='Total Time', cw3=[68,30,200], ct3=["both", "both", "both"], co3=[5,0,5])
        #totalTimeFLD = totalTimeFLD.split('|')[-1]
        cmds.rowColumnLayout(nc=6,cw=[(2,40),(4,40),(6,20)],cs=[(1,3),(2,3),(3,3),(4,3),(5,3),(6,3)])
        #cmds.separator(st="in")
        cmds.setParent(self.LO1)
        self.LO3 = cmds.frameLayout(l="Vigor Distribution",cll=1,cl=1,w=420)
        #cmds.columnLayout(rs=5,cw=300)
        #cmds.text("Shoot Dispersion")
        #cmds.optionVar(remove='shootDispersionGradientOptionVar' )
        #cmds.optionVar(stringValueAppend=['shootDispersionGradientOptionVar', '0.,0.0,0'])
        #cmds.optionVar(stringValueAppend=['shootDispersionGradientOptionVar', '1.,0.98,0'])
        #cmds.gradientControlNoAttr( 'shootDispersionGradient', h=60, w=240)
        #cmds.gradientControlNoAttr( 'shootDispersionGradient', e=True, optionVar='shootDispersionGradientOptionVar' )
        cmds.rowColumnLayout(nc=6,cw=[(1,80),(2,35),(3,15),(4,40),(5,50)])
        cmds.text("Base Vigor")
        self.baseVigorFLD = cmds.floatField(v=.3,min=.05,max=100.,s=.1,pre=2)
        cmds.separator(hr=0, st="in")
        cmds.text(l="Range")
        self.globalGradientRangeFLD = cmds.floatField(v=400.,min=1.,max=10000.,s=1.,pre=1)
        cmds.setParent(self.LO3)
        self.GGGLO = cmds.columnLayout(w=300)
        self.readGlobalGrad = True
        self.gggovName = 'globalGrowthGradientOptionVar'
        #cmds.optionVar(remove='globalGrowthGradientOptionVar' )
        cmds.optionVar(stringValue=[self.gggovName, '.6,0.,3'])
        #cmds.optionVar(stringValueAppend=[self.gggovName, '.6,0.,3'])
        cmds.optionVar(stringValueAppend=[self.gggovName, '.88,.2,3'])
        cmds.optionVar(stringValueAppend=[self.gggovName, '1.,.3,3'])
        self.globalGrowthGradient = cmds.gradientControlNoAttr( 'globalGrowthGradient', h=60, w=300, cc=self.setReadGlobalGrad)
        cmds.gradientControlNoAttr( self.globalGrowthGradient, e=True, optionVar=self.gggovName )
        cmds.setParent(self.LO3)
        cmds.rowColumnLayout(nc=4,cw=[(1,100),(2,40),(3,100),(4,40)])
        cmds.text(l="Effect on Vigor")
        self.globGradVigorEffectFLD = cmds.floatField(v=1.,min=0.,max=1.,s=.01,pre=2)
        cmds.text(l="Effect on Reach")
        self.globGradReachEffectFLD = cmds.floatField(v=1.,min=0.,max=1.,s=.01,pre=2)
        cmds.setParent(self.LO1)
        self.LO4 = cmds.frameLayout(l="Order Controls",cll=1,cl=0,w=420,ec=self.orderUpdate)
        cmds.rowColumnLayout(nc=2,cw=[(1,90),(2,30)])
        cmds.text("Orders")
        self.ordersFLD = cmds.intField(v=2,min=1,max=4,s=1,cc=self.orderUpdate)
        cmds.setParent("..")
        self.earlyDelaysFLD_list, self.lateDelaysFLD_list, self.delayFalloffRngFLD_list, self.rndVigorRngsFLD_list = [], [], [], []
        self.lsShedAgeFLD_list, self.lsShedLengthMinsFLD_list, self.lsShedLengthMaxsFLD_list, self.lsShedFallOffFLD_list = [], [], [], []
        self.lsISTimeThreshFLD_list, self.lsISAgeThreshFLD_list = [], []
        self.cloneFreqMinFLD_list, self.cloneFreqMaxFLD_list, self.cloneOrderInflMinFLD_list, self.cloneOrderInflMaxFLD_list = [], [], [], []
        self.abortFreqMinFLD_list, self.abortFreqMaxFLD_list, self.numTransfMerisFLD_list, self.transfRangeFLD_list = [], [], [], []
        self.SPNMaxsFLD_list, self.nodeRotMaxsFLD_list, self.lsSPNMaxsFLD_list, self.lsNodeRotMaxsFLD_list = [], [], [], []
        self.vigorTimeGradientFLD_list, self.vGradientReachFLD_list, self.selfSustainedFLD_list, self.lightInfluenceFLD_list, self.shadeToleranceFLD_list, self.healthLossRateFLD_list, self.parentGrowthTillShedFLD_list, self.suppressionGradientFLD_list, self.suppReachFLD_list, self.suppEffectGradientFLD_list, self.nodeFreqMinsFLD_list, self.nodeFreqMaxsFLD_list, self.nodeFreqVigorLinksFLD_list, self.SPNMinsFLD_list, self.nodeRotMinsFLD_list, self.leafShootsOnOffFLD_list, self.lsNodeFreqMinsFLD_list, self.lsNodeFreqMaxsFLD_list, self.lsSPNMinsFLD_list, self.lsNodeRotMinsFLD_list, self.DGTropismFLD_list, self.DGTBaseShiftFLD_list = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        self.acGradientReachFLD_list, self.overallACGradientRangeFLD_list, self.pullACGradientFLD_list, self.weightACGradientFLD_list = [], [], [], []
        self.PSStartFLD_list, self.PSRangeFLD_list = [], []
        self.xAreaAddedFLD_list, self.pullForceFLD_list, self.pfSuppLinkFLD_list, self.pLossSuppLinkFLD_list, self.weightMultFLD_list, self.tropismRatioFLD_list, self.backRotationFLD_list, self.straightenerStrFLD_list, self.backRotationDelayFLD_list, self.backRotationOffsetFLD_list = [], [], [], [], [], [], [], [], [], []
        self.collarReachFLD_list, self.collarStrengthFLD_list, self.collarReachGainFLD_list, self.collarStrengthGainFLD_list, self.collarLimitReachFLD_list, self.collarLimitAngleFLD_list, self.sproutAziFLD_list, self.sproutToBaseFLD_list, self.baseAziFLD_list, self.collarJitterPolFLD_list, self.collarJitterAziFLD_list, self.pdDroopFLD_list, self.pddPeakFLD_list, self.pddEndFLD_list, self.windStrengthFLD_list, self.rippleStrengthFLD_list, self.blockPointsOnOffFLD_list, self.ignoreBPointsFLD_list, self.bpResFLD_list, self.bpSizeFLD_list, self.bpDensityFLD_list, self.createBranchMeshChBox_list, self.skinRadiusFLD_list, self.segLengthFLD_list, self.sidesFLD_list = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        self.stripsOnOffFLD_list, self.leafStripWidthFLD_list, self.textureOnOffFLD_list, self.maturityRngFLD_list, self.maturityGradientFLD_list = [], [], [], [], []
        self.bacMaturityLinkFLD_list, self.suppReachMaturityLinkFLD_list = [], []
        self.vtgReadToggles, self.sgReadToggles, self.segReadToggles, self.pullGradReadToggles, self.weightGradReadToggles, self.matGradReadToggles = [], [], [], [], [], []
        self.vtgValues, self.sgValues, self.segValues,  self.pullGValues, self.weightGValues, self.matGValues = [[],[],[],[],[]], [[],[],[],[]], [[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]]

        #Initialize gui field values
        self.initVigorGradientInfos = [['vigorTimeGradient1OptionVar', '.6,0.,3','.7,.09,3','1.,.16,3','.88,.8,3','.53,.91,3','0.,1.,3'],
                                  ['vigorTimeGradient2OptionVar','.8,0.,3','1.,.15,3'],
                                  ['vigorTimeGradient3OptionVar','0.780488,0,3,','0,1,3,','0.853659,0.62,3',',0.390244,0.895,3',',1,0.13,3'],
                                  ['vigorTimeGradient4OptionVar','.15,0.,3','0.,1.,3'],
                                  ['vigorTimeGradient5OptionVar','.45,0.,3','.12,.09,3','0.,1.,3']]
        initTimeGradReaches, initRndVigorMults, initSelfSust, initLightInfluence = [333.,333.,200.,160.,40.], [0.,0.,0.,0.,.1], [.05,.05,.2,.05,.8], [1.,1.,1.,1.,1.]
        initShadeTolerances, initHealthLossRates, initParentGrowthTillSheds = [.7,.7,.7,.7,.7], [.01,.01,.01,.01,.01], [3.,3.,3.,3.,3.]
        self.initSuppGradientInfos = [['suppressionGradient1OptionVar','0.8,0.,3','.46,.17,3','0.23,.4,3','.2,1.,3'],
                                 ['suppressionGradient2OptionVar','.7,0.,3','.34,.2,3','.15,.41,3','0.,1.,3'],
                                 ['suppressionGradient3OptionVar','1.,0.,3','0.,1.,3'],
                                 ['suppressionGradient4OptionVar','1.,0.,3','0.,1.,3']]
        initSuppReaches = [96.,4.,4.,4.]
        self.initSuppEffectGradientInfos = [['suppEffectGradient1OptionVar','1.,0.,3','.93,.8,3','.61,.93,3','0.,1.,3'],
                                       ['suppEffectGradient2OptionVar','1.,0.,3','1.,1.,3'],
                                       ['suppEffectGradient3OptionVar','1.,0.,3','1.,1.,3'],
                                       ['suppEffectGradient4OptionVar','1.,0.,3','1.,1.,3']]
        initACGradientReaches, initOverallACRngs = [10.,2.,2.,2.,2.], [100.,225.,40.,80.,15.]
        self.initPullACGradientInfos = [['pullACGradient1OptionVar','.42,0.,3','.25,.06,3','.1,.25,3','0.,1.,3'],
                                   ['pullACGradient2OptionVar','1.,0.,3','.4,.2,3','.2,.4,3','0.,1.,3'],
                                   ['pullACGradient3OptionVar','1.,0.,3','.5,.4,3','0.,1.,3'],
                                   ['pullACGradient4OptionVar','.1,0.,3'],
                                   ['pullACGradient5OptionVar','1,0,3','0,1,3','0.5,0.215625,3','0.142857,0.521875,3']]
        self.initWeightACGradientInfos = [['weightACGradient1OptionVar','.5,0.,3','.2,.13,3','.05,.4,3','0.,1.,3'],
                                     ['weightACGradient2OptionVar','.2,0.,3','.21,.31,3','.7,.55,3','0.,1.,3'],
                                     ['weightACGradient3OptionVar','.5,0.,3','.5,.8,3','0.,1.,3'],
                                     ['weightACGradient4OptionVar','.1,0.,3'],
                                     ['weightACGradient5OptionVar','0.5,0,3','0.4,0.8,3','0,1,3']]
        initEarlyDelays, initLateDelays, initDelayFalloffs = [0.,0.,0.,0.,0.], [0.,0.,0.,0.,0.], [0.,0.,100.,0.,0.]
        initNodeFreqMins, initNodeFreqMaxs, initNodeFreqVigorLinks, initSPNMins, initSPNMaxs = [4.,.2,4.,2.], [4.,.2,4.,2.], [1.85,0.,1.,1.], [1,1,1,1], [1,1,1,1]
        initNodeRotMins, initNodeRotMaxs = [0.,3.14,1.8,1.8], [0.,3.14,2.3,2.3]
        initCloneFreqMins, initCloneFreqMaxs, initCloneOrderInflMins, initCloneOrderInflMaxs = [999.,999.,999.,999.,999.], [999.,999.,999.,999.,999.], [1.,.7,.7,.7,1.], [1.,.9,.9,.9,.9]
        initAbortFreqMins, initAbortFreqMaxs, initNumTransfMeris, initTransfRanges = [9999.,.5,9999.,9999.,9999.], [9999.,.5,9999.,9999.,9999.], [1,1,1,1,1], [5.,3.,3.,3.,3.]
        initLSOnOff, initLSNodeFreqMins, initLSNodeFreqMaxs = [0,0,0,1], [1.,.01,.01,1.], [1.,.03,.03,1.]
        initLSSPNMins, initLSSPNMaxs, initLSNodeRotMins, initLSNodeRotMaxs = [0,1,1,1], [0,1,1,1], [3.14,3.14,3.14,3.14], [3.14,3.14,3.14,3.14]
        initLSShedLengthMins, initLSShedLengthMaxs, initLSShedFallOffs, initLSShedAge = [4.5,2.5,.9,4.5], [5.5,3.,1.2,5.5], [2.,.7,.3,2.], [20,20,20,20]
        initLSISTimeThresh, initLSISAgeThresh = [30,30,30,30,30], [40.,40.,40.,40.,40.]
        initxAreaAddeds, initSolidificationStarts, initSolidificationRanges = [.01,.01,.002,.002,.003], [1.,60.,40.,2.,3.], [2.,2.,2.,2.,2.]
        initDGTs, initDGTBaseShifts, initPullForces, initPFSuppLinks, initPLossSuppLinks = [0.,0.,1.,1.,1.], [0.,.4,.3,0.,.785],[.39,.022,.05,.09,1.6], [0.,.4,0.,0.,.1], [0.,1.,0.,0.,.3]
        initWeightMults, initGravitropisms, initBackRotations, initStraightenerStrs = [0.,.03,.05,.03,2.], [.9,.02,.05,.5,1.], [0.,0.,.0,0.,0.], [0.,1.5,1.,0.,0.]
        initBackRotDlys, initBackRotOffsets, initCollarReaches, initCollarStrengths = [0.,.07,.1,0.,0.], [1.,.15,.15,1.,1.], [0.,0.,0.,0.,.5], [0.,1.,1.,.5,.5]
        initCollarReachGains, initCollarStrengthGains, initCollarLimitReaches, initCollarLimitAngles = [.0,.45,.2,.0,0.], [.0,.0,.0,.0,0.], [1.,1.,1.,1.,1.], [.3,.3,.3,.3,.3]
        initSproutAzis, initSproutToBases, initBaseAzis =  [1.2,.7,1.,1.1,1.35], [3.,2.6,2.,3.,3.], [1.2,1.3,1.2,1.1,1.35]
        initClrJitterP, initClrJitterA, initPDDroops, initPDDPeaks, initPDDEnds = [0.,0.,.1,0.,.1], [0.,0.,.05,0.,.05], [0.,0.,0.,0.,0.], [0.,.6,0.,0.,0.], [0.,1.5,0.,0.,0.]
        initWindStrengths, initRippleStrengths = [0.,1.,0.,0.,0.], [0.,1.,0.,0.,0.]
        initBlockPointsChBox, initIgnoreBPs, initBPRes, initBPSizes, initBPDensities = [1,1,0,0,0], [0,0,0,0,1], [1,1,1,1,5], [.3,.3,.3,.3,.2], [1.,1.,1.,1.,1.]
        initCreateBranchMeshChBox, initSkinRadii, initSegLengths, initSides, initStripsOnOff = [1,1,1,0,1], [.001,.0001,.0001,.0001,.005], [.3,.1,.1,.1,.1], [8,8,8,8,4], [0,0,0,1,0]
        initLeafStripWidths, initTexturedChBox, initMaturityRanges  = [.4,.35,.25,.25,.25], [0,0,0,0,0], [400.,400.,400.,400.,400.]
        self.initMaturityGradientInfos = [['maturityGradient1OptionVar','.38,0.,3','.5,0.09,3','1.,.23,3'],
                                     ['maturityGradient2OptionVar','.35,0.,3','.5,.05,3','1.,.09,3'],
                                     ['maturityGradient3OptionVar','1.,0.,3','1.,1.,3'],
                                     ['maturityGradient4OptionVar','1.,0.,3','1.,1.,3'],
                                     ['maturityGradient5OptionVar','1.,0.,3','1.,1.,3']]
        initBACMtrLinks, initSuppReachMtrLinks = [0.,6.,0.,0.,0.], [-1.5,0.,0.,0.,0.]

        #Done initializing gui field values

        self.orderFrameLayouts_list = []
        self.previousOrderCount = 2 #set to 2 because the default orderCount is currently 2. - does not include leaf order
        for order in range(5):
            if order == 4:
                cmds.frameLayout(l="Leaf Shoots",cll=1,cl=1)
            else:
                if order <= 1:
                    self.orderFrameLayouts_list.append(cmds.frameLayout(l="Order " + str(order+1),cll=1,cl=1))
                else:
                    #for now, by default we start with 2 orders plus leaf shoots, layouts for additional orders are created but are invisible
                    self.orderFrameLayouts_list.append(cmds.frameLayout(l="Order " + str(order+1),cll=1,cl=1, vis=0))
            cmds.rowColumnLayout(nc=6,cw=[(1,20),(2,40),(3,20),(4,40),(5,20),(6,40)])
            cmds.text(l="edl")
            self.earlyDelaysFLD_list.append(cmds.floatField(v=initEarlyDelays[order],min=0.,max=10000.,s=.1,pre=2))
            cmds.text(l="ldl")
            self.lateDelaysFLD_list.append(cmds.floatField(v=initLateDelays[order],min=0.,max=10000.,s=.1,pre=2))
            cmds.text(l="dfo")
            self.delayFalloffRngFLD_list.append(cmds.floatField(v=initDelayFalloffs[order],min=0.,max=10000.,s=.1,pre=2))
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=4,cw=[(1,180),(2,40),(3,30),(4,40)])
            cmds.text(l="Vigor/Time Gradient Range:")
            self.vGradientReachFLD_list.append(cmds.floatField(v=initTimeGradReaches[order],min=0.,max=5000,s=1.,pre=1))
            cmds.text(l="rvg")
            self.rndVigorRngsFLD_list.append(cmds.floatField(v=initRndVigorMults[order],min=0.,max=1.,pre=2))
            cmds.setParent("..")
            cmds.rowLayout(h=57,nc=2,cw=[(1,225),(2,80)])
            cmds.columnLayout(w=225)
            self.vtgReadToggles.append(True)
            cmds.optionVar(remove=self.initVigorGradientInfos[order][0] )
            for gradInfo in self.initVigorGradientInfos[order][1:]:

                cmds.optionVar(stringValueAppend=[self.initVigorGradientInfos[order][0], gradInfo])

            gradientName = "vigorTimeGradient" + str(order)
            self.vigorTimeGradientFLD_list.append(cmds.gradientControlNoAttr(gradientName, h=65, w=220, cc=partial(self.setReadVTG, order)))
            cmds.gradientControlNoAttr( self.vigorTimeGradientFLD_list[-1], e=True, optionVar=self.initVigorGradientInfos[order][0] )
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=6,cw=[(1,23),(2,35),(3,21),(4,35),(5,20),(6,35)])
            cmds.text(l="ss")
            self.selfSustainedFLD_list.append(cmds.floatField(v=initSelfSust[order],min=0.,max=10.,s=.01,pre=2))
            cmds.text(l="li")
            self.lightInfluenceFLD_list.append(cmds.floatField(v=initLightInfluence[order],min=0.,max=1.,s=.1,pre=2))
            cmds.text(l="stl")
            self.shadeToleranceFLD_list.append(cmds.floatField(v=initShadeTolerances[order],min=0.,max=1.,s=.1,pre=2))
            cmds.text(l="hlr")
            self.healthLossRateFLD_list.append(cmds.floatField(v=initHealthLossRates[order],min=0.,max=10000.,s=.1,pre=2))
            cmds.text(l="gts")
            self.parentGrowthTillShedFLD_list.append(cmds.floatField(v=initParentGrowthTillSheds[order],min=0., max=10000.,s=.1,pre=2))
            cmds.setParent("..")
            cmds.setParent("..")
            if order < 4:
                cmds.rowLayout(h=57,nc=3,cw=[(1,225),(2,70),(3,30)])
                cmds.columnLayout(w=225)
                self.sgReadToggles.append(True)
                cmds.optionVar(remove=self.initSuppGradientInfos[order][0])
                for gradInfo in self.initSuppGradientInfos[order][1:]:

                    cmds.optionVar(stringValueAppend=[self.initSuppGradientInfos[order][0], gradInfo])

                gradientName = "suppressionGradient" + str(order)
                self.suppressionGradientFLD_list.append(cmds.gradientControlNoAttr(gradientName, h=65, w=220, cc=partial(self.setReadSG, order)))
                cmds.gradientControlNoAttr(self.suppressionGradientFLD_list[-1], e=True, optionVar=self.initSuppGradientInfos[order][0] )
                cmds.setParent("..")
                cmds.text(l="Supp Reach")
                self.suppReachFLD_list.append(cmds.floatField(v=initSuppReaches[order],min=0.,max=1000.,s=.1,pre=2))
                cmds.setParent("..")
                cmds.rowLayout(h=57,nc=3,cw=[(1,225),(2,70),(3,30)])
                self.segReadToggles.append(True)
                cmds.optionVar(remove=self.initSuppEffectGradientInfos[order][0])
                for gradInfo in self.initSuppEffectGradientInfos[order][1:]:

                    cmds.optionVar(stringValueAppend=[self.initSuppEffectGradientInfos[order][0], gradInfo])

                self.suppEffectGradientFLD_list.append(cmds.gradientControlNoAttr(h=65, w=220, cc=partial(self.setReadSEG, order)))
                cmds.gradientControlNoAttr(self.suppEffectGradientFLD_list[-1], e=True, optionVar=self.initSuppEffectGradientInfos[order][0] )
                cmds.setParent("..")
                cmds.rowColumnLayout(nc=13,cw=[(1,20),(2,40),(3,40),(4,20),(5,37),(6,40),(7,20),(8,20),(9,25),(10,30),(11,30),(12,30)])
                cmds.text(l="nf")
                self.nodeFreqMinsFLD_list.append(cmds.floatField(v=initNodeFreqMins[order],min=0.,max=1000.,s=1.,pre=3))
                self.nodeFreqMaxsFLD_list.append(cmds.floatField(v=initNodeFreqMaxs[order],min=0.,max=1000.,s=0.1,pre=3))
                cmds.text(l="vl")
                self.nodeFreqVigorLinksFLD_list.append(cmds.floatField(v=initNodeFreqVigorLinks[order],min=0.,max=100.,s=.1,pre=2))
                cmds.text(l="smn")
                self.SPNMinsFLD_list.append(cmds.intField(v=initSPNMins[order],min=0,max=100,s=1))
                cmds.text(l="smx")
                self.SPNMaxsFLD_list.append(cmds.intField(v=initSPNMaxs[order],min=0,max=100,s=1))
                cmds.text(l="nrn")
                self.nodeRotMinsFLD_list.append(cmds.floatField(v=initNodeRotMins[order],min=0.,max=PIm2,s=.01,pre=2))
                cmds.text(l="nrx")
                self.nodeRotMaxsFLD_list.append(cmds.floatField(v=initNodeRotMaxs[order],min=0.,max=PIm2,s=.01,pre=2))
                cmds.setParent("..")
                cmds.columnLayout(co=("left", 113))
                self.leafShootsOnOffFLD_list.append(cmds.checkBox(l="Leaf Shoots",v=initLSOnOff[order]))
                cmds.setParent("..")
                cmds.rowColumnLayout(nc=12,cw=[(1,30),(2,40),(3,30),(4,35),(5,37),(6,40),(7,30),(8,20),(9,25),(10,35),(11,20),(12,35)])
                cmds.text(l="lfn")
                self.lsNodeFreqMinsFLD_list.append(cmds.floatField(v=initLSNodeFreqMins[order],min=0.,max=1000.,s=1.,pre=3))
                cmds.text(l="lfx")
                self.lsNodeFreqMaxsFLD_list.append(cmds.floatField(v=initLSNodeFreqMaxs[order],min=0.,max=1000.,s=0.1,pre=3))
                cmds.text(l="lsn")
                self.lsSPNMinsFLD_list.append(cmds.intField(v=initLSSPNMins[order],min=0,max=100,s=1))
                cmds.text(l="lsx")
                self.lsSPNMaxsFLD_list.append(cmds.intField(v=initLSSPNMaxs[order],min=0,max=100,s=1))
                cmds.text(l="lrn")
                self.lsNodeRotMinsFLD_list.append(cmds.floatField(v=initLSNodeRotMins[order],min=0.,max=PIm2,s=.01,pre=2))
                cmds.text(l="lrx")
                self.lsNodeRotMaxsFLD_list.append(cmds.floatField(v=initLSNodeRotMaxs[order],min=0.,max=PIm2,s=.01,pre=2))
                cmds.text(l="lsa")
                self.lsShedAgeFLD_list.append(cmds.floatField(v=initLSShedAge[order],min=1.,max=10000.,s=1.,pre=0))
                cmds.text(l="sln")
                self.lsShedLengthMinsFLD_list.append(cmds.floatField(v=initLSShedLengthMins[order],min=0.,max=1000.,s=1.,pre=2))
                cmds.text(l="slx")
                self.lsShedLengthMaxsFLD_list.append(cmds.floatField(v=initLSShedLengthMaxs[order],min=0.0,max=1000.,s=.1,pre=2))
                cmds.text(l="slf")
                self.lsShedFallOffFLD_list.append(cmds.floatField(v=initLSShedFallOffs[order],min=0.,max=1000.,s=.1,pre=2))
                cmds.text(l="ist")
                self.lsISTimeThreshFLD_list.append(cmds.intField(v=initLSISTimeThresh[order],min=0,max=10000,s=1))
                cmds.text(l="isa")
                self.lsISAgeThreshFLD_list.append(cmds.floatField(v=initLSISAgeThresh[order],min=0.,max=10000.,s=1.,pre=0))
                cmds.setParent("..")
            cmds.rowColumnLayout(nc=12,cw=[(1,30),(2,40),(3,30),(4,35),(5,30),(6,35),(7,25),(8,35),(9,30),(10,40),(11,30),(12,35)])
            cmds.text(l="cln")
            self.cloneFreqMinFLD_list.append(cmds.floatField(v=initCloneFreqMins[order],min=0.,max=9999.,s=.01,pre=2))
            cmds.text(l="clx")
            self.cloneFreqMaxFLD_list.append(cmds.floatField(v=initCloneFreqMaxs[order],min=0.,max=9999.,s=.01,pre=2))
            cmds.text(l="oin")
            self.cloneOrderInflMinFLD_list.append(cmds.floatField(v=initCloneOrderInflMins[order],min=0.01,max=1.,s=.01,pre=2))
            cmds.text(l="oix")
            self.cloneOrderInflMaxFLD_list.append(cmds.floatField(v=initCloneOrderInflMaxs[order],min=0.01,max=1.,s=.01,pre=2))
            cmds.text(l="abn")
            self.abortFreqMinFLD_list.append(cmds.floatField(v=initAbortFreqMins[order],min=.1,max=10000.,s=.1,pre=2))
            cmds.text(l="abx")
            self.abortFreqMaxFLD_list.append(cmds.floatField(v=initAbortFreqMaxs[order],min=.1,max=10000.,s=.1,pre=2))
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=12,cw=[(1,30),(2,40),(3,30),(4,35),(5,35),(6,25),(7,30),(8,20),(9,30),(10,40),(11,30),(12,35)])
            cmds.text(l="ntm")
            self.numTransfMerisFLD_list.append(cmds.intField(v=initNumTransfMeris[order],min=0,max=10000,s=1))
            cmds.text(l="trg")
            self.transfRangeFLD_list.append(cmds.floatField(v=initTransfRanges[order],min=.01,max=100000.,s=.1,pre=2))
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=10,cw=[(1,30),(2,35),(3,45),(4,35),(5,35),(6,35),(7,40),(8,40),(9,15),(10,40)])
            visible = 1
            if order == 0:
                visible = 0
            cmds.text(l="saz", vis=visible)
            self.sproutAziFLD_list.append(cmds.floatField(v=initSproutAzis[order],min=0.,max=2.8,s=.01,pre=2, vis=visible))
            cmds.text(l="stb", vis=visible)
            self.sproutToBaseFLD_list.append(cmds.floatField(v=initSproutToBases[order],min=0.1,max=10000.,s=.01,pre=2, vis=visible))
            cmds.text(l="baz", vis=visible)
            self.baseAziFLD_list.append(cmds.floatField(v=initBaseAzis[order],min=0.,max=2.8,s=.01,pre=2, vis=visible))
            cmds.text(l="Jitt: P", vis=visible)
            self.collarJitterPolFLD_list.append(cmds.floatField(v=initClrJitterP[order],min=0.,max=1000.,s=.01,pre=2, vis=visible))
            cmds.text(l="A", vis=visible)
            self.collarJitterAziFLD_list.append(cmds.floatField(v=initClrJitterA[order],min=0.,max=1000.,s=.01,pre=2, vis=visible))
            cmds.text(l="DGT", vis=visible)
            self.DGTropismFLD_list.append(cmds.floatField(v=initDGTs[order],min=0.,max=1.,s=.01,pre=2, vis=visible))
            cmds.text(l="DGT BS", vis=visible)
            self.DGTBaseShiftFLD_list.append(cmds.floatField(v=initDGTBaseShifts[order],min=0.,max=1.3,s=.01,pre=2, vis=visible))
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=6,cw=[(1,85),(2,35),(3,75),(4,45),(5,60),(6,40)])
            cmds.text(l="xArea Added")
            self.xAreaAddedFLD_list.append(cmds.floatField(v=initxAreaAddeds[order],min=0.,max=5.,s=.001,pre=4))
            cmds.setParent("..")
            cmds.separator()
            cmds.columnLayout(rs=5)
            cmds.rowColumnLayout(nc=8,cw=[(1,35),(2,40),(3,45),(4,40),(5,40),(6,40)])
            cmds.text(l="Pull")
            self.pullForceFLD_list.append(cmds.floatField(v=initPullForces[order],min=0.,max=100.,s=.01,pre=3))
            cmds.text(l="Range")
            self.acGradientReachFLD_list.append(cmds.floatField(v=initACGradientReaches[order],min=0.,max=10000.,s=1.,pre=2))
            cmds.text(l="Grav")
            self.tropismRatioFLD_list.append(cmds.floatField(v=initGravitropisms[order],min=0.,max=1.,s=.1,pre=2))
            cmds.setParent("..")
            self.pullGradReadToggles.append(True)
            cmds.optionVar(remove=self.initPullACGradientInfos[order][0] )
            for gradInfo in self.initPullACGradientInfos[order][1:]:

                cmds.optionVar(stringValueAppend=[self.initPullACGradientInfos[order][0], gradInfo])

            self.pullACGradientFLD_list.append(cmds.gradientControlNoAttr(h=80, w=340, cc=partial(self.setReadPullG, order)))
            cmds.gradientControlNoAttr( self.pullACGradientFLD_list[-1], e=True, optionVar=self.initPullACGradientInfos[order][0] )
            cmds.rowColumnLayout(nc=7, cw=[(1,50),(2,40),(3,40),(4,40),(5,40),(6,60),(7,40)])
            cmds.text("Sld rng")
            self.PSStartFLD_list.append(cmds.floatField(v=initSolidificationStarts[order],min=0.,max=10000.,s=.1,pre=2))
            self.PSRangeFLD_list.append(cmds.floatField(v=initSolidificationRanges[order],min=0.,max=10000.,s=.1,pre=2))
            cmds.text(l="spLnk")
            self.pfSuppLinkFLD_list.append(cmds.floatField(v=initPFSuppLinks[order],min=0.,max=1.,s=.01,pre=2))
            cmds.text(l="lossSpLnk")
            self.pLossSuppLinkFLD_list.append(cmds.floatField(v=initPLossSuppLinks[order],min=0.,max=100.,s=.1,pre=2))
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=4, cw=[(1,50),(2,40),(3,50),(4,40)])
            cmds.text(l="Weight")
            self.weightMultFLD_list.append(cmds.floatField(v=initWeightMults[order],min=0.,max=1000.,s=.1,pre=3))
            cmds.text(l="Range")
            self.overallACGradientRangeFLD_list.append(cmds.floatField(v=initOverallACRngs[order],min=0.,max=10000.,s=.1,pre=1))
            cmds.setParent("..")
            self.weightGradReadToggles.append(True)
            cmds.optionVar(remove=self.initWeightACGradientInfos[order][0] )
            for gradInfo in self.initWeightACGradientInfos[order][1:]:

                cmds.optionVar(stringValueAppend=[self.initWeightACGradientInfos[order][0], gradInfo])

            self.weightACGradientFLD_list.append(cmds.gradientControlNoAttr(h=80, w=340, cc=partial(self.setReadWeightG, order)))
            cmds.gradientControlNoAttr( self.weightACGradientFLD_list[-1], e=True, optionVar=self.initWeightACGradientInfos[order][0] )
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=8,cw=[(1,30),(2,40),(3,30),(4,40),(5,30),(6,40),(7,30),(8,40)], co=[(1,"left",10)], rs=(2,5))
            cmds.text(l="br")
            self.backRotationFLD_list.append(cmds.floatField(v=initBackRotations[order],min=0.,max=10.,s=.1,pre=3))
            cmds.text(l="sst")
            self.straightenerStrFLD_list.append(cmds.floatField(v=initStraightenerStrs[order],min=0.,max=1000.,s=.1,pre=3))
            cmds.text(l="brd")
            self.backRotationDelayFLD_list.append(cmds.floatField(v=initBackRotDlys[order],min=0.,max=1.,s=.1,pre=3))
            cmds.text(l="bro")
            self.backRotationOffsetFLD_list.append(cmds.floatField(v=initBackRotOffsets[order],min=0.,max=1.,s=.1,pre=3))
            #cmds.text(l="Wt Resist")
            #self.weightResFLD_list.append(cmds.floatField(v=initWeightRes[order],min=0.,max=10000.,s=.1,pre=2))
            #cmds.text(l="Mod Mult")
            #self.modMultFLD_list.append(cmds.floatField(v=initModMults[order],min=0.,max=10000.,s=.1,pre=2))
            #cmds.text(l="Min Mod")
            #self.minModFLD_list.append(cmds.floatField(v=initMinMods[order],min=.001,max=10000.,s=.01,pre=2))
            #cmds.text(l="Dry Rate")
            #self.dryRateFLD_list.append(cmds.floatField(v=initDryRates[order],min=0.,max=100.,s=.01,pre=2))
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=4,cw=[(1,120),(2,45),(3,115),(4,45)])
            cmds.text(l="Init Collar Reach")
            self.collarReachFLD_list.append(cmds.floatField(v=initCollarReaches[order],min=0.,max=10000.,s=.1,pre=2))
            cmds.text(l="Init Collar Strength")
            self.collarStrengthFLD_list.append(cmds.floatField(v=initCollarStrengths[order],min=0.,max=1000.,s=.1,pre=3))
            cmds.text(l="Collar Reach Gain")
            self.collarReachGainFLD_list.append(cmds.floatField(v=initCollarReachGains[order],min=0.,max=1000.,s=.1,pre=3))
            cmds.text(l="Collar Strength Gain")
            self.collarStrengthGainFLD_list.append(cmds.floatField(v=initCollarStrengthGains[order],min=0.,max=1000.,s=.01,pre=3))
            cmds.text(l="Limit Reach")
            self.collarLimitReachFLD_list.append(cmds.floatField(v=initCollarLimitReaches[order],min=0.,max=10000.,s=.1,pre=2))
            cmds.text(l="Limit Angle")
            self.collarLimitAngleFLD_list.append(cmds.floatField(v=initCollarLimitAngles[order],min=0.,max=1000.,s=.1,pre=2))
            cmds.setParent("..")
            cmds.separator()
            cmds.rowColumnLayout(nc=6,cw=[(1,70),(2,40),(3,40),(4,35),(5,35),(6,35)], co=[(1,"left",10)])
            cmds.text(l="PD Droop")
            self.pdDroopFLD_list.append(cmds.floatField(v=initPDDroops[order],min=0.,max=10000.,s=.01,pre=3))
            cmds.text(l="peak")
            self.pddPeakFLD_list.append(cmds.floatField(v=initPDDPeaks[order],min=0.,max=10000.,s=.01,pre=2))
            cmds.text(l="end")
            self.pddEndFLD_list.append(cmds.floatField(v=initPDDEnds[order],min=0.,max=10000.,s=.01,pre=2))
            cmds.text(l="Wind Str")
            self.windStrengthFLD_list.append(cmds.floatField(v=initWindStrengths[order],min=0.,max=5.,s=.01,pre=1))
            cmds.text(l="rps")
            self.rippleStrengthFLD_list.append(cmds.floatField(v=initRippleStrengths[order], min=0.,max=10.,s=.1,pre=1))
            cmds.setParent("..")
            cmds.separator()
            cmds.rowColumnLayout(nc=8,cw=[(1,60),(2,60),(3,40),(4,30),(5,35),(6,30),(7,35),(8,30)],co=[(1,"left",10)])
            self.blockPointsOnOffFLD_list.append(cmds.checkBox(l="bp's", v=initBlockPointsChBox[order]))
            self.ignoreBPointsFLD_list.append(cmds.checkBox(l="ign bp's", v=initIgnoreBPs[order]))
            cmds.text(l="res")
            self.bpResFLD_list.append(cmds.intField(v=initBPRes[order],min=1,max=1000,s=1))
            cmds.text(l="size")
            self.bpSizeFLD_list.append(cmds.floatField(v=initBPSizes[order],min=.1,max=1000.,s=.1,pre=1))
            cmds.text(l="dens")
            self.bpDensityFLD_list.append(cmds.floatField(v=initBPDensities[order],min=.01,max=1.,s=.1,pre=2))
            cmds.setParent("..")
            cmds.separator()
            cmds.rowColumnLayout(nc=5,cw=[(1,145),(2,80),(3,50),(4,20),(5,35)],co=[(1,"left",10)])
            self.createBranchMeshChBox_list.append(cmds.checkBox(l="Create Mesh", v=initCreateBranchMeshChBox[order]))
            cmds.text(l="Skin Radius")
            self.skinRadiusFLD_list.append(cmds.floatField(v=initSkinRadii[order],min=0.,max=1000.,s=.001,pre=4))
            cmds.text(l="sl")
            self.segLengthFLD_list.append(cmds.floatField(v=initSegLengths[order],min=.05,max=100.,s=.1,pre=2))
            cmds.text(l="sides")
            self.sidesFLD_list.append(cmds.intField(v=initSides[order],min=2,max=256,s=1))
            cmds.setParent("..")
            cmds.separator()
            cmds.rowColumnLayout(nc=4,cw=[(1,60),(2,40),(3,45),(4,80)],co=[(1,"left",10),(4,"left",10)])
            self.stripsOnOffFLD_list.append(cmds.checkBox(l="Strip",v=initStripsOnOff[order],onc=partial(self.toggleStrips, order),ofc=partial(self.toggleStrips, order)))
            cmds.text("Width")
            self.leafStripWidthFLD_list.append(cmds.floatField(v=initLeafStripWidths[order],min=0.,max=100.,s=.01,pre=2, en=initStripsOnOff[order]))
            self.textureOnOffFLD_list.append(cmds.checkBox(l="Textured",v=initTexturedChBox[order], en=initStripsOnOff[order]))
            cmds.setParent("..")
            cmds.separator()
            cmds.rowColumnLayout(nc=6,cw=[(2,35),(3,45),(4,35),(5,70)],cs=[(1,5),(2,5),(3,5),(4,5),])
            cmds.text("Maturity Range")
            self.maturityRngFLD_list.append(cmds.floatField(v=initMaturityRanges[order],min=0.,max=10000.,s=1.,pre=0))
            cmds.setParent("..")
            cmds.columnLayout(rs=5,cw=200)
            self.matGradReadToggles.append(True)
            cmds.optionVar(remove=self.initMaturityGradientInfos[order][0] )
            for gradInfo in self.initMaturityGradientInfos[order][1:]:

                    cmds.optionVar(stringValueAppend=[self.initMaturityGradientInfos[order][0], gradInfo])

            self.maturityGradientFLD_list.append(cmds.gradientControlNoAttr(h=80, w=300, cc=partial(self.setReadMatG, order)))
            cmds.gradientControlNoAttr( self.maturityGradientFLD_list[-1], e=True, optionVar=self.initMaturityGradientInfos[order][0] )
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=4,cw=[(1,30),(2,40),(3,30),(4,40)])
            cmds.text(l="bac")
            self.bacMaturityLinkFLD_list.append(cmds.floatField(v=initBACMtrLinks[order],min=-100.,max=100.,s=.1,pre=2))
            cmds.text(l="sr")
            self.suppReachMaturityLinkFLD_list.append(cmds.floatField(v=initSuppReachMtrLinks[order],min=-100.,max=100.,s=.1,pre=2))
            cmds.setParent(self.LO4)

        #cmds.showWindow(winName)
        self.dockCtrl = cmds.dockControl(guiNames.dockName, l="Tree Maker v29", area="right",content=self.mainWindow)
        self.dockParent = cmds.dockControl(self.dockCtrl, q=True, parent=True)
        self.totalTimeFLD = self.totalTimeFLD.replace(self.mainWindow, self.dockParent)

    def makeScaleMan(self, *_):

        scaleManHeight = 2.5
        scaleManHeadRadius = .4
        cmds.polyCube(h=scaleManHeight)
        cmds.move(40,scaleManHeight/2.,0)
        cmds.polySphere(r=scaleManHeadRadius,sx=8,sy=4)
        cmds.move(40,scaleManHeight+scaleManHeadRadius,0)
        cmds.select(cl=1)

    def saveSettings(self, *_):

        presetName = cmds.textField(self.presetNameFLD,q=True,tx=True)
        #need to change any spaces in the string to underscores
        nameAsList = list(presetName)
        indx = 0
        for n in nameAsList:
            if (n == " "):
                nameAsList[indx] = "_"
            indx += 1
        presetName = "".join(nameAsList)

        nameTaken = False
        for presetFile in os.listdir('C:/Users/13308/Documents/maya/scripts/TreeMaker_Interface_Presets'):
            if presetFile.endswith(".txt"):
                if (presetFile == presetName + ".txt"):
                    nameTaken = True

        if(presetName == ""):
            print "you must enter a name for this preset before you can save it"
        elif (nameTaken):
            if(cmds.window("OverwriteSettingsWindow", exists=True)):
                cmds.deleteUI("OverwriteSettingsWindow")
                print("Deleted existing overwrite settings window")
            self.overwriteSettingsWindow = cmds.window("OverwriteSettingsWindow", title="Overwrite Settings File", rtf=True, s=False)
            cmds.columnLayout(co=["both", 10], rs=10)
            cmds.columnLayout()
            cmds.text(l="A settings file with this name already exists.")
            cmds.text(l="       Would you like to replace it?")
            cmds.setParent("..")
            cmds.rowColumnLayout(nc=2,co=[1,"left",74], ro=[1,"bottom",10])
            cmds.button(l="yes",w=40,command=partial(self.overwriteSettings, presetName))
            cmds.button(l="no",w=40, command=self.dontOverwriteSettings)
            cmds.showWindow()
        else:
            settingsFO = open("C:/Users/13308/Documents/maya/scripts/TreeMaker_Interface_Presets/" + presetName + ".txt","w")

            '''we will write each field's value to a text file with "?" set as a delimiter between the value, the short name of the field, and the "\n".  The values
            must be read in the same order as they were written'''
            settingsFO.write(str(cmds.intSliderGrp(self.totalTimeFLD, q=True, v=True)) + "?tt?\n")
            settingsFO.write(str(cmds.floatField(self.baseVigorFLD, q=True, v=True)) + "?bv?\n")
            settingsFO.write(str(cmds.floatField(self.globalGradientRangeFLD , q=True, v=True)) + "?ggr?\n")
            settingsFO.write(cmds.gradientControlNoAttr(self.globalGrowthGradient, q=True, asString=True) + "?gg?\n")
            settingsFO.write(str(cmds.floatField(self.globGradVigorEffectFLD, q=True, v=True)) + "?gvg?\n")
            settingsFO.write(str(cmds.floatField(self.globGradReachEffectFLD, q=True, v=True)) + "?grc?\n")
            settingsFO.write(str(cmds.intField(self.ordersFLD, q=True, v=True)) + "?o?\n")
            for i in range(len(self.earlyDelaysFLD_list)): settingsFO.write(str(cmds.floatField(self.earlyDelaysFLD_list[i], q=True, v=True)) + "?edl"+str(i)+"?\n")
            for i in range(len(self.lateDelaysFLD_list)): settingsFO.write(str(cmds.floatField(self.lateDelaysFLD_list[i], q=True, v=True)) + "?ldl"+str(i)+"?\n")
            for i in range(len(self.delayFalloffRngFLD_list)): settingsFO.write(str(cmds.floatField(self.delayFalloffRngFLD_list[i], q=True, v=True)) + "?dlb"+str(i)+"?\n")
            for i in range(len(self.vGradientReachFLD_list)): settingsFO.write(str(cmds.floatField(self.vGradientReachFLD_list[i], q=True, v=True)) + "?vtr"+str(i)+"?\n")
            for i in range(len(self.rndVigorRngsFLD_list)): settingsFO.write(str(cmds.floatField(self.rndVigorRngsFLD_list[i], q=True, v=True)) + "?rvg"+str(i)+"?\n")

            for i in range(len(self.vigorTimeGradientFLD_list)): settingsFO.write(cmds.gradientControlNoAttr(self.vigorTimeGradientFLD_list[i], q=True, asString=True) + "?vtg"+str(i)+"?\n")

            for i in range(len(self.selfSustainedFLD_list)): settingsFO.write(str(cmds.floatField(self.selfSustainedFLD_list[i], q=True, v=True)) + "?ss"+str(i)+"?\n")
            for i in range(len(self.lightInfluenceFLD_list)): settingsFO.write(str(cmds.floatField(self.lightInfluenceFLD_list[i], q=True, v=True)) + "?li"+str(i)+"?\n")
            for i in range(len(self.shadeToleranceFLD_list)): settingsFO.write(str(cmds.floatField(self.shadeToleranceFLD_list[i], q=True, v=True)) + "?stl"+str(i)+"?\n")
            for i in range(len(self.healthLossRateFLD_list)): settingsFO.write(str(cmds.floatField(self.healthLossRateFLD_list[i], q=True, v=True)) + "?hlr"+str(i)+"?\n")
            for i in range(len(self.parentGrowthTillShedFLD_list)): settingsFO.write(str(cmds.floatField(self.parentGrowthTillShedFLD_list[i], q=True, v=True)) + "?gts"+str(i)+"?\n")

            for i in range(len(self.suppressionGradientFLD_list)): settingsFO.write(cmds.gradientControlNoAttr(self.suppressionGradientFLD_list[i], q=True, asString=True) + "?sg"+str(i)+"?\n")

            for i in range(len(self.suppReachFLD_list)): settingsFO.write(str(cmds.floatField(self.suppReachFLD_list[i], q=True, v=True)) + "?sgr"+str(i)+"?\n")

            for i in range(len(self.suppEffectGradientFLD_list)): settingsFO.write(cmds.gradientControlNoAttr(self.suppEffectGradientFLD_list[i], q=True, asString=True) + "?seg"+str(i)+"?\n")

            for i in range(len(self.nodeFreqMinsFLD_list)): settingsFO.write(str(cmds.floatField(self.nodeFreqMinsFLD_list[i], q=True, v=True)) + "?nfn"+str(i)+"?\n")
            for i in range(len(self.nodeFreqMaxsFLD_list)): settingsFO.write(str(cmds.floatField(self.nodeFreqMaxsFLD_list[i], q=True, v=True)) + "?nfx"+str(i)+"?\n")
            for i in range(len(self.nodeFreqVigorLinksFLD_list)): settingsFO.write(str(cmds.floatField(self.nodeFreqVigorLinksFLD_list[i], q=True, v=True)) + "?nvl"+str(i)+"?\n")
            for i in range(len(self.SPNMinsFLD_list)): settingsFO.write(str(cmds.intField(self.SPNMinsFLD_list[i], q=True, v=True)) + "?smn"+str(i)+"?\n")
            for i in range(len(self.SPNMaxsFLD_list)): settingsFO.write(str(cmds.intField(self.SPNMaxsFLD_list[i], q=True, v=True)) + "?smx"+str(i)+"?\n")
            for i in range(len(self.nodeRotMinsFLD_list)): settingsFO.write(str(cmds.floatField(self.nodeRotMinsFLD_list[i], q=True, v=True)) + "?nrn"+str(i)+"?\n")
            for i in range(len(self.nodeRotMaxsFLD_list)): settingsFO.write(str(cmds.floatField(self.nodeRotMaxsFLD_list[i], q=True, v=True)) + "?nrx"+str(i)+"?\n")

            for i in range(len(self.leafShootsOnOffFLD_list)): settingsFO.write(str(cmds.checkBox(self.leafShootsOnOffFLD_list[i], q=True, v=True)) + "?lst"+str(i)+"?\n")

            for i in range(len(self.lsNodeFreqMinsFLD_list)): settingsFO.write(str(cmds.floatField(self.lsNodeFreqMinsFLD_list[i], q=True, v=True)) + "?lfn"+str(i)+"?\n")
            for i in range(len(self.lsNodeFreqMaxsFLD_list)): settingsFO.write(str(cmds.floatField(self.lsNodeFreqMaxsFLD_list[i], q=True, v=True)) + "?lfx"+str(i)+"?\n")
            for i in range(len(self.lsSPNMinsFLD_list)): settingsFO.write(str(cmds.intField(self.lsSPNMinsFLD_list[i], q=True, v=True)) + "?lsn"+str(i)+"?\n")
            for i in range(len(self.lsSPNMaxsFLD_list)): settingsFO.write(str(cmds.intField(self.lsSPNMaxsFLD_list[i], q=True, v=True)) + "?lsx"+str(i)+"?\n")
            for i in range(len(self.lsNodeRotMinsFLD_list)): settingsFO.write(str(cmds.floatField(self.lsNodeRotMinsFLD_list[i], q=True, v=True)) + "?lrn"+str(i)+"?\n")
            for i in range(len(self.lsNodeRotMaxsFLD_list)): settingsFO.write(str(cmds.floatField(self.lsNodeRotMaxsFLD_list[i], q=True, v=True)) + "?lrx"+str(i)+"?\n")
            for i in range(len(self.lsShedAgeFLD_list)): settingsFO.write(str(cmds.floatField(self.lsShedAgeFLD_list[i], q=True, v=True)) + "?lsa"+str(i)+"?\n")
            for i in range(len(self.lsShedLengthMinsFLD_list)): settingsFO.write(str(cmds.floatField(self.lsShedLengthMinsFLD_list[i], q=True, v=True)) + "?sln"+str(i)+"?\n")
            for i in range(len(self.lsShedLengthMaxsFLD_list)): settingsFO.write(str(cmds.floatField(self.lsShedLengthMaxsFLD_list[i], q=True, v=True)) + "?slx"+str(i)+"?\n")
            for i in range(len(self.lsShedFallOffFLD_list)): settingsFO.write(str(cmds.floatField(self.lsShedFallOffFLD_list[i], q=True, v=True)) + "?slf"+str(i)+"?\n")
            for i in range(len(self.lsISTimeThreshFLD_list)): settingsFO.write(str(cmds.intField(self.lsISTimeThreshFLD_list[i], q=True, v=True)) + "?ist"+str(i)+"?\n")
            for i in range(len(self.lsISAgeThreshFLD_list)): settingsFO.write(str(cmds.floatField(self.lsISAgeThreshFLD_list[i], q=True, v=True)) + "?isa"+str(i)+"?\n")

            for i in range(len(self.cloneFreqMinFLD_list)): settingsFO.write(str(cmds.floatField(self.cloneFreqMinFLD_list[i], q=True, v=True)) + "?cln"+str(i)+"?\n")
            for i in range(len(self.cloneFreqMaxFLD_list)): settingsFO.write(str(cmds.floatField(self.cloneFreqMaxFLD_list[i], q=True, v=True)) + "?clx"+str(i)+"?\n")
            for i in range(len(self.cloneOrderInflMinFLD_list)): settingsFO.write(str(cmds.floatField(self.cloneOrderInflMinFLD_list[i], q=True, v=True)) + "?oin"+str(i)+"?\n")
            for i in range(len(self.cloneOrderInflMaxFLD_list)): settingsFO.write(str(cmds.floatField(self.cloneOrderInflMaxFLD_list[i], q=True, v=True)) + "?oix"+str(i)+"?\n")
            for i in range(len(self.abortFreqMinFLD_list)): settingsFO.write(str(cmds.floatField(self.abortFreqMinFLD_list[i], q=True, v=True)) + "?abn"+str(i)+"?\n")
            for i in range(len(self.abortFreqMaxFLD_list)): settingsFO.write(str(cmds.floatField(self.abortFreqMaxFLD_list[i], q=True, v=True)) + "?abx"+str(i)+"?\n")

            for i in range(len(self.numTransfMerisFLD_list)): settingsFO.write(str(cmds.intField(self.numTransfMerisFLD_list[i], q=True, v=True)) + "?ntm"+str(i)+"?\n")
            for i in range(len(self.transfRangeFLD_list)): settingsFO.write(str(cmds.floatField(self.transfRangeFLD_list[i], q=True, v=True)) + "?trg"+str(i)+"?\n")

            for i in range(len(self.sproutAziFLD_list)): settingsFO.write(str(cmds.floatField(self.sproutAziFLD_list[i], q=True, v=True)) + "?saz"+str(i)+"?\n")
            for i in range(len(self.sproutToBaseFLD_list)): settingsFO.write(str(cmds.floatField(self.sproutToBaseFLD_list[i], q=True, v=True)) + "?stb"+str(i)+"?\n")
            for i in range(len(self.baseAziFLD_list)): settingsFO.write(str(cmds.floatField(self.baseAziFLD_list[i], q=True, v=True)) + "?baz"+str(i)+"?\n")
            for i in range(len(self.collarJitterPolFLD_list)): settingsFO.write(str(cmds.floatField(self.collarJitterPolFLD_list[i], q=True, v=True)) + "?paj"+str(i)+"?\n")
            for i in range(len(self.collarJitterAziFLD_list)): settingsFO.write(str(cmds.floatField(self.collarJitterAziFLD_list[i], q=True, v=True)) + "?aaj"+str(i)+"?\n")
            for i in range(len(self.DGTropismFLD_list)): settingsFO.write(str(cmds.floatField(self.DGTropismFLD_list[i], q=True, v=True)) + "?dgt"+str(i)+"?\n")
            for i in range(len(self.DGTBaseShiftFLD_list)): settingsFO.write(str(cmds.floatField(self.DGTBaseShiftFLD_list[i], q=True, v=True)) + "?dbs"+str(i)+"?\n")
            for i in range(len(self.xAreaAddedFLD_list)): settingsFO.write(str(cmds.floatField(self.xAreaAddedFLD_list[i], q=True, v=True)) + "?xaa"+str(i)+"?\n")

            for i in range(len(self.pullForceFLD_list)): settingsFO.write(str(cmds.floatField(self.pullForceFLD_list[i], q=True, v=True)) + "?gom"+str(i)+"?\n")
            for i in range(len(self.acGradientReachFLD_list)): settingsFO.write(str(cmds.floatField(self.acGradientReachFLD_list[i], q=True, v=True)) + "?agr"+str(i)+"?\n")
            for i in range(len(self.tropismRatioFLD_list)): settingsFO.write(str(cmds.floatField(self.tropismRatioFLD_list[i], q=True, v=True)) + "?g"+str(i)+"?\n")

            for i in range(len(self.pullACGradientFLD_list)): settingsFO.write(cmds.gradientControlNoAttr(self.pullACGradientFLD_list[i], q=True, asString=True) + "?ago"+str(i)+"?\n")

            for i in range(len(self.PSStartFLD_list)): settingsFO.write(str(cmds.floatField(self.PSStartFLD_list[i], q=True, v=True)) + "?sds"+str(i)+"?\n")
            for i in range(len(self.PSRangeFLD_list)): settingsFO.write(str(cmds.floatField(self.PSRangeFLD_list[i], q=True, v=True)) + "?sdr"+str(i)+"?\n")
            for i in range(len(self.pfSuppLinkFLD_list)): settingsFO.write(str(cmds.floatField(self.pfSuppLinkFLD_list[i], q=True, v=True)) + "?psl"+str(i)+"?\n")
            for i in range(len(self.pLossSuppLinkFLD_list)): settingsFO.write(str(cmds.floatField(self.pLossSuppLinkFLD_list[i], q=True, v=True)) + "?lsl"+str(i)+"?\n")
            for i in range(len(self.weightMultFLD_list)): settingsFO.write(str(cmds.floatField(self.weightMultFLD_list[i], q=True, v=True)) + "?gtm"+str(i)+"?\n")
            for i in range(len(self.overallACGradientRangeFLD_list)): settingsFO.write(str(cmds.floatField(self.overallACGradientRangeFLD_list[i], q=True, v=True)) + "?bgr"+str(i)+"?\n")

            for i in range(len(self.weightACGradientFLD_list)): settingsFO.write(cmds.gradientControlNoAttr(self.weightACGradientFLD_list[i], q=True, asString=True) + "?agt"+str(i)+"?\n")

            for i in range(len(self.backRotationFLD_list)): settingsFO.write(str(cmds.floatField(self.backRotationFLD_list[i], q=True, v=True)) + "?br"+str(i)+"?\n")
            for i in range(len(self.straightenerStrFLD_list)): settingsFO.write(str(cmds.floatField(self.straightenerStrFLD_list[i], q=True, v=True)) + "?sst"+str(i)+"?\n")
            for i in range(len(self.backRotationDelayFLD_list)): settingsFO.write(str(cmds.floatField(self.backRotationDelayFLD_list[i], q=True, v=True)) + "?brd"+str(i)+"?\n")
            for i in range(len(self.backRotationOffsetFLD_list)): settingsFO.write(str(cmds.floatField(self.backRotationOffsetFLD_list[i], q=True, v=True)) + "?bro"+str(i)+"?\n")
            for i in range(len(self.collarReachFLD_list)): settingsFO.write(str(cmds.floatField(self.collarReachFLD_list[i], q=True, v=True)) + "?icr"+str(i)+"?\n")
            for i in range(len(self.collarStrengthFLD_list)): settingsFO.write(str(cmds.floatField(self.collarStrengthFLD_list[i], q=True, v=True)) + "?ics"+str(i)+"?\n")
            for i in range(len(self.collarReachGainFLD_list)): settingsFO.write(str(cmds.floatField(self.collarReachGainFLD_list[i], q=True, v=True)) + "?crg"+str(i)+"?\n")
            for i in range(len(self.collarStrengthGainFLD_list)): settingsFO.write(str(cmds.floatField(self.collarStrengthGainFLD_list[i], q=True, v=True)) + "?csg"+str(i)+"?\n")
            for i in range(len(self.collarLimitReachFLD_list)): settingsFO.write(str(cmds.floatField(self.collarLimitReachFLD_list[i], q=True, v=True)) + "?clr"+str(i)+"?\n")
            for i in range(len(self.collarLimitAngleFLD_list)): settingsFO.write(str(cmds.floatField(self.collarLimitAngleFLD_list[i], q=True, v=True)) + "?cla"+str(i)+"?\n")
            for i in range(len(self.pdDroopFLD_list)): settingsFO.write(str(cmds.floatField(self.pdDroopFLD_list[i], q=True, v=True)) + "?pdd"+str(i)+"?\n")
            for i in range(len(self.pddPeakFLD_list)): settingsFO.write(str(cmds.floatField(self.pddPeakFLD_list[i], q=True, v=True)) + "?pdp"+str(i)+"?\n")
            for i in range(len(self.pddEndFLD_list)): settingsFO.write(str(cmds.floatField(self.pddEndFLD_list[i], q=True, v=True)) + "?pde"+str(i)+"?\n")
            for i in range(len(self.windStrengthFLD_list)): settingsFO.write(str(cmds.floatField(self.windStrengthFLD_list[i], q=True, v=True)) + "?wds"+str(i)+"?\n")
            for i in range(len(self.rippleStrengthFLD_list)): settingsFO.write(str(cmds.floatField(self.rippleStrengthFLD_list[i], q=True, v=True)) + "?rps"+str(i)+"?\n")

            for i in range(len(self.blockPointsOnOffFLD_list)): settingsFO.write(str(cmds.checkBox(self.blockPointsOnOffFLD_list[i], q=True, v=True)) + "?cbp"+str(i)+"?\n")
            for i in range(len(self.ignoreBPointsFLD_list)): settingsFO.write(str(cmds.checkBox(self.ignoreBPointsFLD_list[i], q=True, v=True)) + "?ibp"+str(i)+"?\n")

            for i in range(len(self.bpResFLD_list)): settingsFO.write(str(cmds.intField(self.bpResFLD_list[i], q=True, v=True)) + "?brs"+str(i)+"?\n")
            for i in range(len(self.bpSizeFLD_list)): settingsFO.write(str(cmds.floatField(self.bpSizeFLD_list[i], q=True, v=True)) + "?bps"+str(i)+"?\n")
            for i in range(len(self.bpDensityFLD_list)): settingsFO.write(str(cmds.floatField(self.bpDensityFLD_list[i], q=True, v=True)) + "?bpd"+str(i)+"?\n")

            for i in range(len(self.createBranchMeshChBox_list)): settingsFO.write(str(cmds.checkBox(self.createBranchMeshChBox_list[i], q=True, v=True)) + "?cbm"+str(i)+"?\n")

            for i in range(len(self.skinRadiusFLD_list)): settingsFO.write(str(cmds.floatField(self.skinRadiusFLD_list[i], q=True, v=True)) + "?sr"+str(i)+"?\n")
            for i in range(len(self.segLengthFLD_list)): settingsFO.write(str(cmds.floatField(self.segLengthFLD_list[i], q=True, v=True)) + "?osl"+str(i)+"?\n")
            for i in range(len(self.sidesFLD_list)): settingsFO.write(str(cmds.intField(self.sidesFLD_list[i], q=True, v=True)) + "?sid"+str(i)+"?\n")

            for i in range(len(self.stripsOnOffFLD_list)): settingsFO.write(str(cmds.checkBox(self.stripsOnOffFLD_list[i], q=True, v=True)) + "?cts"+str(i)+"?\n")
            for i in range(len(self.leafStripWidthFLD_list)): settingsFO.write(str(cmds.floatField(self.leafStripWidthFLD_list[i], q=True, v=True)) + "?tsw"+str(i)+"?\n")
            for i in range(len(self.textureOnOffFLD_list)): settingsFO.write(str(cmds.checkBox(self.textureOnOffFLD_list[i], q=True, v=True)) + "?ttg"+str(i)+"?\n")

            for i in range(len(self.maturityRngFLD_list)): settingsFO.write(str(cmds.floatField(self.maturityRngFLD_list[i], q=True, v=True)) + "?mr"+str(i)+"?\n")

            for i in range(len(self.maturityGradientFLD_list)): settingsFO.write(cmds.gradientControlNoAttr(self.maturityGradientFLD_list[i], q=True, asString=True) + "?mg"+str(i)+"?\n")

            for i in range(len(self.bacMaturityLinkFLD_list)): settingsFO.write(str(cmds.floatField(self.bacMaturityLinkFLD_list[i], q=True, v=True)) + "?bml"+str(i)+"?\n")
            for i in range(len(self.suppReachMaturityLinkFLD_list)): settingsFO.write(str(cmds.floatField(self.suppReachMaturityLinkFLD_list[i], q=True, v=True)) + "?sml"+str(i)+"?\n")


            cmds.menuItem(presetName + ".txt", l=presetName + ".txt", p=self.loadPresetButton, command = partial(self.loadSettings, presetName + ".txt"))

            print presetName + " preset saved"

    def loadSettings(self, *args):

            settingsFO = open("C:/Users/13308/Documents/maya/scripts/TreeMaker_Interface_Presets/" + args[0],"r")

            ''' the 'line' variable should be a 3 item list consisting of the field value, the short name of the field, and the "\n", in that order '''
            line = settingsFO.readline().split("?")
            if line[1] != "tt": print "WARNING:  WRONG VALUE READ - " + line[1]
            cmds.intSliderGrp(self.totalTimeFLD, e=True, v=int(line[0]))

            line = settingsFO.readline().split("?")
            if line[1] != "bv": print "WARNING:  WRONG VALUE READ - " + line[1]
            cmds.floatField(self.baseVigorFLD, e=True, v=float(line[0]))

            line = settingsFO.readline().split("?")
            if line[1] != "ggr": print "WARNING:  WRONG VALUE READ - " + line[1]
            cmds.floatField(self.globalGradientRangeFLD , e=True, v=float(line[0]))

            '''Ok, time to read in the gradient info, this will be much more complicated than reading single numbers'''
            line = settingsFO.readline().split("?")
            if line[1] != "gg": print "WARNING:  WRONG VALUE READ - " + line[1]
            gggVals = line[0].split(",")
            optionVarSets = []
            for i in range(len(gggVals)):
                if i%3 == 0: optionVarSets.append("")
                if i%3 != 2: optionVarSets[-1] += gggVals[i] + ","
                else: optionVarSets[-1] += gggVals[i]

            '''and now we can finally replace the gradient'''

            self.readGlobalGrad = True #because we are altering the gradient, we need to set this to true so that the values of the gradient are read into a list later
            ''' the only way I can figure to edit a gradientControlNoAttr which already exists is to give it a new option var with a different name.  The next
            line grabs the time value from the clock method (this will always be different) and turns it into a string to attach to the name'''
            newOVName = "gggov" + str(round(time.clock(), 4))
            if newOVName == self.gggovName: print "WARNING:  globalGrowthGradientOptionVar name didn't change"
            self.gggovName = newOVName
            for i in range(len(optionVarSets)):
                if i == 0: cmds.optionVar(stringValue=[self.gggovName, optionVarSets[i]])
                else: cmds.optionVar(stringValueAppend=[self.gggovName, optionVarSets[i]])
            cmds.gradientControlNoAttr( self.globalGrowthGradient, e=True, optionVar=self.gggovName )

            line = settingsFO.readline().split("?")
            if line[1] != "gvg": print "WARNING:  WRONG VALUE READ - " + line[1]
            cmds.floatField(self.globGradVigorEffectFLD , e=True, v=float(line[0]))

            line = settingsFO.readline().split("?")
            if line[1] != "grc": print "WARNING:  WRONG VALUE READ - " + line[1]
            cmds.floatField(self.globGradReachEffectFLD , e=True, v=float(line[0]))

            line = settingsFO.readline().split("?")
            if line[1] != "o": print "WARNING:  WRONG VALUE READ - " + line[1]
            cmds.intField(self.ordersFLD, e=True, v=int(line[0]))
            self.orderUpdate() #need to call orderUpdate here because changing the order value via edit does not call the control's change command

            for i in range(len(self.earlyDelaysFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "edl"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.earlyDelaysFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lateDelaysFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "ldl"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lateDelaysFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.delayFalloffRngFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "dlb"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.delayFalloffRngFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.vGradientReachFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "vtr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.vGradientReachFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.rndVigorRngsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "rvg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.rndVigorRngsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.vigorTimeGradientFLD_list)):
                
                line = settingsFO.readline().split("?")

                if line[1] != "vtg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                vals = line[0].split(",")

                optionVarSets = []
                for j in range(len(vals)):
                    if j%3 == 0: optionVarSets.append("")
                    if j%3 != 2: optionVarSets[-1] += vals[j] + ","
                    else: optionVarSets[-1] += vals[j]

                self.vtgReadToggles[i] = True
                newOVName = "vtgov" + str(i) + " " + str(round(time.clock(), 4))
                if newOVName == self.initVigorGradientInfos[i][0]: print "WARNING:  vigorTimeGradient name didn't change"
                self.initVigorGradientInfos[i][0] = newOVName
                for j in range(len(optionVarSets)):
                    if j == 0: cmds.optionVar(stringValue=[self.initVigorGradientInfos[i][0], optionVarSets[j]])
                    else: cmds.optionVar(stringValueAppend=[self.initVigorGradientInfos[i][0], optionVarSets[j]])
                cmds.gradientControlNoAttr( self.vigorTimeGradientFLD_list[i], e=True, optionVar=self.initVigorGradientInfos[i][0] )

            for i in range(len(self.selfSustainedFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "ss"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.selfSustainedFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lightInfluenceFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "li"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lightInfluenceFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.shadeToleranceFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "stl"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.shadeToleranceFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.healthLossRateFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "hlr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.healthLossRateFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.parentGrowthTillShedFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "gts"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.parentGrowthTillShedFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.suppressionGradientFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                vals = line[0].split(",")
                optionVarSets = []
                for j in range(len(vals)):
                    if j%3 == 0: optionVarSets.append("")
                    if j%3 != 2: optionVarSets[-1] += vals[j] + ","
                    else: optionVarSets[-1] += vals[j]

                self.sgReadToggles[i] = True
                newOVName = "sgov" + str(i) + " " + str(round(time.clock(), 4))
                if newOVName == self.initSuppGradientInfos[i][0]: print "WARNING:  suppression gradient name didn't change"
                self.initSuppGradientInfos[i][0] = newOVName
                for j in range(len(optionVarSets)):
                    if j == 0: cmds.optionVar(stringValue=[self.initSuppGradientInfos[i][0], optionVarSets[j]])
                    else: cmds.optionVar(stringValueAppend=[self.initSuppGradientInfos[i][0], optionVarSets[j]])
                cmds.gradientControlNoAttr( self.suppressionGradientFLD_list[i], e=True, optionVar=self.initSuppGradientInfos[i][0] )

            for i in range(len(self.suppReachFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sgr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.suppReachFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.suppEffectGradientFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "seg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                vals = line[0].split(",")
                optionVarSets = []
                for j in range(len(vals)):
                    if j%3 == 0: optionVarSets.append("")
                    if j%3 != 2: optionVarSets[-1] += vals[j] + ","
                    else: optionVarSets[-1] += vals[j]

                self.segReadToggles[i] = True
                newOVName = "segov" + str(i) + " " + str(round(time.clock(), 4))
                if newOVName == self.initSuppEffectGradientInfos[i][0]: print "WARNING:  suppression effect gradient name didn't change"
                self.initSuppEffectGradientInfos[i][0] = newOVName
                for j in range(len(optionVarSets)):
                    if j == 0: cmds.optionVar(stringValue=[self.initSuppEffectGradientInfos[i][0], optionVarSets[j]])
                    else: cmds.optionVar(stringValueAppend=[self.initSuppEffectGradientInfos[i][0], optionVarSets[j]])
                cmds.gradientControlNoAttr( self.suppEffectGradientFLD_list[i], e=True, optionVar=self.initSuppEffectGradientInfos[i][0] )

            for i in range(len(self.nodeFreqMinsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "nfn"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.nodeFreqMinsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.nodeFreqMaxsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "nfx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.nodeFreqMaxsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.nodeFreqVigorLinksFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "nvl"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.nodeFreqVigorLinksFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.SPNMinsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "smn"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.intField(self.SPNMinsFLD_list[i], e=True, v=int(line[0]))

            for i in range(len(self.SPNMaxsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "smx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.intField(self.SPNMaxsFLD_list[i], e=True, v=int(line[0]))

            for i in range(len(self.nodeRotMinsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "nrn"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.nodeRotMinsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.nodeRotMaxsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "nrx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.nodeRotMaxsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.leafShootsOnOffFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lst"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                ''' gonna have to manually convert the string representation of the boolean to an int, since that is what the checkBox control requires'''
                boolVal = 0
                if line[0] == 'True': boolVal = 1
                cmds.checkBox(self.leafShootsOnOffFLD_list[i], e=True, v=boolVal)

            for i in range(len(self.lsNodeFreqMinsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lfn"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsNodeFreqMinsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lsNodeFreqMaxsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lfx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsNodeFreqMaxsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lsSPNMinsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lsn"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.intField(self.lsSPNMinsFLD_list[i], e=True, v=int(line[0]))

            for i in range(len(self.lsSPNMaxsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lsx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.intField(self.lsSPNMaxsFLD_list[i], e=True, v=int(line[0]))

            for i in range(len(self.lsNodeRotMinsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lrn"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsNodeRotMinsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lsNodeRotMaxsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lrx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsNodeRotMaxsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lsShedAgeFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lsa"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsShedAgeFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lsShedLengthMinsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sln"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsShedLengthMinsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lsShedLengthMaxsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "slx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsShedLengthMaxsFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lsShedFallOffFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "slf"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsShedFallOffFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.lsISTimeThreshFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "ist"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.intField(self.lsISTimeThreshFLD_list[i], e=True, v=int(line[0]))

            for i in range(len(self.lsISAgeThreshFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "isa"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.lsISAgeThreshFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.cloneFreqMinFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "cln"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.cloneFreqMinFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.cloneFreqMaxFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "clx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.cloneFreqMaxFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.cloneOrderInflMinFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "oin"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.cloneOrderInflMinFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.cloneOrderInflMaxFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "oix"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.cloneOrderInflMaxFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.abortFreqMinFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "abn"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.abortFreqMinFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.abortFreqMaxFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "abx"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.abortFreqMaxFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.numTransfMerisFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "ntm"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.intField(self.numTransfMerisFLD_list[i], e=True, v=int(line[0]))

            for i in range(len(self.transfRangeFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "trg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.transfRangeFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.sproutAziFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "saz"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.sproutAziFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.sproutToBaseFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "stb"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.sproutToBaseFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.baseAziFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "baz"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.baseAziFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.collarJitterPolFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "paj"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.collarJitterPolFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.collarJitterAziFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "aaj"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.collarJitterAziFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.DGTropismFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "dgt"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.DGTropismFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.DGTBaseShiftFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "dbs"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.DGTBaseShiftFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.xAreaAddedFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "xaa"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.xAreaAddedFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.pullForceFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "gom"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.pullForceFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.acGradientReachFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "agr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.acGradientReachFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.tropismRatioFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "g"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.tropismRatioFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.pullACGradientFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "ago"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                vals = line[0].split(",")
                optionVarSets = []
                for j in range(len(vals)):
                    if j%3 == 0: optionVarSets.append("")
                    if j%3 != 2: optionVarSets[-1] += vals[j] + ","
                    else: optionVarSets[-1] += vals[j]

                self.pullGradReadToggles[i] = True
                newOVName = "agoov" + str(i) + " " + str(round(time.clock(), 4))
                if newOVName == self.initPullACGradientInfos[i][0]: print "WARNING:  pull gradient name didn't change"
                self.initPullACGradientInfos[i][0] = newOVName
                for j in range(len(optionVarSets)):
                    if j == 0: cmds.optionVar(stringValue=[self.initPullACGradientInfos[i][0], optionVarSets[j]])
                    else: cmds.optionVar(stringValueAppend=[self.initPullACGradientInfos[i][0], optionVarSets[j]])
                cmds.gradientControlNoAttr( self.pullACGradientFLD_list[i], e=True, optionVar=self.initPullACGradientInfos[i][0] )

            for i in range(len(self.PSStartFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sds"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.PSStartFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.PSRangeFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sdr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.PSRangeFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.pfSuppLinkFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "psl"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.pfSuppLinkFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.pLossSuppLinkFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "lsl"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.pLossSuppLinkFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.weightMultFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "gtm"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.weightMultFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.overallACGradientRangeFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "bgr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.overallACGradientRangeFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.weightACGradientFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "agt"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                vals = line[0].split(",")
                optionVarSets = []
                for j in range(len(vals)):
                    if j%3 == 0: optionVarSets.append("")
                    if j%3 != 2: optionVarSets[-1] += vals[j] + ","
                    else: optionVarSets[-1] += vals[j]

                self.weightGradReadToggles[i] = True
                newOVName = "agtov" + str(i) + " " + str(round(time.clock(), 4))
                if newOVName == self.initWeightACGradientInfos[i][0]: print "WARNING:  weight gradient name didn't change"
                self.initWeightACGradientInfos[i][0] = newOVName
                for j in range(len(optionVarSets)):
                    if j == 0: cmds.optionVar(stringValue=[self.initWeightACGradientInfos[i][0], optionVarSets[j]])
                    else: cmds.optionVar(stringValueAppend=[self.initWeightACGradientInfos[i][0], optionVarSets[j]])
                cmds.gradientControlNoAttr( self.weightACGradientFLD_list[i], e=True, optionVar=self.initWeightACGradientInfos[i][0] )

            for i in range(len(self.backRotationFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "br"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.backRotationFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.straightenerStrFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sst"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.straightenerStrFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.backRotationDelayFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "brd"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.backRotationDelayFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.backRotationOffsetFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "bro"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.backRotationOffsetFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.collarReachFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "icr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.collarReachFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.collarStrengthFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "ics"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.collarStrengthFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.collarReachGainFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "crg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.collarReachGainFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.collarStrengthGainFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "csg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.collarStrengthGainFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.collarLimitReachFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "clr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.collarLimitReachFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.collarLimitAngleFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "cla"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.collarLimitAngleFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.pdDroopFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "pdd"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.pdDroopFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.pddPeakFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "pdp"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.pddPeakFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.pddEndFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "pde"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.pddEndFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.windStrengthFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "wds"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.windStrengthFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.rippleStrengthFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "rps"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.rippleStrengthFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.blockPointsOnOffFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "cbp"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                boolVal = 0
                if line[0] == 'True': boolVal = 1
                cmds.checkBox(self.blockPointsOnOffFLD_list[i], e=True, v=boolVal)

            for i in range(len(self.ignoreBPointsFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "ibp"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                boolVal = 0
                if line[0] == 'True': boolVal = 1
                cmds.checkBox(self.ignoreBPointsFLD_list[i], e=True, v=boolVal)

            for i in range(len(self.bpResFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "brs"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.intField(self.bpResFLD_list[i], e=True, v=int(line[0]))

            for i in range(len(self.bpSizeFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "bps"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.bpSizeFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.bpDensityFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "bpd"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.bpDensityFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.createBranchMeshChBox_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "cbm"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                boolVal = 0
                if line[0] == 'True': boolVal = 1
                cmds.checkBox(self.createBranchMeshChBox_list[i], e=True, v=boolVal)

            for i in range(len(self.skinRadiusFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.skinRadiusFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.segLengthFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "osl"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.segLengthFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.sidesFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sid"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.intField(self.sidesFLD_list[i], e=True, v=int(line[0]))

            for i in range(len(self.stripsOnOffFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "cts"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]

                boolVal = 0
                if line[0] == 'True': boolVal = 1
                cmds.checkBox(self.stripsOnOffFLD_list[i], e=True, v=boolVal)

            for i in range(len(self.leafStripWidthFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "tsw"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.leafStripWidthFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.textureOnOffFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "ttg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                boolVal = 0
                if line[0] == 'True': boolVal = 1
                cmds.floatField(self.leafStripWidthFLD_list[i], e=True, en=boolVal)
                cmds.checkBox(self.textureOnOffFLD_list[i], e=True, en=boolVal)
                cmds.checkBox(self.textureOnOffFLD_list[i], e=True, v=boolVal)

            for i in range(len(self.maturityRngFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "mr"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.maturityRngFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.maturityGradientFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "mg"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                vals = line[0].split(",")
                optionVarSets = []
                for j in range(len(vals)):
                    if j%3 == 0: optionVarSets.append("")
                    if j%3 != 2: optionVarSets[-1] += vals[j] + ","
                    else: optionVarSets[-1] += vals[j]

                self.matGradReadToggles[i] = True
                newOVName = "mgov" + str(i) + " " + str(round(time.clock(), 4))
                if newOVName == self.initMaturityGradientInfos[i][0]: print "WARNING:  maturity gradient name didn't change"
                self.initMaturityGradientInfos[i][0] = newOVName
                for j in range(len(optionVarSets)):
                    if j == 0: cmds.optionVar(stringValue=[self.initMaturityGradientInfos[i][0], optionVarSets[j]])
                    else: cmds.optionVar(stringValueAppend=[self.initMaturityGradientInfos[i][0], optionVarSets[j]])
                cmds.gradientControlNoAttr( self.maturityGradientFLD_list[i], e=True, optionVar=self.initMaturityGradientInfos[i][0] )

            for i in range(len(self.bacMaturityLinkFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "bml"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.bacMaturityLinkFLD_list[i], e=True, v=float(line[0]))

            for i in range(len(self.suppReachMaturityLinkFLD_list)):
                line = settingsFO.readline().split("?")
                if line[1] != "sml"+ str(i): print "WARNING:  WRONG VALUE READ - " + line[1]
                cmds.floatField(self.suppReachMaturityLinkFLD_list[i], e=True, v=float(line[0]))

            print "finished loading " + args[0] + " preset"
            settingsFO.close()

    def prepareToBluePrint(self, *_):

        self.initiate()
        orderList = self.orderList
        vtgsAsStrings = []
        suppGradientsAsStrings = []
        suppEffectGradientsAsStrings = []
        agosAsStrings = []
        agtsAsStrings = []
        mgsAsStrings = []

        for count, o in enumerate(orderList[1:]):

            vtgsAsStrings.append("")
            for value in o.vigorTimeGradient:

                vtgsAsStrings[count] += str(value) + ","

            suppGradientsAsStrings.append("")
            suppEffectGradientsAsStrings.append("")

            if count < 4:
                for value in o.suppressionGradient:
                    suppGradientsAsStrings[count] += str(value) + ","

                for value in o.suppEffectGradient:
                    suppEffectGradientsAsStrings[count] += str(value) + ","

            else:
                for i in range(len(orderList[count - 1].suppressionGradient)):
                    suppGradientsAsStrings[count] += "1.,"
                for i in range(len(orderList[count - 1].suppEffectGradient)):
                    suppEffectGradientsAsStrings[count] += "0.,"

            agosAsStrings.append("")
            for value in o.pullACGradient:
                agosAsStrings[count] += str(value) + ","

            agtsAsStrings.append("")
            for value in o.weightACGradient:
                agtsAsStrings[count] += str(value) + ","

            mgsAsStrings.append("")
            for value in o.maturityGradient:
                mgsAsStrings[count] += str(value) + ","

        cmds.makeBluePrint(tt=self.totalTime,
                           bv=self.baseVigor,
                           ggr=self.globalGradientRange,
                           gg=self.globalGrowthGradientValues,
                           gvg=self.globGradVigorEffect,
                           grc=self.globGradReachEffect,
                           o=self.orders,
                           edl=[orderList[1].earlyDelay, orderList[2].earlyDelay, orderList[3].earlyDelay, orderList[4].earlyDelay, orderList[5].earlyDelay],
                           ldl=[orderList[1].lateDelay, orderList[2].lateDelay, orderList[3].lateDelay, orderList[4].lateDelay, orderList[5].lateDelay],
                           dlb=[orderList[1].delayBlend, orderList[2].delayBlend, orderList[3].delayBlend, orderList[4].delayBlend, orderList[5].delayBlend],
                           vtr=[orderList[1].vGradientReach, orderList[2].vGradientReach, orderList[3].vGradientReach, orderList[4].vGradientReach, orderList[5].vGradientReach],
                           rvg=[orderList[1].rndVigorRng, orderList[2].rndVigorRng, orderList[3].rndVigorRng, orderList[4].rndVigorRng, orderList[5].rndVigorRng],
                           vtg=vtgsAsStrings,
                           ss=[orderList[1].selfSustained, orderList[2].selfSustained, orderList[3].selfSustained, orderList[4].selfSustained, orderList[5].selfSustained],
                           li=[orderList[1].lightInfluence, orderList[2].lightInfluence, orderList[3].lightInfluence, orderList[4].lightInfluence, orderList[5].lightInfluence],
                           stl=[orderList[1].shadeTolerance, orderList[2].shadeTolerance, orderList[3].shadeTolerance, orderList[4].shadeTolerance, orderList[5].shadeTolerance],
                           hlr=[orderList[1].healthLossRate, orderList[2].healthLossRate, orderList[3].healthLossRate, orderList[4].healthLossRate, orderList[5].healthLossRate],
                           gts=[orderList[1].parentGrowthTillShed, orderList[2].parentGrowthTillShed, orderList[3].parentGrowthTillShed, orderList[4].parentGrowthTillShed, orderList[5].parentGrowthTillShed],
                           sg=suppGradientsAsStrings,
                           sgr=[orderList[1].suppReach, orderList[2].suppReach, orderList[3].suppReach, orderList[4].suppReach, 0.],
                           seg=suppEffectGradientsAsStrings,
                           nfn=[orderList[1].nodeFreq, orderList[2].nodeFreq, orderList[3].nodeFreq, orderList[4].nodeFreq, 99999.],
                           nfx=[orderList[1].nodeFreqFluct, orderList[2].nodeFreqFluct, orderList[3].nodeFreqFluct, orderList[4].nodeFreqFluct, 99999.],
                           nvl=[orderList[1].nfVigorLink, orderList[2].nfVigorLink, orderList[3].nfVigorLink, orderList[4].nfVigorLink, 0.],
                           smn=[orderList[1].shootsPerNode, orderList[2].shootsPerNode, orderList[3].shootsPerNode, orderList[4].shootsPerNode, 0.],
                           smx=[orderList[1].SPNFluct, orderList[2].SPNFluct, orderList[3].SPNFluct, orderList[4].SPNFluct, 0.],
                           nrn=[orderList[1].nodeRotation, orderList[2].nodeRotation, orderList[3].nodeRotation, orderList[4].nodeRotation, 0.],
                           nrx=[orderList[1].nodeRotFluct, orderList[2].nodeRotFluct, orderList[3].nodeRotFluct, orderList[4].nodeRotFluct, 0.],
                           lst=[orderList[1].lsTgl, orderList[2].lsTgl, orderList[3].lsTgl, orderList[4].lsTgl, False],
                           lfn=[orderList[1].lsNodeFreqMin, orderList[2].lsNodeFreqMin, orderList[3].lsNodeFreqMin, orderList[4].lsNodeFreqMin, 99999.],
                           lfx=[orderList[1].lsNodeFreqMax, orderList[2].lsNodeFreqMax, orderList[3].lsNodeFreqMax, orderList[4].lsNodeFreqMax, 99999.],
                           lsn=[orderList[1].lsSPNMin, orderList[2].lsSPNMin, orderList[3].lsSPNMin, orderList[4].lsSPNMin, 0.],
                           lsx=[orderList[1].lsSPNMax, orderList[2].lsSPNMax, orderList[3].lsSPNMax, orderList[4].lsSPNMax, 0.],
                           lrn=[orderList[1].lsNodeRotMin, orderList[2].lsNodeRotMin, orderList[3].lsNodeRotMin, orderList[4].lsNodeRotMin, 0.],
                           lrx=[orderList[1].lsNodeRotMax, orderList[2].lsNodeRotMax, orderList[3].lsNodeRotMax, orderList[4].lsNodeRotMax, 0.],
                           lsa=[orderList[1].lsShedAge, orderList[2].lsShedAge, orderList[3].lsShedAge, orderList[4].lsShedAge, 99999.],
                           sln=[orderList[1].lsShedLengthMin, orderList[2].lsShedLengthMin, orderList[3].lsShedLengthMin, orderList[4].lsShedLengthMin, 0.],
                           slx=[orderList[1].lsShedLengthMax, orderList[2].lsShedLengthMax, orderList[3].lsShedLengthMax, orderList[4].lsShedLengthMax, 0.],
                           slf=[orderList[1].lsShedFallOff, orderList[2].lsShedFallOff, orderList[3].lsShedFallOff, orderList[4].lsShedFallOff, 0.],
                           ist=[orderList[1].lsISTime, orderList[2].lsISTime, orderList[3].lsISTime, orderList[4].lsISTime, 0.],
                           isa=[orderList[1].lsISAge, orderList[2].lsISAge, orderList[3].lsISAge, orderList[4].lsISAge, 0.],
                           cln=[orderList[1].cloneFreqMin, orderList[2].cloneFreqMin, orderList[3].cloneFreqMin, orderList[4].cloneFreqMin, orderList[5].cloneFreqMin],
                           clx=[orderList[1].cloneFreqMax, orderList[2].cloneFreqMax, orderList[3].cloneFreqMax, orderList[4].cloneFreqMax, orderList[5].cloneFreqMax],
                           oin=[orderList[1].cloneOrdInfl, orderList[2].cloneOrdInfl, orderList[3].cloneOrdInfl, orderList[4].cloneOrdInfl, orderList[5].cloneOrdInfl],
                           oix=[orderList[1].cloneDelay, orderList[2].cloneDelay, orderList[3].cloneDelay, orderList[4].cloneDelay, orderList[5].cloneDelay],
                           abn=[orderList[1].abortFreqMin, orderList[2].abortFreqMin, orderList[3].abortFreqMin, orderList[4].abortFreqMin, orderList[5].abortFreqMin],
                           abx=[orderList[1].abortFreqMax, orderList[2].abortFreqMax, orderList[3].abortFreqMax, orderList[4].abortFreqMax, orderList[5].abortFreqMax],
                           ntm=[orderList[1].numTransfMeris, orderList[2].numTransfMeris, orderList[3].numTransfMeris, orderList[4].numTransfMeris, orderList[5].numTransfMeris],
                           trg=[orderList[1].transfRng, orderList[2].transfRng, orderList[3].transfRng, orderList[4].transfRng, orderList[5].transfRng],
                           dgt=[orderList[1].DGT, orderList[2].DGT, orderList[3].DGT, orderList[4].DGT, orderList[5].DGT],
                           dbs=[orderList[1].DGTSides, orderList[2].DGTSides, orderList[3].DGTSides, orderList[4].DGTSides, orderList[5].DGTSides],
                           xaa=[orderList[1].xAreaAdded, orderList[2].xAreaAdded, orderList[3].xAreaAdded, orderList[4].xAreaAdded, orderList[5].xAreaAdded],
                           agr=[orderList[1].acGradientsReach, orderList[2].acGradientsReach, orderList[3].acGradientsReach, orderList[4].acGradientsReach, orderList[5].acGradientsReach],
                           bgr=[orderList[1].overallACGradReach, orderList[2].overallACGradReach, orderList[3].overallACGradReach, orderList[4].overallACGradReach, orderList[5].overallACGradReach],
                           ago=agosAsStrings,
                           agt=agtsAsStrings,
                           gom=[orderList[1].pullMult, orderList[2].pullMult, orderList[3].pullMult, orderList[4].pullMult, orderList[5].pullMult],
                           psl=[orderList[1].pullSuppLink, orderList[2].pullSuppLink, orderList[3].pullSuppLink, orderList[4].pullSuppLink, orderList[5].pullSuppLink],
                           sds=[orderList[1].PSStart, orderList[2].PSStart, orderList[3].PSStart, orderList[4].PSStart, orderList[5].PSStart],
                           sdr=[orderList[1].PSRange, orderList[2].PSRange, orderList[3].PSRange, orderList[4].PSRange, orderList[5].PSRange],
                           lsl=[orderList[1].pLossSuppLink, orderList[2].pLossSuppLink, orderList[3].pLossSuppLink, orderList[4].pLossSuppLink, orderList[5].pLossSuppLink],
                           gtm=[orderList[1].weightMult, orderList[2].weightMult, orderList[3].weightMult, orderList[4].weightMult, orderList[5].weightMult],
                           g=[orderList[1].gravitropism, orderList[2].gravitropism, orderList[3].gravitropism, orderList[4].gravitropism, orderList[5].gravitropism],
                           br=[orderList[1].backRotation, orderList[2].backRotation, orderList[3].backRotation, orderList[4].backRotation, orderList[5].backRotation],
                           sst=[orderList[1].straightenerStr, orderList[2].straightenerStr, orderList[3].straightenerStr, orderList[4].straightenerStr, orderList[5].straightenerStr],
                           brd=[orderList[1].backRotationDelay, orderList[2].backRotationDelay, orderList[3].backRotationDelay, orderList[4].backRotationDelay, orderList[5].backRotationDelay],
                           bro=[orderList[1].backRotationOffset, orderList[2].backRotationOffset, orderList[3].backRotationOffset, orderList[4].backRotationOffset, orderList[5].backRotationOffset],
                           icr=[orderList[1].collarReach, orderList[2].collarReach, orderList[3].collarReach, orderList[4].collarReach, orderList[5].collarReach],
                           ics=[orderList[1].collarStrength, orderList[2].collarStrength, orderList[3].collarStrength, orderList[4].collarStrength, orderList[5].collarStrength],
                           crg=[orderList[1].collarReachGain, orderList[2].collarReachGain, orderList[3].collarReachGain, orderList[4].collarReachGain, orderList[5].collarReachGain],
                           csg=[orderList[1].collarStrengthGain, orderList[2].collarStrengthGain, orderList[3].collarStrengthGain, orderList[4].collarStrengthGain, orderList[5].collarStrengthGain],
                           clr=[orderList[1].collarLimitReach, orderList[2].collarLimitReach, orderList[3].collarLimitReach, orderList[4].collarLimitReach, orderList[5].collarLimitReach],
                           cla=[orderList[1].collarLimitAngle, orderList[2].collarLimitAngle, orderList[3].collarLimitAngle, orderList[4].collarLimitAngle, orderList[5].collarLimitAngle],
                           saz=[orderList[1].sproutAzimuth, orderList[2].sproutAzimuth, orderList[3].sproutAzimuth, orderList[4].sproutAzimuth, orderList[5].sproutAzimuth],
                           stb=[orderList[1].sproutToBase, orderList[2].sproutToBase, orderList[3].sproutToBase, orderList[4].sproutToBase, orderList[5].sproutToBase],
                           baz=[orderList[1].baseAzimuth, orderList[2].baseAzimuth, orderList[3].baseAzimuth, orderList[4].baseAzimuth, orderList[5].baseAzimuth],
                           paj=[orderList[1].collarJitter[0], orderList[2].collarJitter[0], orderList[3].collarJitter[0], orderList[4].collarJitter[0], orderList[5].collarJitter[0]],
                           aaj=[orderList[1].collarJitter[1], orderList[2].collarJitter[1], orderList[3].collarJitter[1], orderList[4].collarJitter[1], orderList[5].collarJitter[1]],
                           pdd=[orderList[1].pdDroop, orderList[2].pdDroop, orderList[3].pdDroop, orderList[4].pdDroop, orderList[5].pdDroop],
                           pdp=[orderList[1].pddPeak, orderList[2].pddPeak, orderList[3].pddPeak, orderList[4].pddPeak, orderList[5].pddPeak],
                           pde=[orderList[1].pddEnd, orderList[2].pddEnd, orderList[3].pddEnd, orderList[4].pddEnd, orderList[5].pddEnd],
                           wds=[orderList[1].windStrength, orderList[2].windStrength, orderList[3].windStrength, orderList[4].windStrength, orderList[5].windStrength],
                           rps=[orderList[1].rippleStrength, orderList[2].rippleStrength, orderList[3].rippleStrength, orderList[4].rippleStrength, orderList[5].rippleStrength],
                           cbp=[orderList[1].blockPointsTgl, orderList[2].blockPointsTgl, orderList[3].blockPointsTgl, orderList[4].blockPointsTgl, orderList[5].blockPointsTgl],
                           ibp=[orderList[1].ignoreBPsTgl, orderList[2].ignoreBPsTgl, orderList[3].ignoreBPsTgl, orderList[4].ignoreBPsTgl, orderList[5].ignoreBPsTgl],
                           brs=[orderList[1].bpRes, orderList[2].bpRes, orderList[3].bpRes, orderList[4].bpRes, orderList[5].bpRes],
                           bps=[orderList[1].bpSize, orderList[2].bpSize, orderList[3].bpSize, orderList[4].bpSize, orderList[5].bpSize],
                           bpd=[orderList[1].bpDensity, orderList[2].bpDensity, orderList[3].bpDensity, orderList[4].bpDensity, orderList[5].bpDensity],
                           cbm=[orderList[1].branchMeshTgl, orderList[2].branchMeshTgl, orderList[3].branchMeshTgl, orderList[4].branchMeshTgl, orderList[5].branchMeshTgl],
                           sr=[orderList[1].skinRadius, orderList[2].skinRadius, orderList[3].skinRadius, orderList[4].skinRadius, orderList[5].skinRadius],
                           osl=[orderList[1].segmentLength, orderList[2].segmentLength, orderList[3].segmentLength, orderList[4].segmentLength, orderList[5].segmentLength],
                           sid=[orderList[1].sides, orderList[2].sides, orderList[3].sides, orderList[4].sides, orderList[5].sides],
                           cts=[orderList[1].stripsTgl, orderList[2].stripsTgl, orderList[3].stripsTgl, orderList[4].stripsTgl, orderList[5].stripsTgl],
                           tsw=[orderList[1].stripWidth, orderList[2].stripWidth, orderList[3].stripWidth, orderList[4].stripWidth, orderList[5].stripWidth],
                           ttg=[orderList[1].stripTextureTgl, orderList[2].stripTextureTgl, orderList[3].stripTextureTgl, orderList[4].stripTextureTgl, orderList[5].stripTextureTgl],
                           mr=[orderList[1].maturityRange, orderList[2].maturityRange, orderList[3].maturityRange, orderList[4].maturityRange, orderList[5].maturityRange],
                           mg=mgsAsStrings,
                           bml=[orderList[1].bacMtrLink, orderList[2].bacMtrLink, orderList[3].bacMtrLink, orderList[4].bacMtrLink, orderList[5].bacMtrLink],
                           sml=[orderList[1].srMtrLink, orderList[2].srMtrLink, orderList[3].srMtrLink, orderList[4].srMtrLink, orderList[5].srMtrLink])

    # def makeTree(self, *_):
    #
    #     self.initiate()
    #
    #     dominoRes = self.dominoRes
    #     orders, orderList, globalGradientRange, globGradVigorEffect = self.orders, self.orderList, self.globalGradientRange, self.globGradVigorEffect
    #     globGradReachEffect, maxSuppReach, currentVigTimeReachList = self.globGradReachEffect, self.maxSuppReach, self.currentVigTimeReachList
    #     globalGrowthGradientValues = self.globalGrowthGradientValues
    #     blockPoints, pointRemoved, timeElapsed = self.blockPoints, self.pointRemoved, self.timeElapsed
    #     seed, newMeristemCatcher, allMeristems, activeMeristems, elongatedMeristems = self.seed, self.newMeristemCatcher, self.allMeristems, self.activeMeristems, self.elongatedMeristems
    #     totalTime, pointRadius, blockDensity, blockPointResolution = self.totalTime, self.pointRadius, self.blockDensity, self.blockPointResolution
    #     vigorAndBPCalcTime, appendSegTime, forceCalcTime, collarAdjustTime, segmentAdjustTime, drawPointsTime, newShootTime, bSegPrepTime, shedTime= 0., 0., 0., 0., 0., 0., 0., 0., 0.
    #     postDeformersTime = 0.
    #     delayedMeristems, shedMeristems, drawnMeristems = [], [], [seed]
    #
    #     adjAlv = [0.,0.,0.,0.]
    #     segLengthSQU = segLength*segLength
    #     oneDivSegLengthSQU = 1./segLengthSQU
    #     testPullForceVector = (segLength*math.sin(0.5)*math.cos(0.),
    #                            segLength*math.cos(0.5),
    #                            segLength*math.sin(0.5)*math.sin(0.))
    #
    #     sensorReachSegs = 8
    #     sensorReach = 10 * segLength
    #     segX2, segD2, segD3, segX4 = segLength*2., segLength/2, segLength/3, segLength*4.
    #     lastTime, secondToLastTime = totalTime - 1, totalTime - 2
    #     randomPullMult = 1.
    #     rightAngleDistance = (segLength / math.sin(PId2*.5)) * math.sin(PId2) #use law of sines to find the distance between two vectors of magnitude segLength at 90 degrees apart
    #     reorderedMeristems = []
    #     bluePrintProgressWindow = cmds.window(title="Blueprint Progress")
    #     cmds.columnLayout()
    #     bluePrintProgressControl = cmds.progressBar(maxValue=totalTime, width=300)
    #     cmds.showWindow(bluePrintProgressWindow)
    #
    #     for o in orderList[1:]:
    #         o.DGTSides = (PId2+o.DGTSides,PIandAHalf-o.DGTSides)
    #
    #     testPFVectorSums = [[0.,0.,0.], [0.,0.,0.]]
    #     merisToPrep = []
    #     lightBlockRange = 7.
    #     gridUnitSize = 8.
    #     BPGRange = int(math.ceil(lightBlockRange / gridUnitSize))
    #
    #     #clear the block point grid
    #     for x in BPG:
    #         for y in x:
    #             for z in y:
    #                 if len(z) > 0:
    #                     del z[:]
    #
    #     spaceRotator.initiateVectorMatrixList(3)
    #
    #     while timeElapsed < totalTime:
    #
    #         for order in orderList[1:]:
    #
    #             pointOnGradientIndex = min(int((timeElapsed / order.maturityRange)*500), 500)
    #             #order.maturityValue = min(max(order.maturityGradient[pointOnGradientIndex], 0.), 1.)
    #
    #         try:
    #             pointOnGradientIndex = int(round((seed.lengthFromRoot / globalGradientRange)*100, 0))
    #             '''The reach and vigor effect values give us control over how much the global gradient effects their respective attributes.  They are applied in the
    #             following equations.  They shrink the gradient vertically upwards.'''
    #             gradientValueForVigor = ((1.- globGradVigorEffect) + (globGradVigorEffect * globalGrowthGradientValues[pointOnGradientIndex]))
    #             gradientValueForReach = ((1.- globGradReachEffect) + (globGradReachEffect * globalGrowthGradientValues[pointOnGradientIndex]))
    #
    #             currentMaxEndogenousVigor = gradientValueForVigor
    #
    #             for i in range(orders-1):
    #
    #                 index = i+1
    #
    #                 orderList[index].suppReach = maxSuppReach[index]*gradientValueForReach
    #
    #         except (ZeroDivisionError, IndexError):
    #             pass
    #
    #         timeVariable = time.time()
    #
    #         for meri in elongatedMeristems:
    #
    #             if meri.parentProximity - meri.branchLength > meri.selfShedLength:
    #
    #                 shedMeristems.append(meri)
    #
    #         for meri in shedMeristems:
    #
    #             activeMeristems.remove(meri)
    #             elongatedMeristems.remove(meri)
    #
    #             try:
    #                 drawnMeristems.remove(meri)
    #             except ValueError:
    #                 pass
    #
    #         shedMeristems = []
    #         shedTime += (time.time() - timeVariable)
    #
    #         timeVariable = time.time()
    #
    #         if timeElapsed == 5000:
    #
    #             nearestNodeMeris = seed.axialChildren[-1].nodeSiblings
    #
    #             siblings = len(nearestNodeMeris)
    #
    #             if siblings > 2:
    #
    #                 siblingsAway = siblings/2 #to prevent an index error this must be rounded down, this is done automatically when dividing integers
    #
    #                 index1 = random.randint(0, siblingsAway - 1)
    #                 index2 = index1 + siblingsAway
    #
    #                 transferMeri1 = nearestNodeMeris[index1]
    #                 transferMeri2 = nearestNodeMeris[index2]
    #
    #                 reorderedMeristems = [transferMeri1, transferMeri2]
    #                 print "reordered meris", allMeristems.index(transferMeri1), allMeristems.index(transferMeri2)
    #                 for meri in reorderedMeristems:
    #
    #                     seed.orderChildren.remove(meri)
    #
    #                 for child in seed.orderChildren:
    #
    #                     child.orderParents = []
    #                     child.orderParents.extend(reorderedMeristems)
    #
    #                 for meri in reorderedMeristems:
    #
    #                     meri.orderParents = seed.orderParents
    #                     meri.order = 1
    #                     meri.orderInfluence = .5
    #                     orderChildrenSum = []
    #                     orderChildrenSum.extend(seed.orderChildren)
    #                     orderChildrenSum.extend(meri.orderChildren)
    #                     meri.orderChildren = orderChildrenSum
    #                     meri.parentProximity = seed.parentProximity
    #                     meri.parentLengthAtRoot = seed.parentLengthAtRoot
    #                     meri.age = seed.age
    #                     meri.collarLimiters = []
    #                     meri.collarLimiters.extend(reorderedMeristems)
    #                     meri.collarLimiters.remove(meri)
    #
    #                     #for seg in meri.pathSegs[meri.rootSegIndx:]:
    #                     #    seg.prevAngsBtwnLmtrs = []
    #                     #
    #                     #Since the meri has new limiters we must update its segments' prevAngsBtwnLmtrs attribute
    #                     #for meri2 in meri.collarLimiters:
    #                     #
    #                     #    limiterSegVector = None
    #                     #
    #                     #    try:
    #                     #        limiterSegVector = meri2.pathSegs[meri.rootSegIndx].vector
    #                     #    except IndexError:
    #                     #        if meri.rootSegIndx == meri2.rootSegIndx: #this means the limiter's root segment has not yet grown
    #                     #            merisToPrep.append(meri)
    #                     #        else:
    #                     #            limiterSegVector = meri2.pathSegs[-1].vector
    #                     #
    #                     #    if limiterSegVector != None:
    #                     #        for seg in meri.pathSegs[meri.rootSegIndx:]:
    #                     #
    #                     #            dotProduct = limiterSegVector[0]*seg.vector[0] + limiterSegVector[1]*seg.vector[1] + limiterSegVector[2]*seg.vector[2]
    #                     #            angBetween = math.acos(max(min(dotProduct*oneDivSegLengthSQU, 1.), -1))
    #                     #
    #                     #            seg.prevAngsBtwnLmtrs.append(angBetween)
    #
    #                     meri.collarStrengthenees.extend(nearestNodeMeris)
    #                     meri.collarStrengthenees.remove(meri)
    #                     meri.suppression = seed.suppression
    #                     meri.bakedSuppressedVigor = seed.bakedSuppressedVigor
    #                     meri.timeGradReach = seed.timeGradReach
    #                     meri.delay = 0.
    #                     meri.selfShedLength = seed.selfShedLength
    #                     nodeFreq = orderList[meri.order].nodeFreq
    #                     nodeFluctRange = orderList[meri.order].nodeFreqFluct * nodeFreq
    #                     meri.lengthAtNextNode = meri.branchLength + (nodeFreq - divmod(meri.branchLength, nodeFreq)[1])
    #                     meri.lengthAtNextNode += random.uniform(-nodeFluctRange, nodeFluctRange)
    #                     lsNodeFreqMin = orderList[meri.order].lsNodeFreqMin
    #                     lsNodeFluctRange = orderList[meri.order].lsNodeFreqMax * lsNodeFreqMin
    #                     meri.lengthAtNextLSNode = meri.branchLength + (lsNodeFreqMin - divmod(meri.branchLength, lsNodeFreqMin)[1])
    #                     meri.lengthAtNextLSNode += random.uniform(-lsNodeFluctRange, nodeFluctRange)
    #
    #             activeMeristems.remove(seed)
    #
    #         #for count, meri in enumerate(reorderedMeristems):
    #         #
    #         #    pfTotal = testPFVectorSums[count]
    #         #    pfTotal = [pfTotal[0] + meri.pullForceVector[0], pfTotal[1] + meri.pullForceVector[1], pfTotal[2] + meri.pullForceVector[2]]
    #         #    testPFVectorSums[count] = pfTotal
    #         #
    #         #    print allMeristems.index(meri), angleFinder.findVectorAngles(pfTotal)
    #         '''The following loop determines the current vigor of each meristem.  As of v27, this loop also checks blockPoints to determine the desired direction
    #         of growth and the adjustment of vigor due to light loss'''
    #         for meri in activeMeristems:
    #
    #             '''Because analyzing the blockPoints is so time consuming we will not do so at every iteration.  Instead we will use the lightCheck attribute.  There are two
    #             lightCheck triggers:  when the meri is born, and when a new segment is appended'''
    #             if meri.lightCheck:
    #
    #                 meri.lightCheck = False
    #
    #                 meriLoc = meri.loc
    #
    #                 '''If branch has at least 1 segment, we will say the meristem is now able to react to light vectors and block points.  We will use its
    #                 sensor direction to determine the direction of the strongest light.'''
    #                 if len(meri.pathSegs[meri.rootSegIndx:]) > 0:
    #
    #                     '''I've assumed that it is not only the tip of the meristem that detects light and determines the direction to grow, but rather many points
    #                     along the branch within a certain range from the tip.  We will still use the tip as the detection point, however we will not use the last vector
    #                     as the detection angle.  Instead we will draw a vector from the beginning of this detection range to the tip and use this vector's direction as our
    #                     detection angle.'''
    #
    #                     if orderList[meri.order].ignoreBPsTgl == 0:
    #                         if meri.branchLength > sensorReach:
    #                             sensorStartPoint = meri.pathSegs[-sensorReachSegs].startPoint
    #                         else:
    #                             sensorStartPoint = meri.pathSegs[meri.rootSegIndx].startPoint
    #
    #                         sensorVector = (meriLoc[0] - sensorStartPoint[0], meriLoc[1] - sensorStartPoint[1], meriLoc[2] - sensorStartPoint[2])
    #                     else:
    #
    #                         if meri.branchLength > sensorReach:
    #                             sensorVector = (0.,0.,0.)
    #                             for seg in meri.pathSegs[-sensorReachSegs:]:
    #
    #                                 sensorVector = (sensorVector[0]+seg.vector[0], sensorVector[1]+seg.vector[1], sensorVector[2]+seg.vector[2])
    #                         else:
    #                             sensorVector = meri.vectorSum
    #
    #                 else: #if the meristem has no segments yet, we will have to use the meristem's tip pol and azi to create the imaginary vector, we will also use this vector as the pullForce vector
    #
    #                     lengthTimesSin = segLength*math.sin(meri.azi)
    #                     sensorVector = (lengthTimesSin*math.cos(meri.pol),
    #                                     segLength*math.cos(meri.azi),
    #                                     lengthTimesSin*math.sin(meri.pol))
    #                     sensorStartPoint = meriLoc
    #
    #                 try:
    #                     angles = angleFinder.findVectorAngles(sensorVector)
    #                 except ZeroDivisionError:
    #                     print meri.order, meriLoc, sensorStartPoint
    #                     quit()
    #                 try:
    #                     sensorPolar = angles[0]
    #                     sensorAzi = angles[1]
    #                 except IndexError:
    #                     print angles
    #                     quit()
    #                 try:
    #                     aziIndex = int(min(sensorAzi,3.1399) * 5.0929581)
    #                 except ValueError:
    #                     print "got a NaN", meri.pathSegs[-1].vector
    #                     quit()
    #
    #                 polIndex = int(min(sensorPolar,6.2799) / (6.28/len(lvInfoMatrix[aziIndex])))
    #
    #                 vInfo = lvInfoMatrix[aziIndex][polIndex] #this variable contains the average light vector for the meristem based on its sensor direction
    #
    #                 '''If the ignore block points toggle is off, we will have to use the meristem's position and angle to determine how to adjust the average light
    #                 vector according to the block points.'''
    #                 if orderList[meri.order].ignoreBPsTgl == 0:
    #
    #                     xDiff = 0.
    #                     yDiff = 0.
    #                     zDiff = 0.
    #
    #                     blockedVectors = []
    #                     blockageDensities = []
    #                     energyLoss = 0.
    #
    #                     '''We are using the int function to round.  This will always round towards zero, which means coordinate values between -1 and 1 will be rounded to zero,
    #                     giving them the same index value in our matrix.  We do not want this.  To account for this, we will simply add half of the total grid size (only for
    #                     x and z since y coordinates are all above 0) to the coordinate value before applying the int function.  This way no index values will be negative'''
    #                     #add 1 to the upper boundary because it will be used as the upper limit of a slice range - slice ranges are "up to but not including" the upper value
    #                     xLoc = int(meriLoc[0]/gridUnitSize + 8.)
    #                     xUpper = min(xLoc + BPGRange, 15) + 1
    #                     xLower = max(xLoc - BPGRange, 0)
    #                     yLoc = int(meriLoc[1]/gridUnitSize)
    #                     yUpper = min(yLoc + BPGRange, 23) + 1
    #                     yLower = max(yLoc - BPGRange, 0)
    #                     zLoc = int(meriLoc[2]/gridUnitSize + 8.)
    #                     zUpper = min(zLoc + BPGRange, 15) + 1
    #                     zLower = max(zLoc - BPGRange, 0)
    #
    #                     for x in BPG[xLower:xUpper]:
    #                         for y in x[yLower:yUpper]:
    #                             for z in y[zLower:zUpper]:
    #
    #                                 for bp in z:
    #
    #                                     try:
    #                                         angles = angleFinder.distanceAndAngles(meriLoc, bp)
    #                                     except ZeroDivisionError: #this exception should mean the blockpoint is in the exact location as the meriLoc (possibly it is the meristem tip)
    #                                         continue
    #
    #                                     proximity = angles[2]
    #
    #                                     if proximity < lightBlockRange: #only calculate light blockage if the point is within this range
    #
    #                                         try:
    #                                             aziIndex = int(min(angles[1],3.1399) * 5.414013)
    #                                         except ValueError:
    #                                             print "another NaN"
    #                                             print meriLoc, bp
    #
    #                                         polIndex = int(min(angles[0],6.2799) / (6.28/len(vInfo[6][aziIndex])))
    #
    #                                         if vInfo[6][aziIndex][polIndex][0] == 'On':
    #
    #                                             #print timeElapsed, allMeristems.index(meri), bp, sensorPolar, sensorAzi
    #                                             angleIncrease = math.atan(pointRadius/proximity)
    #
    #                                             for lvl in lvInfoMatrix[aziIndex][polIndex][7][0: int(angleIncrease*4.54) +1]:
    #
    #                                                 for v in lvl:
    #
    #                                                     if vInfo[6][v[0]][v[1]][0] == 'On':
    #
    #                                                         if v in blockedVectors:
    #                                                             blockageDensities[blockedVectors.index(v)] += blockDensity
    #                                                         else:
    #                                                             blockedVectors.append(v)
    #                                                             blockageDensities.append(blockDensity)
    #
    #                     for count, d in enumerate(blockageDensities):  #adjust the blockage density values so that they are not greater than 1
    #                         blockageDensities[count] = min(1.,d)
    #
    #                     for count, v in enumerate(blockedVectors):
    #
    #                         energyLoss += v[2] * blockageDensities[count]
    #
    #                         xDiff += angleMatrix[v[0]][v[1]][0][0] * blockageDensities[count]
    #                         yDiff += angleMatrix[v[0]][v[1]][0][1] * blockageDensities[count]
    #                         zDiff += angleMatrix[v[0]][v[1]][0][2] * blockageDensities[count]
    #
    #                     lightPercentage = (vInfo[5] - energyLoss) / vInfo[4]
    #                     meri.lightMult = 1. - ((1. - lightPercentage) * orderList[meri.order].lightInfluence)
    #
    #
    #                     #print timeElapsed, allMeristems.index(meri), meri.lightMult, len(blockedVectors), meriLoc
    #
    #                     adjAlv[0] = vInfo[0] - xDiff/vInfo[4]
    #                     adjAlv[1] = vInfo[1] - yDiff/vInfo[4]
    #                     adjAlv[2] = vInfo[2] - zDiff/vInfo[4]
    #
    #                 else: #if ignore block points is on, the average light vector does not need adjustment
    #
    #                     adjAlv[0] = vInfo[0]
    #                     adjAlv[1] = vInfo[1]
    #                     adjAlv[2] = vInfo[2]
    #
    #                 adjAlv[3] = math.sqrt(adjAlv[0]*adjAlv[0] + adjAlv[1]*adjAlv[1] + adjAlv[2]*adjAlv[2])
    #
    #
    #                 gravitropism = orderList[meri.order].gravitropism
    #                 phototropism = 1. - gravitropism
    #
    #                 multiplier = phototropism / adjAlv[3]
    #                 lightDirectionVector = (adjAlv[0]*multiplier, adjAlv[1]*multiplier, adjAlv[2]*multiplier)
    #
    #                 vectorSum = (lightDirectionVector[0], lightDirectionVector[1] + gravitropism, lightDirectionVector[2])
    #                 mag = math.sqrt(vectorSum[0]*vectorSum[0] + vectorSum[1]*vectorSum[1] + vectorSum[2]*vectorSum[2])
    #                 normalizer = segLength / mag
    #                 meri.pullForceVector = (vectorSum[0] * normalizer, vectorSum[1] * normalizer, vectorSum[2] * normalizer)
    #
    #             repay = True
    #
    #             selfSustMult = orderList[meri.order].selfSustained
    #             endogMult = 1. - selfSustMult
    #
    #             while repay == True:
    #
    #                 repay = False
    #
    #                 if meri.cloneInfo.isClone == True:
    #
    #                     meri.vigor = meri.axialParent.vigor * meri.cloneInfo.vigorPercent
    #
    #                 else:
    #
    #                     try:
    #                         pointOnTimeGradientIndex = int(round((meri.age / meri.timeGradReach)*500, 0))
    #                         valueOnVigorGradient = min(max(orderList[meri.order].vigorTimeGradient[pointOnTimeGradientIndex], 0.), 1.)
    #                     except IndexError:
    #                         valueOnVigorGradient = min(max(orderList[meri.order].vigorTimeGradient[500],0.),1.)
    #                     try:
    #                         pointOnParentTimeGradientIndex = int(round((meri.orderParents[0].age / meri.orderParents[0].timeGradReach)*500,0))
    #                         pointOnSuppGradientIndex = int(round((meri.parentProximity / orderList[meri.orderParents[0].order].suppReach)*100, 0))
    #
    #                         try:
    #                             valueOnSuppEffectGradient = min(max(orderList[meri.orderParents[0].order].suppEffectGradient[pointOnParentTimeGradientIndex],0.),1.)
    #                         except IndexError:
    #                             valueOnSuppEffectGradient = min(max(orderList[meri.orderParents[0].order].suppEffectGradient[500],0.),1.)
    #                         try:
    #                             valueOnSuppGradient = min(max(orderList[meri.orderParents[0].order].suppressionGradient[pointOnSuppGradientIndex],0.),1.)
    #                         except IndexError:
    #                             valueOnSuppGradient = min(max(orderList[meri.orderParents[0].order].suppressionGradient[100],0.),1.)
    #
    #                         '''In the event of a split, a meristem will have multiple parents. This will alter the suppression acting on the meristem'''
    #                         totalInfluence = 0.
    #
    #                         #if a meristems has multiple parents, find the average influence among them
    #                         for parent in meri.orderParents:
    #
    #                             totalInfluence += parent.orderInfluence
    #
    #                         avgInfluence = totalInfluence / len(meri.orderParents)
    #
    #                         #multiply this average by the normal order suppression value
    #                         meri.suppression = (1.-(valueOnSuppEffectGradient*(1.-valueOnSuppGradient))) * avgInfluence
    #
    #                         effectiveSuppression = meri.suppression
    #
    #                         orderParent = meri.orderParents[0]
    #                         while orderParent.order > 1:
    #
    #                             effectiveSuppression *= orderParent.suppression
    #                             orderParent = orderParent.orderParents[0]
    #
    #                         #'''unsuppression - if the effectiveSuppression goes up passed the suppLimit, suppLimit will slowly increase until it reaches it, however this only
    #                         #happens up to a certain age (currently set to 1 as seen below).  The closer the meristem gets to that age, the longer it will take to unsuppress'''
    #                         #if effectiveSuppression <= meri.suppLimit:
    #                         #    meri.suppLimit = effectiveSuppression
    #                         #else:
    #                         #    meri.suppLimit += ((1. - min(meri.age, 1.)) / 1.) * 0.1
    #                         #
    #                         #meri.vigor = min(effectiveSuppression, meri.suppLimit)*valueOnVigorGradient*currentMaxEndogenousVigor
    #
    #                         '''Using the bakedSuppressedVigor attribute as a min and then updating it with the current vigor will permenantly set the current vigor
    #                         as a maximum vigor value for the meristem'''
    #                         currentEndogenousVigor = min(meri.bakedSuppressedVigor, effectiveSuppression*endogMult*valueOnVigorGradient*currentMaxEndogenousVigor)
    #                         meri.bakedSuppressedVigor = currentEndogenousVigor
    #
    #                     except IndexError: #this indexError should mean that the meristem has no parents
    #
    #                         currentEndogenousVigor = endogMult*valueOnVigorGradient*currentMaxEndogenousVigor*meri.orderInfluence
    #
    #                 meri.vigor = currentEndogenousVigor + (selfSustMult * valueOnVigorGradient)
    #                 meri.vigor *= meri.lightMult
    #
    #                 if meri.hasGrowthDebt:
    #                     #print "yep", allMeristems.index(meri), meri.timeOwed, meri.vigor
    #                     repay = True
    #                     meri.age += meri.timeOwed
    #                     segmentProgressIncrement = meri.timeOwed * meri.vigor
    #                     meri.segmentProgress += segmentProgressIncrement
    #                     preciseGrowth = segmentProgressIncrement * segLength
    #                     meri.branchLength += preciseGrowth
    #                     meri.lengthFromRoot += preciseGrowth
    #                     meri.parentProximity += preciseGrowth
    #
    #                     meri.hasGrowthDebt = False
    #
    #         vigorAndBPCalcTime += (time.time() - timeVariable)
    #
    #         for meri in activeMeristems: #determine, based on vigor, whether a new segment should be appended
    #
    #             meri.newSegs = 0
    #             meri.age += 1.
    #             meri.segmentProgress += meri.vigor
    #             preciseGrowth = meri.vigor * segLength
    #             meri.branchLength += preciseGrowth
    #             meri.lengthFromRoot += preciseGrowth
    #             meri.parentProximity += preciseGrowth
    #             for seg in meri.limiterSegments:
    #                 try:
    #                     seg.vectorSnapShot = None
    #                 except AttributeError:
    #                     pass
    #
    #             if meri.segmentProgress >= 1. or timeElapsed == lastTime:
    #                 '''If this is last loop, a segment is created regardless of segmentProgress.  It will be treated as a segment of normal length until the end of the segment adjustment
    #                 loop, where its length and vector will be scaled according to its segment progress or branchlength'''
    #                 meri.newSegs = max(int(meri.segmentProgress), 1)
    #                 meri.lightCheck = True
    #                 meri.segmentProgress -= meri.newSegs
    #
    #                 if len(meri.pathSegs[meri.rootSegIndx:]) == 0 and meri.rootSegIndx > 0:
    #                     #print "length at sprouting", allMeristems.index(meri), meri.branchLength
    #                     elongatedMeristems.append(meri)
    #
    #                     if orderList[meri.order].blockPointsTgl == 1:
    #                         drawnMeristems.append(meri)
    #
    #                     '''The location and direction of the start point for a new meristem may have changed before it started to grow (usually true for delayed or slow growing
    #                     meristems).  For this reason, we wait until now to set the world coordinates and direction of the meristem for the first time - so that the beginning
    #                     of its growth will be accurate.'''
    #
    #                     parentSegAngles = angleFinder.findVectorAngles(meri.pathSegs[-1].vector)
    #                     spaceRotator.rotateSpace(parentSegAngles[0], parentSegAngles[1])
    #                     aziJitter = orderList[meri.order].collarJitter[1]
    #                     if aziJitter > 0.:
    #                         rootRelativeAzi = orderList[meri.order].baseAzimuth + random.triangular(-aziJitter,aziJitter,0.)
    #                     else:
    #                         rootRelativeAzi = orderList[meri.order].baseAzimuth
    #
    #                     tempVector = spaceRotator.getVector(meri.rootRelativePolar, rootRelativeAzi, segLength)
    #                     angles = angleFinder.findVectorAngles(tempVector)
    #                     meri.pol = angles[0]
    #                     meri.azi = angles[1]
    #                     meri.branchAzi = angles[1]
    #                     #the next line will force the meristem's pullforce to equal its angle at sprouting, I think this will help make the beginning of its growth more accurate
    #                     meri.pullForceVector = tempVector
    #
    #                     try:
    #                         meri.loc = meri.axialParent.pathSegs[meri.rootSegIndx].startPoint #NOTE - this will not be correct for intersegmental meristems, needs revision if we are to have intersegmentals
    #                     except IndexError:
    #                         meri.loc = meri.axialParent.loc
    #
    #                     for seg in meri.pathSegs:
    #
    #                         seg.xArea += meri.xAreaAdded
    #
    #                     meri.pathSegs[-1].merisOnSeg.append(meri) #If the index before the meri's root segment index doesn't yet exist on its parent, this will be wrong
    #
    #                     if meri.pathSegs[-1].split == False: #check if the segment at this point on the axialParent meri has been marked as split
    #
    #                         meri.pathSegs[-1].split = True
    #
    #         timeVariable = time.time()
    #
    #         for meri in activeMeristems: #create the new segment and add it to the meristem's path segment list
    #
    #             for i in range(meri.newSegs):
    #
    #                 #prevAngsBetween = []
    #                 #
    #                 #for meri2 in meri.collarLimiters:
    #                 #
    #                 #    limiterSegVector = None
    #                 #
    #                 #    try:
    #                 #        limiterSegVector = meri2.pathSegs[meri.rootSegIndx].vector
    #                 #    except IndexError:
    #                 #        if meri.rootSegIndx == meri2.rootSegIndx:
    #                 #            merisToPrep.append(meri)
    #                 #        else:
    #                 #            limiterSegVector = meri2.pathSegs[-1].vector
    #                 #
    #                 #    if limiterSegVector != None:
    #                 #        dotProduct = imaginaryVector[0]*limiterSegVector[0] + imaginaryVector[1]*limiterSegVector[1] + imaginaryVector[2]*limiterSegVector[2]
    #                 #        angBetween = math.acos(max(min(dotProduct*oneDivSegLengthSQU, 1.), -1.))
    #                 #
    #                 #        prevAngsBetween.append(angBetween)
    #
    #                 if len(meri.pathSegs[meri.rootSegIndx:]) > 0:
    #                     imaginaryVector = meri.pathSegs[-1].vector
    #                 else:
    #                     lengthTimesSin = segLength*math.sin(meri.azi)
    #                     imaginaryVector = (lengthTimesSin*math.cos(meri.pol),
    #                                        segLength*math.cos(meri.azi),
    #                                        lengthTimesSin*math.sin(meri.pol))
    #
    #                 #for now, segments' startPoints will not be needed at creation, meri.loc will be used as a placeholder
    #                 #if i > 0:
    #                 #    startPoint = (startPoint[0] + imaginaryVector[0], startPoint[1] + imaginaryVector[1], startPoint[2] + imaginaryVector[2])
    #                 #else:
    #                 #    startPoint = meri.loc
    #
    #                 meri.pathSegs.append(Segment(meri.loc, imaginaryVector, segLength, meri.pol, meri.azi, 0.0001, 0., 0., 0., (0.,0.,0.), meri.lengthFromRoot, meri.branchLength,
    #                                      False, [], None, [], 0, None, None))
    #                 #meri.lengthFromRoot += segLength
    #                 #meri.branchLength += segLength
    #                 #meri.parentProximity += segLength
    #                 #meri.collarReach += meri.collarReachGain
    #                 #meri.collarStrength += meri.collarStrengthGain
    #
    #                 latestIndex = len(meri.pathSegs) - 1
    #
    #                 if latestIndex in meri.limiterSegments:
    #
    #                     meri.limiterSegments[meri.limiterSegments.index(latestIndex)] = meri.pathSegs[-1]
    #
    #             lengthAdded = segLength*meri.newSegs
    #
    #             for seg in meri.pathSegs[meri.rootSegIndx:]:
    #
    #                 seg.distalLength += lengthAdded
    #
    #             for meri2 in meri.orderChildren:
    #
    #                 meri2.parentProximity += lengthAdded
    #
    #             for meri2 in meri.collarStrengthenees:
    #
    #                 #these may be slightly inaccurate on the lastGo since the last segment length may not be = segLength
    #                 meri2.collarStrength += meri2.collarStrengthGain*meri.newSegs
    #                 meri2.collarReach += meri2.collarReachGain*meri.newSegs
    #
    #                 #for meri2 in meri.axialChildren:
    #                 #    #these may be slightly inaccurate on the lastGo since the last segment length may not be = segLength
    #                 #    meri2.collarStrength += meri2.collarStrengthGain
    #                 #    meri2.collarReach += meri2.collarReachGain
    #
    #         appendSegTime += (time.time() - timeVariable)
    #
    #         '''Since some meristems may have limiters who just sprouted their limiter segment in the last loop, their segments' prevAngsBtwnLmtrs attribute
    #         may not be correctly updated.  This loop goes through these meristems and updates them'''
    #         #for meri in merisToPrep:
    #         #
    #         #    for meri2 in meri.collarLimiters:
    #         #
    #         #        if len(meri2.pathSegs) - 1 == meri2.rootSegIndx:
    #         #
    #         #            limiterSegVector = meri2.pathSegs[-1].vector
    #         #
    #         #            for seg in meri.pathSegs[meri.rootSegIndx:]:
    #         #
    #         #                dotProduct = limiterSegVector[0]*seg.vector[0] + limiterSegVector[1]*seg.vector[1] + limiterSegVector[2]*seg.vector[2]
    #         #                angBetween = math.acos(max(min(dotProduct*oneDivSegLengthSQU, 1.), -1))
    #         #
    #         #                seg.prevAngsBtwnLmtrs.append(angBetween)
    #         #
    #         #merisToPrep = []
    #
    #         timeVariable = time.time()
    #         for meri in elongatedMeristems: #adjust segment vectors to account for added weight and pull force
    #
    #             if meri.newSegs > 0:
    #
    #                 rootSegIndx = meri.rootSegIndx
    #                 weightMult = orderList[meri.order].weightMult
    #                 pullMult = orderList[meri.order].pullMult * meri.randomPullMult
    #                 pfVectorX, pfVectorY, pfVectorZ = meri.pullForceVector[0], meri.pullForceVector[1], meri.pullForceVector[2] #testPullForceVector[0],  testPullForceVector[1], testPullForceVector[2]
    #                 acGradientsReach = orderList[meri.order].acGradientsReach
    #                 overallACGradReach = orderList[meri.order].overallACGradReach
    #                 weightACGradient = orderList[meri.order].weightACGradient
    #                 pullACGradient = orderList[meri.order].pullACGradient
    #                 collarLimitReach = orderList[meri.order].collarLimitReach * meri.branchLength
    #                 collarLimitAngle = orderList[meri.order].collarLimitAngle
    #                 collarReach = meri.collarReach
    #                 collarStrength = meri.collarStrength
    #                 rootSegVector = meri.pathSegs[rootSegIndx].vector
    #                 for seg in meri.limiterSegments:
    #                     try:
    #                         seg.vectorSnapShot = seg.vector
    #                     except AttributeError:
    #                         pass
    #
    #                 balancePolar = angleFinder.findVectorPolar(meri.vectorSum[0],meri.vectorSum[2])
    #
    #                 try:
    #                     rootStartPoint = meri.axialParent.pathSegs[rootSegIndx].startPoint
    #                 except IndexError:
    #                     rootStartPoint = meri.axialParent.loc
    #
    #                 '''BackRotation is a value added to the angleChangeDueToWeight.  It is stronger at the tip of the meristem as it is intended to simulate rotation that
    #                 occurs as a result of segments closer to the base rotating.  Delay can be added to give further control over how much backRotation occurs early on
    #                 in a branch's growth'''
    #
    #                 backRotationDelay = orderList[meri.order].backRotationDelay
    #                 if backRotationDelay > 0.:
    #                     delayEffect = min(meri.branchLength / backRotationDelay, 1.)
    #                 else:
    #                     delayEffect = 1.
    #
    #                 backRotationMult = orderList[meri.order].backRotation * delayEffect
    #                 straightenerStr = orderList[meri.order].straightenerStr
    #
    #                 #gradientPointIndex = min(int((meri.branchLength / acGradientsReach) * 500), 500) #this will use branchLength to determine angle change
    #                 gradientPointIndex = min(int(((meri.parentProximity - meri.branchLength) / overallACGradReach) * 500), 500) #this will use the proximity of the base of the meristem to its parent to determine angle change
    #                 gradientValue = max(min(weightACGradient[gradientPointIndex], 1.), 0.)
    #
    #                 '''Trying something different with the weight gradient.  Actually this makes it more than a weight gradient.  The value will be checked solely with branchLength,
    #                 and all segments will have the same rotation for each time iteration.  Values above .5 will cause an increase in pull while values below .5 cause an increase in
    #                 weight, with 0. being the strongest weight value, and 1. being the strongest pull value.  A value of .5 means no change for either'''
    #                 #if allMeristems.index(meri) == 1:
    #                 #    print timeElapsed, gradientValue, branchAzi, aziChange, branchAziChangeVector1, branchAziChangeVector2, meri.vectorSum, branchPolar
    #                 #gradientValue *= orderList[meri.order].maturityValue
    #                 #
    #                 #if gradientValue >= .5:
    #                 #    gradientValue = (gradientValue - .5) * 2.
    #                 #    branchAngleChangeDueToPull = gradientValue * weightMult
    #                 #    branchAngleChangeDueToWeight = 0.
    #                 #else:
    #                 #    gradientValue = (.5 - gradientValue) * 2.
    #                 #    branchAngleChangeDueToWeight = gradientValue * weightMult
    #                 #    branchAngleChangeDueToPull = 0.
    #
    #                 '''Again, something different with the weightGradient.  This will make it so that the weightGradient determines an absolute overall azimuth angle for the
    #                 branch.  For example, a gradient value of .5 will attempt to set the overall azimuth angle of the branch to .5*weightMult.  Horizontal values should
    #                 correspond to the branch base's proximity to its parent meri for this to work correctly'''
    #                 branchAzi = gradientValue * weightMult #for setting an absolute azi angle
    #                 aziChange = meri.branchAzi - branchAzi
    #                 meri.branchAzi = branchAzi
    #                 if len(meri.pathSegs[meri.rootSegIndx:]) < 4: #if the meristem has little to no growth yet - does not yet have a vector sum
    #                     branchPolar = meri.pol
    #                 else:
    #                     branchPolar = angleFinder.findVectorPolar(meri.vectorSum[0], meri.vectorSum[2])
    #
    #                 lengthTimesSin = segLength*math.sin(PId2)
    #                 sinPolar, cosPolar = math.sin(branchPolar), math.cos(branchPolar)
    #                 branchAziChangeVector1 = (lengthTimesSin*cosPolar, 0., lengthTimesSin*sinPolar)
    #                 lengthTimesSin = segLength*math.sin(PId2 - aziChange)
    #                 branchAziChangeVector2 = (lengthTimesSin*cosPolar, segLength*math.cos(PId2 - aziChange), lengthTimesSin*sinPolar)
    #                 spaceRotator.matrixFromVectors(0, (branchAziChangeVector1, segLength), (branchAziChangeVector2, segLength))
    #
    #                 meri.vectorSum = (0.,0.,0.)
    #
    #                 for count, seg in enumerate(meri.pathSegs[rootSegIndx:]):
    #
    #                     segVectorX, segVectorY, segVectorZ = seg.vector[0], seg.vector[1], seg.vector[2]
    #
    #                     '''miniscule computer miscalculations can accumulate and cause seg.vector's length to not equal segLength, the following 3 lines will readjust
    #                     the size of the vector to correct this'''
    #                     segVectorLength = math.sqrt(segVectorX*segVectorX + segVectorY*segVectorY + segVectorZ*segVectorZ)
    #                     normalizer = segLength / segVectorLength
    #                     segVectorX, segVectorY, segVectorZ = segVectorX*normalizer, segVectorY*normalizer, segVectorZ*normalizer
    #
    #                     segVectorBeforeX, segVectorBeforeY, segVectorBeforeZ = segVectorX, segVectorY, segVectorZ
    #                     segVectorBefore = (segVectorBeforeX, segVectorBeforeY, segVectorBeforeZ)
    #
    #                     gradientPointIndex = min(int(((seg.distalLength - segLength) / acGradientsReach) * 500), 500)
    #                     #angleChangeDueToWeight = max(min(weightACGradient[gradientPointIndex] * weightMult, weightMult),0.)
    #                     #angleChangeDueToWeight = branchAngleChangeDueToWeight
    #                     #angleChangeDueToPull = branchAngleChangeDueToPull
    #                     angleChangeDueToPull = max(min(pullACGradient[gradientPointIndex] * pullMult, pullMult),0.)
    #
    #                     segAziChange = aziChange
    #                     #time to factor in collar strength and reduce the amount of angle change accordingly
    #
    #                     if seg.basalLength < collarReach:
    #                         collarProximity = (collarReach - seg.basalLength) / collarReach #this will be a value between 1 and 0 to multiply the collar strength by
    #                         lossPercentage = min(collarStrength*collarProximity, 1.)
    #                         #angleChangeDueToWeight -= angleChangeDueToWeight*lossPercentage #for use with old weight method
    #                         #angleChangeDueToWeight -= angleChangeDueToWeight*lossPercentage
    #                         angleChangeDueToPull -= angleChangeDueToPull*lossPercentage
    #
    #                         segAziChange -= segAziChange*lossPercentage
    #                         lengthTimesSin = segLength*math.sin(PId2 - aziChange)
    #                         branchAziChangeVector2 = (lengthTimesSin*cosPolar, segLength*math.cos(PId2 - segAziChange), lengthTimesSin*sinPolar)
    #                         spaceRotator.matrixFromVectors(1, (branchAziChangeVector1, segLength), (branchAziChangeVector2, segLength))
    #                         newVector = spaceRotator.vectorFromVectorMatrix(1, seg.vector)
    #                     else:
    #                         newVector = spaceRotator.vectorFromVectorMatrix(0, seg.vector)
    #
    #                     segVectorX, segVectorY, segVectorZ = newVector[0], newVector[1], newVector[2]
    #
    #                     #if seg.distalLength < straightenerStr:
    #                     limit = min(meri.branchLength, straightenerStr)
    #                     angleChangeDueToWeight = max(((limit - seg.distalLength)/ straightenerStr), 0.) * backRotationMult
    #                     #if allMeristems.index(meri) == 1:
    #                     #    print timeElapsed, count, seg.distalLength, max(((limit - seg.distalLength)/ straightenerStr), 0.) * backRotationMult
    #                     seg.azi = math.acos(max(min(segVectorY / segLength, 1.),-1))#maybe unnecessary?
    #                     azi = seg.azi
    #
    #                     '''the angle between the downward vector and the segment vector is equal to PI - seg.azi. The angle across from the new vector is equal to seg.azi.
    #                     By subtracting the sum of the latter and angleChangeDueToWeight we get the third angle in the triangle.'''
    #                     if angleChangeDueToWeight > 0.:
    #                         if azi > 0.001:
    #
    #                             angOppositeSegVector = PI - (angleChangeDueToWeight + azi)
    #                             #if the angleChange crosses the downward vector(i.e. the angOppositeSegVector <= 0.), the equations below won't work
    #                             if angOppositeSegVector > 0.:
    #
    #                                 #now use the law of sines to find the length of the vector to add
    #                                 lengthOfVectorToAdd = (math.sin(angleChangeDueToWeight) * segLength) / math.sin(angOppositeSegVector)
    #                                 #now add this to the seg vector to get a vector that has rotated by angleChangeDueToWeight
    #                                 tempVectorX, tempVectorY, tempVectorZ = segVectorX, segVectorY-lengthOfVectorToAdd, segVectorZ
    #                                 tempVectorLength = math.sqrt(tempVectorX*tempVectorX + tempVectorY*tempVectorY + tempVectorZ*tempVectorZ)
    #                                 normalizer = segLength / tempVectorLength
    #                                 segVectorX, segVectorY, segVectorZ = tempVectorX*normalizer, tempVectorY*normalizer, tempVectorZ*normalizer
    #                                 #backRotationW += angleChangeDueToWeight
    #                             else:
    #                                 '''Since the segment is not rotating the full angleChangeDueToWeight value, we will need to find the angBetween to know what to add
    #                                 to backRotationW'''
    #                                 dotProduct = segVectorY*-segLength
    #                                 angBetween = math.acos(max(min(dotProduct*oneDivSegLengthSQU, 1.),-1.))
    #                                 #backRotationW += angBetween
    #                                 segVectorX, segVectorY, segVectorZ = 0., -segLength, 0.
    #
    #
    #                         else: #the vector is facing straight up, so use the balance polar angle to rotate it
    #                             lengthTimesSin = segLength*math.sin(angleChangeDueToWeight)
    #                             segVectorX = lengthTimesSin*math.cos(balancePolar)
    #                             segVectorY = segLength*math.cos(angleChangeDueToWeight)
    #                             segVectorZ = lengthTimesSin*math.sin(balancePolar)
    #                             #backRotationW += angleChangeDueToWeight
    #
    #                     if angleChangeDueToPull > 0.:
    #
    #                         dotProduct = segVectorX*pfVectorX + segVectorY*pfVectorY + segVectorZ*pfVectorZ
    #                         angBetween = math.acos(max(min(dotProduct*oneDivSegLengthSQU, 1.),-1.))
    #
    #                         if angBetween > angleChangeDueToPull:
    #                             angOppositeSegVector = PI - (PI - angBetween) - angleChangeDueToPull
    #                             lengthOfVectorToAdd = (math.sin(angleChangeDueToPull)*segLength) / math.sin(angOppositeSegVector)
    #                             normalizer = lengthOfVectorToAdd / segLength
    #                             vectorToAddX, vectorToAddY, vectorToAddZ = pfVectorX*normalizer, pfVectorY*normalizer, pfVectorZ*normalizer
    #                             tempVectorX, tempVectorY, tempVectorZ = segVectorX+vectorToAddX, segVectorY+vectorToAddY, segVectorZ+vectorToAddZ
    #                             tempVectorLength = math.sqrt(tempVectorX*tempVectorX + tempVectorY*tempVectorY + tempVectorZ*tempVectorZ)
    #                             normalizer = segLength / tempVectorLength
    #                             segVectorX, segVectorY, segVectorZ = tempVectorX*normalizer, tempVectorY*normalizer, tempVectorZ*normalizer
    #                             #backRotationP += angleChangeDueToPull
    #                         else:
    #                             segVectorX, segVectorY, segVectorZ = pfVectorX, pfVectorY, pfVectorZ
    #                             #backRotationP += angBetween
    #
    #
    #                     for count2, meri2 in enumerate(meri.collarLimiters):#possibly needs revision to make backRotation accurate when limiting is applied
    #
    #                         if seg.basalLength <= collarLimitReach:
    #                             if allMeristems.index(meri) == 1 and count == 0:
    #                                 print "limiting?"
    #                             '''To ensure that segment angles are compared to their positions prior to the current iteration, a "snapshot" is taken for each limiter's
    #                             limiter segment at the beginning of the segment adjust loop.  If this snapshot exists, it will be used as the angle for comparison.  If it does not
    #                             exist, we know that the segment has not been altered yet, so we can use the limiter segment's current position.'''
    #                             if meri2.pathSegs[rootSegIndx].vectorSnapShot == None:
    #                                 limiterVector = meri2.pathSegs[rootSegIndx].vector
    #                             else:
    #                                 limiterVector = meri2.pathSegs[rootSegIndx].vectorSnapShot
    #
    #                             dotProduct = segVectorX*limiterVector[0] + segVectorY*limiterVector[1] + segVectorZ*limiterVector[2]
    #                             angBetween = math.acos(max(min(dotProduct*oneDivSegLengthSQU,1.),-1.))
    #
    #                             #try:
    #                             #    prevAngBetween = seg.prevAngsBtwnLmtrs[count2]
    #                             #
    #                             #    angChangeTowardsLimit = prevAngBetween - angBetween
    #                             #
    #                             #    if angChangeTowardsLimit > 0.:
    #                             #
    #                             crossProduct = (segVectorY*limiterVector[2] - segVectorZ*limiterVector[1],
    #                                             segVectorZ*limiterVector[0] - segVectorX*limiterVector[2],
    #                                             segVectorX*limiterVector[1] - segVectorY*limiterVector[0])
    #
    #                             #angleProximity = max(((prevAngBetween + angBetween) * 0.5) / PI, 0.)
    #                             #angleProximityFactor = -1*angleProximity*angleProximity*angleProximity + 1.
    #                             lengthProximity = seg.basalLength / collarLimitReach
    #                             collarProximityFactor = -1.*lengthProximity + 1.
    #
    #                             #counterRotation = collarLimitAngle #* angleProximityFactor# * collarProximityFactor
    #                             #counterRotation = min(counterRotation, angChangeTowardsLimit)
    #
    #                             limit = collarProximityFactor*collarLimitAngle
    #                             if angBetween < limit:
    #                                 counterRotation = (limit - angBetween)
    #                             else:
    #                                 counterRotation = 0.
    #                             try:
    #                                 cpAngles = angleFinder.findVectorAnglesAndDist(crossProduct)
    #                                 spaceRotator.rotateSpace(cpAngles[0], cpAngles[1])
    #                                 polarFromLimiter = spaceRotator.getRelativePolar((segVectorX, segVectorY, segVectorZ))
    #                                 adjustedVector = spaceRotator.getVector(polarFromLimiter + counterRotation, PId2, segLength)
    #                                 segVectorX, segVectorY, segVectorZ = adjustedVector[0], adjustedVector[1], adjustedVector[2]
    #                                 #seg.prevAngsBtwnLmtrs[count2] = angBetween + counterRotation
    #
    #                             except ZeroDivisionError:
    #                                 pass
    #
    #                                 #else:
    #                                 #    seg.prevAngsBtwnLmtrs[count2] = angBetween
    #
    #                             #except IndexError:
    #                             #
    #                             #    seg.prevAngsBtwnLmtrs.append(angBetween)
    #
    #                     seg.vector = segVectorX, segVectorY, segVectorZ
    #
    #                     '''As long as segment angle changes are not triggering a domino effect along the branch itself, we will not need to trigger a domino effect for
    #                     descendant branches unless they are rooted on the segment (i.e. if seg.split is true).  We can then rotate the branches that need to be domino'd
    #                     with seg.merisOnSeg'''
    #                     if seg.split:
    #
    #                         dotProduct = segVectorX*segVectorBeforeX + segVectorY*segVectorBeforeY + segVectorZ*segVectorBeforeZ
    #                         angBetween = math.acos(max(min(dotProduct*oneDivSegLengthSQU, 1.),-1.))
    #
    #                         if angBetween > .0005: #if the vector has changed direction at all
    #
    #                             spaceRotator.matrixFromVectors(2, (segVectorBefore,segLength), ((segVectorX, segVectorY, segVectorZ),segLength))
    #
    #                             #for seg2 in meri.pathSegs[rootSegIndx+count+1:]: #rotates segments down the branch
    #                             #
    #                             #    seg2.vector = spaceRotator.vectorFromVectorMatrix(1, seg2.vector)
    #
    #                             for meri2 in seg.merisOnSeg: #rotates segments in descendant branches
    #
    #                                 for seg2 in meri2.pathSegs[meri2.rootSegIndx:]:
    #
    #                                     seg2.vector = spaceRotator.vectorFromVectorMatrix(2, seg2.vector)
    #
    #                     '''Here we will update the startPoint for the segment.  This also happens in the draw loop, but only for meristems that are
    #                     creating block points'''
    #
    #                     seg.startPoint =  (rootStartPoint[0] + meri.vectorSum[0], rootStartPoint[1] + meri.vectorSum[1], rootStartPoint[2] + meri.vectorSum[2])
    #                     meri.vectorSum = (meri.vectorSum[0] + seg.vector[0], meri.vectorSum[1] + seg.vector[1], meri.vectorSum[2] + seg.vector[2])
    #
    #                 #update meristem location
    #                 meri.loc = (rootStartPoint[0] + meri.vectorSum[0], rootStartPoint[1] + meri.vectorSum[1], rootStartPoint[2] + meri.vectorSum[2])
    #
    #                 if timeElapsed == lastTime:
    #                     #time to calculate the length of the last segment and scale its vector accordingly
    #                     meri.lastSegLength = meri.branchLength - len(meri.pathSegs[meri.rootSegIndx:-1])*segLength
    #                     normalizer = meri.lastSegLength / segLength
    #                     meri.pathSegs[-1].vector = (meri.pathSegs[-1].vector[0]*normalizer, meri.pathSegs[-1].vector[1]*normalizer, meri.pathSegs[-1].vector[2]*normalizer)
    #                     meri.pathSegs[-1].length = meri.lastSegLength
    #
    #         segmentAdjustTime += (time.time() - timeVariable)
    #
    #         timeVariable = time.time()
    #
    #         if timeElapsed == lastTime: #if this is the last cycle of the last time loop
    #             pass
    #             #self.polarRandomizer(elongatedMeristems)
    #             #self.branchNoise(elongatedMeristems, segLength)
    #
    #             #self.wavies(elongatedMeristems, segLength, orderList)
    #
    #             #We will need to know the boundaries of the tree
    #             #xMin, xMax, yMin, yMax, zMin, zMax = 0.,0.,0.,0.,0.,0.
    #             #
    #             #for meri in elongatedMeristems:
    #             #
    #             #    if meri.order < 5:
    #             #
    #             #        for seg in meri.pathSegs[meri.rootSegIndx:]:
    #             #
    #             #            if seg.startPoint[0] < xMin:
    #             #                xMin = seg.startPoint[0]
    #             #            elif seg.startPoint[0] > xMax:
    #             #                xMax = seg.startPoint[0]
    #             #
    #             #            if seg.startPoint[1] > yMax:
    #             #                yMax = seg.startPoint[1]
    #             #
    #             #            if seg.startPoint[2] < zMin:
    #             #                zMin = seg.startPoint[2]
    #             #            elif seg.startPoint[2] > zMax:
    #             #                zMax = seg.startPoint[2]
    #             #
    #             #treeBoundingBox = (xMin, xMax, yMin, yMax, zMin, zMax)
    #
    #             #self.windDeformer(elongatedMeristems, treeBoundingBox, segLength)
    #
    #         postDeformersTime += (time.time() - timeVariable)
    #
    #         if timeElapsed == secondToLastTime:
    #
    #             drawnMeristems = elongatedMeristems
    #
    #         timeVariable = time.time()
    #
    #         for meri in drawnMeristems:  #update block point locations and append any new block points
    #
    #             if timeElapsed == lastTime and meri.baseOffSet != 0.: #apply base offset
    #                 '''the code in this if block will simply push the base of the meristem up or down its parent branch axis by the amount in meri.baseOffSet'''
    #
    #                 try:
    #                     startPoint = meri.axialParent.pathSegs[meri.rootSegIndx].startPoint
    #                     if meri.baseOffSet > 0.:
    #                         segmentOnParent = meri.axialParent.pathSegs[meri.rootSegIndx]
    #                     else:
    #                         segmentOnParent = meri.axialParent.pathSegs[meri.rootSegIndx - 1]
    #                 except IndexError:
    #                     segmentOnParent = meri.axialParent.pathSegs[-1]
    #                     startPoint = meri.axialParent.loc
    #
    #                 normalizer = meri.baseOffSet / segmentOnParent.length
    #                 vectorToAdd = (segmentOnParent.vector[0]*normalizer,segmentOnParent.vector[1]*normalizer,segmentOnParent.vector[2]*normalizer)
    #                 meri.pathSegs[meri.rootSegIndx].startPoint = (startPoint[0]+vectorToAdd[0], startPoint[1]+vectorToAdd[1], startPoint[2]+vectorToAdd[2])
    #
    #             else:
    #
    #                 meri.pathSegs[meri.rootSegIndx].startPoint = meri.axialParent.pathSegs[meri.rootSegIndx].startPoint
    #
    #             segIndexFromBranchRoot = 0
    #             if meri.newSegs > 0:
    #                 oldSegsEnd = len(meri.pathSegs[meri.rootSegIndx:]) - meri.newSegs
    #             else:
    #                 oldSegsEnd = len(meri.pathSegs[meri.rootSegIndx:])
    #
    #             for seg in meri.pathSegs[meri.rootSegIndx:oldSegsEnd]:
    #
    #                 #if count >= len(currentbSegPointsList) - 1 + prevPoints and totalBranchSegs >= BSI + 2:
    #                 #
    #                 #    radiusTotal = 0.
    #                 #    finalScootVectorX, finalScootVectorY, finalScootVectorZ = 0.,0.,0.
    #                 #
    #                 #    for meri2 in meri.pathSegs[meri.rootSegIndx+count-1].merisOnSeg:
    #                 #
    #                 #        radiusTotal += meri2.bSegs[0].radius
    #                 #
    #                 #    for meri2 in meri.pathSegs[meri.rootSegIndx+count-1].merisOnSeg:
    #                 #
    #                 #        sibSegVector = meri2.pathSegs[meri2.rootSegIndx].vector
    #                 #        dotProduct = seg.vector[0]*sibSegVector[0] + seg.vector[1]*sibSegVector[1] + seg.vector[2]*sibSegVector[2]
    #                 #        angleBetween = round(math.acos(min(dotProduct/(segLength*segLength),1.0)),4)
    #                 #        scalarProj = math.cos(angleBetween)*segLength#sibLength
    #                 #        percentOfSegLength = scalarProj / segLength
    #                 #        scalarProjVector = (seg.vector[0]*percentOfSegLength, seg.vector[1]*percentOfSegLength, seg.vector[2]*percentOfSegLength)
    #                 #        differenceVector = (scalarProjVector[0]-sibSegVector[0], scalarProjVector[1]-sibSegVector[1], scalarProjVector[2]-sibSegVector[2])
    #                 #        differenceVectorLength = math.sqrt(differenceVector[0]*differenceVector[0] + differenceVector[1]*differenceVector[1] + differenceVector[2]*differenceVector[2])
    #                 #        percentOfDiffVLength = (radiusDiff / differenceVectorLength)
    #                 #        scootVector = (differenceVector[0]*percentOfDiffVLength, differenceVector[1]*percentOfDiffVLength, differenceVector[2]*percentOfDiffVLength)
    #                 #
    #                 #        multiplier = meri2.bSegs[0].radius / radiusTotal
    #                 #
    #                 #        finalScootVector = (finalScootVector[0] + (scootVector[0]*multiplier), finalScootVector[1] + (scootVector[1]*multiplier), finalScootVector[2] + (scootVector[2]*multiplier))
    #                 #
    #                 #    currentbSegPointsList[0] = (prevbSegPointsList[-1][0]+finalScootVectorX,
    #                 #                                prevbSegPointsList[-1][1]+finalScootVectorY,
    #                 #                                prevbSegPointsList[-1][2]+finalScootVectorZ)
    #                 #
    #
    #                 if orderList[meri.order].blockPointsTgl == 1:
    #                     if segIndexFromBranchRoot % blockPointResolution == 0 and segIndexFromBranchRoot > 0:
    #
    #                         BPG[seg.bpgIndices[0]][seg.bpgIndices[1]][seg.bpgIndices[2]].remove(seg.bpLoc)
    #
    #                         point = seg.startPoint
    #                         newBPGIndices = (int(point[0]/gridUnitSize + 8.), int(point[1]/gridUnitSize), int(point[2]/gridUnitSize + 8.))
    #                         BPG[newBPGIndices[0]][newBPGIndices[1]][newBPGIndices[2]].append(point)
    #                         seg.bpgIndices = newBPGIndices
    #                         seg.bpLoc = point
    #
    #                 segIndexFromBranchRoot += 1
    #
    #             for seg in meri.pathSegs[oldSegsEnd:]:
    #
    #                 if orderList[meri.order].blockPointsTgl == 1:
    #                     if segIndexFromBranchRoot % blockPointResolution == 0 and segIndexFromBranchRoot > 0:
    #
    #                         newPoint = seg.startPoint
    #                         '''We are using the int function to round our coordinates.  This always rounds towards zero, therefore we must be sure to add the shift value
    #                         before applying the int function, or else values between -1. and 0. will have the same bpg index as values between 1. and 0..'''
    #                         bpgIndices = (int(newPoint[0]/gridUnitSize + 8.), int(newPoint[1]/gridUnitSize), int(newPoint[2]/gridUnitSize + 8.))
    #                         BPG[bpgIndices[0]][bpgIndices[1]][bpgIndices[2]].append(newPoint)
    #                         seg.bpgIndices = bpgIndices
    #                         seg.bpLoc = newPoint
    #
    #                 if segIndexFromBranchRoot + 1 == len(meri.pathSegs[meri.rootSegIndx:]):#this should be moved to the append seg loop right?
    #
    #                     for meri2 in meri.merisIndebtedTo:
    #                         #this only works if meri2 is only owed 1 segment
    #                         meri2.pathSegs.insert(meri2.rootSegIndx, meri.pathSegs[meri2.rootSegIndx])
    #                         meri2.rootSegIndx += 1
    #
    #                     meri.merisIndebtedTo = []
    #
    #
    #                 segIndexFromBranchRoot += 1
    #
    #             lastSeg = meri.pathSegs[-1]
    #             meri.loc = (lastSeg.startPoint[0]+lastSeg.vector[0], lastSeg.startPoint[1]+lastSeg.vector[1], lastSeg.startPoint[2]+lastSeg.vector[2])
    #             segAngles = angleFinder.findVectorAnglesUsingDist(lastSeg.vector, lastSeg.length)
    #             meri.pol = segAngles[0]
    #             meri.azi = segAngles[1]
    #
    #         drawPointsTime += (time.time() - timeVariable)
    #
    #         timeVariable = time.time()
    #         for meri in elongatedMeristems: #determine if a new shoot should grow and grow it if it should
    #
    #             shootGrown = False
    #             lsGrown = False
    #             currentOrderNumber = meri.order
    #
    #             if meri.branchLength >= meri.lengthAtNextNode - .0001 and currentOrderNumber < orders-1 and meri.branchLength >= .6:
    #
    #                 currentOrder = orderList[currentOrderNumber]
    #                 nextOrder = orderList[currentOrderNumber + 1]
    #                 currentNodeFreq = currentOrder.nodeFreq
    #                 currentFluct = currentOrder.nodeFreqFluct*currentNodeFreq #this could be made a class attribute to save time
    #                 existingPathLength = len(meri.pathSegs[meri.rootSegIndx:])*segLength
    #                 pathSegCount = len(meri.pathSegs)
    #
    #                 #bSegIndex = len(meri.bSegs)-1
    #                 newMeriNodeFreqFluctRange = nextOrder.nodeFreq * nextOrder.nodeFreqFluct
    #                 newMeriLSNodeFreqFluctRange = nextOrder.lsNodeFreqMin * nextOrder.lsNodeFreqMax
    #                 nodeDelayFluctRng = nextOrder.lateDelay
    #                 delay = nextOrder.earlyDelay
    #                 polJitter = nextOrder.collarJitter[0]
    #                 dgtSide1 = nextOrder.DGTSides[0]
    #                 dgtSide2 = nextOrder.DGTSides[1]
    #                 spaceRotator.rotateSpace(meri.pol, meri.azi) #might be inacurrate if many segments have grown this loop
    #                 nodesCreated = 0
    #
    #                 while meri.lengthAtNextNode - .0001 <= meri.branchLength:
    #
    #                     #if we are making multiple nodes in this while loop, the budPolar must be rotated within the loop
    #                     if nodesCreated > 0:
    #                         meri.budPolar += currentOrder.nodeRotation + random.uniform(-currentOrder.nodeRotFluct, currentOrder.nodeRotFluct)
    #
    #                         if meri.budPolar > PIm2:
    #                             meri.budPolar -= PIm2
    #
    #                     shiftSeg = 0
    #                     indebted = False
    #                     hasGrowthDebt = False
    #                     timeOwed = 0.
    #                     lengthAtCurrentNode = meri.lengthAtNextNode
    #                     segsAway = round((lengthAtCurrentNode - existingPathLength),5) / segLength
    #                     segsAwayInt = int(segsAway)
    #                     remainder = segsAway - segsAwayInt
    #
    #                     if remainder < 0.:
    #                         if remainder <= -.5:
    #                             baseOffSet = (1. + remainder)*segLength
    #                             shiftSeg = segsAwayInt - 1
    #                         else:
    #                             baseOffSet = remainder*segLength
    #                             shiftSeg = segsAwayInt
    #                     else:
    #                         if remainder > .5:
    #                             baseOffSet = (-1. + remainder)*segLength
    #                             shiftSeg = segsAwayInt + 1
    #                         else:
    #                             baseOffSet = remainder*segLength
    #                             shiftSeg = segsAwayInt
    #
    #                     '''If it is calculated that the new meri's root seg index is a value greater than the number of existing segments on its parent branch (i.e. shiftSeg > 0),
    #                     we will temporarily set it to equal the number of existing segments so that the program works should the meri begin growing before its parent branch segment
    #                     fills in.  I'm hoping this will only cause negligable inaccuracies.  We will put the new meri in a list of merisIndebtedTo on the parent branch, and once
    #                     the parent branch segment is created, the new meri's root seg and bSeg indices will be updated'''
    #
    #                     if shiftSeg > 0:
    #                         shiftSeg = 0
    #                         indebted = True
    #
    #                     timeOwed = (meri.branchLength - lengthAtCurrentNode)/(meri.vigor * segLength) #an estimate of the time that would have passed since this node would have been created
    #                     if timeOwed > .001:
    #                         hasGrowthDebt = True
    #
    #                     nodeRootSegIndx = pathSegCount + shiftSeg
    #                     #bSegPointIndx = (len(meri.bSegs[bSegIndex].points)-1)+shiftSeg
    #                     nodeLengthFromRoot = meri.lengthFromRoot - (meri.branchLength - lengthAtCurrentNode)
    #                     rootRelativePolar = meri.budPolar
    #                     nodeBudRotation = meri.budPolar
    #                     nodeDelay = max(delay + random.uniform(-nodeDelayFluctRng, nodeDelayFluctRng), 0.) #all shoots on this node will have the same delay
    #                     nodeSiblings = []
    #
    #                     normalizer = baseOffSet / segLength
    #
    #                     if nodeRootSegIndx == pathSegCount:
    #
    #                         if baseOffSet == 0.:
    #                             nodeLocation = meri.loc
    #                         else:
    #                             vectorToAdd = (meri.pathSegs[-1].vector[0]*normalizer, meri.pathSegs[-1].vector[1]*normalizer, meri.pathSegs[-1].vector[2]*normalizer)
    #                             nodeLocation = (meri.loc[0] + vectorToAdd[0], meri.loc[1] + vectorToAdd[1], meri.loc[2] + vectorToAdd[2])
    #                     else:
    #                         if baseOffSet == 0.:
    #                             nodeLocation = meri.pathSegs[nodeRootSegIndx].startPoint
    #                         else:
    #                             if baseOffSet > 0.:
    #                                 vectorToAdd = (meri.pathSegs[nodeRootSegIndx].vector[0]*normalizer, meri.pathSegs[nodeRootSegIndx].vector[1]*normalizer, meri.pathSegs[nodeRootSegIndx].vector[2]*normalizer)
    #                             else: #baseOffSet < 0.
    #                                 vectorToAdd = (meri.pathSegs[nodeRootSegIndx-1].vector[0]*normalizer, meri.pathSegs[nodeRootSegIndx-1].vector[1]*normalizer, meri.pathSegs[nodeRootSegIndx-1].vector[2]*normalizer)
    #
    #                             nodeLocation = (meri.pathSegs[nodeRootSegIndx].startPoint[0] + vectorToAdd[0], meri.pathSegs[nodeRootSegIndx].startPoint[1] + vectorToAdd[1], meri.pathSegs[nodeRootSegIndx].startPoint[2] + vectorToAdd[2])
    #
    #                     shoots = currentOrder.shootsPerNode + random.randint(-currentOrder.SPNFluct, currentOrder.SPNFluct)
    #                     #print meri.branchLength, existingPathLength, lengthAtCurrentNode, indebted
    #                     for shoot in range(shoots):
    #
    #                         shootGrown = True
    #                         shootBudPolar = random.uniform(0.,PIm2)
    #
    #                         if polJitter > 0.: #get a random value to add to the polar angle
    #                             polRand = random.triangular(-polJitter,polJitter,0.)
    #                         else:
    #                             polRand = 0.
    #
    #                         dgt = nextOrder.DGT
    #
    #                         if dgt > 0.:
    #
    #                             if nodeBudRotation < PI:
    #                                 if nodeBudRotation > dgtSide1:
    #                                     rootRelativePolar = nodeBudRotation - (dgt*(nodeBudRotation - dgtSide1))
    #                                 else:
    #                                     rootRelativePolar = nodeBudRotation + (dgt*(dgtSide1 - nodeBudRotation))
    #                             else:
    #                                 if nodeBudRotation > dgtSide2:
    #                                     rootRelativePolar = nodeBudRotation - (dgt*(nodeBudRotation - dgtSide2))
    #                                 else:
    #                                     rootRelativePolar = nodeBudRotation + (dgt*(dgtSide2 - nodeBudRotation))
    #                         else:
    #
    #                             rootRelativePolar = nodeBudRotation
    #
    #                         rotatedTempVector = spaceRotator.getVector(rootRelativePolar, 1.57, 1.)
    #                         angles = angleFinder.findVectorAngles(rotatedTempVector)
    #                         #newBSeg = B_Segment([], None, None, None, [])
    #                         newMeri = A_Meristem(nodeLocation, #location
    #                                              (0.,0.,0.), #vector sum
    #                                              angles[0], #polar angle
    #                                              angles[1], #azimuthal angle
    #                                              None, #branch relative azi
    #                                              [], #path segments
    #                                              [meri], #orderParents
    #                                              meri, #axialParent
    #                                              nodeRootSegIndx, #root segment index
    #                                              nodeLengthFromRoot, #length from root
    #                                              0., #branch length
    #                                              0., #segment progress
    #                                              0, #newSegs
    #                                              True, #light check
    #                                              [], #orderChildren
    #                                              [], #axialChildren
    #                                              [], #node siblings
    #                                              [], #descendants
    #                                              [meri], #ancestors
    #                                              meri.order + 1, #order
    #                                              None, #current vigor
    #                                              1., #lightMult
    #                                              1., #individual vigor multiplier
    #                                              1.,
    #                                              timeElapsed + random.uniform(.5, 1.), #random pull change timer
    #                                              nextOrder.xAreaAdded, #xArea added
    #                                              baseOffSet, #base offset
    #                                              [], #linked points
    #                                              segLength, #last segment length
    #                                              0., #parent proximity
    #                                              lengthAtCurrentNode, #parent length at the new meristem's base
    #                                              0., #age
    #                                              shootBudPolar, #bud polar angle
    #                                              shootBudPolar,
    #                                              rootRelativePolar + polRand, #root relative polar
    #                                              nextOrder.collarReach, # current collar reach
    #                                              nextOrder.collarStrength, # current collar strength
    #                                              nextOrder.collarReachGain, #collar reach gain
    #                                              nextOrder.collarStrengthGain, #collar strength gain
    #                                              [], #collar limiters
    #                                              [], #collar strengthenees
    #                                              [nodeRootSegIndx], #limiter segments
    #                                              (0.,0.,0.,0.), #pull force vector
    #                                              1., #suppression multiplier (1. means no suppression is being applied)
    #                                              1., #suppression limit
    #                                              currentMaxEndogenousVigor,
    #                                              1., #suppression applied
    #                                              0., #suppression level
    #                                              currentVigTimeReachList[meri.order + 1], #current falloff reach
    #                                              nextOrder.nodeFreq,
    #                                              nextOrder.lsNodeFreqMin,
    #                                              (.6 + nextOrder.nodeFreq) + random.uniform(-newMeriNodeFreqFluctRange, newMeriNodeFreqFluctRange),
    #                                              (.6 + nextOrder.lsNodeFreqMin) + random.uniform(-newMeriLSNodeFreqFluctRange, newMeriLSNodeFreqFluctRange),
    #                                              [],
    #                                              hasGrowthDebt,
    #                                              timeOwed,
    #                                              CloneInfo(False, None, None), #clone info class
    #                                              nodeDelay, #delay time
    #                                              max(segLength, nextOrder.lsShedLengthMin + random.triangular(-nextOrder.lsShedLengthMax, nextOrder.lsShedLengthMax, 0.)),
    #                                              1000000.)
    #
    #                         nodeSiblings.append(newMeri)
    #
    #                         if shiftSeg < 0 :
    #                             newMeri.pathSegs.extend(meri.pathSegs[0:shiftSeg])
    #                         else:
    #                             newMeri.pathSegs.extend(meri.pathSegs)
    #
    #                         if indebted:
    #                             meri.merisIndebtedTo.append(newMeri)
    #
    #                         meri.axialChildren.append(newMeri)
    #                         meri.orderChildren.append(newMeri)
    #                         meri.collarStrengthenees.append(newMeri)
    #
    #                         newMeri.ancestors.extend(meri.ancestors)
    #                         meri.descendants.append(newMeri)
    #
    #                         for meri2 in meri.ancestors:
    #
    #                             meri2.descendants.append(newMeri)
    #
    #                         newMeristemCatcher.append(newMeri)
    #
    #                         nodeBudRotation += PIm2 / shoots
    #
    #                         if nodeBudRotation > PIm2:
    #                             nodeBudRotation -= PIm2
    #
    #                     nodesCreated += 1
    #
    #                     if currentNodeFreq > segX4:
    #                         meri.lengthAtNextNode = round((meri.lengthAtNextNode + (currentNodeFreq + random.uniform(-currentFluct, currentFluct)))/segLength) * segLength
    #                     else:
    #                         meri.lengthAtNextNode = meri.lengthAtNextNode + (currentNodeFreq + random.uniform(-currentFluct, currentFluct))
    #
    #                     '''Any segment with an index equal to one of its meristem's child branch root segments is a potential limiter segment.  Since the segment may not yet
    #                     exist, we will place the index itself into the limterSegments list.  Later, when the segment is created, we will check the list for its index.  If it is
    #                     found we will replace the integer value with the segment.'''
    #                     if nodeRootSegIndx not in meri.limiterSegments:
    #                             meri.limiterSegments.append(nodeRootSegIndx)
    #
    #                     for sib in nodeSiblings:
    #
    #                         sib.nodeSiblings.extend(nodeSiblings)
    #
    #
    #             if orderList[currentOrderNumber].lsTgl and meri.branchLength >= meri.lengthAtNextLSNode - .0001 and meri.branchLength > 0.6:
    #
    #                 currentOrder = orderList[currentOrderNumber]
    #                 currentNodeFreq = currentOrder.lsNodeFreqMin
    #                 currentFluct = currentOrder.lsNodeFreqMax*currentNodeFreq #this could be made a class attribute to save time
    #
    #                 if timeElapsed < orderList[currentOrderNumber].lsISTime:
    #                     nodesCreated = 0
    #                     while meri.lengthAtNextLSNode - .0001 <= meri.branchLength:
    #                         if currentNodeFreq > segX4:
    #                             meri.lengthAtNextLSNode = round((meri.lengthAtNextLSNode + (currentNodeFreq + random.uniform(-currentFluct, currentFluct)))/segLength) * segLength
    #                         else:
    #                             meri.lengthAtNextLSNode = meri.lengthAtNextLSNode + (currentNodeFreq + random.uniform(-currentFluct, currentFluct))
    #                         nodesCreated += 1
    #
    #                     for seg in meri.pathSegs: #insta-shed meristems still need to effect the thickness of their parents
    #
    #                         seg.xArea += meri.xAreaAdded * nodesCreated
    #                 else:
    #
    #                     existingPathLength = len(meri.pathSegs[meri.rootSegIndx:])*segLength
    #                     pathSegCount = len(meri.pathSegs)
    #                     #bSegIndex = len(meri.bSegs)-1
    #                     lsDelayFluctRng = orderList[-1].lateDelay
    #                     delay = orderList[-1].earlyDelay
    #                     polJitter = orderList[-1].collarJitter[0]
    #                     dgtSide1 = orderList[-1].DGTSides[0]
    #                     dgtSide2 = orderList[-1].DGTSides[1]
    #                     spaceRotator.rotateSpace(meri.pol, meri.azi)
    #                     nodesCreated = 0
    #
    #                     while meri.lengthAtNextLSNode - .0001 <= meri.branchLength:
    #
    #                         #if we are making multiple nodes in this while loop, the budPolar must be rotated within the loop
    #                         if nodesCreated > 0:
    #                             meri.lsBudPolar += currentOrder.lsNodeRotMin + random.uniform(-currentOrder.lsNodeRotMax, currentOrder.lsNodeRotMax)
    #
    #                             if meri.lsBudPolar > PIm2:
    #                                 meri.lsBudPolar -= PIm2
    #
    #                         shiftSeg = 0
    #                         indebted = False
    #                         hasGrowthDebt = False
    #                         timeOwed = 0.
    #                         lengthAtCurrentNode = meri.lengthAtNextLSNode
    #                         segsAway = round((lengthAtCurrentNode - existingPathLength),5) / segLength
    #                         segsAwayInt = int(segsAway)
    #                         remainder = segsAway - segsAwayInt
    #
    #                         if remainder < 0.:
    #                             if remainder <= -.5:
    #                                 baseOffSet = (1. + remainder)*segLength
    #                                 shiftSeg = segsAwayInt - 1
    #                             else:
    #                                 baseOffSet = remainder*segLength
    #                                 shiftSeg = segsAwayInt
    #                         else:
    #                             if remainder > .5:
    #                                 baseOffSet = (-1. + remainder)*segLength
    #                                 shiftSeg = segsAwayInt + 1
    #                             else:
    #                                 baseOffSet = remainder*segLength
    #                                 shiftSeg = segsAwayInt
    #
    #                         if shiftSeg > 0:
    #                             shiftSeg = 0
    #                             indebted = True
    #
    #                         timeOwed = (meri.branchLength - lengthAtCurrentNode)/(meri.vigor * segLength) #an estimate of the time that would have passed since this node would have been created
    #                         if timeOwed > .001:
    #                             hasGrowthDebt = True
    #
    #                         nodeRootSegIndx = pathSegCount + shiftSeg
    #                         #bSegPointIndx = (len(meri.bSegs[bSegIndex].points)-1)+shiftSeg
    #                         nodeLengthFromRoot = meri.lengthFromRoot - (meri.branchLength - lengthAtCurrentNode)
    #                         rootRelativePolar = meri.lsBudPolar
    #                         nodeBudRotation = meri.lsBudPolar
    #                         lsDelay = max(delay + random.uniform(-lsDelayFluctRng, lsDelayFluctRng), 0.)
    #                         nodeSiblings = []
    #
    #                         normalizer = baseOffSet / segLength
    #
    #                         if nodeRootSegIndx == pathSegCount:
    #
    #                             if baseOffSet == 0.:
    #                                 nodeLocation = meri.loc
    #                             else:
    #                                 vectorToAdd = (meri.pathSegs[-1].vector[0]*normalizer, meri.pathSegs[-1].vector[1]*normalizer, meri.pathSegs[-1].vector[2]*normalizer)
    #                                 nodeLocation = (meri.loc[0] + vectorToAdd[0], meri.loc[1] + vectorToAdd[1], meri.loc[2] + vectorToAdd[2])
    #                         else:
    #                             if baseOffSet == 0.:
    #                                 nodeLocation = meri.pathSegs[nodeRootSegIndx].startPoint
    #                             else:
    #                                 if baseOffSet > 0.:
    #                                     vectorToAdd = (meri.pathSegs[nodeRootSegIndx].vector[0]*normalizer, meri.pathSegs[nodeRootSegIndx].vector[1]*normalizer, meri.pathSegs[nodeRootSegIndx].vector[2]*normalizer)
    #                                 else: #baseOffSet < 0.
    #                                     vectorToAdd = (meri.pathSegs[nodeRootSegIndx-1].vector[0]*normalizer, meri.pathSegs[nodeRootSegIndx-1].vector[1]*normalizer, meri.pathSegs[nodeRootSegIndx-1].vector[2]*normalizer)
    #
    #                                 nodeLocation = (meri.pathSegs[nodeRootSegIndx].startPoint[0] + vectorToAdd[0], meri.pathSegs[nodeRootSegIndx].startPoint[1] + vectorToAdd[1], meri.pathSegs[nodeRootSegIndx].startPoint[2] + vectorToAdd[2])
    #
    #                         leafShoots = currentOrder.lsSPNMin + random.randint(-currentOrder.lsSPNMax, currentOrder.lsSPNMax)
    #
    #                         for leafShoot in range(leafShoots):
    #
    #                             shootGrown = True
    #                             lsGrown = True
    #
    #                             shootBudPolar = random.uniform(0.,PIm2)
    #
    #                             if polJitter > 0.:
    #                                 polRand = random.triangular(-polJitter,polJitter,0.)
    #                             else:
    #                                 polRand = 0.
    #
    #                             dgt = orderList[-1].DGT
    #
    #                             if dgt > 0.:
    #
    #                                 if nodeBudRotation < PI:
    #                                     if nodeBudRotation > dgtSide1:
    #                                         rootRelativePolar = nodeBudRotation - (dgt*(nodeBudRotation - dgtSide1))
    #                                     else:
    #                                         rootRelativePolar = nodeBudRotation + (dgt*(dgtSide1 - nodeBudRotation))
    #                                 else:
    #                                     if nodeBudRotation > dgtSide2:
    #                                         rootRelativePolar = nodeBudRotation - (dgt*(nodeBudRotation - dgtSide2))
    #                                     else:
    #                                         rootRelativePolar = nodeBudRotation + (dgt*(dgtSide2 - nodeBudRotation))
    #                             else:
    #
    #                                 rootRelativePolar = nodeBudRotation
    #
    #                             selfShedLength = meri.lsShedLengthMin + random.triangular(0., currentOrder.lsShedLengthMax, 0.)
    #
    #                             rotatedTempVector = spaceRotator.getVector(rootRelativePolar, 1.57, 1.)
    #                             angles = angleFinder.findVectorAngles(rotatedTempVector)
    #                             #newBSeg = B_Segment([], None, None, None, [])
    #                             newMeri = A_Meristem(nodeLocation, #location
    #                                                  (0.,0.,0.), #vector sum
    #                                                  angles[0], #polar angle
    #                                                  angles[1], #azimuthal angle
    #                                                  None, #branch relative azi
    #                                                  [], #path segments
    #                                                  [meri], #orderParents
    #                                                  meri, #axialParent
    #                                                  len(meri.pathSegs)+shiftSeg, #root segment index
    #                                                  nodeLengthFromRoot, #length from root
    #                                                  0., #branch length
    #                                                  0., #segment progress
    #                                                  0, #newSegs
    #                                                  True, #light check
    #                                                  [], #orderChildren
    #                                                  [], #axialChildren
    #                                                  [], #node siblings
    #                                                  [], #descendants
    #                                                  [meri], #ancestors
    #                                                  5, #order
    #                                                  None, #current vigor
    #                                                  1., #lightMult
    #                                                  1., #individual vigor multiplier
    #                                                  1.,
    #                                                  timeElapsed + random.uniform(.5, 1.), #random pull change timer
    #                                                  orderList[-1].xAreaAdded, #xArea added
    #                                                  baseOffSet, #base offset
    #                                                  [], #linked points
    #                                                  segLength, #last segment length
    #                                                  0., #parent proximity
    #                                                  lengthAtCurrentNode,
    #                                                  0., #age
    #                                                  shootBudPolar, #bud polar angle
    #                                                  shootBudPolar,
    #                                                  rootRelativePolar + polRand,
    #                                                  orderList[-1].collarReach, # current collar reach
    #                                                  orderList[-1].collarStrength, # current collar strength
    #                                                  orderList[-1].collarReachGain, #collar reach gain
    #                                                  orderList[-1].collarStrengthGain, #collar strength gain
    #                                                  [], #collar limiters
    #                                                  [], #collar strengthenees
    #                                                  [], #limiter segments
    #                                                  (0.,0.,0.,0.), #pull force vector
    #                                                  1., #suppression multiplier (1. means no suppression is being applied)
    #                                                  1., #suppression
    #                                                  currentMaxEndogenousVigor,
    #                                                  1., #suppression applied
    #                                                  0., #suppression level
    #                                                  currentVigTimeReachList[-1], #current falloff reach
    #                                                  99999., #node freq
    #                                                  99999., #leaf shoot node freq
    #                                                  99999., #length at next node
    #                                                  99999., #length at next ls node
    #                                                  [],
    #                                                  hasGrowthDebt,
    #                                                  timeOwed,
    #                                                  CloneInfo(False, None, None), #clone info class
    #                                                  lsDelay,
    #                                                  None,
    #                                                  selfShedLength)
    #
    #                             nodeSiblings.append(newMeri)
    #
    #                             if shiftSeg < 0 :
    #                                 newMeri.pathSegs.extend(meri.pathSegs[0:shiftSeg])
    #                             else:
    #                                 newMeri.pathSegs.extend(meri.pathSegs)
    #
    #                             if indebted:
    #                                 meri.merisIndebtedTo.append(newMeri)
    #
    #                             meri.axialChildren.append(newMeri)
    #                             meri.orderChildren.append(newMeri)
    #                             meri.collarStrengthenees.append(newMeri)
    #
    #                             newMeri.ancestors.extend(meri.ancestors)
    #                             meri.descendants.append(newMeri)
    #
    #                             for meri2 in meri.ancestors:
    #
    #                                 meri2.descendants.append(newMeri)
    #
    #                             newMeristemCatcher.append(newMeri)
    #
    #                             nodeBudRotation += PIm2 / shoots
    #
    #                             if nodeBudRotation > PIm2:
    #                                 nodeBudRotation -= PIm2
    #
    #                         nodesCreated += 1
    #
    #                         if currentNodeFreq > segX4:
    #                             meri.lengthAtNextLSNode = round((meri.lengthAtNextLSNode + (currentNodeFreq + random.uniform(-currentFluct, currentFluct)))/segLength) * segLength
    #                         else:
    #                             meri.lengthAtNextLSNode = meri.lengthAtNextLSNode + (currentNodeFreq + random.uniform(-currentFluct, currentFluct))
    #
    #             if shootGrown: #calculate the relative polar angle of the next node
    #
    #                 if lsGrown:
    #
    #                     meri.lsBudPolar += currentOrder.lsNodeRotMin + random.uniform(-currentOrder.lsNodeRotMax,currentOrder.lsNodeRotMax)
    #
    #                     if meri.lsBudPolar > PIm2:
    #                         meri.lsBudPolar -= PIm2
    #
    #                 else:
    #
    #                     meri.budPolar += currentOrder.nodeRotation + random.uniform(-currentOrder.nodeRotFluct, currentOrder.nodeRotFluct)
    #
    #                     if meri.budPolar > PIm2:
    #                         meri.budPolar -= PIm2
    #
    #
    #
    #         undelayedMeristems = []
    #
    #         for meri in delayedMeristems:
    #
    #             meri.age += 1.
    #             meri.delay -= 1.
    #
    #             if meri.delay <= 0.:
    #
    #                 meri.delay = 0.
    #                 undelayedMeristems.append(meri)
    #
    #         for meri in undelayedMeristems:
    #
    #             delayedMeristems.remove(meri)
    #             activeMeristems.append(meri)
    #
    #         for meri in newMeristemCatcher:
    #
    #             if meri.delay > 0.:
    #
    #                 delayedMeristems.append(meri)
    #
    #             else:
    #
    #                 activeMeristems.append(meri)
    #
    #         allMeristems.extend(newMeristemCatcher)
    #         newMeristemCatcher = []
    #
    #
    #         newShootTime += (time.time() - timeVariable)
    #
    #         timeElapsed += 1.
    #         cmds.progressBar(bluePrintProgressControl, edit=1, step=1)
    #
    #     cmds.deleteUI(bluePrintProgressWindow)
    #
    #     #for b in blockPoints:
    #     #    cmds.sphere(r=pointRadius)
    #     #    cmds.move(b[0], b[1], b[2])
    #
    #     #for x in BPG:
    #     #    for y in x:
    #     #        for z in y:
    #     #            for pt in z:
    #     #
    #     #                cmds.sphere(r=pointRadius)
    #     #                cmds.move(pt[0], pt[1], pt[2])
    #     #
    #
    #
    #     #if len(allMeristems) > 1:
    #     #    for seg in allMeristems[1].pathSegs[allMeristems[1].rootSegIndx:]:
    #     #        cmds.sphere(r=.5)
    #     #        cmds.move(seg.startPoint[0], seg.startPoint[1], seg.startPoint[2])
    #
    #     timeVariable = time.time()
    #
    #
    #     for meri in elongatedMeristems: #create the linked points list for meristems
    #
    #         for seg in meri.pathSegs[meri.rootSegIndx:]:
    #             meri.linkedPoints.append(seg.startPoint)
    #
    #         meri.linkedPoints.append(meri.loc)
    #
    #     bSegPrepTime += (time.time() - timeVariable)
    #
    #     bluePrintingTime = time.time()
    #     print "Blueprinting time:", bluePrintingTime - self.startTime
    #     print "Intro time", self.introTime
    #     print "Vigor/Light calc time", vigorAndBPCalcTime
    #     print "Append seg time:", appendSegTime
    #     print "force calc time:", forceCalcTime
    #     print "collar adjust time:", collarAdjustTime
    #     print "segment adjust time:", segmentAdjustTime
    #     print "draw points time:", drawPointsTime
    #     print "new shoots time:", newShootTime
    #     print "bSeg prep time:", bSegPrepTime
    #     print "shed time:", shedTime
    #     print "postDeformersTime:", postDeformersTime
    #     print "Trunk length:", seed.lengthFromRoot
    #     if len(allMeristems) > 1:
    #         print "first node age and length", allMeristems[1].age, allMeristems[1].branchLength
    #
    #     timeVariable = time.time()
    #     for meri in elongatedMeristems:
    #
    #         segVectors = []
    #         radii = []
    #         dividers = 0
    #         origin = meri.pathSegs[meri.rootSegIndx].startPoint
    #         currentXArea = meri.pathSegs[meri.rootSegIndx].xArea
    #         dividerWidths = []
    #         skinRadius = orderList[meri.order].skinRadius
    #
    #         for index, seg in enumerate(meri.pathSegs[meri.rootSegIndx:]):
    #
    #             radius = math.sqrt(seg.xArea / PI) + skinRadius
    #             radii.append(radius)
    #             segVectors.append((seg.vector[0], seg.vector[1], seg.vector[2]))
    #             if seg.xArea < currentXArea:
    #                 dividers += 1
    #                 maxRadius = 0.
    #
    #                 for meri2 in meri.pathSegs[(meri.rootSegIndx + index) - 1].merisOnSeg:
    #
    #                     branchingRadius = math.sqrt(meri2.pathSegs[meri2.rootSegIndx].xArea / PI)
    #
    #                     if branchingRadius  > maxRadius:
    #                         maxRadius = branchingRadius
    #
    #                 dividerWidths.append(maxRadius*2)
    #                 currentXArea = seg.xArea
    #
    #         cmds.createMesh(sv=segVectors, r=radii, o=origin, sl=segLength, dw=dividerWidths)
    #
    #
    #     print "in python: ", len(lvInfoMatrix[1][3][7][4])
    #     print "in python: ", len(lvInfoMatrix[2][8][7][3])
    #     print "in python: ", len(lvInfoMatrix[3][6][7][6])
    #     print "in python: ", len(lvInfoMatrix[4][13][7][7])
    #     print "in python: ", len(lvInfoMatrix[5][4][7][0])
    #
    #
    #     #self.buildTreeMesh(elongatedMeristems, orderList, segLength)
    #
    #     endTime = time.time()
    #     print "Building time", endTime - timeVariable

    # def branchNoise(self, meristemList, segLength):
    #
    #     for meri in meristemList:
    #
    #             #angles = angleFinder.findVectorAnglesUsingDist(meri.pathSegs[meri.rootSegIndx].vector, segLength)
    #             #spaceRotator.rotateSpace(angles[0],angles[1])
    #             #rndPol = random.uniform(0., 6.28)
    #             #azi = 2.356
    #             #vectorToAdd = spaceRotator.getVector(rndPol, azi, .1)
    #
    #             #if meristemList.index(meri) == 1:
    #             #    points = []
    #             #    for seg in meri.pathSegs[meri.rootSegIndx:]:
    #             #
    #             #        points.append(seg.startPoint)
    #             #
    #             #    cmds.curve(d=1, p=points)
    #         if meri.order == 1:
    #
    #             '''Branch noise approach 1:  Loop through the branch segments starting at its root.  On the first one, and every so often, find the angles of the
    #             current branch segment and rotate space to those angles.  With each loop, add (or subract) a random amount to both a polar and azimuth value, and set
    #             the segment's vector according to these values'''
    #
    #             pol = random.uniform(0., 6.28)
    #             azi = 0.
    #             curvePoint = meri.pathSegs[meri.rootSegIndx].startPoint
    #             angles = angleFinder.findVectorAnglesUsingDist(meri.pathSegs[meri.rootSegIndx].vector, segLength)
    #             spaceRotator.rotateSpace(angles[0],angles[1])
    #             lengthCounter = 0
    #             straightenerLimiter = 0
    #             lengthLimit = 30. #the noise strength will be weaker closer to a distalLength of 80., any length 80 or higher will not have noise
    #
    #             for seg in meri.pathSegs[meri.rootSegIndx:]:
    #
    #                 if lengthCounter > .9: #this is just to save time.  Space doesn't need to be rotated at every segment, so only do it every so often.
    #                     angles = angleFinder.findVectorAnglesUsingDist(seg.vector, seg.length)
    #                     spaceRotator.rotateSpace(angles[0],angles[1])
    #                     lengthCounter = 0.
    #
    #             #if meristemList.index(meri) == 1:
    #                 '''If the polar and azimuth angles are continually incremented, there is a good chance that the curve drawn with these angles (the deformed branch) will
    #                 end up far away from its original curve.  We may not want this deformer to cause such a large scale change, so every so often we will check the deformed
    #                 curve's distance from the original.  If it is outside of a set radius from the original branch, we will redirect the curve.'''
    #
    #                 '''Redirecting the curve may cause an abrupt change in its angle, and since the curve may be outside of the boundary even after being redirected,
    #                 doing it in every loop may cause a very zig-zaggy curve, which we generally don't want. So we add a counter (straightenerLimiter) to make sure
    #                 that the curve isn't redirected too often'''
    #                 if straightenerLimiter > 3:
    #                     curveToBranchVector = (curvePoint[0] - seg.startPoint[0], curvePoint[1] - seg.startPoint[1], curvePoint[2] - seg.startPoint[2])
    #                     curveToBranchDist = math.sqrt(curveToBranchVector[0]*curveToBranchVector[0] + curveToBranchVector[1]*curveToBranchVector[1] + curveToBranchVector[2]*curveToBranchVector[2])
    #
    #                     if curveToBranchDist > .1:
    #
    #                         #print "adjusting", azi, seg.basalLength
    #                         azi = 0.
    #                         #pol = spaceRotator.getRelativePolar(curveToBranchVector)
    #                         #print "adjusted", pol
    #                         #print " "
    #                         straightenerLimiter = 0
    #                 else:
    #                     straightenerLimiter += 1
    #
    #                 pol += random.uniform(-.785, .785)
    #                 azi += random.uniform(-.02,.02) #* max((lengthLimit - seg.distalLength) / lengthLimit, 0.)
    #                 seg.vector = spaceRotator.getVector(pol, azi, seg.length)
    #                 curvePoint = (curvePoint[0] + seg.vector[0], curvePoint[1] + seg.vector[1], curvePoint[2] + seg.vector[2])
    #                 lengthCounter += segLength
    #
    #
    #         if 1 < meri.order < 5:
    #
    #             '''BranchNoise approach 2:  This is designed to create small vertical curves of random sizes and at random locations along each branch'''
    #             out = True
    #             increase = True
    #             bendLength = random.uniform(segLength*2, segLength*6)
    #             bendProgress = 0.
    #             pauseProgress = 0.
    #             pol = 0.
    #             azi = 0.
    #             lastAngleChange = 0.
    #             totalOutAngle = 0.
    #             angleChange = random.uniform(.01,.07)
    #
    #             angles = angleFinder.findVectorAnglesUsingDist(meri.pathSegs[meri.rootSegIndx].vector, segLength)
    #
    #             spaceRotator.rotateSpace(angles[0],angles[1])
    #             #curvePoint = meri.pathSegs[meri.rootSegIndx].startPoint
    #
    #             if random.uniform(0.,1.) > .5: #give a chance to pause (not bend) for a length of the branch
    #                 pauseLength = random.uniform(segLength,segLength*10)
    #                 bend = False
    #             else:
    #                 bend = True
    #
    #             for count, seg in enumerate(meri.pathSegs[meri.rootSegIndx:]):
    #
    #                 if bend:
    #
    #                     angles = angleFinder.findVectorAnglesUsingDist(seg.vector, seg.length)
    #                     spaceRotator.rotateSpace(angles[0],angles[1])
    #
    #                     if out: #bending away from the branch
    #                         if increase:
    #                             azi += angleChange
    #                         else:
    #                             azi -= angleChange
    #
    #                     else:
    #                         if increase:
    #                             azi -= angleChange
    #                         else:
    #                             azi += angleChange
    #
    #                     seg.vector = spaceRotator.getVector(pol, azi, seg.length)
    #                     #curvePoint = (curvePoint[0] + seg.vector[0], curvePoint[1] + seg.vector[1], curvePoint[2] + seg.vector[2])
    #
    #                     bendProgress += segLength
    #
    #                     if bendProgress > bendLength:
    #
    #                         #curveToBranchVector = (curvePoint[0] - seg.startPoint[0], curvePoint[1] - seg.startPoint[1], curvePoint[2] - seg.startPoint[2])
    #                         #curveToBranchDist = math.sqrt(curveToBranchVector[0]*curveToBranchVector[0] + curveToBranchVector[1]*curveToBranchVector[1] + curveToBranchVector[2]*curveToBranchVector[2])
    #
    #                         if out:
    #                             out = False
    #                         else:
    #                             out = True
    #                         increase = True
    #                         lastAngleChange = 0.
    #                         bendProgress = 0.
    #                         bendLength = random.uniform(segLength*2, segLength*6)
    #                         angleChange = random.uniform(.01,.07)
    #
    #                         if random.uniform(0.,1.) > .5: #give a chance to pause (not bend) for a length of the branch
    #                             pauseLength = random.uniform(segLength,segLength*10)
    #                             bend = False
    #
    #                     elif bendProgress > bendLength*.5:
    #                         if increase:
    #                             increase = False
    #                             lastAngleChange = 0.
    #
    #                 else:
    #
    #                     pauseProgress += segLength
    #
    #                     if pauseProgress > pauseLength:
    #                         bend = True
    #                         pauseProgress = 0.

    # def polarRandomizer(self, meristemList):
    #
    #     '''Because there are only so many light vectors, meristems within similar vicinities may continually choose the same one and over time end up with identical
    #     angles (most noticeable longitudinally).  To avoid this unnatural appearance, this function just applies a small random polar rotation to branches'''
    #
    #     for meri in meristemList:
    #
    #         if meri.order == 2:
    #
    #             parentSegVector = meri.pathSegs[meri.rootSegIndx - 1].vector
    #             orientation = angleFinder.findVectorAngles(parentSegVector)
    #             spaceRotator.rotateSpace(orientation[0], orientation[1])
    #             #create two vectors at 90 degree azimuth angles and separated by a random polar angle in the meristem's parent orientation
    #             vector1 = spaceRotator.getVector(0.,PId2,1.)
    #             vector2 = spaceRotator.getVector(0. + random.uniform(-0.174533,0.174533),PId2,1.)
    #             #create a matrix from these vectors with which to multiply each segment vector in the branch
    #             spaceRotator.matrixFromVectors(0, (vector1,1.),(vector2,1.))
    #
    #             for seg in meri.pathSegs[meri.rootSegIndx:]:
    #
    #                 seg.vector = spaceRotator.vectorFromVectorMatrix(0, seg.vector)
    #
    #             for meri2 in meri.descendants:
    #
    #                 for seg in meri2.pathSegs[meri2.rootSegIndx:]:
    #
    #                     seg.vector = spaceRotator.vectorFromVectorMatrix(0, seg.vector)

    # def windDeformer(self, meristemList, boundingBox, segLength):
    #
    #     '''To create an ambient wind deformer, we will create imaginary spheres of randomly differing sizes at random locations throughout the tree and
    #     assign each sphere with a vector representing the direction and magnitude of the wind in that sphere.  We will then check the distance of each
    #     effected branch to each sphere to determine how to deform the branch.
    #     To ensure that the spheres are placed in such a way that at least most of the branches will have some wind deformation, we can divide the space in which
    #     the tree exists into sectors, each with a range of values from which to draw a random value.  The sectors' information will be stored in a list of lists,
    #     with the primary elements representing vertical levels divided by height, and secondary elements representing the sectors around the center axis divided
    #     by polar angles.  like this:
    #     [[(levelHeightRngStart, levelHeightRngEnd),(sectorPolarRngStart, sectorPolarRngEnd)], [(levelHeightRngStart, levelHeightRngEnd),(sectorPolarRngStart, sectorPolarRngEnd)]]'''
    #
    #     '''for now we're assuming the tree is somewhat symmetrical, so we only need a distance from the center of the tree (radius), which we can estimate
    #     by finding the difference between either the x or z boundaries and dividing it in two'''
    #     xRangeDiv2 = (boundingBox[1] - boundingBox[0]) / 2
    #
    #     boundaryRadius = xRangeDiv2
    #
    #     ambientWindDeformerLevels = int(round(boundingBox[3]/boundaryRadius))
    #     ambientWindDeformerSectors = 3
    #     ambientWindDeformerSpace = []
    #     levelHeight = boundingBox[3] / ambientWindDeformerLevels
    #     height = 0.
    #
    #     for lv in range(ambientWindDeformerLevels):
    #
    #         heightRngStart = height
    #         height += levelHeight
    #         heightRngEnd = height
    #         lvInfo = [(heightRngStart, heightRngEnd)]
    #         polar = 0.
    #
    #         for sect in range(ambientWindDeformerSectors):
    #
    #             rngStart = polar
    #             polar += PIm2 / ambientWindDeformerSectors
    #             rngEnd = polar
    #             lvInfo.append((rngStart, rngEnd))
    #
    #         ambientWindDeformerSpace.append(lvInfo)
    #
    #     windSpheres = []
    #
    #     for lv in ambientWindDeformerSpace:
    #
    #         for sect in lv[1:]:
    #
    #             randomRadius = boundaryRadius*0.8 + random.uniform(-boundaryRadius*.1,boundaryRadius*.1)
    #             yCoord = random.uniform(lv[0][0], lv[0][1])
    #             polarCoord = random.uniform(sect[0], sect[1])
    #             xCoord = randomRadius * math.cos(polarCoord)
    #             zCoord = randomRadius * math.sin(polarCoord)
    #             sphereRadius = boundaryRadius*0.7 + random.uniform(-boundaryRadius*.1, boundaryRadius*.1)
    #
    #             cmds.sphere(r=sphereRadius)
    #             cmds.move(xCoord, yCoord, zCoord)
    #
    #             strength = random.uniform(.3,.8)
    #             azi = random.uniform(1.4, 1.7)
    #             '''Im guessing the polar angle of the wind should be close to tangent with the perimeter of the tree.  We will
    #             factor this in by adding or subtracting 90 degrees from the sphere's polar coordinate, and then randomizing from that starting point.'''
    #             sides = [polarCoord + 1.57, polarCoord - 1.57]
    #             pol = random.choice(sides) + random.uniform(-.4,.4)
    #             windVector = ((strength*math.sin(azi)*math.cos(pol),
    #                            strength*math.cos(azi),
    #                            strength*math.sin(azi)*math.sin(pol)))
    #
    #             windSpheres.append([(xCoord, yCoord, zCoord), sphereRadius, windVector])
    #
    #     for meri in meristemList:
    #
    #         if meri.order == 2:
    #
    #             branchMidPoint = meri.pathSegs[meri.rootSegIndx + int((meri.branchLength / segLength) / 2)].startPoint
    #             midPointX, midPointY, midPointZ = branchMidPoint[0], branchMidPoint[1], branchMidPoint[2]
    #             finalWindVector = (0.,0.,0.)
    #
    #             for ws in windSpheres:
    #
    #                 #find each sphere's proximity to the branch's midPoint
    #                 xDiff, yDiff, zDiff = ws[0][0] - midPointX, ws[0][1] - midPointY, ws[0][2] - midPointZ
    #                 distance = math.sqrt(xDiff*xDiff + yDiff*yDiff + zDiff*zDiff)
    #
    #                 if distance < ws[1]:
    #                     '''if the sphere is within range of the midpoint, determine the wind strength based on the sphere's proximity, then add the
    #                     adjusted vector to the finalWindVector'''
    #                     strengthMult = 1. - (distance / ws[1])
    #                     effectiveWindVector = (ws[2][0]*strengthMult, ws[2][1]*strengthMult, ws[2][2]*strengthMult)
    #                     finalWindVector = (finalWindVector[0] + effectiveWindVector[0], finalWindVector[1] + effectiveWindVector[1], finalWindVector[2] + effectiveWindVector[2])
    #
    #             finalWindVectorMag = math.sqrt(finalWindVector[0]*finalWindVector[0] + finalWindVector[1]*finalWindVector[1] + finalWindVector[2]*finalWindVector[2])
    #
    #             if finalWindVectorMag > 0.:
    #
    #                 for seg in meri.pathSegs[meri.rootSegIndx:-1]:
    #
    #                     dotProduct = finalWindVector[0]*seg.vector[0] + finalWindVector[1]*seg.vector[1] + finalWindVector[2]*seg.vector[2]
    #                     angBetween = math.acos(max(min(dotProduct/(finalWindVectorMag*segLength), 1.),-1.))
    #                     effectiveStrengthMult = (seg.basalLength / boundaryRadius) * math.sin(angBetween)
    #                     effectiveWindVector = (finalWindVector[0]*effectiveStrengthMult, finalWindVector[1]*effectiveStrengthMult, finalWindVector[2]*effectiveStrengthMult)
    #                     sumVector = (seg.vector[0]+effectiveWindVector[0], seg.vector[1]+effectiveWindVector[1], seg.vector[2]+effectiveWindVector[2])
    #                     sumVectorMag = math.sqrt(sumVector[0]*sumVector[0] + sumVector[1]*sumVector[1] + sumVector[2]*sumVector[2])
    #                     normalizer = seg.length / sumVectorMag
    #                     seg.vector = (sumVector[0]*normalizer, sumVector[1]*normalizer, sumVector[2]*normalizer)
    #
    #                 '''Since the last segment may be a different length from the rest, we must scale down the wind vector accordingly to get the correct angle change'''
    #                 lastSeg = meri.pathSegs[-1]
    #                 normalizer = lastSeg.length / segLength
    #                 scaledWindVectorMag = finalWindVectorMag * normalizer
    #                 scaledWindVector = (finalWindVector[0]*normalizer, finalWindVector[1]*normalizer, finalWindVector[2]*normalizer)
    #
    #                 dotProduct = scaledWindVector[0]*lastSeg.vector[0] + scaledWindVector[1]*lastSeg.vector[1] + scaledWindVector[2]*lastSeg.vector[2]
    #                 angBetween = math.acos(max(min(dotProduct/(scaledWindVectorMag*lastSeg.length), 1.),-1.))
    #                 effectiveStrengthMult = (lastSeg.basalLength / boundaryRadius) * math.sin(angBetween)
    #                 effectiveWindVector = (scaledWindVector[0]*effectiveStrengthMult, scaledWindVector[1]*effectiveStrengthMult, scaledWindVector[2]*effectiveStrengthMult)
    #                 sumVector = (lastSeg.vector[0]+effectiveWindVector[0], lastSeg.vector[1]+effectiveWindVector[1], lastSeg.vector[2]+effectiveWindVector[2])
    #                 sumVectorMag = math.sqrt(sumVector[0]*sumVector[0] + sumVector[1]*sumVector[1] + sumVector[2]*sumVector[2])
    #                 normalizer = lastSeg.length / sumVectorMag
    #                 lastSeg.vector = (sumVector[0]*normalizer, sumVector[1]*normalizer, sumVector[2]*normalizer)

    # def wavies(self, meristemList, segLength, orderList):
    #
    #     for meri in meristemList:
    #
    #         if meri.order == 2:
    #
    #             bendAt = random.uniform(.9, 2.)
    #             bending = False
    #
    #             for seg in meri.pathSegs[meri.rootSegIndx:]:
    #
    #                 if bending:
    #                     pass
    #                 elif seg.basalLength > bendAt:
    #
    #                     angles = angleFinder.findVectorAnglesUsingDist(seg.vector, segLength)
    #                     spaceRotator.rotateSpace(angles[0],angles[1])
    #                     rndPol = random.uniform(0., 6.28)
    #                     azi = 2.356
    #                     bending = True
    #                     vectorToAdd = spaceRotator.getVector(rndPol, azi, segLength)

    # def createTextureStrips1(self, stripCount, meshGroups, textureUVWidth, textureUVs, branchPoints, rootSegVector, stripWidth, segLength, lastSegLength):
    #
    #     '''The textureUVDimensions argument is a list containing a tuple for each different texture on the sheet.  Each tuple contains: the uv length in 0-1,
    #     the top left u value, and the top left v value...in that order. They do not contain the uv width of each texture.  Since it is the same for all textures, it is
    #     stored in the textureUVWidth argument'''
    #     angles = angleFinder.findVectorAnglesUsingDist(rootSegVector, segLength)
    #     spaceRotator.rotateSpace(angles[0],angles[1])
    #     polar = random.uniform(1.4,1.75)
    #     cmds.curve(d=1, p=branchPoints)
    #     leafPathCurveName = cmds.ls(sl=1)[0]
    #     pointsInBranch, segmentsInBranch = len(branchPoints), len(branchPoints) - 1 #this will be used alot so lets put it in a variale to make it easier to read and...faster?
    #
    #     for strip in range(stripCount):
    #
    #         leafProfileHalfVector = spaceRotator.getVector(polar,1.57,stripWidth*0.5)
    #         leafProfilePoint1 = (branchPoints[0][0] + leafProfileHalfVector[0], branchPoints[0][1] + leafProfileHalfVector[1], branchPoints[0][2] + leafProfileHalfVector[2])
    #         leafProfilePoint2 = (branchPoints[0][0] - leafProfileHalfVector[0], branchPoints[0][1] - leafProfileHalfVector[1], branchPoints[0][2] - leafProfileHalfVector[2])
    #
    #         cmds.curve(d=1, p=[leafProfilePoint1,leafProfilePoint2])
    #         leafProfileCurveName = cmds.ls(sl=1)[0]
    #         cmds.xform(cp=1)
    #         cmds.extrude(leafProfileCurveName, leafPathCurveName, et=2, ch=0, rn=0, po=1, ucp=1, fpt=1, upn=1, rsp=1)
    #         leafMesh = cmds.ls(sl=1)[0]
    #         meshGroups[0].append(leafMesh)
    #         '''when a strip is created with extrude like this, by default, the uv's for each poly are square shaped, with the square for the first poly occupying the 0-1 space
    #         on the uv grid and each next poly's square 1 square above the one before it.  We will reshape, resize, and relocate these manually to minimize stretching and set them
    #         to the right texture.'''
    #
    #         lastUVIndex = pointsInBranch*2 - 1 #we know the last uv index because there are two uv's per point in linkedPoints
    #         '''A strip segment's dimensions in 3D space are segLength by leafStripWidth*2.  In uv space they
    #         are 1 by 1, so lets adjust their size in the uv space to make the dimensions match'''
    #         '''Because of length smoothing, the last segment on the strip may be longer or shorter than the others, lets adjust its top two uv's to correct its uv length'''
    #         cmds.polyEditUV(leafMesh+".map[{0}]".format(pointsInBranch-1), leafMesh+".map[{0}]".format(lastUVIndex),v=lastSegLength/segLength - 1.)
    #         '''Now lets correct the uv width of all segments.  segLength is to 1 as stripWidth is to x. x is our u scale value'''
    #         cmds.polyEditUV(leafMesh+".map[0:{0}]".format(lastUVIndex),pu=0.,su=stripWidth/segLength,r=0)
    #         '''Now lets cut the uv's so that different parts of the strip can be used for different textures in the texture sheet.  The perpendicular edges on a strip
    #         are always ordered - 3,1,5,8,11,14,17...'''
    #         '''We will need to know the uniform scale value. Scaling the uv's uniformly with this value will bring them to match the width of the textures on the texture sheet'''
    #         uniformScale = .25 / (stripWidth/segLength) #assuming all textures are .25 in width
    #         stripUVLength = ((segmentsInBranch-1) + lastSegLength/segLength) * uniformScale
    #         cmds.polyEditUV(leafMesh+".map[0:{0}]".format(lastUVIndex),pu=0.,pv=0.,su=uniformScale,sv=uniformScale)
    #
    #         '''the values in shellTextures indicate which of the textures on the sheet to use - corresponding to the textureUVs list.'''
    #         shellTextures = [0,1]
    #         '''Find the edge to cut.  This will depend on the length of the texture, and for the tip shell we must factor in lastSegLength'''
    #         segmentsCut = int(round((1. - ((lastSegLength/segLength)*uniformScale)) / uniformScale) + 1)
    #         shellLength = ((segmentsCut-1) + lastSegLength/segLength)*uniformScale
    #
    #         cutEdge = segmentsInBranch - segmentsCut
    #
    #         if cutEdge > 1:
    #             cutEdgeIndex = cutEdge*3 - 1
    #         elif cutEdge < 1:
    #             pass
    #         else:
    #             cutEdgeIndex = 1
    #
    #         '''Now to move the uv's into position.  For the tip texture, we want the shell's top left corner to be in the same place as the top left corner of the texture.
    #         The uv position of the tip texture's top left corner is 0,1.  From this we will subtract the current uv position of the shell's upper left corner.  This will be
    #         the sum of the regular length segments in the branch (each should be 1.) and the last segment, which may be a different length (some percentage of 1.)'''
    #         if cutEdge > 0:
    #             '''If the shell has been cut, selecting the uv shell becomes an issue since we have created two new uv's and they are out of order.  The last uv index
    #             is now at the top right of the lower shell, so we don't want to select it.  The second to last index is at the bottom left of our shell.  We will be selecting
    #             indices cutEdge+1 through pointsInBranch-1 (this is the left side not including the second to last index), and indices cutEdge+pointsInBranch through pointsInBranch*2
    #             (this is the right side plus the second to last index, which is on the bottom left) '''
    #             cmds.polyMapCut(leafMesh+".e[{0}]".format(cutEdgeIndex))
    #             topLeftUVRange = (cutEdge + 1, pointsInBranch - 1)
    #             topRightUVRange = (cutEdge+pointsInBranch,pointsInBranch*2)
    #             cmds.polyEditUV(leafMesh+".map[{0}:{1}]".format(topLeftUVRange[0],topLeftUVRange[1]),leafMesh+".map[{0}:{1}]".format(topRightUVRange[0],topRightUVRange[1]),
    #                             u=0+textureUVs[shellTextures[0]][1],v=1-stripUVLength)
    #             '''The shell should be scaled uniformly to match the width of the texture, however, after this the shell is still not the exact same length as the texture so we will
    #             have to scale it in v to make it fit.  This will stretch/squish the texture a bit but it should be minimal.  To figure out the amount to vScale, we just need to divide
    #             1 by the shellLength (if the shell didn't get cut, this will be the same as the total strip length'''
    #             vScale=1.
    #             if stripUVLength > 1.:
    #                 vScale = 1./shellLength
    #                 cmds.polyEditUV(leafMesh+".map[{0}:{1}]".format(topLeftUVRange[0],topLeftUVRange[1]),leafMesh+".map[{0}:{1}]".format(topRightUVRange[0],topRightUVRange[1]),
    #                                 pu=0,pv=1,sv=vScale,r=0)
    #             '''now move and scale the remaining shell'''
    #             cmds.polyEditUV(leafMesh+".map[0:{0}]".format(cutEdge),leafMesh+".map[{0}:{1}]".format(pointsInBranch,pointsInBranch+cutEdge-1),
    #                             leafMesh+".map[{0}]".format(pointsInBranch*2 + 1),u=.25,v=1.-cutEdge*uniformScale)
    #         else:
    #             cmds.polyEditUV(leafMesh+".map[0:{0}]".format(lastUVIndex),u=0-0,v=1-stripUVLength)
    #
    #         cmds.delete(leafProfileCurveName)
    #         polar += 3.14/stripCount
    #
    #     cmds.delete(leafPathCurveName)

    # def createTextureStrips2(self, stripCount, meshGroups, textureFileDimensions, textureUVWidth, textureUVs, branchPoints, rootSegVector, stripWidth, segLength, lastSegLength, textured):
    #
    #     '''The textureUVDimensions argument is a list containing a tuple for each different texture on the sheet.  Each tuple contains: the uv length in 0-1,
    #     the top left u value, and the top left v value...in that order. They do not contain the uv width of each texture.  Since it is the same for all textures, it is
    #     stored in the textureUVWidth argument'''
    #     angles = angleFinder.findVectorAnglesUsingDist(rootSegVector, segLength)
    #     spaceRotator.rotateSpace(angles[0],angles[1])
    #     polar = random.uniform(1.4,1.75)
    #     cmds.curve(d=1, p=branchPoints)
    #     leafPathCurveName = cmds.ls(sl=1)[0]
    #     pointsInBranch, segmentsInBranch = len(branchPoints), len(branchPoints) - 1 #this will be used alot so lets put it in a variale to make it easier to read and...faster?
    #
    #     '''we need to increaseount for any stretching/squishing of the texture sheet if it is not a square.  Dividing width by height will tell us how much the texture's length(height) has
    #     been stretched.'''
    #     stretching = textureFileDimensions[0] / textureFileDimensions[1]
    #
    #     offSet = 0.
    #
    #     for strip in range(stripCount):
    #
    #         leafProfileHalfVector = spaceRotator.getVector(polar,1.57,stripWidth*0.5)
    #         leafProfilePoint1 = (branchPoints[0][0] + leafProfileHalfVector[0], branchPoints[0][1] + leafProfileHalfVector[1], branchPoints[0][2] + leafProfileHalfVector[2])
    #         leafProfilePoint2 = (branchPoints[0][0] - leafProfileHalfVector[0], branchPoints[0][1] - leafProfileHalfVector[1], branchPoints[0][2] - leafProfileHalfVector[2])
    #
    #         cmds.curve(d=1, p=[leafProfilePoint1,leafProfilePoint2])
    #         leafProfileCurveName = cmds.ls(sl=1)[0]
    #         cmds.xform(cp=1)
    #         cmds.extrude(leafProfileCurveName, leafPathCurveName, et=2, ch=0, rn=0, po=1, ucp=1, fpt=1, upn=1, rsp=1)
    #         if textured == 1:
    #             leafMesh = cmds.ls(sl=1)[0]
    #             meshGroups[0].append(leafMesh)
    #             '''when a strip is created with extrude like this, by default, the uv's for each poly are square shaped, with the square for the first poly occupying the 0-1 space
    #             on the uv grid and each next poly's square 1 square above the one before it.  We will reshape, resize, and relocate these manually to minimize stretching and set them
    #             to the right texture.'''
    #
    #             lastUVIndex = pointsInBranch*2 - 1 #we know the last uv index because there are two uv's per point in linkedPoints
    #             '''A strip segment's dimensions in 3D space are segLength by leafStripWidth*2.  In uv space they
    #             are 1 by 1, so lets adjust their size in the uv space to make the dimensions match'''
    #             '''Because of length smoothing, the last segment on the strip may be longer or shorter than the others, lets adjust its top two uv's to correct its uv length'''
    #             cmds.polyEditUV(leafMesh+".map[{0}]".format(pointsInBranch-1), leafMesh+".map[{0}]".format(lastUVIndex),v=lastSegLength/segLength - 1.)
    #             '''Now lets correct the uv width of all segments.  segLength is to 1 as stripWidth is to x. x is our u scale value'''
    #             cmds.polyEditUV(leafMesh+".map[0:{0}]".format(lastUVIndex),pu=0.,su=stripWidth/segLength,r=0)
    #             '''We will need to know the uniform scale value. Scaling the uv's uniformly with this value will bring them to match the width of the textures on the texture sheet'''
    #             uniformScale = textureUVWidth / (stripWidth/segLength)
    #             stripUVLength = ((segmentsInBranch-1) + lastSegLength/segLength) * uniformScale * stretching
    #             cmds.polyEditUV(leafMesh+".map[0:{0}]".format(lastUVIndex),pu=0.,pv=0.,su=uniformScale,sv=uniformScale*stretching)
    #
    #             '''Now time to move the uv's into place.  For this we need the uv location of the texture we're using'''
    #             cmds.polyEditUV(leafMesh+".map[0:{0}]".format(lastUVIndex),u=.125,v=(1.- stripUVLength)+offSet)
    #
    #         cmds.delete(leafProfileCurveName)
    #         polar += 3.14/stripCount
    #         offSet += .035
    #
    #     cmds.delete(leafPathCurveName)

    def overwriteSettings(self, *args):

        print "args: ", args
        os.remove("/C:/Users/13308/Documents/maya/scripts/TreeMaker_Interface_Presets/"+args[0]+".txt")
        menuItems = cmds.popupMenu(self.loadPresetButton, q=True, ia=True)
        cmds.popupMenu(self.loadPresetButton, e=True, dai=True)
        menuItems.remove(args[0] + "_txt")

        for item in menuItems:
            #for some dumbass reason the ".txt" gets changed to "_txt" when queried from the popupMenu so we have to change it back I think
            itemAsList = list(item)
            del itemAsList[-1]
            del itemAsList[-1]
            del itemAsList[-1]
            del itemAsList[-1]
            presetName = "".join(itemAsList) + ".txt"
            cmds.menuItem(presetName, l=presetName, p=self.loadPresetButton, command = partial(self.loadSettings, presetName))

        self.saveSettings()
        cmds.deleteUI("OverwriteSettingsWindow")

    def dontOverwriteSettings(self, *_):

        cmds.deleteUI("OverwriteSettingsWindow")

    def setReadGlobalGrad(self, *_):

        self.readGlobalGrad = True
        print cmds.gradientControlNoAttr(self.globalGrowthGradient, q=True, asString=True)

    def setReadVTG(self, *args):

        self.vtgReadToggles[args[0]] = True

        print args

    def setReadSG(self, *args):

        self.sgReadToggles[args[0]] = True
        print args

    def setReadSEG(self, *args):

        self.segReadToggles[args[0]] = True
        print args

    def setReadPullG(self, *args):

        self.pullGradReadToggles[args[0]] = True
        print args

    def setReadWeightG(self, *args):

        self.weightGradReadToggles[args[0]] = True
        print args

    def setReadMatG(self, *args):

        self.matGradReadToggles[args[0]] = True
        print args

    def toggleStrips(self, *args):

        cmds.floatField(self.leafStripWidthFLD_list[args[0]], e=True, en=args[1])
        cmds.checkBox(self.textureOnOffFLD_list[args[0]], e=True, en=args[1])

    def orderUpdate(self, *_):

        newOrderCount = cmds.intField(self.ordersFLD, q=True, v=True)

        for i in range(4):

            if i < newOrderCount:
                cmds.frameLayout(self.orderFrameLayouts_list[i], e=True, vis=1)
            else:
                cmds.frameLayout(self.orderFrameLayouts_list[i], e=True, vis=0)

    def initiate(self, *_):

        self.startTime = time.time()
        self.totalTime = cmds.intSliderGrp(self.totalTimeFLD, q=True, v=True)
        self.pointRadius = 1.
        self.blockDensity = 1.
        self.blockPointResolution = 5
        self.orders = cmds.intField(self.ordersFLD, q=True, v=True) + 1 #plus one because there are always leaf shoots, and these are listed as the last order
        self.orderList = ["dummy"]
        for order in range(5):
            #the gradients will be added to the orders after initiating
            vigorTimeGradient = None
            suppressionGradient = None
            suppEffectGradient = None
            pullACGradient = None
            weightACGradient = None
            maturityGradient = None

            if order == 4: #the last order is always leaf shoots

                suppReach = None
                freq = None
                nodeFluct = None
                shootsPerNode = None
                SPNFluct = None
                nodeRotation = None
                nodeRotFluct = None
                lsOnOff = None
                lsFreq = None
                lsNodeFluct = None
                lsSPNMin = None
                lsSPNMax = None
                lsNodeRotMin = None
                lsNodeRotMax = None
                lsShedLengthMin = None
                lsShedLengthMax = None

                self.orderList.append(Order(cmds.floatField(self.earlyDelaysFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lateDelaysFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.delayFalloffRngFLD_list[order], q=True, v=True),
                                            vigorTimeGradient, cmds.floatField(self.vGradientReachFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.rndVigorRngsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.selfSustainedFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lightInfluenceFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.shadeToleranceFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.healthLossRateFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.parentGrowthTillShedFLD_list[order], q=True, v=True),
                                            suppressionGradient, suppReach, suppEffectGradient, freq, nodeFluct, None, shootsPerNode, SPNFluct,
                                            nodeRotation, nodeRotFluct, lsOnOff, lsFreq, lsNodeFluct, lsSPNMin, lsSPNMax, lsNodeRotMin,
                                            lsNodeRotMax, None, lsShedLengthMin, lsShedLengthMax, None, None, None,
                                            cmds.floatField(self.cloneFreqMinFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.cloneFreqMaxFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.cloneOrderInflMinFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.cloneOrderInflMaxFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.abortFreqMinFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.abortFreqMaxFLD_list[order], q=True, v=True),
                                            cmds.intField(self.numTransfMerisFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.transfRangeFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.DGTropismFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.DGTBaseShiftFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.xAreaAddedFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.acGradientReachFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.overallACGradientRangeFLD_list[order], q=True, v=True),
                                            pullACGradient, weightACGradient,
                                            cmds.floatField(self.pullForceFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.pfSuppLinkFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.PSStartFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.PSRangeFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.pLossSuppLinkFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.pullDecayFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.weightMultFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.tropismRatioFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.backRotationFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.straightenerStrFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.backRotationDelayFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.backRotationOffsetFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.weightResFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.modMultFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.minModFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.dryRateFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarReachFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarStrengthFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarReachGainFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarStrengthGainFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarLimitReachFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarLimitAngleFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.sproutAziFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.sproutToBaseFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.baseAziFLD_list[order], q=True, v=True),
                                            (cmds.floatField(self.collarJitterPolFLD_list[order], q=True, v=True),cmds.floatField(self.collarJitterAziFLD_list[order], q=True, v=True)),
                                            cmds.floatField(self.pdDroopFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.pddPeakFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.pddEndFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.windStrengthFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.rippleStrengthFLD_list[order], q=True, v=True),
                                            cmds.checkBox(self.blockPointsOnOffFLD_list[order], q=True, v=True),
                                            cmds.checkBox(self.ignoreBPointsFLD_list[order], q=True, v=True),
                                            cmds.intField(self.bpResFLD_list[order],q=True, v=True),
                                            cmds.floatField(self.bpSizeFLD_list[order],q=True, v=True),
                                            cmds.floatField(self.bpDensityFLD_list[order],q=True, v=True),
                                            cmds.checkBox(self.createBranchMeshChBox_list[order], q=True, v=True),
                                            cmds.floatField(self.skinRadiusFLD_list[order],q=True, v=True),
                                            cmds.floatField(self.segLengthFLD_list[order],q=True, v=True),
                                            cmds.intField(self.sidesFLD_list[order],q=True, v=True),
                                            cmds.checkBox(self.stripsOnOffFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.leafStripWidthFLD_list[order], q=True, v=True),
                                            cmds.checkBox(self.textureOnOffFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.maturityRngFLD_list[order], q=True, v=True),
                                            maturityGradient,
                                            cmds.floatField(self.bacMaturityLinkFLD_list[order],q=True, v=True),
                                            cmds.floatField(self.suppReachMaturityLinkFLD_list[order],q=True, v=True)))
            else:
                #values for node frequency that are greater than segLength*4. will be rounded to the nearest value divisible by segLength
                orderSegLength = cmds.floatField(self.segLengthFLD_list[order],q=True, v=True)

                freqMin = cmds.floatField(self.nodeFreqMinsFLD_list[order], q=True, v=True)

                if freqMin > orderSegLength*4.:
                    freqMin = round(freqMin/orderSegLength) * orderSegLength

                freqMax = cmds.floatField(self.nodeFreqMaxsFLD_list[order], q=True, v=True)

                if freqMax > orderSegLength*4.:
                    freqMax = round(freqMax/orderSegLength) * orderSegLength

                self.orderList.append(Order(cmds.floatField(self.earlyDelaysFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lateDelaysFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.delayFalloffRngFLD_list[order], q=True, v=True),
                                            vigorTimeGradient, cmds.floatField(self.vGradientReachFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.rndVigorRngsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.selfSustainedFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lightInfluenceFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.shadeToleranceFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.healthLossRateFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.parentGrowthTillShedFLD_list[order], q=True, v=True),
                                            suppressionGradient, cmds.floatField(self.suppReachFLD_list[order], q=True, v=True), suppEffectGradient,
                                            freqMin, freqMax, cmds.floatField(self.nodeFreqVigorLinksFLD_list[order], q=True, v=True),
                                            cmds.intField(self.SPNMinsFLD_list[order], q=True, v=True),
                                            cmds.intField(self.SPNMaxsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.nodeRotMinsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.nodeRotMaxsFLD_list[order], q=True, v=True),
                                            cmds.checkBox(self.leafShootsOnOffFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lsNodeFreqMinsFLD_list[order],q=True, v=True),
                                            cmds.floatField(self.lsNodeFreqMaxsFLD_list[order], q=True, v=True),
                                            cmds.intField(self.lsSPNMinsFLD_list[order], q=True, v=True),
                                            cmds.intField(self.lsSPNMaxsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lsNodeRotMinsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lsNodeRotMaxsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lsShedAgeFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lsShedLengthMinsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lsShedLengthMaxsFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lsShedFallOffFLD_list[order], q=True, v=True),
                                            cmds.intField(self.lsISTimeThreshFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.lsISAgeThreshFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.cloneFreqMinFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.cloneFreqMaxFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.cloneOrderInflMinFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.cloneOrderInflMaxFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.abortFreqMinFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.abortFreqMaxFLD_list[order], q=True, v=True),
                                            cmds.intField(self.numTransfMerisFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.transfRangeFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.DGTropismFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.DGTBaseShiftFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.xAreaAddedFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.acGradientReachFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.overallACGradientRangeFLD_list[order], q=True, v=True),
                                            pullACGradient, weightACGradient,
                                            cmds.floatField(self.pullForceFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.pfSuppLinkFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.PSStartFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.PSRangeFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.pLossSuppLinkFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.pullDecayFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.weightMultFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.tropismRatioFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.backRotationFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.straightenerStrFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.backRotationDelayFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.backRotationOffsetFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.weightResFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.modMultFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.minModFLD_list[order], q=True, v=True),
                                            #cmds.floatField(self.dryRateFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarReachFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarStrengthFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarReachGainFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarStrengthGainFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarLimitReachFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.collarLimitAngleFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.sproutAziFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.sproutToBaseFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.baseAziFLD_list[order], q=True, v=True),
                                            (cmds.floatField(self.collarJitterPolFLD_list[order], q=True, v=True),cmds.floatField(self.collarJitterAziFLD_list[order], q=True, v=True)),
                                            cmds.floatField(self.pdDroopFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.pddPeakFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.pddEndFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.windStrengthFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.rippleStrengthFLD_list[order], q=True, v=True),
                                            cmds.checkBox(self.blockPointsOnOffFLD_list[order], q=True, v=True),
                                            cmds.checkBox(self.ignoreBPointsFLD_list[order], q=True, v=True),
                                            cmds.intField(self.bpResFLD_list[order],q=True, v=True),
                                            cmds.floatField(self.bpSizeFLD_list[order],q=True, v=True),
                                            cmds.floatField(self.bpDensityFLD_list[order],q=True, v=True),
                                            cmds.checkBox(self.createBranchMeshChBox_list[order], q=True, v=True),
                                            cmds.floatField(self.skinRadiusFLD_list[order],q=True, v=True),
                                            orderSegLength,
                                            cmds.intField(self.sidesFLD_list[order],q=True, v=True),
                                            cmds.checkBox(self.stripsOnOffFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.leafStripWidthFLD_list[order], q=True, v=True),
                                            cmds.checkBox(self.textureOnOffFLD_list[order], q=True, v=True),
                                            cmds.floatField(self.maturityRngFLD_list[order], q=True, v=True),
                                            maturityGradient,
                                            cmds.floatField(self.bacMaturityLinkFLD_list[order],q=True, v=True),
                                            cmds.floatField(self.suppReachMaturityLinkFLD_list[order],q=True, v=True)))

        self.baseVigor = cmds.floatField(self.baseVigorFLD, q=True, v=True)
        self.globalGradientRange = cmds.floatField(self.globalGradientRangeFLD, q=True, v=True)
        self.globGradVigorEffect = cmds.floatField(self.globGradVigorEffectFLD, q=True, v=True)
        self.globGradReachEffect = cmds.floatField(self.globGradReachEffectFLD, q=True, v=True)
        self.maxSuppReach = ["dummy", self.orderList[1].suppReach, self.orderList[2].suppReach, self.orderList[3].suppReach, self.orderList[4].suppReach]
        self.currentVigTimeReachList = ["dummy", self.orderList[1].vGradientReach, self.orderList[2].vGradientReach, self.orderList[3].vGradientReach, self.orderList[4].vGradientReach, self.orderList[5].vGradientReach]

        if self.readGlobalGrad:

            self.globalGrowthGradientValues = []
            increment = 0.0
            while increment < 1.01:
                self.globalGrowthGradientValues.append(cmds.gradientControlNoAttr(self.globalGrowthGradient, q=True, vap=increment))
                increment += 0.01

            self.readGlobalGrad = False

        for order in range(5):

            if self.vtgReadToggles[order]:

                self.vtgValues[order] = []

                increment = 0.0
                while increment < 1.002:
                    self.vtgValues[order].append(cmds.gradientControlNoAttr(self.vigorTimeGradientFLD_list[order], q=True, vap=increment))
                    increment += 0.002

                self.vtgReadToggles[order] = False

            self.orderList[order+1].vigorTimeGradient = self.vtgValues[order]

            if order < 4:

                if self.sgReadToggles[order]:

                    self.sgValues[order] = []

                    increment = 0.0
                    while increment < 1.01:
                        self.sgValues[order].append(cmds.gradientControlNoAttr(self.suppressionGradientFLD_list[order], q=True, vap=increment))
                        increment += 0.01

                    self.sgReadToggles[order] = False

                self.orderList[order+1].suppressionGradient = self.sgValues[order]

                if self.segReadToggles[order]:

                    self.segValues[order] = []

                    increment = 0.0
                    while increment < 1.002:
                        self.segValues[order].append(cmds.gradientControlNoAttr(self.suppEffectGradientFLD_list[order], q=True, vap=increment))
                        increment += 0.002

                    self.segReadToggles[order] = False

                self.orderList[order+1].suppEffectGradient = self.segValues[order]

            if self.pullGradReadToggles[order]:

                self.pullGValues[order] = []

                increment = 0.
                while increment < 1.002:
                    self.pullGValues[order].append(cmds.gradientControlNoAttr(self.pullACGradientFLD_list[order], q=True, vap=increment))
                    increment += 0.002

                self.pullGradReadToggles[order] = False

            self.orderList[order+1].pullACGradient = self.pullGValues[order]

            if self.weightGradReadToggles[order]:

                self.weightGValues[order] = []

                increment = 0.
                while increment < 1.002:
                    self.weightGValues[order].append(cmds.gradientControlNoAttr(self.weightACGradientFLD_list[order], q=True, vap=increment))
                    increment += 0.002

                self.weightGradReadToggles[order] = False

            self.orderList[order+1].weightACGradient = self.weightGValues[order]

            if self.matGradReadToggles[order]:

                self.matGValues[order] = []

                increment = 0.
                while increment < 1.002:
                    self.matGValues[order].append(cmds.gradientControlNoAttr(self.maturityGradientFLD_list[order], q=True, vap=increment))
                    increment += 0.002

                self.matGradReadToggles[order] = False

            self.orderList[order+1].maturityGradient = self.matGValues[order]

        seedBudPolar = 0.#random.uniform(0.,PIm2)
        self.blockPoints = []
        self.pointRemoved = True
        self.timeElapsed = 0

        globalGradientValueForVigor = ((1.- self.globGradVigorEffect) + (self.globGradVigorEffect * self.globalGrowthGradientValues[0]))

        seedVigor = self.orderList[1].vigorTimeGradient[0]*globalGradientValueForVigor
        nodeFreqFluctRange = self.orderList[1].nodeFreq * self.orderList[1].nodeFreqFluct
        lsNodeFreqFluctRange = self.orderList[1].lsNodeFreqMin * self.orderList[1].lsNodeFreqMax

        if self.orderList[1].nodeFreq > self.orderList[1].segmentLength:
            lengthAtNextNode = round((.6 + (self.orderList[1].nodeFreq + random.uniform(-nodeFreqFluctRange, nodeFreqFluctRange)))/.3) * .3
        else:
            lengthAtNextNode = .6 + (self.orderList[1].nodeFreq + random.uniform(-nodeFreqFluctRange, nodeFreqFluctRange))

        if self.orderList[1].lsNodeFreqMin > self.orderList[1].segmentLength:
            lengthAtNextLSNode = round((.6 + (self.orderList[1].lsNodeFreqMin + random.uniform(-lsNodeFreqFluctRange, lsNodeFreqFluctRange)))/.3) * .3
        else:
            lengthAtNextLSNode = .6 + (self.orderList[1].lsNodeFreqMin + random.uniform(-lsnodeFreqFluctRange, lsnodeFreqFluctRange))

        # self.seed = A_Meristem((0.,0.,0.), #location
        #                   (0.,0.,0.), #vector sum
        #                   0., #polar angle
        #                   0., #azimuthal angle
        #                   0., #branch relative azi
        #                   [], #path segments
        #                   [], #orderParents
        #                   None, #axialParent
        #                   0, #root segment index
        #                   0., #length from root
        #                   0., #branch length
        #                   0., #segment progress
        #                   0, #newSegs
        #                   True, #lightCheck
        #                   [], #orderChildren
        #                   [], #axialChildren
        #                   [], #node siblings
        #                   [], #descendants
        #                   [], #ancestors
        #                   1, #order
        #                   seedVigor, #current vigor
        #                   1., #lightMult
        #                   1., #individual vigor multiplier
        #                   1., #random pull multiplier
        #                   random.uniform(1., 4.), #random pull change timer
        #                   self.orderList[1].xAreaAdded, #xArea added
        #                   0., #base offset
        #                   [], #linked points
        #                   self.orderList[1].segmentLength, #last segment length
        #                   0., #parent proximity
        #                   0.,
        #                   0., #age
        #                   seedBudPolar, #bud polar angle
        #                   seedBudPolar, #leaf shoot bud polar angle
        #                   0., #root relative polar
        #                   self.orderList[1].collarReach, #current collar reach
        #                   self.orderList[1].collarStrength, #current collar strength
        #                   self.orderList[1].collarReachGain, #collar reach gain
        #                   self.orderList[1].collarStrengthGain, #collar strength gain
        #                   [], #collar limiters
        #                   [], #collar strengthenees
        #                   [], #limiter segments
        #                   (0.,0.,0.,0.), #pull force vector
        #                   1., #suppression multiplier
        #                   1., #suppression limit
        #                   1., #suppressed vigor
        #                   1., #suppression applied
        #                   0., #suppression level
        #                   self.currentVigTimeReachList[1], #timeGradReach
        #                   self.orderList[1].nodeFreq, #node freq
        #                   self.orderList[1].lsNodeFreqMin, #leaf shoot node freq
        #                   lengthAtNextNode,
        #                   lengthAtNextLSNode,
        #                   [], # meristems indebted to
        #                   False,
        #                   0.,
        #                   CloneInfo(False, None, None), #clone info class
        #                   0., #delay
        #                   max(self.orderList[1].segmentLength, self.orderList[1].lsShedLengthMin + random.triangular(-self.orderList[1].lsShedLengthMax, self.orderList[1].lsShedLengthMax, 0.)),
        #                   1000000.) #shed length
        #
        # self.seed.axialParent = self.seed
        # self.newMeristemCatcher = []
        # self.allMeristems = [self.seed]
        # self.activeMeristems = [self.seed]
        # self.elongatedMeristems = [self.seed]


        self.introTime = time.time() - self.startTime

    # def buildTreeMesh(self, elongatedMeristems, orderList, segLength):
    #
    #     buildProgressWindow = cmds.window(title="Build Progress")
    #     cmds.columnLayout()
    #     buildProgressControl = cmds.progressBar(maxValue=len(elongatedMeristems), width=300)
    #     cmds.showWindow(buildProgressWindow)
    #
    #     #for meri in elongatedMeristems:
    #     #
    #     #    points = []
    #     #    for seg in meri.pathSegs[meri.rootSegIndx:]:
    #     #
    #     #        points.append(seg.startPoint)
    #     #
    #     #    points.append(meri.loc)
    #     #    cmds.curve(d=1,p=points)
    #     #    #cmds.curve(d=1,p=[meri.pathSegs[-1].startPoint, (meri.pathSegs[-1].startPoint[0]+meri.pathSegs[-1].vector[0], meri.pathSegs[-1].startPoint[1]+meri.pathSegs[-1].vector[1], meri.pathSegs[-1].startPoint[2]+meri.pathSegs[-1].vector[2])])
    #     #
    #     #quit()
    #
    #     #cmds.circle(nr=(0,1,0),r=1.)
    #     sides = 3
    #     azi = 1.5708
    #     pol = 0.
    #     radius = 1.
    #     profileCurvePts = []
    #
    #     for i in range(sides):
    #
    #         profileCurvePts.append((radius*math.sin(azi)*math.cos(pol),
    #                                 radius*math.cos(azi),
    #                                 radius*math.sin(azi)*math.sin(pol)))
    #
    #         pol += 6.28319 / sides
    #
    #     cmds.curve(d=1,p=profileCurvePts)
    #     profileCurveName = cmds.ls(sl=1)[0]
    #     cmds.closeCurve(ch=0,ps=0,rpo=1,bb=0.5,bki=0,p=.1)
    #     cmds.xform(profileCurveName, cp=1) #for some reason we need to center the pivot to avoid a warning message for every extrude with this profile
    #     #the following line sets the pivot point for the profile curve to have the exact same y coordinate value as the bottom of its bounding box
    #     #cmds.move(0.,cmds.exactWorldBoundingBox(profileCurveName)[4],0., profileCurveName+'.scalePivot', profileCurveName+'.rotatePivot', r=0)
    #     leafMeshes = []
    #     youngBranchMeshes = []
    #
    #
    #     for meri in elongatedMeristems:
    #
    #         meshes = []
    #
    #         for count, bSeg in enumerate(meri.bSegs):
    #
    #             if len(bSeg.points) > 1 and orderList[meri.order].branchMeshTgl == 1:
    #
    #                 #cmds.circle(profileCurveName, e=1, r=bSeg.radius)
    #                 #cmds.scale(bSeg.radius, bSeg.radius, bSeg.radius, profileCurveName, r=0)
    #                 cmds.delete(profileCurveName)
    #                 '''we are creating a new profile curve for every bSeg because, for some reason, simply scaling the original curve to the match the new radius
    #                 causes a warning message to be generated on the next extrude.  For now the solution we have is to just delete the original and make a new one'''
    #                 sides = 3
    #                 azi = 1.5708
    #                 pol = 0.
    #                 profileCurvePts = []
    #
    #                 for i in range(sides):
    #
    #                     profileCurvePts.append((bSeg.radius*math.sin(azi)*math.cos(pol),
    #                                             bSeg.radius*math.cos(azi),
    #                                             bSeg.radius*math.sin(azi)*math.sin(pol)))
    #
    #                     pol += 6.28319 / sides
    #
    #                 cmds.curve(d=1,p=profileCurvePts)
    #                 profileCurveName = cmds.ls(sl=1)[0]
    #                 cmds.closeCurve(ch=0,ps=0,rpo=1,bb=0.5,bki=0,p=.1)
    #                 cmds.xform(profileCurveName, cp=1) #for some reason we need to center the pivot to avoid a warning message for every extrude with this profile
    #                 #the following line sets the pivot point for the profile curve to have the exact same y coordinate value as the bottom of its bounding box
    #                 #cmds.move(0.,cmds.exactWorldBoundingBox(profileCurveName)[4],0., profileCurveName+'.scalePivot', profileCurveName+'.rotatePivot', r=0)
    #
    #                 cmds.curve(d=1,p=bSeg.points)
    #                 pathCurveName = cmds.ls(sl=1)[0]
    #                 cmds.extrude(profileCurveName, pathCurveName, et=2, ch=0, rn=0, po=1, ucp=1, fpt=1, upn=1, rsp=1)
    #                 meshName = cmds.ls(sl=1)[0]
    #                 cmds.delete(ch=1)
    #                 cmds.delete(pathCurveName)
    #                 meshes.append(meshName)
    #
    #                 vertStep = len(bSeg.points)
    #
    #                 if count - 1 > -1:
    #
    #                     bottomLoopEdges = cmds.polySelect(eb=3, ns=1)
    #
    #                     percentOfSegLength = maxRadius / bSeg.bottomSegment.length
    #                     scaledVector = (bSeg.bottomSegment.vector[0]*percentOfSegLength, bSeg.bottomSegment.vector[1]*percentOfSegLength, bSeg.bottomSegment.vector[2]*percentOfSegLength)
    #                     self.moveEdges(sides, scaledVector, bottomLoopEdges, meshName)
    #                     self.extrudeEdges(sides, bottomLoopEdges, meshName)
    #
    #                     vertCount = vertStep * sides
    #                     newLoopVerts = self.fillNewVertList(sides, vertCount)
    #
    #                     lastVector = meri.bSegs[count-1].topSegment.vector
    #                     nextVector = bSeg.bottomSegment.vector
    #                     betweenVector = ((lastVector[0]+nextVector[0])*0.5, (lastVector[1]+nextVector[1])*0.5, (lastVector[2]+nextVector[2])*0.5)
    #                     betweenVectorMag = math.sqrt(betweenVector[0]*betweenVector[0] + betweenVector[1]*betweenVector[1] + betweenVector[2]*betweenVector[2])
    #                     normalizer = 1./betweenVectorMag
    #                     betweenVector = (betweenVector[0]*normalizer, betweenVector[1]*normalizer, betweenVector[2]*normalizer)
    #
    #                     newVertCoords = []
    #
    #                     for vertIndex in newLoopVerts[:2]:
    #
    #                         newVertCoords.append(cmds.pointPosition(meshName+'.vtx[{0}]'.format(vertIndex)))
    #
    #                     connectorIndices = []
    #                     lastConnectorIndex = -1
    #
    #                     for newVertCoord in newVertCoords:
    #
    #                         minDiff = 2.
    #
    #                         for count2, coord in enumerate(topVertCoords):
    #
    #                             connectVector = (newVertCoord[0]-coord[0], newVertCoord[1]-coord[1], newVertCoord[2]-coord[2])
    #                             connectVectorMag = math.sqrt(connectVector[0]*connectVector[0] + connectVector[1]*connectVector[1] + connectVector[2]*connectVector[2])
    #                             normalizer = 1./connectVectorMag
    #                             connectVector = (connectVector[0]*normalizer, connectVector[1]*normalizer, connectVector[2]*normalizer)
    #                             diffVector = (betweenVector[0] - connectVector[0], betweenVector[1] - connectVector[1], betweenVector[2] - connectVector[2])
    #                             diffVectorMag = math.sqrt(diffVector[0]*diffVector[0] + diffVector[1]*diffVector[1] + diffVector[2]*diffVector[2])
    #                             #print "connectVector, diffVector, diffMag:", connectVector, diffVector, diffVectorMag
    #                             if diffVectorMag < minDiff:
    #
    #                                 if count2 != lastConnectorIndex: #this prevents the two coordinates from choosing the same connector vert
    #                                     minDiff = diffVectorMag
    #                                     connectorIndex = count2
    #
    #                         lastConnectorIndex = connectorIndex
    #                         connectorIndices.append(connectorIndex)
    #
    #                     #print "connectorIndices:", connectorIndices
    #                     #print "newLoopVertsBefore:", newLoopVerts
    #                     if connectorIndices[0]+1 == connectorIndices[1] or connectorIndices[0]-(sides-1) == connectorIndices[1]:
    #                         pass
    #                     else:
    #                         newLoopVerts.reverse()
    #
    #                         newLoopVerts = deque(newLoopVerts)
    #                         newLoopVerts.rotate(connectorIndices[0]+1)
    #
    #                         #print "connector:", connectorIndices[0]
    #                         #print "newLoopVertsAfter:", newLoopVerts
    #                         #print "topVerts", topVerts
    #                     for count2, coord in enumerate(topVertCoords):
    #
    #                         cmds.move(coord[0], coord[1], coord[2], meshName+'.vtx[{0}]'.format(newLoopVerts[count2]))
    #
    #                 if count + 1 < len(meri.bSegs):
    #
    #                     maxRadius = 0.
    #
    #                     for meri2 in bSeg.topSegment.merisOnSeg:
    #
    #                         if meri2.bSegs[0].radius > maxRadius:
    #                             maxRadius = meri2.bSegs[0].radius
    #
    #                     topVerts = [len(bSeg.points)-1]
    #                     for i in range(sides - 1):
    #                         topVerts.append(topVerts[-1]+vertStep)
    #
    #                     percentOfSegLength = maxRadius / bSeg.topSegment.length * -1 #multiply by -1 because this loop will be slid downward
    #                     scaledVector = (bSeg.topSegment.vector[0]*percentOfSegLength, bSeg.topSegment.vector[1]*percentOfSegLength, bSeg.topSegment.vector[2]*percentOfSegLength)
    #                     self.moveVerts(sides, scaledVector, topVerts, meshName)
    #
    #                     topVertCoords = []
    #                     for vertIndex in topVerts:
    #                         topVertCoords.append(cmds.pointPosition(meshName+'.vtx[{0}]'.format(vertIndex)))
    #
    #                 else:
    #
    #                     '''Time to put a cap at the end of each branch.  First need to find the numbers of the edges on the end border of the branch.  When maya builds a tube
    #                     with the extrude we are using, the beginning border always contains edge number 3.  The second edge loop always contains edge number 1.  And the third
    #                     edge loop always contains number 5.  From there on we can get the number of an edge in the same ring as the 3,1, and 5 by multiplying the number of points
    #                     in the bSeg by 3 and then subtracting 4'''
    #                     if len(bSeg.points) == 2:
    #                         endBorderEdges = cmds.polySelect(eb=1, ns=1)
    #                     elif len(bSeg.points) == 3:
    #                         endBorderEdges = cmds.polySelect(eb=5, ns=1)
    #                     else:
    #                         endBorderEdges = cmds.polySelect(eb=len(bSeg.points)*3 - 4, ns=1)
    #
    #                     capFaceIndex = cmds.polyEvaluate(meshName, f=1)
    #                     normalizer = (bSeg.radius*2) / meri.lastSegLength
    #                     translateVector = [meri.pathSegs[-1].vector[0]*normalizer, meri.pathSegs[-1].vector[1]*normalizer, meri.pathSegs[-1].vector[2]*normalizer]
    #
    #                     if sides < 5:
    #                         if sides == 3:
    #                             cmds.polyCloseBorder(meshName+".e[{0}]".format(endBorderEdges[0]), meshName+".e[{0}]".format(endBorderEdges[1]), meshName+".e[{0}]".format(endBorderEdges[2]))
    #                         else: #sides = 4
    #                             cmds.polyCloseBorder(meshName+".e[{0}]".format(endBorderEdges[0]), meshName+".e[{0}]".format(endBorderEdges[1]), meshName+".e[{0}]".format(endBorderEdges[2]),
    #                                                  meshName+".e[{0}]".format(endBorderEdges[3]))
    #
    #                         cmds.polyExtrudeFacet(meshName+".f[{0}]".format(capFaceIndex),ch=1,kft=1,d=1,t=translateVector,s=[.4,.4,.4])
    #
    #                     else:
    #                         if sides == 5:
    #                             cmds.polyCloseBorder(meshName+".e[{0}]".format(endBorderEdges[0]), meshName+".e[{0}]".format(endBorderEdges[1]), meshName+".e[{0}]".format(endBorderEdges[2]),
    #                                                  meshName+".e[{0}]".format(endBorderEdges[3]), meshName+".e[{0}]".format(endBorderEdges[4]))
    #                         elif sides == 6:
    #                             cmds.polyCloseBorder(meshName+".e[{0}]".format(endBorderEdges[0]), meshName+".e[{0}]".format(endBorderEdges[1]), meshName+".e[{0}]".format(endBorderEdges[2]),
    #                                                  meshName+".e[{0}]".format(endBorderEdges[3]), meshName+".e[{0}]".format(endBorderEdges[4]), meshName+".e[{0}]".format(endBorderEdges[5]))
    #                         elif sides == 7:
    #                             cmds.polyCloseBorder(meshName+".e[{0}]".format(endBorderEdges[0]), meshName+".e[{0}]".format(endBorderEdges[1]), meshName+".e[{0}]".format(endBorderEdges[2]),
    #                                                  meshName+".e[{0}]".format(endBorderEdges[3]), meshName+".e[{0}]".format(endBorderEdges[4]), meshName+".e[{0}]".format(endBorderEdges[5]),
    #                                                  meshName+".e[{0}]".format(endBorderEdges[6]))
    #                         else:
    #                             cmds.polyCloseBorder(meshName+".e[{0}]".format(endBorderEdges[0]), meshName+".e[{0}]".format(endBorderEdges[1]), meshName+".e[{0}]".format(endBorderEdges[2]),
    #                                                  meshName+".e[{0}]".format(endBorderEdges[3]), meshName+".e[{0}]".format(endBorderEdges[4]), meshName+".e[{0}]".format(endBorderEdges[5]),
    #                                                  meshName+".e[{0}]".format(endBorderEdges[6]), meshName+".e[{0}]".format(endBorderEdges[7]))
    #
    #                         cmds.polyExtrudeFacet(meshName+".f[{0}]".format(capFaceIndex),ch=1,kft=1,d=1,t=translateVector,s=[.4,.4,.4])
    #                         cmds.polyPoke(meshName+".f[{0}]".format(capFaceIndex),ch=1,ws=1)
    #
    #         #time to create the leaf mesh, if there is one
    #         if orderList[meri.order].stripsTgl == 1:
    #
    #             if meri.age < .5:
    #                 stripWidth = max(0.4,(meri.age/.5)) * orderList[meri.order].stripWidth
    #             else:
    #                 stripWidth = orderList[meri.order].stripWidth
    #
    #             self.createTextureStrips2(1, [leafMeshes], (1024, 256), 0.125, [(1.,0.125,1.)], meri.linkedPoints, meri.pathSegs[meri.rootSegIndx].vector, stripWidth, segLength,
    #                                  meri.lastSegLength, orderList[meri.order].stripTextureTgl)
    #             #createTextureStrips1(1, [leafMeshes], 0.25, [(1.,0.,1.),(1.,.25,1.),(1.,.5,1.)], meri.linkedPoints, meri.pathSegs[meri.rootSegIndx].vector, stripWidth,
    #             #                   segLength, meri.lastSegLength)
    #
    #         try:
    #             if len(meshes) > 0:
    #                 cmds.polyUnite(meshes, ch=0)
    #                 meshName = cmds.ls(sl=1)[0]
    #                 youngBranchMeshes.append(meshName)
    #                 cmds.polyMergeVertex(meshName, d=0.0001,am=1,ch=0)
    #                 cmds.polySoftEdge(meshName, a=180, ch=1)
    #                 cmds.delete(ch=1)
    #         except RuntimeError:
    #             if len(meshes) > 0:
    #                 youngBranchMeshes.append(meshes[0])
    #                 cmds.polySoftEdge(meshName, a=180, ch=1)
    #                 cmds.delete(ch=1)
    #             pass
    #
    #         cmds.progressBar(buildProgressControl, edit=True, step=1)
    #
    #     cmds.delete(profileCurveName)
    #     cmds.deleteUI(buildProgressWindow)
    #
    #
    #     if len(leafMeshes) > 0:
    #         youngLeafShader = makinShaders.createSG_wTransp("/Users/danneag/Desktop/Tree References/Textures/NorfolkPine_leaves1.png")
    #         cmds.sets(leafMeshes, e=1, forceElement=youngLeafShader)
    #     if len(youngBranchMeshes) > 0:
    #         youngBranchShader = makinShaders.createSG_noTransp("/Users/danneag/Desktop/Tree References/Textures/Pine_YoungBranch.png")
    #         cmds.sets(youngBranchMeshes, e=1, forceElement=youngBranchShader)
    #
    #     cmds.select(cl=1)

    # def moveEdges(self, sides, scaledVector, edgeList, meshName):
    #
    #     if sides == 3:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.e[{0}]'.format(edgeList[0]),
    #                   meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]), r=1)
    #
    #     elif sides == 4:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.e[{0}]'.format(edgeList[0]),
    #                   meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),meshName+'.e[{0}]'.format(edgeList[3]), r=1)
    #
    #     elif sides == 5:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.e[{0}]'.format(edgeList[0]),
    #                   meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),meshName+'.e[{0}]'.format(edgeList[3]),
    #                   meshName+'.e[{0}]'.format(edgeList[4]),r=1)
    #
    #     elif sides == 6:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.e[{0}]'.format(edgeList[0]),
    #                   meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),meshName+'.e[{0}]'.format(edgeList[3]),
    #                   meshName+'.e[{0}]'.format(edgeList[4]),meshName+'.e[{0}]'.format(edgeList[5]),r=1)
    #
    #     elif sides == 7:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.e[{0}]'.format(edgeList[0]),
    #                   meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),meshName+'.e[{0}]'.format(edgeList[3]),
    #                   meshName+'.e[{0}]'.format(edgeList[4]),meshName+'.e[{0}]'.format(edgeList[5]),meshName+'.e[{0}]'.format(edgeList[6]),r=1)
    #
    #     elif sides == 8:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.e[{0}]'.format(edgeList[0]),
    #                   meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),meshName+'.e[{0}]'.format(edgeList[3]),
    #                   meshName+'.e[{0}]'.format(edgeList[4]),meshName+'.e[{0}]'.format(edgeList[5]),meshName+'.e[{0}]'.format(edgeList[6]),
    #                   meshName+'.e[{0}]'.format(edgeList[7]),r=1)

    # def moveVerts(self, sides, scaledVector, vertList, meshName):
    #
    #     if sides == 3:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.vtx[{0}]'.format(vertList[0]),
    #                   meshName+'.vtx[{0}]'.format(vertList[1]),meshName+'.vtx[{0}]'.format(vertList[2]), r=1)
    #
    #     elif sides == 4:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.vtx[{0}]'.format(vertList[0]),
    #                   meshName+'.vtx[{0}]'.format(vertList[1]),meshName+'.vtx[{0}]'.format(vertList[2]),meshName+'.vtx[{0}]'.format(vertList[3]), r=1)
    #
    #     elif sides == 5:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.vtx[{0}]'.format(vertList[0]),
    #                   meshName+'.vtx[{0}]'.format(vertList[1]),meshName+'.vtx[{0}]'.format(vertList[2]),meshName+'.vtx[{0}]'.format(vertList[3]),
    #                   meshName+'.vtx[{0}]'.format(vertList[4]),r=1)
    #
    #     elif sides == 6:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.vtx[{0}]'.format(vertList[0]),
    #                   meshName+'.vtx[{0}]'.format(vertList[1]),meshName+'.vtx[{0}]'.format(vertList[2]),meshName+'.vtx[{0}]'.format(vertList[3]),
    #                   meshName+'.vtx[{0}]'.format(vertList[4]),meshName+'.vtx[{0}]'.format(vertList[5]),r=1)
    #
    #     elif sides == 7:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.vtx[{0}]'.format(vertList[0]),
    #                   meshName+'.vtx[{0}]'.format(vertList[1]),meshName+'.vtx[{0}]'.format(vertList[2]),meshName+'.vtx[{0}]'.format(vertList[3]),
    #                   meshName+'.vtx[{0}]'.format(vertList[4]),meshName+'.vtx[{0}]'.format(vertList[5]),meshName+'.vtx[{0}]'.format(vertList[6]),r=1)
    #
    #     elif sides == 8:
    #
    #         cmds.move(scaledVector[0], scaledVector[1], scaledVector[2], meshName+'.vtx[{0}]'.format(vertList[0]),
    #                   meshName+'.vtx[{0}]'.format(vertList[1]),meshName+'.vtx[{0}]'.format(vertList[2]),meshName+'.vtx[{0}]'.format(vertList[3]),
    #                   meshName+'.vtx[{0}]'.format(vertList[4]),meshName+'.vtx[{0}]'.format(vertList[5]),meshName+'.vtx[{0}]'.format(vertList[6]),
    #                   meshName+'.vtx[{0}]'.format(vertList[7]),r=1)

    # def extrudeEdges(self, sides, edgeList, meshName):
    #
    #     if sides == 3:
    #
    #         cmds.polyExtrudeEdge(meshName+'.e[{0}]'.format(edgeList[0]),meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),
    #                              kft=1,d=1)
    #
    #     elif sides == 4:
    #
    #         cmds.polyExtrudeEdge(meshName+'.e[{0}]'.format(edgeList[0]),meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),
    #                              meshName+'.e[{0}]'.format(edgeList[3]),kft=1,d=1)
    #
    #     elif sides == 5:
    #
    #         cmds.polyExtrudeEdge(meshName+'.e[{0}]'.format(edgeList[0]),meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),
    #                              meshName+'.e[{0}]'.format(edgeList[3]),meshName+'.e[{0}]'.format(edgeList[4]),kft=1,d=1)
    #
    #     elif sides == 6:
    #
    #         cmds.polyExtrudeEdge(meshName+'.e[{0}]'.format(edgeList[0]),meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),
    #                              meshName+'.e[{0}]'.format(edgeList[3]),meshName+'.e[{0}]'.format(edgeList[4]),meshName+'.e[{0}]'.format(edgeList[5]),
    #                              kft=1,d=1)
    #
    #     elif sides == 7:
    #
    #         cmds.polyExtrudeEdge(meshName+'.e[{0}]'.format(edgeList[0]),meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),
    #                              meshName+'.e[{0}]'.format(edgeList[3]),meshName+'.e[{0}]'.format(edgeList[4]),meshName+'.e[{0}]'.format(edgeList[5]),
    #                              meshName+'.e[{0}]'.format(edgeList[6]),kft=1,d=1)
    #
    #     elif sides == 8:
    #
    #         cmds.polyExtrudeEdge(meshName+'.e[{0}]'.format(edgeList[0]),meshName+'.e[{0}]'.format(edgeList[1]),meshName+'.e[{0}]'.format(edgeList[2]),
    #                              meshName+'.e[{0}]'.format(edgeList[3]),meshName+'.e[{0}]'.format(edgeList[4]),meshName+'.e[{0}]'.format(edgeList[5]),
    #                              meshName+'.e[{0}]'.format(edgeList[6]),meshName+'.e[{0}]'.format(edgeList[7]),kft=1,d=1)

    # def fillNewVertList(self, sides, vertCount):
    #
    #     if sides == 3:
    #         newLoopVerts = [vertCount+1,vertCount,vertCount+2]
    #     elif sides == 4:
    #         newLoopVerts = [vertCount+1,vertCount,vertCount+2,vertCount+3]
    #     elif sides == 5:
    #         newLoopVerts = [vertCount+1,vertCount,vertCount+2,vertCount+3,vertCount+4]
    #     elif sides == 6:
    #         newLoopVerts = [vertCount+1,vertCount,vertCount+2,vertCount+3,vertCount+4,vertCount+5]
    #     elif sides == 7:
    #         newLoopVerts = [vertCount+1,vertCount,vertCount+2,vertCount+3,vertCount+4,vertCount+5,vertCount+6]
    #     elif sides == 8:
    #         newLoopVerts = [vertCount+1,vertCount,vertCount+2,vertCount+3,vertCount+4,vertCount+5,vertCount+6,vertCount+7]
    #
    #     return newLoopVerts
