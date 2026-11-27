#!/usr/bin/env python3
"""설치된 스킬의 SKILL.md frontmatter(name, description)를 모아 JSON으로 출력한다."""
import argparse
import json
import sys
from pathlib import Path


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta, key = {}, None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line[:1] in (" ", "\t") and key:  # 여러 줄 값(> 또는 |)의 이어지는 줄
            meta[key] = (meta[key] + " " + line.strip()).strip()
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key, value = key.strip(), value.strip()
            if value in (">", "|", ">-", "|-"):
                value = ""
            meta[key] = value.strip("\"'")
    return meta


def collect(dirs):
    """dirs: [(source, path)]. 뒤에 오는 source가 같은 이름을 덮어쓴다."""
    found = {}
    for source, base in dirs:
        for skill_md in sorted(Path(base).expanduser().glob("*/SKILL.md")):
            try:
                meta = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError) as e:
                print(f"읽기 실패: {skill_md}: {e}", file=sys.stderr)
                continue
            name = meta.get("name")
            if not name:
                print(f"name 없음, 건너뜀: {skill_md}", file=sys.stderr)
                continue
            found[name] = {
                "name": name,
                "description": meta.get("description", ""),
                "source": source,
                "path": str(skill_md),
            }
    found.pop("skill-orchestrator", None)
    return sorted(found.values(), key=lambda s: s["name"])


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--home", default="~/.claude/skills")
    p.add_argument("--project", default=".claude/skills")
    args = p.parse_args()
    skills = collect([("home", args.home), ("project", args.project)])
    print(json.dumps(skills, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
