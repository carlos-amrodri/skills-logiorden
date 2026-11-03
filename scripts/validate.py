#!/usr/bin/env python3
"""Valida las convenciones del repo de skills.

Chequea que:
- cada temática en skills/ tenga README.md
- cada skill tenga SKILL.md y README.md
- el frontmatter tenga name y description válidos
- name coincida con la carpeta y sea único
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if line and not line.startswith((" ", "\t")) and ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip('"')
    return data


def main() -> int:
    errors, names = [], {}
    for tematica in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        if not (tematica / "README.md").exists():
            errors.append(f"{tematica.name}: falta README.md de la temática")
        for skill in sorted(p for p in tematica.iterdir() if p.is_dir()):
            rel = f"{tematica.name}/{skill.name}"
            skill_md = skill / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"{rel}: falta SKILL.md")
                continue
            if not (skill / "README.md").exists():
                errors.append(f"{rel}: falta README.md")
            fm = frontmatter(skill_md)
            name, desc = fm.get("name", ""), fm.get("description", "")
            if not NAME_RE.match(name) or len(name) > 64:
                errors.append(f"{rel}: name inválido '{name}' (minúsculas, números y guiones)")
            if name != skill.name:
                errors.append(f"{rel}: name '{name}' no coincide con la carpeta")
            if not desc or len(desc) > 1024:
                errors.append(f"{rel}: description vacía o mayor a 1024 caracteres")
            if name in names:
                errors.append(f"{rel}: name repetido (también en {names[name]})")
            names[name] = rel

    if errors:
        print("Errores encontrados:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(names)} skill(s) válidas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
