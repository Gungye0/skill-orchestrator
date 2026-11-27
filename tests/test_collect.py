"""collect_skills.py 검증: python3 tests/test_collect.py"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "scripts"))
from collect_skills import collect, parse_frontmatter  # noqa: E402

env = HERE / "fake-env"
skills = collect([("home", env / "home/.claude/skills"), ("project", env / "project/.claude/skills")])
by_name = {s["name"]: s for s in skills}

assert sorted(by_name) == ["csv-cleaner", "independent-judge", "report-writer"], by_name
assert by_name["independent-judge"]["source"] == "project"
assert by_name["csv-cleaner"]["source"] == "home"
assert "JSON 형식의 요약 데이터" in by_name["report-writer"]["description"]  # 여러 줄(>) description
assert parse_frontmatter("no frontmatter") == {}
# 프로젝트 쪽이 같은 이름을 덮어쓴다
dup = collect([("home", env / "project/.claude/skills"), ("project", env / "project/.claude/skills")])
assert dup[0]["source"] == "project"
# independent-judge가 없는 환경
assert "independent-judge" not in {s["name"] for s in collect([("home", env / "home/.claude/skills")])}
print("test_collect: 6개 검사 통과")
