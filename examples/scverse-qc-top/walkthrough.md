## Request

> Speed up top-expression proportions while matching the dense Scanpy result for supported sparse inputs. Make implicit zeros, signed values and CSR/CSC formats explicit in the correctness fixtures.

## Setup

The timing fixtures were nonnegative, but the advertised dense-equivalence behaviour was broader. The retained candidate had a stable weighted score on those fixtures. A new contract should use dense outputs as the independent oracle and include short rows, implicit zeros and signed inputs.

## Change

When a sparse row has few stored values, skip selection work and treat those values as the top entries. This is valid only when implicit zeros cannot outrank stored entries. Negative stored values invalidate that shortcut.

## Evaluation

The independent audit tested [-3, 0, 0, 0] at ranks 1, 2, 3 and 4. Dense results were (0, 0, 0, 1); retained CSR and CSC returned (1, 1, 1, 1). A fixture speedup had passed while the broader semantic claim failed.

## Result

The **2.18×** weighted fixture result is rejected because signed inputs fail. The audit proposed a zero-padded partition/segment-sum fallback for signed short rows; that repair remains untested.

## Follow-up

Keep the signed-row counterexample in the tests. Route signed short rows through the baseline partition path, then rerun CSR, CSC and public QC comparisons before timing.
