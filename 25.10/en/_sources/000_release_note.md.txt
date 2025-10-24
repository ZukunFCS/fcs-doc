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

#### Retarget Accuracy
We also fixed a few longstanding bugs in our prediction pipeline. As a result, it should generate much more stable animation even for older pipelines (Rich, RP, Robust).

In addition, we also create a new ****experimental**** feature to boost accuracy for retargeting, by allowing the user to create more fine-grain control over the controller beyond the four regions. This is for advanced users who would want to create very accurate, low-noise result. This will be completely optional. The manual will be updated later to provide a more thorough explanation.

### Misc

- Remove Hover text for controller tab, this has been known to cause crashes in some systems and do not provide too much helpful information.
- Optimize the application launch time
- Optimize controller table saving
