## Request

> Optimise normalize_total under unchanged output semantics. Calibrate a stable baseline and require improvements large enough to exceed observed timing variability.

## Setup

The baseline was 2.590367 ms; retention required a 20.9685% latency reduction. Later baseline reruns exceeded the 25% coefficient-of-variation limit for one public-call case.

## Change

Substitute NumPy reduceat for a reduction path. The hypothesis is useful only if it passes empty-row and other contracted semantics and improves the complete scalar under stable measurement.

## Evaluation

Nine valid scored experiments were rejected and fifteen other attempts produced no valid score. The retained source remained identical to baseline. The audit passed corpus, semantic and focused upstream checks but found baseline CV values of 40.7% and 46.7%, preventing a trustworthy restart without recalibration.

## Result

The best rejected candidate was **2.322919 ms**, a **10.3247% latency reduction**, below the required improvement. Its lower recorded RSS does not override the latency acceptance rule. The campaign closes with **no accepted win**.

## Follow-up

Stabilise the public-call baseline and recalibrate the keep margin before restarting. Preserve rejected timings and distinguish valid scored experiments from crashes or invalid runs.
