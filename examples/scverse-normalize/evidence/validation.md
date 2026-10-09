# Validation report

NO_CANDIDATE : close this campaign as no win. The retained source matches the baseline exactly, and all nine valid scored experiments were rejected.

The best rejected result was 2.322919 ms versus the frozen 2.590367 ms baseline: a 10.3247% apparent latency reduction, short of the required 20.9685%. Its peak RSS was 449,608 KiB versus 457,864 KiB for baseline. Fifteen other attempts produced no valid score.

The corpus check, semantic suite, and focused upstream tests passed (30 passed, 39 skipped). Two independent baseline timing reruns failed the stability gate, with `compact_f32:api` CV of 40.7% and 46.7% against a 25% limit. A renewed effort would first need stable, paired baseline and candidate measurements.
