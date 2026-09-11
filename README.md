@'

\# Dryland Biodiversity AI



A reproducible exploratory workflow for evaluating dryland wildlife and pastoral-animal classification and preparing for biodiversity-climate integration in dryland landscapes.



The project currently tests two computer-vision workflows using the SPARROW Engine:



1\. direct full-image species classification;

2\. animal detection followed by species classification.



The pilot is designed as a transfer-performance experiment rather than a formal model benchmark.



\---



\## Pilot Overview



The current evaluation contains:



\- \*\*18 images\*\*

\- \*\*9 target classes\*\*

\- \*\*2 images per class\*\*

\- wildlife and pastoral livestock

\- mostly ordinary photographs rather than camera-trap imagery

\- one explicitly identified out-of-region stress-test image



\### Target classes



\- cattle

\- cheetah

\- dikdik

\- domestic goat

\- donkey

\- dromedary camel

\- East African oryx

\- gerenuk

\- striped hyena



\---



\## Models



The workflow uses the SPARROW Engine with:



\- `sub-saharan-drylands` species classifier

\- `MDV6-yolov10-c` animal detector



Model files are not stored in this repository.



\---



\## Main Results



| Evaluation | Correct | Image-level success |

|---|---:|---:|

| Direct classification | 8 / 18 | \*\*44.4%\*\* |

| Detector + classifier | 10 / 18 | \*\*55.6%\*\* |



The detector-classifier workflow produced an improvement of:



\*\*+11.1 percentage points\*\*



Two images that failed under direct classification were recovered after animal localization:



\- `dromedary\_camel\_02`

\- `cattle\_01`



No directly correct image became unsuccessful under the image-level pipeline rule.



\---



\## Species-Level Performance



| Species | Direct | Detector + classifier |

|---|---:|---:|

| cattle | 50% | 100% |

| cheetah | 100% | 100% |

| dikdik | 100% | 100% |

| domestic goat | 0% | 0% |

| donkey | 0% | 0% |

| dromedary camel | 0% | 50% |

| East African oryx | 0% | 0% |

| gerenuk | 50% | 50% |

| striped hyena | 100% | 100% |



!\[Species-level pilot performance](figures/pilot\_species\_performance.png)



\---



\## What the Pilot Shows



Performance differed strongly among taxa.



\*\*Cheetah, dikdik, and striped hyena\*\* were classified correctly in both images and both workflows.



Animal localization improved performance for:



\- cattle

\- dromedary camel



However, localization did not solve all classification errors.



\*\*Domestic goat, donkey, and East African oryx\*\* remained unsuccessful in both workflows.



Several failed images nevertheless received strong animal detections. This indicates that, for those cases, the main limitation was species-level classification rather than animal localization.



East African oryx also showed repeated confusion with related ungulate classes, particularly gemsbok.



\---



\## Evaluation Rule



Direct classification is evaluated once per image.



For the detector-classifier workflow, an image is considered successful when at least one valid `animal` detection is classified as the true class.



Individual detections are preserved for diagnostic analysis but are not treated as independent test images.



Exact classifier labels are retained in the strict evaluation. For example:



`cow` is not automatically counted as `cattle`.



This distinction is important for avoiding inflated performance estimates.



\---



\## Repository Structure



```text

dryland-biodiversity-ai/

|

|-- data/

|   `-- pilot\_metadata.csv

|

|-- docs/

|   `-- pilot\_results.md

|

|-- figures/

|   |-- pilot\_species\_performance.png

|   `-- pilot\_species\_performance.pdf

|

|-- outputs/

|   |-- pilot\_failure\_diagnostics.csv

|   |-- pilot\_image\_summary.csv

|   |-- pilot\_results.csv

|   `-- pilot\_species\_summary.csv

|

|-- scripts/

|   `-- 05\_pilot\_analysis.py

|

|-- .gitignore

|-- README.md

`-- requirements.txt

