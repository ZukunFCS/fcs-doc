# Release Note

## Compatibility
| open\create | 24.10.01 | 24.10.02 | 24.10.03 | 24.10.04 | 24.10.05 | 24.10.06 | 24.10.07 | 24.10.08 | 24.10.09 |
|:---------------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| **24.10.01** | o | o | o | o | o | x | x | x | x |
| **24.10.02** | o | o | o | o | o | x | x | x | x |
| **24.10.03** | o | o | o | o | o | x | x | x | x |
| **24.10.04** | o | o | o | o | o | x | x | x | x |
| **24.10.05** | o | o | o | o | o | x | x | x | x |
| **24.10.06** | o | o | o | o | o | o | o | o | o |
| **24.10.07** | o | o | o | o | o | o | o | o | o |
| **24.10.08** | o | o | o | o | o | o | o | o | o |
| **24.10.09** | o | o | o | o | o | o | o | o | o |

## FCS 24.10.09
- Date: 2024/11/05
- Version: 24.10.09
- Stage: Stable

### Overview
1. Fixed profile image being saved at a different resolution in some cases, introduced at 24.10.06.   
   This affects the predicted animation's result. If you are using version 24.10.06 - 24.10.08, we recommend upgrading immediately. An automatic update will be applied to fix the resolution of the image.

## FCS 24.10.08
- Date: 2024/10/30
- Version: 24.10.08
- Stage: Stable

### Overview
1. Fixed Maya imagePlane is setup incorrectly 
2. Changed default imagePlane and camera name to imagePlane and fcs_cam respectively
3. Fixed an error which prevent switching to the newly created Actor and character when creating new session
4. Fixed prediction result not being sent to Maya even when To maya is ON. 


## FCS 24.10.07
- Date: 2024/10/29
- Version: 24.10.07
- Stage: Stable

### Overview
1. Fixed program crashes when trying to display LM
2. Fixed session info profile count shows incorrect value
3. Fixed an error where the Maya image plane is named incorrectly 
4. Added a feature to clear all caches when opening session in a different version 

## FCS 24.10.06
- Date: 2024/10/16
- Version: 24.10.06
- Stage: Stable

### !Cannot be downgraded!
**Once opened in this version, your FCS session will not be abled to downgraded to a previous version of FCS, including FCS 24.10.05. We strongly recommend you to backup your files before using the update.**


### Overview
1. Fixed animation timeline off by 1 frame
2. Optimized launch spped
3. Improved logging 

#### Fixed animation timeline off by 1 frame
Fixed a bug where the first frame of a video is used twice (i.e., the 99th frame is presented as the 100th frame). All previously created profiles are all off by one frame, which will be fixed once imported using the new version of FCS. However, it also means that it will be incorrect if the fixed profile is imported back to a previous version of FCS. Therefore, once imported to the new version, it is not possible to downgrade to use the previous version. 


## FCS 24.10.05
- Date: 2024/10/11
- Version: 24.10.05
- Stage: Stable

### Overview
1. Fixed a bug where video is not cached when opened for viewing
2. Fixed a bug where the auto profile assigns the wrong name to the profile in ROM mode 
3. Added a new feature for exported solver for real-time use
4. Added a warning sign for invalid controller info.

## FCS 24.10.04
- Date: 2024/10/07
- Version: 24.10.04
- Stage: Stable

### Overview
1. Fixed a bug where landmark frame output crashes the application under specific circumstances.

## FCS 24.10.03
- Date: 2024/09/25
- Version: 24.10.03
- Stage: Stable

### Overview
1. Fixed gallery issues
2. Fixed installer issues
3. Misc.

### Detail
#### Fixed gallery issues
1. Fixed an issue where reset on FCS UI doesn't get send to Maya
2. Fixed a bug where disabled regions' values are still sent to Maya

#### Fixed installer issues
1. Changed the default install path to C drive
2. Updated the installer icon
3. Added Japanese support

