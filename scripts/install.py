#!/usr/bin/env python3
"""Install AI Garage Motion from this repository. Standard library only."""

import argparse
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tool", required=True, choices=("claude", "codex"))
    parser.add_argument("--scope", required=True, choices=("user", "project"))
    parser.add_argument("--project", type=Path, help="Existing project directory; required for project scope")
    parser.add_argument("--dry-run", action="store_true", help="Show paths without writing files")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills" / "ai-garage-motion"
    if args.scope == "project":
        if args.project is None:
            parser.error("--scope project requires --project PATH")
        base = args.project.expanduser().resolve()
        if not base.is_dir():
            parser.error("The project directory must already exist.")
    else:
        if args.project is not None:
            parser.error("Use --project only with --scope project.")
        base = Path.home()
    tool_dir = ".claude" if args.tool == "claude" else ".agents"
    destination = base / tool_dir / "skills" / "ai-garage-motion"
    if not (source / "SKILL.md").is_file():
        parser.error("Source skill is missing. Run this installer from a complete repository download.")
    if any(p.is_symlink() for p in source.rglob("*")):
        parser.error("Source contains symlinks; inspect the package before installing.")
    if destination.exists() or destination.is_symlink():
        parser.error("An installation already exists at {}. No files were changed. Review or back up that version before updating.".format(destination))
    print("Source: {}".format(source))
    print("Destination: {}".format(destination))
    if args.dry_run:
        print("Dry run: no files changed.")
        return
    # copytree refuses an existing destination, including a concurrently created one.
    shutil.copytree(source, destination)
    print("Installed AI Garage Motion. Open a new agent session in your project.")
    print("Invoke: {}ai-garage-motion".format("/" if args.tool == "claude" else "$"))


if __name__ == "__main__":
    main()
