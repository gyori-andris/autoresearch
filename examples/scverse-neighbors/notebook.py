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
            location / "examples" / "scverse-neighbors"
            for location in (Path.cwd(), *Path.cwd().parents)
            if (location / "examples" / "scverse-neighbors" / "case.json").exists()
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
    _audit = case_dir / "evidence" / "validation.md"
    _links = "[Evidence record](evidence/provenance.json)"
    if _audit.exists():
        _links += " · [Validation report](evidence/validation.md)"
    mo.md("## Evidence\n\n" + _links)
    return


if __name__ == "__main__":
    app.run()
