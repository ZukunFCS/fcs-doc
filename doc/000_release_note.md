# Release Note
[Download FCS here](https://github.com/ZukunFCS/fcs-doc/releases)

## FCS 25.10.02
- Date: 2025/10/06
- Version: 25.10.02
- Stage: Stable

### Fix
- Fixed segmented animation output not being processed properly
- Fixed release note not being wrapped properly to the window

## FCS 25.10.01
- Date: 2025/09/30
- Version: 25.10.01
- Stage: Stable

25.10 mostly focus on accuracy update.

### New Features
- This version introduces two big main improvement, improved tracking and improved retargeting.

#### Tracking Accuracy
We introduce two new pipelines, RP+ and Robust+. They use a new facial tracking algorithm developed by Zukun. They are essentially upgrades over our existing pipelines, they are specifically designed to improve animation accuracy for studio with low profiles count (less than 50). Results generated using these pipelines cannot be visualized (LM plots are disabled).

We will include more comparison in our [Advanced Manual](https://zukunfcs.github.io/fcs-doc-advanced/latest/en/index.html).

Facial tracking results generated with the new pipelines can be edited in a later version of FCS.

Added on November 28;  
Although facial tracking accuracy itself has improved, we have confirmed that its contribution to the overall quality of output facial animation is small. Furthermore, new pipelines currently have issues in process of converting face tracking data into controller animation. While we aim to address these issues in an early update, we anticipate that it will require a significant amount of time.

#### Retarget Accuracy
We also fixed a few longstanding bugs in our prediction pipeline. As a result, it should generate much more stable animation even for older pipelines (Rich, RP, Robust).

In addition, we also create a new ****experimental**** feature to boost accuracy for retargeting, by allowing the user to create more fine-grain control over the controller beyond the four regions. This is for advanced users who would want to create very accurate, low-noise result. This will be completely optional. Please see the [Advanced manual](https://ryota-nakajima-toei.github.io/fcs-doc-advanced/25.10/en/002_processing.html) here for instructions on how to use it.

Added on November 28;  
In version 25.10, retargeting accuracy has improved regardless of pipelines used. Therefore, output animation results may differ even with older pipelines compared to version 25.07. For this reason, legacy pipelines will remain available for your continued use.

### Misc

- Remove Hover text for controller tab, this has been known to cause crashes in some systems and do not provide too much helpful information.
- Optimize the application launch time
- Optimize controller table saving
