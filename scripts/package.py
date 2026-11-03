#!/usr/bin/env python3
"""Empaqueta cada skill en dist/<nombre>.zip para subir a Claude o ChatGPT.

El README.md de la skill (pensado para personas) no se incluye en el zip.
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
EXCLUDE = {"README.md", ".DS_Store"}


def main() -> None:
    DIST.mkdir(exist_ok=True)
    count = 0
    for skill_md in sorted(SKILLS.glob("*/*/SKILL.md")):
        skill = skill_md.parent
        out = DIST / f"{skill.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill.rglob("*")):
                if f.is_file() and f.name not in EXCLUDE:
                    z.write(f, Path(skill.name) / f.relative_to(skill))
        print(f"  {out.relative_to(ROOT)}")
        count += 1
    print(f"{count} skill(s) empaquetadas en dist/")


if __name__ == "__main__":
    main()
