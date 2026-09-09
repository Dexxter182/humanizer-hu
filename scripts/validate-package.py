#!/usr/bin/env python3
"""A Humanizer-hu csomagfájljainak ellenőrzése külső függőség nélkül."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "humanizer-hu"


def read_package_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"Nem olvasható: {path.relative_to(ROOT)}: {error}")


SKILL_PATH = ROOT / "SKILL.md"
SKILL = read_package_file(SKILL_PATH)
README = read_package_file(ROOT / "README.md")
try:
    PLUGIN = json.loads(read_package_file(ROOT / ".claude-plugin" / "plugin.json"))
except json.JSONDecodeError as error:
    raise SystemExit(f"Javítsd a JSON-t a .claude-plugin/plugin.json fájlban: {error}")


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


yaml_metadata = require_match(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "A SKILL.md-nek YAML metaadattal kell kezdődnie",
).group(1)

for unsupported_field in ("version:", "compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(unsupported_field)}", yaml_metadata):
        raise SystemExit(f"Vedd ki a nem támogatott YAML mezőt: {unsupported_field[:-1]}")

skill_name = require_match(
    re.search(r"(?m)^name:\s*(\S+)\s*$", yaml_metadata),
    "Add meg a skill nevét a SKILL.md metaadatában",
).group(1)
if skill_name != SKILL_NAME or PLUGIN.get("name") != SKILL_NAME:
    raise SystemExit(f"A skill és a plugin neve legyen {SKILL_NAME}: {skill_name}, {PLUGIN.get('name')}")

skill_version = require_match(
    re.search(r'(?m)^\s+version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$', yaml_metadata),
    "Add meg a metadata.version mezőt a SKILL.md-ben, háromtagú verzióval",
).group(1)
readme_version = require_match(
    re.search(r"(?m)^- ([0-9]+\.[0-9]+\.[0-9]+) - ", README),
    "Írj verzióbejegyzést a README.md-be: '- X.Y.Z - ...' formában",
).group(1)

package_versions = {skill_version, readme_version, str(PLUGIN.get("version", ""))}
if len(package_versions) != 1:
    raise SystemExit(
        f"Egy verzió legyen minden fájlban: {sorted(package_versions)}"
    )

skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
if SKILL_PATH.is_symlink() or skill_files != {Path("SKILL.md")}:
    raise SystemExit("Egyetlen, valódi SKILL.md legyen a repo gyökerében")
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit("A Claude plugin skill betöltője a repo gyökerére mutasson")

pattern_numbers = [
    int(number)
    for number in re.findall(r"(?m)^### ([0-9]+)\. ", SKILL)
]
pattern_count = len(pattern_numbers)
if pattern_count == 0 or pattern_numbers != list(range(1, pattern_count + 1)):
    raise SystemExit(f"A SKILL.md mintáit 1-től hézag nélkül számozd: {pattern_numbers}")

readme_numbers = [
    int(number) for number in re.findall(r"(?m)^\| ([0-9]+) \|", README)
]
if sorted(readme_numbers) != pattern_numbers:
    raise SystemExit(
        f"A README tábláiban 1-től {pattern_count}-ig minden minta egyszer szerepeljen: {sorted(readme_numbers)}"
    )
if f"## A {pattern_count} minta" not in README:
    raise SystemExit(f"A README mintaszakaszának címe legyen 'A {pattern_count} minta'")

if len(SKILL.splitlines()) > 400:
    raise SystemExit("A SKILL.md legfeljebb 400 soros lehet")

print(f"A Humanizer-hu csomag v{skill_version} érvényes")
