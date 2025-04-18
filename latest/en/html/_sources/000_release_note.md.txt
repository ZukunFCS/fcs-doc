# Release Note
[Download FCS here](https://github.com/ZukunFCS/fcs-doc/releases)

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
