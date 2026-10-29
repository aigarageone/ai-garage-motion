#!/usr/bin/env python3
"""Build inspectable, deterministic AI Garage Motion release ZIPs locally."""

import hashlib
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
TOP_FILES = ("README.md", "README.uk.md", "LICENSE", "VERSION", ".gitignore")


def public_files():
    files = [ROOT / name for name in TOP_FILES]
    for folder in ("docs", "scripts", "skills"):
        files.extend(p for p in (ROOT / folder).rglob("*")
                     if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    for path in files:
        if path.is_symlink():
            raise ValueError("Symlinks cannot be packaged: {}".format(path.relative_to(ROOT)))
        if not path.is_file():
            raise ValueError("Missing file: {}".format(path.relative_to(ROOT)))
    return sorted(files)


def verify(files):
    skill = ROOT / "skills" / "ai-garage-motion"
    core = (skill / "SKILL.md").read_text(encoding="utf-8")
    if not core.startswith("---\nname: ai-garage-motion\n") or "\ndescription:" not in core:
        raise ValueError("Invalid skill entrypoint")
    if (skill / "LICENSE").read_bytes() != (ROOT / "LICENSE").read_bytes():
        raise ValueError("Skill and repository license notices differ")
    for path in files:
        if path.suffix == ".py":
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        if path.suffix != ".md":
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            url = urlsplit(target)
            if url.scheme or target.startswith("#"):
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                raise ValueError("Broken local link in {}: {}".format(path.relative_to(ROOT), target))


def archive(path, entries):
    # Exclusive creation prevents silently replacing an earlier release artifact.
    with path.open("xb") as stream:
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as output:
            for source, name in sorted(entries, key=lambda item: item[1]):
                info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                output.writestr(info, source.read_bytes())


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without producing archives")
    args = parser.parse_args()
    files = public_files()
    verify(files)
    print("Verified {} public source files and local Markdown links.".format(len(files)))
    if args.check:
        return
    version = (ROOT / "VERSION").read_text().strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("VERSION must be a semantic release number")
    output = ROOT / "dist"
    skill_zip = output / "ai-garage-motion.zip"
    source_zip = output / "ai-garage-motion-source-v{}.zip".format(version)
    sums = output / "SHA256SUMS.txt"
    if any(p.exists() for p in (skill_zip, source_zip, sums)):
        parser.error("Release artifacts already exist. Preserve or move them before rebuilding.")
    output.mkdir(exist_ok=True)
    skill_root = ROOT / "skills" / "ai-garage-motion"
    archive(skill_zip, [(p, "ai-garage-motion/" + p.relative_to(skill_root).as_posix())
                        for p in files if p.is_relative_to(skill_root)])
    archive(source_zip, [(p, "ai-garage-motion-v{}/{}".format(version, p.relative_to(ROOT).as_posix()))
                         for p in files])
    lines = []
    for path in (skill_zip, source_zip):
        lines.append("{}  {}".format(hashlib.sha256(path.read_bytes()).hexdigest(), path.name))
        print("Built {} ({} bytes)".format(path.name, path.stat().st_size))
    with sums.open("x", encoding="utf-8") as stream:
        stream.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
