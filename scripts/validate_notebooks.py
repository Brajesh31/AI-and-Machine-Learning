#!/usr/bin/env python3
"""Validate notebook structure and Python syntax without executing notebook cells."""
from __future__ import annotations

import ast
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted(ROOT.glob("*.ipynb"))


def python_source(source: str) -> str:
    """Remove common IPython magic/shell lines before Python AST parsing."""
    kept: list[str] = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("%", "!")):
            kept.append("# IPython command omitted from static syntax check")
        else:
            kept.append(line)
    return "\\n".join(kept)


def main() -> int:
    if not NOTEBOOKS:
        print("ERROR: no notebooks found at repository root", file=sys.stderr)
        return 1

    errors: list[str] = []
    for path in NOTEBOOKS:
        try:
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
        except Exception as exc:  # report malformed files without hiding other failures
            errors.append(f"{path.name}: invalid notebook structure: {exc}")
            continue

        for number, cell in enumerate(notebook.cells, start=1):
            if cell.cell_type != "code":
                continue
            source = python_source(cell.source)
            if not source.strip():
                continue
            try:
                ast.parse(source, filename=f"{path.name}:cell-{number}")
            except SyntaxError as exc:
                errors.append(
                    f"{path.name}: cell {number}: Python syntax error at line "
                    f"{exc.lineno}: {exc.msg}"
                )

        if not any(error.startswith(path.name + ":") for error in errors):
            print(f"VALID: {path.name}")

    if errors:
        print("\\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(NOTEBOOKS)} notebook(s). Cell execution was not performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
