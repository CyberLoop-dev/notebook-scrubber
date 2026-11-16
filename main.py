#!/usr/bin/env python3
"""Remove saved outputs from Jupyter notebooks without touching cell source."""
import argparse
import copy
import json
import shutil
import sys
from pathlib import Path


def scrub(notebook):
    if not isinstance(notebook, dict) or not isinstance(notebook.get("cells"), list):
        raise ValueError("Expected a notebook object with a cells array")
    cleaned = copy.deepcopy(notebook)
    changed = 0
    for cell in cleaned["cells"]:
        if not isinstance(cell, dict) or cell.get("cell_type") != "code":
            continue
        dirty = bool(cell.get("outputs")) or cell.get("execution_count") is not None
        if dirty:
            changed += 1
        cell["outputs"] = []
        cell["execution_count"] = None
    return cleaned, changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="exit 1 if cleaning is needed")
    mode.add_argument("--in-place", action="store_true", help="rewrite the notebook and create a .bak copy")
    args = parser.parse_args()
    try:
        original = json.loads(args.notebook.read_text(encoding="utf-8"))
        cleaned, changed = scrub(original)
        if args.check:
            print("clean" if changed == 0 else f"needs cleaning: {changed} code cell(s)")
            return 0 if changed == 0 else 1
        rendered = json.dumps(cleaned, ensure_ascii=False, indent=1) + "\n"
        if args.in_place:
            backup = args.notebook.with_suffix(args.notebook.suffix + ".bak")
            if backup.exists():
                raise FileExistsError(f"Backup already exists: {backup}")
            shutil.copy2(args.notebook, backup)
            args.notebook.write_text(rendered, encoding="utf-8")
            print(f"Cleaned {changed} code cell(s); backup: {backup}")
        else:
            sys.stdout.write(rendered)
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
