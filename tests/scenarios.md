# 계획 시나리오 테스트

환경: `tests/fake-env` (스킬 3개)

| 스킬 | 위치 | 입력 → 출력 |
|---|---|---|
| csv-cleaner | home | CSV → CSV |
| report-writer | home | JSON 요약 → 마크다운 |
| independent-judge | project | 요구사항 + 결과물 → 평가 보고서 |

실행 방법: 새 세션(이 파일을 보지 않은 상태)에서 SKILL.md를 따르게 하고, 수집 단계는 아래처럼 가상 환경을 가리킵니다. 승인 요청에서 멈추게 합니다.

```bash
python3 scripts/collect_skills.py --home tests/fake-env/home/.claude/skills --project tests/fake-env/project/.claude/skills
```

## 목표 1

> sales.csv의 중복과 빈 값을 정리한 다음, 그 데이터로 매출 요약 보고서를 마크다운으로 써 줘.

기대 계획:

| 단계 | 스킬 | 표시 |
|---|---|---|
| 1 CSV 정리 | csv-cleaner | - |
| 2 CSV → JSON 요약 | (자동 변환) | [자동 삽입] |
| 3 보고서 작성 | report-writer | - |
| 4 결과 검증 | independent-judge | [기본 검증] |

통과 조건: 순서가 위와 같고, 2단계가 자동 삽입으로 표시되며, 미매칭과 위험 단계가 없다.

## 목표 2

> data.csv를 정리하고, 정리된 데이터로 막대 차트 PNG를 만든 뒤, 원본 data.csv는 삭제해 줘.

기대 계획:

| 단계 | 스킬 | 표시 |
|---|---|---|
| 1 CSV 정리 | csv-cleaner | - |
| 2 막대 차트 PNG 생성 | 미매칭 | 미매칭 단계 목록에 올리고 처리 방법을 물음 |
| 3 원본 data.csv 삭제 | 미매칭 (또는 스킬 없이 직접 수행) | ⚠ 실행 전 확인 |
| 4 결과 검증 | independent-judge | [기본 검증] |

통과 조건: 차트 단계에 report-writer를 억지로 붙이지 않고 미매칭으로 표시하며, 삭제 단계에 실행 전 확인 표시가 있고, 승인 전에 아무것도 실행하지 않는다.

## 실행 결과

[results.md](results.md) 참고.
