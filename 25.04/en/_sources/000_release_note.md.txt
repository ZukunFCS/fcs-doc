# Release Note
[Download FCS here](https://github.com/ZukunFCS/fcs-doc/releases)

## FCS 25.04.09
- Date: 2025/05/23
- Version: 25.04.09
- Stage: Stable

#### Fixes
1. Fixed the Robust Pipeline
2. Fixed From Maya causing crashes

## FCS 25.04.08
- Date: 2025/05/13
- Version: 25.04.08
- Stage: Beta

#### Fixes
1. Fixed a bug that create more profiles during Auto Profile than specified  
2. Prevented the app from crashing when the application does not have read/write access to the $HOME folder, show an error instead.  
3. Improved app stability

#### Update
1. Changed the update CDN from AWS to Github. If you are not able to connect to github directly, please consider using a system-wise VPN to download the update via the application, or use a VPN in your browser and download it directly from [Github](https://github.com/ZukunFCS/fcs-doc/releases).  
2. Optimize the tooltip (hovered text)


## FCS 25.04.07
- Date: 2025/04/23
- Version: 25.04.07
- Stage: Beta

#### Fixes
1. Fixed a bug where non-HMC(head mount camera) footages are processed as HMC footages. 
2. Fixed a bug where footages encoded when highly compressed video will drop frames when being processed. There is a very low chance of happening if you ingress raw video footage off your camera prior to processing it with FCS. On the other hand, if you process video footages encoded with libx265 with very few I-frames in between (high b-frames ratio), there might be a chance that you were affected. In which case you might notice the timing of the animation does not match the timing of the footage (the character's blink might happens faster/earlier than it is in the footage). We inherented this memory issues from the library we used to process video footages when using multiprocess. Explicit multiprocessing has since been disabled for footage process, leading to a slightly longer processing time in some systems but more accurate animations. An upcoming fix in 25.07 will speed up the processing. 
3. Fixed a bug where missing controller in the Maya scene lead to other following controllers to fail to be sent/received.
4. Fixed a bug where prioritizing profile does not work when profiles are very cloes to each other (within the user-defined window, defaults to 1 second)

#### Update
1. Updated Terms of Service 

## FCS 25.04.06
- Date: 2025/04/08
- Version: 25.04.06
- Stage: Stable

#### Fixes
1. Fixed a bug where processing videos would take longer time during process spawning
2. Changed the border color of tabs
3. Removed old dlls

## FCS 25.04.05
- Date: 2025/04/03
- Version: 25.04.05
- Stage: Stable

#### New features
1. Gallery 
   1. Added new sort method: "Randomized"
   2. Added batch tagging for profiles
   3. Added a dropdown to limit how many profiles to display at a time

#### Fixes
1. Fixed gallery sorting order being inconsistent in some cases
2. Fixed an issue where deleting smoothing profile can crash the app
3. Fixed an issue where right click menu can stay out of screen
4. Fix rearranging controller crashes the app
5. Fix controller renaming crashes the app
6. Disallow adding empty or duplicated profile tag
7. Disallow layout with no name

## FCS 25.04.04
- Date: 2025/03/27
- Version: 25.04.04
- Stage: Beta

#### New features
1. Added support for Maya 2025
2. Added toggle in Editor to hide the image panel

#### Fixes
1. Fixed an issue where exporting a session would not work with Assets folder
2. Fixed an issue where deleting smoothing profile can crash the app
3. Fixed an issue where right click menu can stay out of screen

## FCS 25.04.03
- Date: 2025/03/24
- Version: 25.04.03
- Stage: Beta

#### Fixes
1. Fixed controller table bug that causes the application to crash
2. Optimized keyboard shortcut responsiveness
3. Modified the text for the process feature that allows the user to re-process only a segment of the video

## FCS 25.04.02
- Date: 2025/03/19
- Version: 25.04.02
- Stage: Beta

#### New Features
Timeline 
1. Added a new feature that allows processing part of the video

#### Bug Fixes
1. Fix unstable issue with timeline checkboxes
2. Fix a bug where sorting controller table would not work as intended
3. Fix a bug where shortcut input does not function

## FCS 25.04.01
- Date: 2025/03/05
- Version: 25.04.01
- Stage: Beta

#### Changes
Timeline
1. Moved buttons from timeline to right click menu (matching behaviour in Maya)

Shortcut Key
1. Changed the timeline shortcut keys to match the ones in Maya

#### New Features
Timeline 
1. Added looped playback support
2. Added audio playback support

Settings
1. Added a new feature to import user setting from a previous version
2. Added AV1 codec support for better web support
3. Added support for a new set of symbols for shortcut keys

#### Bug Fixes
1. Fixed a bug where long video might the process in some systems
2. Fixed a bug where batch renaming controllers crashes the application when there is no profile at all.
