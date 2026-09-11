# Dryland Biodiversity AI Pilot Results

## Objective

This pilot evaluates the transfer performance of the `sub-saharan-drylands` wildlife classifier within the SPARROW Engine on a small set of dryland wildlife and pastoral-animal photographs.

Two workflows were compared:

1. Direct full-image classification.
2. Animal detection followed by species classification.

## Pilot Design

- 18 images
- 9 target classes
- 2 images per class
- Wildlife and pastoral livestock included
- Mostly ordinary photographs rather than camera-trap imagery
- One striped-hyena image retained as an explicit out-of-region stress test

Target classes:

- cattle
- cheetah
- dikdik
- domestic goat
- donkey
- dromedary camel
- East African oryx
- gerenuk
- striped hyena

## Main Results

| Metric | Result |
|---|---:|
| Direct Top-1 success | 8/18 (44.4%) |
| Detector-classifier image-level success | 10/18 (55.6%) |
| Improvement | +11.1 percentage points |

The detector-classifier workflow recovered two images that failed under direct classification:

- `dromedary_camel_02`
- `cattle_01`

No image that was correct under direct classification became unsuccessful under the image-level pipeline rule.

## Species-Level Performance

| Species | Direct | Pipeline |
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

## Diagnostic Interpretation

Performance varied strongly among taxa.

Cheetah, dikdik, and striped hyena were consistently classified correctly in both workflows.

Localization improved image-level performance for cattle and dromedary camel, showing that isolating the animal from broader scene context can help in some cases.

Domestic goat, donkey, and East African oryx remained unsuccessful in both workflows.

Several failed images still received strong animal detections, suggesting that the primary limitation in those cases was species classification rather than animal localization.

East African oryx showed repeated confusion with morphologically related classes, particularly gemsbok.

## Evaluation Rule

Direct classification is evaluated once per image.

For the detector-classifier workflow, an image is considered successful when at least one valid `animal` detection is classified as the true class.

Individual detections are retained separately for diagnostic analysis and are not treated as independent test images.

Exact model labels are preserved. For example, `cow` is not automatically counted as `cattle` in the strict evaluation.

## Limitations

This is a small exploratory transfer-performance pilot and should not be interpreted as a formal accuracy benchmark.

Important limitations include:

- only 18 images;
- only two images per class;
- mostly ordinary photographs rather than camera-trap imagery;
- heterogeneous image context and quality;
- possible geographic and visual-domain shift relative to model training data;
- one explicitly out-of-region striped-hyena stress-test image;
- image-level pipeline success can conceal mixed classifications within multi-animal scenes.

A larger independent camera-trap evaluation is required before making conclusions about operational performance in Somaliland or the wider Horn of Africa.

## Next Phase

The next stage will extend the project toward dryland ecological monitoring by linking biodiversity observations with agroclimatic and rangeland indicators such as seasonal rainfall, rainfall anomalies, vegetation condition, drought indicators, temperature, and rangeland condition.

The longer-term objective is to explore a reproducible biodiversity-climate monitoring workflow relevant to dryland and pastoral landscapes.
