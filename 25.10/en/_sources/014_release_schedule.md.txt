## Release Schedule
Updated: February 27, 2026<br><br>
Starting in 2026, the release cycle for FCS will change from the previous quarterly updates to semi-annual updates in April and October (twice a year).<br>

#### 1. Regular releases (major versions)
Major versions that mainly include specification changes, such as adding new features and changing algorithms, will be released twice a year, in April and October.<br>
By changing the release frequency, we aim to further stabilize the quality of each version.

#### 2. Hotfix releases (minor versions)
Once a major version is released, feature set is frozen until the next regular release.<br>
Minor version could include subtle improvements such as UI refinement and bug fixes, will be released as needed (e.g., 24.10.01).
<br>

### Upgrading FCS
We have discontinued dividing our products into different versions (LTS/Standard/Preview) based on support status, etc.
To simplify operations, we have now standardized our format, providing all customers with the same support period and the latest updates.

#### Compatibility
FCS sessions are forward-compatible unless explicitly noted otherwise; however, backward compatibility is not always guaranteed, especially across major versions (e.g., 25.07, 25.10).<br>
This means you can open FCS sessions created in a previous version of FCS using newer versions. However, once a session is opened in a newer version, it may no longer be possible to open it in an older version of FCS.<br>
Therefore, it is critical to back up your files before upgrading to a newer version of FCS.<br>
We strive to maintain backward compatibility within a major version (e.g., across 25.10.01–25.10.04); however, this is not guaranteed.<br>

#### Steps to upgrade
1. [Export your data](#export-header-target). 
2. Open the exported data using the newly downloaded version of FCS.
