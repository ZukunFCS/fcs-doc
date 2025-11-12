# Release Note
[Download FCS](https://github.com/ZukunFCS/fcs-doc/releases)

## FCS 25.01.05
- Date: 2025/02/17
- Version: 25.01.05
- Stage: Stable

#### General
1. Fixed floating point FPS is set incorrectly as int with Maya
2. Fixed a bug where batch processing stops in some system when processing a large amount of videos
3. Added a selected video counter in the Batch process window 
4. Fixed a bug where batch applying range values in Controller Info went to the wrong field
5. Optimized the loading procedure when opening a session created in a previous version of FCS

## FCS 25.01.04
- Date: 2025/01/10
- Version: 25.01.04
- Stage: Stable

#### General
1. Fixed a bug related to assigning new controller to a session

## FCS 25.01.03
- Date: 2025/01/07
- Version: 25.01.03
- Stage: Stable

#### General
1. Added indicator for right-clickable menu items
2. Fixed bug that leads to slower session loading
3. Fixed bug where Maya animation is not deleted outside the current timeline range 
4. Fixed bug where processing video could lead to crashing in some race condition

## FCS 25.01.02
- Date: 2024/12/16
- Version: 25.01.02
- Stage: Preview

#### General
1. Made gallery filter case insensitive
2. Fixed reset in Editor
3. Fixed UI for batch editing in Gallery
4. Fixed Maya controller selection issue
5. Fixed videos opening to single click to double click
6. Other backend fixes


## FCS 25.01.01
- Date: 2024/12/01
- Version: 25.01.01
- Stage: Preview

### ！Cannot be downgraded！
Session opened in 25.01 will not competitable with previous version of FCS. 
As usual, please backup before you upgrade your existing session. 

#### General
1. Added minor version in the app title bar
2. Optimized the startup process so it should now be slightly faster
3. Fixed an error that prevent the third party licenses from loading
4. Fixed a bug where the right click menu goes outside the screen
5. Removed custom animations for better performance
6. Added a new feature to allow opening a different session even when one is already open (we just restart the app for you, a more permanent solution is in discussion)
7. Improved the shortcut key handling so when a key is released the function will stop in the next frame
8. Added command line launch options
   1. --session: Open a session file (.yaml) after launch
   2. --maya_command_port: Use a different Maya Command Port instead of the one specified in Settings
9. Added User Tag for Profile tagging
10. Added Video Rotation Support
   
#### Controller
1. Newly added controllers will have their checkboxes checked so it is easier if you want to immediately assign a value/region to them.
2. Rearrange controller is set to disabled by default, you can still rearrange them if you check the box under Advanced/Rearrange. 
3. Checking the box for controller is now easier, you can left click on the controller name. 
4. Added validation when trying to save the table, you can no longer save a table with null region.
5. Added Value Set so you can change the value of all checked controllers at once. 

#### Creating Session
1. Hid the loading indicator when the task is in fact done. 
2. Added a feature to automatically fill in Maya base if the workspace.mel file is found nearby.

#### Maya
1. Fixed a bug where not connectable attributes will also be added to Controller

#### Timeline
1. Fixed a bug where the timeline is not set on Maya side even when Sync is set to ON. 
2. Fixed a bug where the timeline will still be dragged around even when dragging outside the timeline. 
3. Added a snapping flag to disable snapping

#### Videos
1. Video Processing will now give you a progress bar so you know much longer it would take. 
2. Fixed a bug when trying to open a video that is invalid (file missing) crashes the app
3. Added a feature that allow rotation when importing the video
   1. Note this rotation happens dynamically, so your original video file is never altered and no extra disk space will be taken up, but in turn, it would be more demanding for your local machine to decode on the fly.  
4. Changed the behaviour of opening video from single click to double click
5. Added a feature that allows you to rotate the video when you import the video
   
#### Solver
1. Added a reminder if you try to export a solver for FCSRT but do not have a solver object yet, you can train one by clicking the button next to it. 
2. Added a new face tracker option for more robust (but less rich) tracking, more oriented for real-time tracker. 


#### Gallery
1. Added a checkbox to hide the tooltip
2. Changed the behaviour of predict to only apply to enabled region(s)
3. Added a filter support based on Tag
4. Added Confident Sort
   1. You can now sort your profiles based on how closely it matches the algorithm prediction, this is useful for debugging when you are trying to figure out whether you mistakenly created something wrong. 

#### Editor
1. Add User Tag support
   1. You can add/remove custom tag for profile
   2. You can also add default tags that will be automatically applied to newly created profiles
2. Controller value in disabled region(s) will be excluded from 
   1. From Maya
   2. To Maya
   3. Predict
