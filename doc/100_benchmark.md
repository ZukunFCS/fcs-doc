# Benchmarks (WIP)
This page contains a collection of benchmarks to showcase more practical aspects of FCS. 
This page serves a few purposes, first and more importantly is to set a realistic expectation regarding the amount of work you need to achieve the animation quality using our software. Second it should also gives you a more visual understanding of different algorithms that are implemented in FCS.  

We reserve all right to all material, including images and videos used on this page. Please contact us if you were to use the material.   
### Table of Contents
- [Benchmarks (WIP)](#benchmarks-wip)
    - [Table of Contents](#table-of-contents)
  - [Processing Profiles](#processing-profiles)
    - [Background](#background)
    - [Scenario Detail](#scenario-detail)
    - [Gallery](#gallery)
  - [Challenging conditions](#challenging-conditions)
    - [Background](#background-1)
    - [Scenario Detail](#scenario-detail-1)
    - [Gallery](#gallery-1)
  - [Different Actors](#different-actors)
    - [Background](#background-2)

## Processing Profiles
### Background
FCS provides a selection of carefully crafted processing profiles. They are essentially algorithms that we developed to turn facial captures to character movements. In this benchmark we showcase the differences performance between different algorithms. 

### Scenario Detail


### Gallery



## Challenging conditions

### Background
In the case when you are processing videos that is heavily occluded, by facial hair and other external factors, our tracking will not work as well as it does. This is an area where we are actively working on, nonetheless, you can still improve the final quality of the animation by simply adding more profiles to the gallery. The most effective way to improve the animation quality of a particular video is to add more profiles from within the video itself. 

### Scenario Detail
In this show case, we selected and rigged 50 profiles from the [ROM video](https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/roms/nagaki_rom.mp4). The occluded region tends to produce less-than-ideal animation results. This can be mitigated by adding profiles from within the video. We showcases how the performance improve when you add a number of profiles. 


### Gallery
<details>
  <summary >Display gallery</summary>
  
| Performance Video | Baseline (50+0 Profiles) | 50 + 5 Profiles | 
| --------- | --------- | --------- |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/cheek_pull_both_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/cheek_pull_both_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/cheek_pull_both_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/cheek_pull_right_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/cheek_pull_right_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/cheek_pull_right_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/down_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/down_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/down_normal_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/down_silence_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/down_silence_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/down_silence_t01.mp4" type="video/mp4"></video> |      
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/eye_scratch_both_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/eye_scratch_both_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/eye_scratch_both_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/eye_scratch_left_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/eye_scratch_left_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/eye_scratch_left_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/eyemask_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/eyemask_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/eyemask_normal_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/eyepatch_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/eyepatch_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/eyepatch_normal_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/Gendou_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/Gendou_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/Gendou_normal_t01.mp4" type="video/mp4"></video> |   
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/glasses_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/glasses_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/glasses_normal_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/hide_right_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/hide_right_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/hide_right_normal_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/kurohige_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/kurohige_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/kurohige_normal_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/mask_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/mask_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/mask_normal_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/shirohige_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/shirohige_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/shirohige_normal_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/tobacco_disgyst_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/tobacco_disgyst_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/tobacco_disgyst_t01.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/tobacco_normal_t03.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/tobacco_normal_t03.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/tobacco_normal_t03.mp4" type="video/mp4"></video> |
| <video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/common/challenging_reference_set/yubibue_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/baseline/yubibue_normal_t01.mp4" type="video/mp4"></video> |<video height="300" controls><source src="https://github.com/ZukunFCS/artifacts/raw/refs/heads/master/benchmarks/profile_counts/p_5/yubibue_normal_t01.mp4" type="video/mp4"></video> |


</details>


## Different Actors
### Background
FCS expects you to use the one actor for one character in one session. But we also understand there is demand for a more one-size-fit-all solution that works across different actors. This is not our main focus with FCS, but we do demonstrate how one would do that just in case.


