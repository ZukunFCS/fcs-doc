# Release Note
[Download FCS here](https://github.com/ZukunFCS/fcs-doc/releases)

## FCS 25.07.03
-Date: 2025/06/25
- Version: 25.07.03
- Stage: Stable

#### Bug fixes
- Fixed shortcut keys triggering when modifier is active (Triggering Period when Ctrl + Period is pressed)
- Fixed deleting profile leading to app crashing

#### Misc
- Remove distribute button in the processor tab (we will release it once the CLI app is complete)

## FCS 25.07.02
- Date: 2025/06/16
- Version: 25.07.02
- Stage: Beta

#### Bug fixes
- Fixed Gallery Renders from Maya not getting deleted when renaming a profile
- Fixed batch processing generating scene and video even when not checked
- Fixed certain text input field blocking keyboard shortcuts
- Fixed the gallery display mode when switching from picture to render

## FCS 25.07.01
- Date: 2025/06/09
- Version: 25.07.01
- Stage: Beta

#### New manual
Added a [new advanced manual](https://zukunfcs.github.io/fcs-doc-advanced/latest/en/index.html) for technical artists at fcs-doc-advanced, with algorithm benchmarks and other evaluations to help you understand the amount of effort you need to put into to obtain the result you want.

#### Character Preview
When you save a profile, FCS will now attemp to save a screenshot of the character, so you can see double check your profiles without Maya. You can also change the display of the gallery from showing the HMC image to showing the character image.  
This features is automatically on, but requires you to have the Maya camera setup (otherwise it would just shows a blank image). You can turn this off in Settings.

#### Denosing (Previously 'Smoothing')
We renamed the feature that generates more animator-friendly curves from smoothing to denoising.  
This more accurately describes what this feature is supposed to do for the animators.  
We also add our first new, non-smoothing denoising method, peak-preserving denoising.  
It essentially flattens the animation curve while trying to preserve as much of the peaks as possible.  
As a part of the new denosing pipeline, we added a preview feature, that allows you to see what an animation curve could look like before and after the denosing operation, and allows you to quickly play around with the parameters etc.

#### Misc
1. Added Maya 2026 support
2. Added a new postprocessing feature: Gaze-freezing, you can now automatically freeze gaze animation when the eye is closed.
3. Improved security: We now sign all executables (e.g., exe, dll) not just the installer. This should make it less likely for security software to flag FCS. If your anti-virus still flags us, please kindly let us know.