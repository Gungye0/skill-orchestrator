# skill-orchestrator

사용자의 목표를 받아 설치된 스킬 중 적합한 것을 골라 실행 순서를 짜고, 단계 사이의 입출력을 이어 주는 Claude 스킬입니다.

- `~/.claude/skills/`와 프로젝트의 `.claude/skills/`에서 SKILL.md frontmatter를 읽어 스킬 목록 수집
- 목표를 단계로 나누고 단계마다 스킬 하나를 매칭, 맞는 스킬이 없으면 "미매칭"으로 알림
- 출력과 입력 형식이 다르면 변환 단계를 자동으로 넣고 계획에 표시
- 마지막에 [independent-judge](https://github.com/<사용자>/independent-judge) 검증 단계를 기본으로 넣음(미설치 시 생략하고 알림)
- 실행 전에 계획을 보여주고 승인을 받음, 외부 전송과 파일 삭제는 실행 직전에 다시 확인

## 설치

복사:

```bash
mkdir -p ~/.claude/skills && cp -r skill-orchestrator ~/.claude/skills/skill-orchestrator
```

또는 git clone:

```bash
git clone https://github.com/<사용자>/skill-orchestrator.git ~/.claude/skills/skill-orchestrator
```

검증 단계까지 쓰려면 independent-judge도 같은 방식으로 설치합니다. Python 3가 필요합니다(표준 라이브러리만 사용).

## 사용 예시

```
skill-orchestrator로 진행해 줘: sales.csv를 정리하고 매출 요약 보고서를 마크다운으로 써 줘.
```

스킬이 먼저 [scripts/plan_template.md](scripts/plan_template.md) 형식의 계획을 보여줍니다.

```
| 단계 | 할 일 | 스킬 | ... | 표시 |
| 1 | CSV 정리 | csv-cleaner | ... | - |
| 2 | CSV → JSON 요약 | (자동 변환) | ... | [자동 삽입] |
| 3 | 보고서 작성 | report-writer | ... | - |
| 4 | 결과 검증 | independent-judge | ... | [기본 검증] |
```

승인하면 순서대로 실행합니다. 설치된 스킬 목록만 보려면:

```bash
python3 ~/.claude/skills/skill-orchestrator/scripts/collect_skills.py
```

## 테스트

```bash
python3 tests/test_frontmatter.py
python3 tests/test_collect.py
```

`tests/fake-env`는 스킬 3개가 설치된 가상 환경입니다. 목표 2개에 대한 기대 계획은 [tests/scenarios.md](tests/scenarios.md), 실제 실행 결과는 [tests/results.md](tests/results.md)에 있습니다.

## 한계

- 스킬 매칭은 description 문장만 보고 모델이 판단합니다. description이 부실한 스킬은 잘못 매칭되거나 미매칭될 수 있습니다.
- 입출력 형식은 description과 단계 설명에서 추론합니다. 스킬이 형식을 명시하지 않으면 "확인 필요"로 묻습니다.
- 단계 하나에 스킬 하나만 붙입니다. 여러 스킬을 섞어 한 단계를 처리하지 않습니다.
- 플러그인으로 설치된 스킬(`~/.claude/plugins/` 등)은 수집하지 않습니다.
- frontmatter 파서는 단순한 `키: 값`과 `>`/`|` 여러 줄 값만 처리합니다.

## 라이선스

MIT. [LICENSE](LICENSE) 참고.
