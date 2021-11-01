# BranchMeshTester

This program is a plug-in for Autodesk Maya that acts as a tester for a class in a larger plug-in I made to generate models of plants.  I created this one to have something more to show potential employers, and because the larger one is being overhauled.  The code in the BMTCommand files (BMTCommand.h, BMTCommand_newSyntax.cpp, and BMTCommand_doIt.cpp) and in the Python files is written exclusively for this program, the rest is mostly imported from the primary plug-in.  The class being tested is called BranchMesh.  Its purpose is to take input in the form of a linked list of Segments, and convert it into data that can be passed to the create() method of the Maya API's MFnMesh class which, in turn, creates the polygonal mesh in Maya.

To run...

  - have Autodesk Maya 2018 installed (other versions may well work, but I cannot gaurantee).
  - have Python installed 
  - download the three files from this repository: BranchMeshTester.mll, BranchMeshTester_GUI.py, and Branch.py
  - place the files in the correct directories...for Windows users, I can summarize:
  
    - both .py files go in C:\Users\<Your User Name>\Documents\maya\scripts
    - the .mll file can be placed anywhere - then with Maya open, from the top bar go to Windows -> Settings/Preferences -> Plug-in Manager
    - within the plug-in manager window, click the browse button on the bottom left, navigate to the .mll file, then make sure the 'loaded' checkbox is checked for it
    - (a similar process should work for other operating systems. If it doesn't, see the link below)

  - open Maya's script editor:  Windows -> General Editors -> Script Editor.  Then, on the bottom half of the window, make sure you have a Python tab open
  - enter the following 3 lines of python code:
    
    import BranchMeshTester_GUI  
    reload(BranchMeshTester_GUI)  
    BranchMeshTester_GUI.GUI()  
    
  - execute it by clicking the 'Execute' button along the top of the script editor
  - the BranchMesh Tester window should now be open, giving an interface to the plug-in

If this does not work for you I apologize.  You can try to follow Autodesk's guide to installing plug-ins [&lt;here&gt;](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Maya-Customizing/files/GUID-FA51BD26-86F3-4F41-9486-2C3CF52B9E17-htm.html)

For more info on usage, view the Demo file in this repository.

Thank you for checking out my work!
