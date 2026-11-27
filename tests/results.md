# 테스트 실행 결과 (2026-11-27)

## 자동 검사

```
$ python3 tests/test_frontmatter.py
test_frontmatter: skill-orchestrator 통과 (description 178자)
$ python3 tests/test_collect.py
test_collect: 6개 검사 통과
```

## 계획 시나리오 ([scenarios.md](scenarios.md))

실행 방식: 시나리오와 기대 결과를 보지 않은 새 컨텍스트의 에이전트가 SKILL.md와 plan_template.md만 읽고, `collect_skills.py`를 가상 환경에 대해 실행한 뒤 승인 요청에서 멈춤. 파일 생성, 수정, 삭제 없음.

수집 결과: csv-cleaner(home), independent-judge(project), report-writer(home). 3개 모두 수집됨.

### 목표 1: 통과

| 단계 | 기대 | 실제 |
|---|---|---|
| 1 | csv-cleaner | csv-cleaner |
| 2 | (자동 변환) [자동 삽입] | CSV → JSON 요약, (자동 변환) [자동 삽입] |
| 3 | report-writer | report-writer |
| 4 | independent-judge [기본 검증] | independent-judge [기본 검증] |

미매칭 없음. 추가로 "정리본은 새 파일로 저장해 원본을 덮어쓰지 않음, 덮어쓰면 실행 전 확인"을 알림에 적음.

### 목표 2: 통과

| 단계 | 기대 | 실제 |
|---|---|---|
| 1 | csv-cleaner | csv-cleaner |
| 2 | 미매칭 | 미매칭 ("report-writer는 마크다운 보고서용") |
| 3 | 미매칭, ⚠ 실행 전 확인 | 미매칭, ⚠ 실행 전 확인 |
| 4 | independent-judge [기본 검증] | independent-judge [기본 검증] |

미매칭 단계 2, 3을 목록에 올리고 (a) 직접 수행 (b) 건너뜀 (c) 중단 중 무엇을 할지 물음. 승인 전에 실행한 단계 없음.

## 검사하지 않은 것

- 승인 이후 실제 실행(가짜 스킬은 본문이 없음)
- independent-judge가 없는 환경에서 "검증 단계 생략" 알림을 내는지(수집 쪽 판별은 test_collect.py에서 검사함)
