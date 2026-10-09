# Validation report

**NO_CANDIDATE : close as no retained win.** The current sparse kernel matches the frozen baseline. Across 95 scored experiments, none cleared the required improvement of more than 2.575230 ms.

The fastest historical trial measured 125.312323 ms against the 127.646739 ms baseline: a 2.334416 ms improvement, or **1.01862878× speedup**. It missed the keep threshold by 0.240814 ms and was reverted. A future candidate would need a median below 125.071509 ms, with all semantic and contamination gates passing.

A fresh locked check passed all 68 canonical cases. The measured `np.zeros` interval benefits from lazy page allocation; subsequent writes incur page faults, so the diagnostic “scatter” time cannot be attributed solely to ISA instructions. The timed worker also does not record output ownership, although the canonical gate checks it and the current source allocates a new array.