#### Misc 
1. Fixed a bug where controller rename triggers app crashes
2. Fixed a bug where smoothing is not applied （Fixed in 24.10.01）
3. Fixed Prioritize Profile

## FCS 24.10.02
- Date: 2024/09/09
- Version: 24.10.02
- Stage: Beta

### Overview
1. Improved filtering feature in Gallery, allowing batch edit/delete  
2. Fixed a bug where editor landmark preview is turned off when opening a new profile.
3. Fixed a bug where the cursor position does not exactly move to 
4. Optimized gallery render speed
5. Added Prioritize Profile
6. Added a feature to batch rename all controllers
7. Improved video playback speed

### Detail
#### Improved filtering feature in Gallery, allowing batch edit/delete  
1. Add filtering by region, video name etc.

#### Fixed a bug where the cursor position does not exactly move to 
1. Ctrl + Left mouse button click to enter value directly 
2. Cursor position will translate to the value of the slider
   
#### Prioritize Profile
1. Added a feature to match the output animation with the defined profiles. 
2. Enabled by checking Solver/Post-processing/Prioritize Profile

#### Batch rename controller
1. Select controllers in Controller Info to rename, useful for adding prefix/suffix etc. 
2. The change will propagate to the profiles previously created.

#### Improved video playback speed
1. Added a feature to use RAM to speed up video playback, mostly useful for legacy computers.
2. Default to enabled. 
3. You can store a maximum of 5 videos to your memory if it allows.

#### Added a solver export feature for real time use 
1. Export a solver file using Solver/Export.
2. Import the file into the real time application (WIP) for view your character moving in real-time

## FCS 24.10.01
- Date: 2024/08/29
- Version: 24.10.01
- Stage: Beta

### Overview
1. Added a language and version switcher for the manual (left bottom)
1. [English manual](https://zukunfcs.github.io/fcs-doc/24.10/en/index.html) (draft) now available
2. Added experimental linux support
3. Added an installer for FCS
4. Added a feature to download ffmpeg if it doesn't exist on the user system.
5. [Added a feature to automatically generate profile from video](https://zukunfcs.github.io/fcs-doc/latest/en/012_auto_pickup.html)
6. Added UI elements and download for the new version. 

### Info for upgrading from a previous version
You can safely open your session from 24.07.
    

### Detail

#### Installer
1. Changed build method to Themida. Using virtual machine and debugger together with FCS is unsupported. If you need to allow these for specific reason please contact us.
2. Added installer, default installation path is C:\FCS. Please ensure the program has write access to the folder.

#### FFMPEG
1. Pull ffmpeg directly from [github](https://github.com/BtbN/FFmpeg-Builds/) if it doesn't exist in the user system.
2. If you cannot connect to github please directly install ffmpeg and add it to path.   

#### UI
1. You can now open and view a video using double click
2. Fixed a bug where the layout is not retained  
3. Fixed the initial layout of FCS when first launch in a new computer
4. Added timeline drag
5. Added a feature to retain user interface states so it persist between program launches. 
6. Updated japanese translations
7. Added support for modifier keys
8. Added support for shortcut keys
   - Save profile
   - Open Profile from video
   - Send value from Editor to Maya (To Maya) 
   - Receive controller value from Maya (From Maya)
   - Change layout 
9. Renamed Enforce Annotation to Prioritize Profile

#### Maya
1. Disabled region values are not sent from FCS to maya

#### Updater
1. Added a new feature to check for new updates 
2. Update settings are as follow
   1. Update channel: All | Patch | None  
    Decide what kind of updates are checked for. 
   2. Use Beta
    Use the unstable build.

#### Linux Support
FCS supports Fedora 8 now, please contact us if you are interested.

#### Misc.
1. Program data location is changed from `$USER/.fcs/Cortado` to `$USER/.fcs/Cortado/$version`.
