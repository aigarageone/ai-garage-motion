#!/usr/bin/env python3
"""Create a small AI Garage Motion planning folder; no rendering or installation."""

import argparse
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--language", choices=("en", "uk"), default="en")
    args = parser.parse_args()
    destination = args.destination.expanduser().resolve()
    if destination.exists() or destination.is_symlink():
        parser.error("Destination already exists; no files were changed.")
    templates = Path(__file__).resolve().parents[1] / "assets" / "templates"
    sources = [templates / (name + "." + args.language + ".md")
               for name in ("brief", "storyboard", "review", "delivery")]
    if not all(p.is_file() for p in sources):
        parser.error("Templates are missing; use a complete skill installation.")
    destination.mkdir(parents=True, exist_ok=False)
    for source, name in zip(sources, ("BRIEF.md", "STORYBOARD.md", "REVIEW.md", "DELIVERY.md")):
        shutil.copyfile(source, destination / name)
    print("Created planning documents: {}".format(destination))
    print("No media, dependencies, or background processes were created.")


if __name__ == "__main__":
    main()
