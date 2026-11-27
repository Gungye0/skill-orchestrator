"""SKILL.md frontmatter 규칙 검사: python3 tests/test_frontmatter.py"""
import re
from pathlib import Path

text = (Path(__file__).parent.parent / "SKILL.md").read_text(encoding="utf-8")
assert text.startswith("---\n"), "frontmatter 없음"
fm = text.split("---\n")[1]
meta = dict(line.split(": ", 1) for line in fm.strip().splitlines())
name, desc = meta["name"], meta["description"]

assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name), f"name 형식: {name}"
assert len(name) <= 64
assert "claude" not in name and "anthropic" not in name
assert len(desc) <= 1024, len(desc)
assert "<" not in desc and ">" not in desc
assert len(re.findall(r"[.!?](\s|$)", desc)) <= 1, "description은 한 문장"
print(f"test_frontmatter: {name} 통과 (description {len(desc)}자)")
