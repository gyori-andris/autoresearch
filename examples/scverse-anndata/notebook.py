import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import json
    from pathlib import Path
    import marimo as mo
    try:
        case_dir = Path(__file__).resolve().parent
    except NameError:  # Jupyter does not define __file__.
        case_dir = next(
            location / "examples" / "scverse-anndata"
            for location in (Path.cwd(), *Path.cwd().parents)
            if (location / "examples" / "scverse-anndata" / "case.json").exists()
        )
    case = json.loads((case_dir / "case.json").read_text())
    return case, case_dir, json, mo


@app.cell
def _(case, mo):
    mo.md(f"# {case['title']}\n\nStatus: **{case['status']}**")
    return


@app.cell
def _(case_dir, mo):
    mo.md((case_dir / "walkthrough.md").read_text())
    return


@app.cell
def _(case_dir, mo):
    mo.md(
        "## Contract and handover\n\n"
        + (case_dir / "CONTRACT.md").read_text()
        + "\n\n---\n\n"
        + (case_dir / "HANDOVER.md").read_text()
    )
    return


@app.cell
def _(case_dir, json, mo):
    _path = case_dir / "evidence" / "replay.json"
    if _path.exists():
        import statistics
        import math
        _record = json.loads(_path.read_text())
        _rows = []
        for _name, _samples in _record['result']['absolute_samples_ms'].items():
            _base = statistics.median(s['reference_ms'] for s in _samples)
            _candidate = statistics.median(s['candidate_ms'] for s in _samples)
            _rows.append({'case': _name, 'reference_ms': _base, 'candidate_ms': _candidate, 'speedup': _base / _candidate})
        _score = 1 / _record['result']['relative_geomean']
        _table = "| Case | Reference (ms) | Candidate (ms) | Ratio of medians |\n| --- | ---: | ---: | ---: |\n"
        _table += "\n".join(
            f"| {row['case']} | {row['reference_ms']:.2f} | {row['candidate_ms']:.2f} | {row['speedup']:.3f}× |"
            for row in _rows
        )
        _view = mo.md(
            f"## Recorded replay\n\nGeometric mean speedup: **{_score:.3f}×**. "
            "The table shows latency medians of six samples per implementation per case. "
            "The aggregate score instead uses per-case medians of paired latency ratios.\n\n"
            + _table
        )
    else:
        _view = mo.md("")
    _view
    return


@app.cell
def _(case_dir, json):
    from statistics import median
    import matplotlib.pyplot as plt
    _samples = json.loads(
        (case_dir / "evidence/replay.json").read_text()
    )["result"]["absolute_samples_ms"]
    _fig, _ax = plt.subplots(figsize=(10, 5), layout="constrained")
    for _i, (_name, _pairs) in enumerate(_samples.items()):
        for _offset, _field, _label, _colour in (
            (-.18, "reference_ms", "Reference", "#777777"),
            (.18, "candidate_ms", "Candidate", "#357b71"),
        ):
            _values = [pair[_field] for pair in _pairs]
            _ax.barh(_i + _offset, median(_values), height=.32, color=_colour,
                     label=_label if _i == 0 else None)
            _ax.scatter(_values, [_i + _offset] * len(_values), color="black",
                        s=10, alpha=.6, zorder=3)
    _ax.set_yticks(range(len(_samples)), list(_samples))
    _ax.set_xlabel("Conversion latency (ms); bars: medians; dots: paired observations")
    _ax.invert_yaxis()
    _ax.legend()
    _fig
    return


@app.cell
def _(case_dir, mo):
    _audit = case_dir / "evidence" / "validation.md"
    _links = "[Evidence record](evidence/provenance.json)"
    if _audit.exists():
        _links += " · [Validation report](evidence/validation.md)"
    mo.md("## Evidence\n\n" + _links)
    return


if __name__ == "__main__":
    app.run()
