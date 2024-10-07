# Auto pickup (experimental) 
FCS introduces a new way to select frames for retargetting from video effectively with little to no human supervision. 
This allows you to get the most out of FCS with the least effort. 

```{attention}
This feature is currently in beta and we expect it would break for particular cases. We welcome feedback from the community regarding the implementation.  
```

### How to use Auto Pickup 
Auto pickup window can be opened by right clicking on the video in the Video tab. 

![](images/012_auto_profiles.jpg)

This should bring up the auto profile window. 
![](images/012_auto_profile_window.jpg)

This window allows you to automatically select frames from the video. After confirming the video is correctly selected, you are provided with a couple options regarding what kind of frames you would like to pick up from the video. 

### Selection method
Currently, two methods are implemented to allow you to select frames, based on the type of video, `General` and `ROM`, for slightly different use case.    

**General** is designed for using on any video. It will looks for frame that is a good representation of the overall facial expression as it appears in the video.

Inside *General* you can decide any number of profiles that you would like to add from the video, the algorithm will look at the entire video, and look for facial expression(s) that can overall represent the video.  

**ROM** looks for video frames that match that the specific facial expressions as included in the ROM.pdf included with starter kit. 

In the *ROM* method, you can choose what exact facial expression that you are looking for inside the video. The algorithm will look for the closest match inside the video. 

In the future we will release another version where custom ROM sequence can used. 