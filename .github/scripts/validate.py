#!/usr/bin/env python3
"""Validate skills, Markdown links and SVG files. Standard library only."""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []


def fail(msg):
    errors.append(msg)
    print(f"::error::{msg}")


# 1. Skill frontmatter: folder name == name, description present
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if not skills:
    fail("no skills/*/SKILL.md found")
for f in skills:
    rel = f.relative_to(ROOT).as_posix()
    m = re.match(r"^---\n(.*?)\n---\n", f.read_text(encoding="utf-8"), re.S)
    if not m:
        fail(f"{rel}: missing YAML frontmatter")
        continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)", fm, re.M | re.S)
    if not name:
        fail(f"{rel}: frontmatter has no name")
    else:
        if name.group(1) != f.parent.name:
            fail(f"{rel}: name '{name.group(1)}' != folder '{f.parent.name}'")
        if not NAME_RE.match(name.group(1)):
            fail(f"{rel}: name must be lowercase letters, digits and hyphens")
    if not desc or not desc.group(1).replace(">-", "").strip():
        fail(f"{rel}: frontmatter has no description")


# 2. Relative links and anchors in README and docs
def slug(h):
    h = re.sub(r"[^\w\- ]", "", h.strip().lower())
    return h.replace(" ", "-")


def anchors(p):
    t = p.read_text(encoding="utf-8")
    found = {slug(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.+)$", t, re.M)}
    return found | set(re.findall(r'<a id="([^"]+)"', t))


md_files = [ROOT / "README.md"] + sorted((ROOT / "docs").rglob("*.md"))
for f in md_files:
    text = re.sub(r"(```|~~~).*?\1", "", f.read_text(encoding="utf-8"), flags=re.S)
    links = re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r'(?:src|href)\s*=\s*"([^"]+)"', text)
    for link in links:
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        path, _, frag = link.partition("#")
        target = (f.parent / path).resolve() if path else f.resolve()
        rel = f.relative_to(ROOT).as_posix()
        if not target.exists():
            fail(f"{rel}: broken link {link}")
        elif frag and target.suffix == ".md" and frag not in anchors(target):
            fail(f"{rel}: missing anchor {link}")


# 3. SVG files parse as XML
for f in sorted((ROOT / "docs").rglob("*.svg")):
    try:
        ET.parse(f)
    except ET.ParseError as e:
        fail(f"{f.relative_to(ROOT).as_posix()}: invalid SVG ({e})")

print(f"checked {len(skills)} skills, {len(md_files)} Markdown files")
sys.exit(1 if errors else 0)
