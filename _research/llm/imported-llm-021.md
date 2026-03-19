---
title: "gpt5 API"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-4 (실습)gpt5_API"
source_path: "13_LLM_GenAI/Code_Snippets/3-4 (실습)gpt5_API.md"
excerpt: "/ 모드 (Mode) / 용도 (Use Case) / 속도 (Speed, 1~5) / 정확도 (Accuracy, 1~5) / 비용 (Cost, 1~5) / /------------------/--------------------/-------------------..."
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 16 |
| Execution Cells | 13 |
| Libraries | `os`, `getpass`, `openai` |
| Source Note | `3-4 (실습)gpt5_API` |

## What I Worked On

- GPT-5.1 와 API 사용 예
- 1. OpenAI Python 라이브러리 설치
- OpenAI API key
- API키 설정
- **API Key 발급**

## Implementation Flow

1. GPT-5.1 와 API 사용 예
2. 1. OpenAI Python 라이브러리 설치
3. OpenAI API key
4. API키 설정
5. **API Key 발급**
6. 간단한 테스트

## Code Highlights

### 2. 실전 활용

```python
prompt = """
다음 Python 코드를 리뷰하고 개선점을 제시하세요:

def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] > 0:
            result.append(data[i] * 2)
    return result
"""

# API call
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[{"role": "user", "content": prompt}]
)
print(response.choices[0].message.content)
```

### 3. 성능 최적화

```python
from openai import OpenAI
client = OpenAI()

# ============================================
# 1. 매우 긴 system 프롬프트 준비 (약 2000+ 토큰)
# ============================================

base_text = """
You are an expert AI engineer. Provide concise, correct answers.
This is prefix text for prompt caching demonstration.
Repeat this section many times to increase token length.
"""

# 동일한 문장을 여러 번 반복 → 길고 반복되는 prefix 생성
long_system_prompt = base_text * 150   # 약 2000~2500 토큰

# 유저 메시지
user_prompt = "이 프롬프트 캐싱 예제에서 system 프롬프트는 몇 글자인가요?"


# ============================================
# 2. 함수: API 호출 + usage 출력
# ============================================

def call_api(tag):
    print(f"\n=== {tag} 호출 ===")
    response = client.chat.completions.create(
        model="gpt-5.1-chat-latest",
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-4 (실습)gpt5_API.md`
- Source formats: `md`
- Companion files: `3-4 (실습)gpt5_API.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `platform.openai.com`, `openai.com`, `localhost`

## Note Preview

> / 모드 (Mode) / 용도 (Use Case) / 속도 (Speed, 1~5) / 정확도 (Accuracy, 1~5) / 비용 (Cost, 1~5) / /------------------/--------------------/---------------------/--------------------------/-------------------/ / **Instant** / 일상 작업 / 3 / 4 / 2 / / **Thinking** / 복잡한 추론 / 2 / 5 / 3 / / **No Reasoning** / 빠른 응답 / 4 / 3 / 1 /
> ✅ GPT-5.1 API 모델명 (Instant / Thinking)
