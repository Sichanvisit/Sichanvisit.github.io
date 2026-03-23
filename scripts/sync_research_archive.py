from __future__ import annotations

from datetime import datetime
import html
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parent.parent
RESEARCH_ROOT = REPO_ROOT / "_research"
KNOWLEDGE_ROOT = Path(r"C:\Users\bhs33\Desktop\옵시디언(시찬)\Sichan\10_AI_Engineering")

TRACKS = [
    {
        "tab": "ML",
        "folder": "ml",
        "tag": "ml",
        "source": KNOWLEDGE_ROOT / "11_Machine_Learning" / "Code_Snippets",
    },
    {
        "tab": "DL",
        "folder": "dl",
        "tag": "dl",
        "source": KNOWLEDGE_ROOT / "12_Deep_Learning" / "Code_Snippets",
    },
    {
        "tab": "LLM",
        "folder": "llm",
        "tag": "llm",
        "source": KNOWLEDGE_ROOT / "13_LLM_GenAI" / "Code_Snippets",
    },
]

CODE_FENCE_RE = re.compile(r"^```(?P<info>.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s*(.+)$")
IMPORT_RE = re.compile(r"^\s*import\s+([a-zA-Z0-9_\.]+)")
FROM_IMPORT_RE = re.compile(r"^\s*from\s+([a-zA-Z0-9_\.]+)\s+import\s+")


def escape_yaml(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def compact_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strip_yaml_value(text: str) -> str:
    value = text.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value.strip()


def clean_markdown_text(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"<!--.*?-->", "", cleaned)
    cleaned = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", cleaned)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    cleaned = cleaned.replace("`", "")
    cleaned = cleaned.replace("|", "/")
    return compact_spaces(cleaned)


def clean_notebook_heading_text(text: str) -> str:
    cleaned = text.strip()
    cleaned = cleaned.replace("**", "").replace("__", "")
    cleaned = re.sub(r"^[^\w가-힣A-Za-z0-9]+", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(":- ")
    return cleaned or normalize_display_text(text) or text.strip()


def get_ml_heading_level(title: str, current_level: int, has_major_section: bool = False) -> int:
    cleaned = clean_notebook_heading_text(title)

    major_section_pattern = re.compile(r"^\d+\.\s*")
    numbered_subsection_pattern = re.compile(r"^\d+\)\s*")

    if cleaned == "미션 설명" or major_section_pattern.match(cleaned):
        return 2

    if (
        numbered_subsection_pattern.match(cleaned)
        or cleaned.startswith("참고 -")
        or cleaned in {
            "데이터 설명",
            "강사 Tip",
            "1차 데이터 확인",
            "특정 컬럼 데이터 확인",
            "그래프 결과 해석",
            "데이터 시각화 후 추가 파생변수 생성",
            "데이터 다듬기",
            "문자 데이터 가공",
            "정규화/표준화",
            "데이터 합치기",
        }
    ):
        return 3

    if cleaned in {
        "고객 특성 관련 변수",
        "이전 캠페인 관련 변수",
        "경제/거시 지표 관련 변수",
        "SMOTE 적용시 주의사항",
        "stratify=y의미",
    }:
        return 4

    if current_level <= 1:
        if has_major_section:
            return 3
        return 2
    if current_level == 2:
        return 3
    return min(current_level, 4)


def sanitize_raw_note_markdown(raw_text: str, research_tab: str) -> str:
    if not raw_text.strip():
        return ""

    if research_tab != "ML":
        return raw_text.strip()

    cleaned_lines: list[str] = []
    in_code_block = False
    previous_rule = False
    ml_major_section_seen = False

    for raw_line in raw_text.splitlines():
        stripped = raw_line.strip()

        if stripped.startswith("<!--") and ("#region" in stripped or "#endregion" in stripped):
            continue

        fence_match = CODE_FENCE_RE.match(stripped)
        if fence_match:
            if not in_code_block:
                info = fence_match.group("info").strip()
                lang = get_code_language(info)
                cleaned_lines.append(f"```{lang}" if lang else "```")
                in_code_block = True
            else:
                cleaned_lines.append("```")
                in_code_block = False
            previous_rule = False
            continue

        if in_code_block:
            cleaned_lines.append(raw_line.rstrip())
            previous_rule = False
            continue

        if re.fullmatch(r"[-=]{20,}", stripped):
            if not previous_rule:
                cleaned_lines.append("---")
                previous_rule = True
            continue

        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            hashes, title = heading_match.groups()
            cleaned_title = clean_notebook_heading_text(title)
            level = len(hashes)
            if research_tab == "ML":
                level = get_ml_heading_level(cleaned_title, level, has_major_section=ml_major_section_seen)
                if level == 2:
                    ml_major_section_seen = True
            cleaned_lines.append(f"{'#' * level} {cleaned_title}".rstrip())
            previous_rule = False
            continue

        if not stripped:
            if cleaned_lines and cleaned_lines[-1] != "":
                cleaned_lines.append("")
            previous_rule = False
            continue

        cleaned_lines.append(raw_line.rstrip())
        previous_rule = False

    while cleaned_lines and cleaned_lines[0] == "":
        cleaned_lines.pop(0)
    while cleaned_lines and cleaned_lines[-1] == "":
        cleaned_lines.pop()

    return "\n".join(cleaned_lines)


def normalize_display_text(text: str) -> str:
    cleaned = clean_markdown_text(text)
    cleaned = cleaned.replace("**", "").replace("__", "")
    cleaned = re.sub(r"^\d+(?:\.\d+)*[\.\)]\s+", "", cleaned)
    cleaned = re.sub(r"^[A-Za-z]\.\s*", "", cleaned)
    cleaned = cleaned.strip(":- ")
    return compact_spaces(cleaned)


def escape_html_text(text: str) -> str:
    return html.escape(normalize_display_text(text), quote=True)


def is_meaningful_sentence(text: str) -> bool:
    normalized = normalize_display_text(text)
    if len(normalized) < 16:
        return False
    token_count = len(normalized.split())
    if token_count >= 4:
        return True
    return ":" in normalized or "," in normalized or "(" in normalized


GENERIC_LABELS = {
    "overview",
    "archive note",
    "지침",
    "데이터셋 설명",
    "가이드라인",
    "환경준비",
    "import",
    "gpu 설정",
    "한글 폰트 설치",
    "구글 마운트 + 저장경로 설정",
    "setup",
    "imports",
}


SECTION_TITLE_ALIASES = {
    "지침": "문제 개요",
    "데이터셋 설명": "데이터 맥락",
    "가이드라인": "구현 가이드",
    "환경준비": "실행 환경",
    "import": "라이브러리 준비",
    "gpu 설정": "런타임 설정",
}


def normalize_section_title(text: str) -> str:
    normalized = normalize_display_text(text)
    lowered = normalized.lower()
    return SECTION_TITLE_ALIASES.get(lowered, normalized)


def is_generic_label(text: str) -> bool:
    normalized = normalize_display_text(text).lower()
    if normalized in GENERIC_LABELS:
        return True
    if re.match(r"^(스프린트\s*)?미션\s*\d+$", normalized):
        return True
    if re.match(r"^mission\s*\d+$", normalized):
        return True
    return False


def format_plain_list(items: list[str]) -> str:
    cleaned = [normalize_display_text(item) for item in items if normalize_display_text(item)]
    if not cleaned:
        return ""
    if len(cleaned) == 1:
        return cleaned[0]
    if len(cleaned) == 2:
        return f"{cleaned[0]} and {cleaned[1]}"
    return ", ".join(cleaned[:-1]) + f", and {cleaned[-1]}"


def format_korean_list(items: list[str], limit: int | None = None, max_item_len: int = 52) -> str:
    cleaned: list[str] = []
    for item in items:
        normalized = normalize_display_text(item)
        if not normalized:
            continue
        cleaned.append(trim_text(normalized, max_item_len))
        if limit is not None and len(cleaned) >= limit:
            break
    return ", ".join(cleaned)


def ensure_sentence(text: str) -> str:
    cleaned = compact_spaces(text)
    if not cleaned:
        return ""
    if cleaned[-1] in ".!?":
        return cleaned
    return cleaned + "."


def condense_focus_item(text: str, max_len: int = 60) -> str:
    normalized = normalize_display_text(text)
    if not normalized:
        return ""
    if ":" in normalized:
        prefix, _ = normalized.split(":", 1)
        prefix = prefix.strip()
        if 2 <= len(prefix) <= 24:
            return prefix
    return trim_text(normalized, max_len)


LOW_SIGNAL_PREFIXES = (
    "여기서는",
    "이 경우",
    "먼저",
    "그 다음",
    "다음으로",
    "마지막으로",
)

AUXILIARY_SECTION_TOKENS = (
    "참고",
    "한글 오류",
    "한줄 설치",
    "폰트",
    "설치",
    "마운트",
    "런타임",
    "실행 환경",
    "라이브러리 준비",
)

TITLE_KEYWORD_STOPWORDS = {
    "ai",
    "archive",
    "note",
    "overview",
    "practice",
    "mission",
    "sprint",
    "guide",
    "project",
    "record",
    "answer",
    "answers",
    "team",
    "shared",
    "study",
    "실습",
    "코드실습",
    "코딩실습",
    "연습",
    "문제",
    "미션",
    "스프린트",
    "강사",
    "강사공유",
    "공유",
    "답안",
    "기",
    "팀",
    "기초",
    "심화",
    "응용",
    "정리",
    "가이드",
    "실전",
    "과제",
    "자료",
    "eda",
    "overview",
    "데이터",
    "데이터셋",
    "확인",
    "설명",
    "지침",
    "가이드라인",
    "파일",
    "결측치",
    "이상치",
    "중복값",
    "분석",
    "드릴다운",
    "결과",
    "포인트",
    "살펴보기",
    "system",
    "시스템",
    "이해",
    "환경준비",
    "import",
    "from",
    "as",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "torch",
    "sklearn",
    "scikit",
    "learn",
    "dataset",
    "data",
    "gpu",
    "setup",
    "mount",
    "download",
    "install",
    "head",
    "info",
    "describe",
}

LOW_SIGNAL_SECTION_TOKENS = (
    "환경준비",
    "import",
    "gpu",
    "폰트",
    "마운트",
    "저장경로",
    "다운로드",
    "설치",
    "데이터셋 설명",
    "지침",
    "가이드라인",
    "localhost",
)

EDA_SECTION_TOKENS = (
    "eda",
    "데이터 살펴보기",
    "결측치",
    "중복값",
    "이상치",
    "분포 확인",
    "1차 데이터 확인",
    "설명서 확인",
    "속성 목록",
    "파일 설명",
)

DL_PRIORITY_SECTION_TOKENS = (
    "cnn",
    "resnet",
    "alexnet",
    "mask r-cnn",
    "fasterrcnn",
    "yolo",
    "segmentation",
    "unet",
    "diffusion",
    "gan",
    "생성",
    "모델",
    "학습",
    "평가",
    "추론",
    "loss",
    "optimizer",
    "dataloader",
    "augmentation",
    "전이학습",
)

LLM_PRIORITY_SECTION_TOKENS = (
    "rag",
    "retriever",
    "vectorstore",
    "embedding",
    "임베딩",
    "학습준비",
    "모델",
    "전처리 비교 실험",
    "3종 임베딩 실험",
    "추가 실험",
    "파인튜닝",
    "lora",
    "qlora",
    "langgraph",
    "agent",
    "프롬프트",
    "chain",
    "평가",
    "결과",
    "lstm",
    "gru",
)

DL_PRIORITY_CODE_TOKENS = (
    "conv2d",
    "maxpool",
    "resnet",
    "alexnet",
    "maskrcnn",
    "fasterrcnn",
    "segmentation",
    "unet",
    "forward(",
    "optimizer",
    "loss",
    "dataloader",
    "transforms",
    "backward(",
)

LLM_PRIORITY_CODE_TOKENS = (
    "tokenizer",
    "embedding",
    "word2vec",
    "fasttext",
    "glove",
    "lstm",
    "gru",
    "retriever",
    "vectorstore",
    "faiss",
    "chroma",
    "langgraph",
    "agent",
    "lora",
    "qlora",
    "trainer",
    "optimizer",
    "classification_report",
    "f1_score",
)


def clean_section_label(text: str) -> str:
    normalized = normalize_display_text(text)
    normalized = re.sub(r"[\U00010000-\U0010ffff]", "", normalized)
    normalized = re.sub(r"[📌🎯🚲🏦🪛📑🧪✅⭐✨🔥🔍📊📈📉🛠️]", "", normalized)
    normalized = normalized.strip(" -")
    return compact_spaces(normalized)


def format_section_path(path: list[str], max_depth: int = 2) -> str:
    cleaned = [clean_section_label(item) for item in path if clean_section_label(item)]
    if not cleaned:
        return ""
    if max_depth and len(cleaned) > max_depth:
        cleaned = cleaned[-max_depth:]
    return " > ".join(cleaned)


def is_auxiliary_section(text: str) -> bool:
    normalized = clean_section_label(text).lower()
    if not normalized:
        return True
    return any(token in normalized for token in AUXILIARY_SECTION_TOKENS)


def contains_any(text: str, tokens: tuple[str, ...]) -> bool:
    normalized = normalize_display_text(text).lower()
    if not normalized:
        return False
    return any(token in normalized for token in tokens)


def is_low_signal_code_block(body: str) -> bool:
    lower = body.lower()
    lines = get_code_lines(body)
    if not lines:
        return False
    if is_import_heavy_block(body) and len(lines) <= 14:
        return True
    if any(token in lower for token in ("google.colab", "drive.mount", "apt-get", "fc-cache", "font_manager", "warnings.filterwarnings")) and len(lines) <= 16:
        return True
    inspection_hits = sum(
        1
        for token in (".head(", ".info(", ".describe(", ".shape", "print(data.keys(", "display(")
        if token in lower
    )
    if inspection_hits >= 2 and len(lines) <= 14:
        return True
    return False


def extract_title_keywords(text: str, max_terms: int = 8) -> list[str]:
    normalized = clean_section_label(text)
    if not normalized:
        return []

    tokens = re.findall(r"[A-Za-z][A-Za-z0-9\+\-]*|[가-힣]{2,}", normalized)
    keywords: list[str] = []
    seen: set[str] = set()
    for token in tokens:
        lowered = token.lower()
        if lowered in TITLE_KEYWORD_STOPWORDS:
            continue
        if lowered.isdigit():
            continue
        if len(lowered) <= 1:
            continue
        if lowered not in seen:
            seen.add(lowered)
            keywords.append(lowered)
        if len(keywords) >= max_terms:
            break
    return keywords


def build_title_anchor_keywords(
    title: str,
    headings: list[str],
    sections: list[dict[str, object]],
    code_blocks: list[dict[str, object]] | None = None,
    max_terms: int = 8,
) -> list[str]:
    keywords = extract_title_keywords(title, max_terms=max_terms)
    seen = set(keywords)
    code_blocks = code_blocks or []

    def add_keywords(text: str) -> None:
        nonlocal keywords
        for token in extract_title_keywords(text, max_terms=max_terms):
            if token in seen:
                continue
            seen.add(token)
            keywords.append(token)
            if len(keywords) >= max_terms:
                return

    ranked_code_blocks = sorted(
        code_blocks,
        key=lambda block: -score_code_block(block),
    )

    if len(keywords) < max_terms:
        for block in ranked_code_blocks:
            body = str(block.get("body", ""))
            if is_import_heavy_block(body) or is_low_signal_code_block(body):
                continue
            candidates = [
                normalize_display_text(get_code_label(block)),
                normalize_display_text(str(block.get("heading", ""))),
                normalize_display_text(str(block.get("path_text", ""))),
                normalize_display_text("\n".join(body.splitlines()[:8])),
            ]
            for candidate in candidates:
                if not candidate or is_auxiliary_section(candidate):
                    continue
                add_keywords(candidate)
                if len(keywords) >= max_terms:
                    break
            if len(keywords) >= max_terms:
                break

    if len(keywords) < 2:
        for heading in headings:
            normalized = normalize_display_text(heading)
            if (
                not normalized
                or is_generic_label(normalized)
                or is_auxiliary_section(normalized)
                or contains_any(normalized, LOW_SIGNAL_SECTION_TOKENS)
            ):
                continue
            add_keywords(normalized)
            if len(keywords) >= max_terms:
                break

    if len(keywords) < 3:
        for section in sections:
            label = format_section_path(section.get("path", []), max_depth=3)
            summary = summarize_section_content(section, max_len=160)
            for candidate in (label, summary):
                normalized = normalize_display_text(candidate)
                if (
                    not normalized
                    or is_auxiliary_section(normalized)
                    or contains_any(normalized, LOW_SIGNAL_SECTION_TOKENS)
                ):
                    continue
                add_keywords(normalized)
                if len(keywords) >= max_terms:
                    break
            if len(keywords) >= max_terms:
                break

    return keywords[:max_terms]


def score_text_against_keywords(text: str, keywords: list[str]) -> int:
    normalized = normalize_display_text(text).lower()
    if not normalized or not keywords:
        return 0

    score = 0
    for keyword in keywords:
        if keyword not in normalized:
            continue
        score += 10 if len(keyword) <= 3 else 18 if len(keyword) <= 5 else 26
        if normalized.startswith(keyword):
            score += 4
        if f" {keyword} " in f" {normalized} ":
            score += 2
    return score


def score_section_for_title(section: dict[str, object], title_keywords: list[str]) -> int:
    label = format_section_path(section.get("path", []), max_depth=3) or clean_section_label(str(section.get("heading", "")))
    summary = summarize_section_content(section, max_len=220)
    level = int(section.get("level") or 9)
    score = score_text_against_keywords(" ".join(part for part in (label, summary) if part), title_keywords)
    score += {1: 16, 2: 12, 3: 7, 4: 3}.get(level, 0)
    score += min(len(section.get("paragraphs", [])), 3) * 2
    score += min(len(section.get("code_blocks", [])), 4) * 5
    if is_generic_label(label):
        score -= 10
    if is_auxiliary_section(label):
        score -= 120
    return score


def score_code_block_for_title(block: dict[str, object], title_keywords: list[str]) -> int:
    if not title_keywords:
        return 0
    body = str(block["body"])
    heading = normalize_display_text(str(block.get("heading", "")))
    snippet = "\n".join(body.splitlines()[:40])
    return score_text_against_keywords(" ".join(part for part in (heading, snippet) if part), title_keywords)


def score_code_block_for_track(
    block: dict[str, object],
    research_tab: str,
    title_keywords: list[str] | None = None,
) -> int:
    title_keywords = title_keywords or []
    body = str(block["body"])
    lower = body.lower()
    heading = normalize_display_text(str(block.get("heading", ""))).lower()
    combined = f"{heading}\n{lower}"
    score = score_code_block(block) + score_code_block_for_title(block, title_keywords)

    if research_tab == "ML":
        stage = get_ml_stage(block)
        if stage in {"modeling", "training", "evaluation"}:
            score += 18
        elif stage in {"preprocessing", "feature_engineering"}:
            score += 12
        elif stage == "data_load":
            score += 4
        elif stage == "setup":
            score -= 28
    elif research_tab == "DL":
        if contains_any(combined, DL_PRIORITY_CODE_TOKENS):
            score += 34
        if contains_any(combined, LOW_SIGNAL_SECTION_TOKENS) or contains_any(combined, EDA_SECTION_TOKENS):
            score -= 24
    elif research_tab == "LLM":
        if contains_any(combined, LLM_PRIORITY_CODE_TOKENS):
            score += 38
        if contains_any(combined, LOW_SIGNAL_SECTION_TOKENS) or contains_any(combined, EDA_SECTION_TOKENS):
            score -= 28

    return score


def summarize_section_content(section: dict[str, object], max_len: int = 200) -> str:
    collected: list[str] = []
    for paragraph in section.get("paragraphs", []):
        normalized = normalize_display_text(str(paragraph))
        normalized = re.sub(r"[\U00010000-\U0010ffff]", "", normalized)
        normalized = re.sub(r"[📌🎯🚲🏦🪛📑🧪✅⭐✨🔥🔍📊📈📉🛠️]", "", normalized)
        normalized = compact_spaces(normalized.strip(" -"))
        if len(normalized) < 8:
            continue
        collected.append(normalized)
        if len(collected) >= 2:
            break
    if not collected:
        return ""
    return trim_text(compact_spaces(" ".join(collected)), max_len)


ML_LOW_PRIORITY_ROOT_TOKENS = (
    "추가할 사항",
    "결론",
    "강사 tip",
    "1차 데이터 확인",
    "데이터 설명",
    "공식",
)


def build_ml_section_corpus(section: dict[str, object]) -> str:
    paragraphs = [normalize_display_text(str(paragraph)) for paragraph in section.get("paragraphs", [])[:4]]
    code_bodies = [str(block["body"]) for block in section.get("code_blocks", [])[:4]]
    return "\n".join(part for part in paragraphs + code_bodies if part)


def is_low_signal_ml_summary(text: str) -> bool:
    normalized = normalize_display_text(text)
    if len(normalized) < 18:
        return True
    low_signal_phrases = (
        "같은 코드를 직접 따라가며",
        "흐름을 확인했습니다",
        "아래 코드와 함께 읽으면",
        "이 장의 설명을 먼저 읽고",
        "구현 의도가 더 잘 보이는 구간",
    )
    return any(phrase in normalized for phrase in low_signal_phrases)


def build_ml_rule_summary(section: dict[str, object]) -> str:
    label = format_section_path(section.get("path", []), max_depth=3)
    normalized_label = normalize_display_text(label).lower()
    corpus = build_ml_section_corpus(section)
    lower = corpus.lower()

    if "미션 설명" in normalized_label:
        return "문제 목표, 예측 대상, 평가 기준을 먼저 잡고 이번 실습의 방향을 정리하는 도입부입니다."
    if "데이터 설명" in normalized_label or "파일 설명" in normalized_label or normalized_label == "데이터":
        return "사용할 데이터셋의 컬럼 의미와 타깃 변수를 정리해 이후 전처리와 모델링 판단 기준을 세우는 구간입니다."
    if "강사 tip" in normalized_label:
        return "비즈니스 상황에 따라 Precision, Recall 같은 어떤 평가 기준을 우선할지 정리하는 해설 구간입니다."
    if "추가할 사항" in normalized_label:
        return "모델 결과를 KPI와 마케팅 전략으로 연결할 때 어떤 비즈니스 지표를 설계할지 정리한 보충 메모입니다."
    if "결론" in normalized_label:
        return "실험 결과를 비교해 어떤 전처리와 모델 조합이 가장 적합했는지 정리하는 마무리 구간입니다."
    if "1차 데이터 확인" in normalized_label and any(token in lower for token in ("campaign", "pdays", "previous", "value_counts", "describe", "unknown")):
        return "타깃 불균형, campaign 이상치, pdays=999 같은 주의 지점을 먼저 확인해 이후 전처리 방향을 정하는 단계입니다."
    if "특정 컬럼 데이터 확인" in normalized_label and any(token in lower for token in ("duration", "pdays", "previous")):
        return "duration, pdays, previous처럼 예측력은 크지만 해석상 주의가 필요한 컬럼을 따로 점검하는 단계입니다."
    if "데이터 확인" in normalized_label and any(token in lower for token in (".head(", ".info(", ".describe(", ".shape", "value_counts", "histplot", "boxplot")):
        return "컬럼 구조와 분포를 먼저 점검해 어떤 변수와 이상치를 주의해서 볼지 정리하는 단계입니다."
    if "데이터 시각화" in normalized_label and any(token in lower for token in ("plt.", "sns.", "histplot", "boxplot", "barplot", "heatmap", "countplot")):
        return "주요 변수와 타깃 분포를 그래프로 확인해 어떤 가설과 파생 변수를 세울지 판단하는 단계입니다."
    if "결측치 확인" in normalized_label and "isnull" in lower:
        return "결측치가 실제로 존재하는지 먼저 확인하고 이후 처리 방식을 정하는 점검 단계입니다."
    if "종속변수 이진 변환" in normalized_label and any(token in lower for token in ("yes", "no", "lambda", "map(", "labelencoder", "astype")):
        return "yes/no 타깃 값을 0/1로 바꿔 분류 모델이 바로 학습할 수 있는 형태로 맞추는 단계입니다."
    if "datetime" in normalized_label or ("pd.to_datetime" in lower and ".dt." in lower):
        return "datetime 컬럼을 파싱하고 hour, month, year, weekday 같은 시간 파생 변수를 만드는 단계입니다."
    if "로그 변환" in normalized_label or "log_count" in lower or "np.log1p" in lower:
        return "타깃 값을 로그 스케일로 바꿔 RMSLE 기준에 맞는 회귀 목표로 정리하는 단계입니다."
    if "season" in normalized_label and ("month" in lower or "redefine_season" in lower):
        return "month 값을 기준으로 season을 다시 매핑해 실제 계절 정보와 맞추는 전처리입니다."
    if "duration 컬럼" in normalized_label and "duration" in lower:
        return "duration이 타깃을 과하게 설명할 수 있는 변수인지 확인하고, 모델 입력에서 제외할지 판단하는 단계입니다."
    if "windspeed 조사" in normalized_label and "windspeed" in lower:
        return "windspeed 극단값이 실제 가능한 범위인지 확인하고 제거 또는 변환 기준을 세우는 조사 단계입니다."
    if "humidity 조사" in normalized_label and "humidity" in lower:
        return "humidity 0/100 구간과 대여량 관계를 확인해 이상치로 볼지 유지할지 판단하는 조사 단계입니다."
    if "이상치" in normalized_label and "windspeed" in lower:
        return "windspeed 분포와 극단값을 확인해 제거 또는 변환 여부를 판단하는 단계입니다."
    if "이상치" in normalized_label and "campaign" in lower:
        return "campaign 분포를 확인해 극단값을 바로 제거할지, 로그 스케일로 볼지 판단하는 단계입니다."
    if "중복값" in normalized_label and "duplicated" in lower:
        return "중복 행을 확인하고 제거해 학습 데이터 품질을 먼저 정리하는 단계입니다."
    if "범주형 변수 처리" in normalized_label and "labelencoder" in lower:
        if "unknown" in lower:
            return "unknown 값을 따로 두고 나머지 범주형 컬럼을 라벨 인코딩하는 전처리 단계입니다."
        return "범주형 컬럼을 숫자로 바꿔 트리 기반 모델이 학습할 수 있도록 입력 형식을 정리하는 단계입니다."
    if "파생변수 추가" in normalized_label and any(token in lower for token in ("is_rush_hour", "is_morning", "is_night", "is_workhour", "is_weekend")):
        return "시간대와 운영 패턴을 반영한 파생 변수를 추가해 자전거 수요나 행동 패턴을 더 잘 설명하도록 만드는 단계입니다."
    if "파생변수 추가" in normalized_label and any(token in lower for token in ("was_contacted_before", "had_prev_success", "is_target_", "few_contacts", "low_euribor3m", "neg_emp_var_rate")):
        return "고객/캠페인/경제지표 정보를 묶은 파생 변수를 추가해 가입 가능성이 높은 구간을 더 잘 구분하려는 단계입니다."
    if "파생변수 추가" in normalized_label and any(token in lower for token in ("humidity_ideal", "weather_ideal", "humidity_bin")):
        return "날씨와 습도 조건을 구간화해 대여량 또는 가입 패턴을 더 잘 설명하는 파생 변수를 만드는 단계입니다."
    if "파생변수 추가" in normalized_label and any(token in lower for token in ("is_", "map(", "pd.cut(", "between(", "isin(")):
        return "도메인 규칙을 반영한 새 컬럼을 추가해 모델이 중요한 패턴을 더 잘 잡도록 만드는 단계입니다."
    if any(token in normalized_label for token in ("unknown", "pdays")) and any(token in lower for token in ("unknown", "pdays", "999")):
        return "unknown과 pdays=999를 결측 또는 미접촉 신호로 보고 별도 처리 전략을 세우는 단계입니다."
    if "smote" in normalized_label or "smote(" in lower:
        return "훈련 데이터에만 SMOTE를 적용해 클래스 불균형을 완화하고 데이터 누수를 피하는 모델링 단계입니다."
    if "stratify" in normalized_label and "train_test_split" in lower:
        return "불균형 데이터에서 train/test를 나눌 때 타깃 비율이 유지되도록 stratify를 적용하는 단계입니다."
    if any(token in normalized_label for token in ("1차 모델링", "2차 모델링", "3차 모델링", "4차 모델링", "5차 모델링", "6차 모델링")):
        if any(token in lower for token in ("xgbregressor", "xgbclassifier", "xgboost")):
            return "XGBoost를 최종 후보로 올려 기존 모델 대비 성능 개선 여부를 확인하는 모델링 단계입니다."
        if "smote(" in lower:
            return "SMOTE로 불균형 데이터를 보정한 뒤 모델별 Precision, Recall, F1 변화를 비교하는 단계입니다."
        if "gridsearchcv" in lower or "param_grids" in lower:
            return "하이퍼파라미터를 조정하며 여러 회귀 모델의 성능 차이를 비교하는 모델링 단계입니다."
        if any(token in lower for token in ("humidity_ideal", "weather_ideal", "humidity_bin", "windspeed_z")):
            return "새 파생 변수나 변환된 입력을 추가해 이전 모델보다 성능이 나아지는지 다시 확인하는 단계입니다."
        if any(token in lower for token in ("scale_pos_weight", "had_prev_success", "is_target_age", "few_contacts")):
            return "불균형 비율과 도메인 파생 변수를 반영해 정기 예금 가입 분류 성능을 끌어올리는 모델링 단계입니다."
        if any(token in lower for token in ("polynomialfeatures", "linearregression", "ridge", "lasso", "elasticnet")):
            return "기본 회귀 모델과 다항 회귀를 비교해 첫 베이스라인을 만들고 이후 개선 방향을 찾는 단계입니다."
    if "결과 저장" in normalized_label or "submission" in lower or "to_csv(" in lower:
        return "최종 모델로 test 데이터를 예측하고 제출용 CSV를 저장하는 마무리 단계입니다."
    if "데이터 전처리" in normalized_label:
        return "결측치, 인코딩, 이상치, 파생 변수처럼 모델 입력을 정리하는 전처리 과정을 모아 둔 장입니다."
    if "xgboost 회귀" in normalized_label:
        dataset = "California Housing 데이터를" if "fetch_california_housing" in lower else "회귀 데이터를"
        metric = "RMSE" if "mean_squared_error" in lower or "rmse" in lower else "회귀 지표"
        return f"{dataset} train/test로 나누고 XGBRegressor를 학습한 뒤 {metric}로 성능을 확인하는 실습입니다."
    if "xgboost 분류" in normalized_label:
        dataset = "Iris 데이터를" if "load_iris" in lower else "분류 데이터를"
        metric = "Accuracy" if "accuracy_score" in lower else "분류 지표"
        return f"{dataset} train/test로 나누고 XGBClassifier를 학습한 뒤 {metric}로 성능을 확인하는 실습입니다."
    if "모델링" in normalized_label and "gridsearchcv" in lower:
        return "여러 모델과 하이퍼파라미터를 바꿔가며 성능이 가장 좋은 조합을 찾는 모델링 단계입니다."
    if "모델링" in normalized_label and any(token in lower for token in ("decisiontree", "randomforest", "xgb", "lightgbm", "catboost")):
        return "Decision Tree, RandomForest, XGBoost 같은 후보를 비교하며 성능과 지표 변화를 확인하는 모델링 단계입니다."
    if "모델링" in normalized_label:
        return "여러 모델과 파라미터를 바꿔가며 가장 성능이 좋은 조합을 찾는 단계입니다."
    return ""


def get_ml_section_summary(section: dict[str, object], max_len: int = 190) -> str:
    direct_summary = summarize_section_content(section, max_len=max_len)
    rule_summary = build_ml_rule_summary(section)
    label = format_section_path(section.get("path", []), max_depth=3).lower()
    rule_priority_tokens = (
        "결측치 확인",
        "datetime",
        "season",
        "이상치",
        "duration 컬럼",
        "범주형 변수 처리",
        "파생변수 추가",
        "unknown",
        "pdays",
        "smote",
        "결과 저장",
    )

    if rule_summary and (
        not direct_summary
        or is_low_signal_ml_summary(direct_summary)
        or any(token in label for token in rule_priority_tokens)
    ):
        return trim_text(rule_summary, max_len)
    if direct_summary:
        return direct_summary
    if rule_summary:
        return trim_text(rule_summary, max_len)
    return ""


def score_ml_source_section(section: dict[str, object], title_keywords: list[str] | None = None) -> int:
    title_keywords = title_keywords or []
    label = format_section_path(section.get("path", []), max_depth=3).lower()
    level = int(section.get("level") or 9)
    score = {1: 40, 2: 30, 3: 18, 4: 10}.get(level, 0)
    score += score_text_against_keywords(label, title_keywords)
    score += score_text_against_keywords(get_ml_section_summary(section, max_len=160), title_keywords)

    if "미션 설명" in label:
        score += 42
    elif "데이터 설명" in label or label == "데이터":
        score += 48
    elif "강사 tip" in label or "1차 데이터 확인" in label:
        score += 28
    elif any(token in label for token in ("전처리", "결측치", "이상치", "파생변수", "범주형 변수")):
        score += 86
    elif any(token in label for token in ("모델", "학습", "평가", "튜닝")):
        score += 94
    elif any(token in label for token in ("해석", "가설", "컬럼", "데이터 확인")):
        score += 22

    if any(token in label for token in ML_LOW_PRIORITY_ROOT_TOKENS):
        score -= 110
    if "결론" in label and len(section.get("code_blocks", [])) == 0:
        score -= 35

    if "공식" in label:
        score -= 40

    score += min(len(section.get("paragraphs", [])), 4)
    score += min(len(section.get("code_blocks", [])), 6)

    if is_auxiliary_section(label):
        score -= 120
    return score


def describe_ml_source_section(section: dict[str, object]) -> str:
    label = format_section_path(section.get("path", []), max_depth=3).lower()
    readable_label = format_section_path(section.get("path", []), max_depth=2) or clean_section_label(str(section.get("heading", "")))
    rule_summary = build_ml_rule_summary(section)
    if rule_summary:
        return rule_summary
    if "데이터 설명" in label or (("데이터" in label or "컬럼" in label) and "전처리" not in label):
        return "데이터 구조와 주의할 변수부터 읽고 실험 방향을 정리하는 구간입니다."
    if "강사 tip" in label or "1차 데이터 확인" in label or "해석" in label or "가설" in label:
        return "EDA 결과를 해석하고 다음 전처리나 모델링 판단으로 이어지는 구간입니다."
    if any(token in label for token in ("전처리", "결측치", "이상치", "파생변수", "범주형 변수", "중복값")):
        return "모델 입력을 만들기 위해 데이터를 실제로 가공하는 구간입니다."
    if any(token in label for token in ("모델", "학습", "튜닝", "gridsearch", "교차검증")):
        return "비교할 모델과 학습 조건을 세우고 성능을 시험하는 구간입니다."
    if any(token in label for token in ("평가", "결과")):
        return "지표와 결과를 바탕으로 어떤 선택이 맞았는지 정리하는 구간입니다."
    if "미션 설명" in label:
        return "문제 정의, 목표, 평가 기준을 먼저 잡는 구간입니다."
    if section.get("code_blocks"):
        return f"{readable_label} 아래 코드와 함께 읽으면 구현 의도가 더 잘 보이는 구간입니다."
    if any(token in readable_label for token in ("기초", "응용", "심화", "문제", "실습")):
        return f"{readable_label} 아래 세부 항목들을 묶어 보는 구간입니다."
    return f"{readable_label} 아래에 이어질 세부 설명과 코드를 읽기 전 흐름을 잡는 구간입니다."


def build_ml_code_focus_items(section: dict[str, object], limit: int = 3) -> list[dict[str, object]]:
    section_label = clean_section_label(str(section.get("heading", "")))
    items: list[dict[str, object]] = []
    seen: set[str] = set()
    ranked_blocks = sorted(
        [
            block
            for block in section.get("code_blocks", [])
            if get_code_lines(str(block["body"]))
        ],
        key=lambda block: (
            1 if get_ml_stage(block) in {"setup", "other"} else 0,
            -score_ml_block_for_stage(block, get_ml_stage(block)),
        ),
    )

    for block in ranked_blocks:
        comment_clues = extract_comment_clues(str(block["body"]), limit=2)
        label = ""
        for clue in comment_clues:
            normalized_clue = normalize_display_text(clue)
            if not normalized_clue:
                continue
            if section_label and normalized_clue.lower() == section_label.lower():
                continue
            label = normalized_clue
            break

        if not label:
            label = normalize_display_text(get_code_label(block, "ML"))
        if section_label and label and label.lower() == section_label.lower():
            continue
        if not label:
            continue
        label_key = label.lower()
        if label_key in seen:
            continue
        seen.add(label_key)
        summary = infer_ml_code_purpose(block)
        if summary == "원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.":
            summary = f"{trim_text(label, 36)} 코드를 직접 실행하며 {section_label or '이 장'} 흐름을 익혔습니다."
        items.append(
            {
                "label": trim_text(label, 46),
                "summary": summary,
                "code_blocks": [block],
            }
        )
        if len(items) >= limit:
            break

    return items


def build_ml_root_summary(
    *,
    root_label: str,
    root_section: dict[str, object],
    child_items: list[dict[str, str]],
) -> str:
    direct_summary = get_ml_section_summary(root_section, max_len=190)
    if direct_summary:
        return direct_summary

    code_labels = [item["label"] for item in child_items if item.get("label")]
    if code_labels:
        return f"{format_korean_list(code_labels, limit=3, max_item_len=22)} 같은 코드를 직접 따라가며 {root_label} 흐름을 확인했습니다."

    child_summaries = [item["summary"] for item in child_items if item.get("summary")]
    if child_summaries:
        combined = " ".join(child_summaries[:2])
        return trim_text(compact_spaces(combined), 190)

    root_blocks = list(root_section.get("code_blocks", []))
    if root_blocks:
        block_labels = unique_preserve_order([get_code_label(block, "ML") for block in root_blocks])[:2]
        if block_labels:
            return f"{format_korean_list(block_labels, limit=2, max_item_len=24)} 코드를 직접 따라가며 {root_label} 구현 흐름을 확인했습니다."
        return f"{root_label}에서는 {infer_ml_code_purpose(root_blocks[0])}"

    return f"{root_label}와 관련된 핵심 흐름을 원본 노트 기준으로 다시 읽을 수 있게 정리했습니다."


def build_ml_outline_labels(sections: list[dict[str, object]], limit: int = 5) -> list[str]:
    labels: list[str] = []
    for section in sections:
        path = [clean_section_label(item) for item in section.get("path", []) if clean_section_label(item)]
        if len(path) != 1:
            continue
        label = path[0]
        if not label or is_auxiliary_section(label) or is_generic_label(label):
            continue
        labels.append(label)
    if labels:
        return unique_cleaned_items(labels, limit=limit)

    fallback: list[str] = []
    for section in sections:
        label = format_section_path(section.get("path", []), max_depth=2)
        if not label or is_auxiliary_section(label):
            continue
        fallback.append(label)
    return unique_cleaned_items(fallback, limit=limit)


def score_ml_summary_label(label: str) -> int:
    normalized = normalize_display_text(label).lower()
    score = 0
    if any(token in normalized for token in ("모델링", "학습", "평가")):
        score += 120
    if any(token in normalized for token in ("전처리", "파생변수", "결과 저장")):
        score += 100
    if "시각화" in normalized:
        score += 70
    if any(token in normalized for token in ("데이터 확인", "데이터")):
        score += 45
    if "미션 설명" in normalized:
        score += 28
    if "분석 드릴다운" in normalized:
        score -= 25
    if any(token in normalized for token in ML_LOW_PRIORITY_ROOT_TOKENS):
        score -= 90
    return score


def choose_ml_summary_labels(study_notes: list[dict[str, object]], limit: int = 3) -> list[str]:
    ranked = sorted(
        (
            (score_ml_summary_label(str(note.get("label", ""))), index, str(note.get("label", "")))
            for index, note in enumerate(study_notes)
            if normalize_display_text(str(note.get("label", "")))
        ),
        key=lambda item: (-item[0], item[1]),
    )
    labels = [label for _, _, label in ranked]
    return unique_cleaned_items(labels, limit=limit)


def is_topic_sparse_title(title: str) -> bool:
    return len(extract_title_keywords(title, max_terms=4)) <= 1


def score_section_for_track(
    section: dict[str, object],
    research_tab: str,
    title_keywords: list[str] | None = None,
) -> int:
    title_keywords = title_keywords or []
    if research_tab == "ML":
        return score_ml_source_section(section, title_keywords=title_keywords)

    label = format_section_path(section.get("path", []), max_depth=3)
    summary = summarize_section_content(section, max_len=180)
    combined = " ".join(part for part in (label, summary) if part)
    score = score_section_for_title(section, title_keywords)

    if research_tab == "DL" and contains_any(combined, DL_PRIORITY_SECTION_TOKENS):
        score += 78
    if research_tab == "LLM" and contains_any(combined, LLM_PRIORITY_SECTION_TOKENS):
        score += 82
    if contains_any(combined, EDA_SECTION_TOKENS):
        score -= 48
    if contains_any(combined, LOW_SIGNAL_SECTION_TOKENS):
        score -= 130
    if int(section.get("level") or 9) == 1 and len(section.get("code_blocks", [])) >= 2:
        score += 12
    return score


def describe_track_source_section(section: dict[str, object], research_tab: str) -> str:
    label = format_section_path(section.get("path", []), max_depth=3).lower()
    readable_label = format_section_path(section.get("path", []), max_depth=2) or clean_section_label(str(section.get("heading", "")))

    if research_tab == "LLM":
        if contains_any(label, ("rag", "retriever", "vectorstore")):
            return "검색과 컨텍스트 주입 단계를 실제 코드로 묶어 보는 구간입니다."
        if contains_any(label, ("전처리", "token", "clean")):
            return "텍스트 정제와 토큰 구성을 바꾸며 입력 품질을 비교하는 구간입니다."
        if contains_any(label, ("임베딩", "lstm", "gru", "모델", "학습")):
            return "임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다."
        if contains_any(label, ("실험", "평가", "결과", "추가 실험")):
            return "실험 조건을 바꾸고 지표를 비교하며 어떤 설정이 맞는지 확인하는 구간입니다."
        if contains_any(label, EDA_SECTION_TOKENS):
            return "데이터 상태를 점검한 뒤 다음 전처리와 학습 단계로 넘어가기 위한 구간입니다."

    if research_tab == "DL":
        if contains_any(label, ("segmentation", "unet", "mask r-cnn", "fasterrcnn", "yolo", "detection")):
            return "비전 모델이 객체나 픽셀 단위를 어떻게 예측하는지 구현으로 따라가는 구간입니다."
        if contains_any(label, ("모델", "학습", "loss", "optimizer", "전이학습")):
            return "모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다."
        if contains_any(label, ("dataset", "dataloader", "augmentation", "전처리")):
            return "이미지 입력을 배치로 묶고 증강하며 학습 가능한 형태로 만드는 구간입니다."
        if contains_any(label, ("평가", "추론", "결과")):
            return "예측 결과를 확인하고 어떤 부분이 잘 동작했는지 해석하는 구간입니다."

    if section.get("code_blocks"):
        return f"{readable_label} 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다."
    return f"{readable_label}에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다."


def build_track_code_focus_items(
    section: dict[str, object],
    research_tab: str,
    limit: int = 3,
) -> list[dict[str, str]]:
    section_label = clean_section_label(str(section.get("heading", "")))
    items: list[dict[str, str]] = []
    seen: set[str] = set()

    ranked_blocks = sorted(
        section.get("code_blocks", []),
        key=lambda block: -score_code_block_for_track(block, research_tab, []),
    )

    for block in ranked_blocks:
        label = normalize_display_text(get_code_label(block, research_tab))
        if not label or (section_label and label.lower() == section_label.lower()):
            continue
        label_key = label.lower()
        if label_key in seen:
            continue
        seen.add(label_key)
        summary = infer_ml_code_purpose(block) if research_tab == "ML" else describe_code_block(block, research_tab)
        items.append(
            {
                "label": trim_text(label, 46),
                "summary": trim_text(normalize_display_text(summary), 160),
            }
        )
        if len(items) >= limit:
            break

    return items


def build_track_root_summary(
    *,
    root_label: str,
    root_section: dict[str, object],
    child_items: list[dict[str, str]],
    research_tab: str,
) -> str:
    direct_summary = summarize_section_content(root_section, max_len=190)
    if direct_summary:
        return direct_summary

    code_labels = [item["label"] for item in child_items if item.get("label")]
    if code_labels:
        return f"{format_korean_list(code_labels, limit=3, max_item_len=22)} 같은 코드를 직접 따라가며 {root_label} 흐름을 확인했습니다."

    child_summaries = [item["summary"] for item in child_items if item.get("summary")]
    if child_summaries:
        return trim_text(compact_spaces(" ".join(child_summaries[:2])), 190)

    root_blocks = list(root_section.get("code_blocks", []))
    if root_blocks:
        block_labels = unique_preserve_order([get_code_label(block, research_tab) for block in root_blocks])[:2]
        if block_labels:
            return f"{format_korean_list(block_labels, limit=2, max_item_len=24)} 코드를 직접 따라가며 {root_label} 흐름을 확인했습니다."
        return trim_text(normalize_display_text(describe_code_block(root_blocks[0], research_tab)), 190)

    return describe_track_source_section(root_section, research_tab)


def build_track_source_notes(
    research_tab: str,
    sections: list[dict[str, object]],
    title_keywords: list[str] | None = None,
    limit: int = 6,
) -> list[dict[str, object]]:
    title_keywords = title_keywords or []
    grouped: dict[str, dict[str, object]] = {}

    for index, section in enumerate(sections):
        path = [clean_section_label(item) for item in section.get("path", []) if clean_section_label(item)]
        if not path:
            continue

        root = path[0]
        if not root or is_auxiliary_section(root) or is_generic_label(root):
            continue

        entry = grouped.get(root)
        if entry is None:
            entry = {
                "root": root,
                "index": index,
                "root_section": section,
                "summary": "",
                "summary_score": -10_000,
                "practice": "",
                "children": [],
            }
            grouped[root] = entry

        score = score_section_for_track(section, research_tab, title_keywords=title_keywords)
        summary = summarize_section_content(section, max_len=190)
        if not summary:
            code_focus = build_track_code_focus_items(section, research_tab, limit=1)
            if code_focus:
                summary = code_focus[0]["summary"]

        if len(path) == 1 and summary and score > int(entry["summary_score"]):
            entry["summary"] = summary
            entry["summary_score"] = score
            entry["practice"] = describe_track_source_section(section, research_tab)

        if len(path) >= 2:
            child_label = format_section_path(path[1:], max_depth=2)
            child_summary = summarize_section_content(section, max_len=160)
            if not child_summary:
                code_focus = build_track_code_focus_items(section, research_tab, limit=1)
                if code_focus:
                    child_summary = code_focus[0]["summary"]

            existing_labels = {str(item["label"]).lower() for item in entry["children"]}
            if child_label and child_label.lower() not in existing_labels and not is_auxiliary_section(child_label):
                entry["children"].append(
                    {
                        "index": index,
                        "label": child_label,
                        "summary": child_summary or describe_track_source_section(section, research_tab),
                        "score": score,
                    }
                )

    notes: list[dict[str, object]] = []
    ranked_entries = sorted(
        grouped.values(),
        key=lambda entry: (-int(entry["summary_score"]), int(entry["index"])),
    )[:limit]

    preferred_entries = [
        entry
        for entry in ranked_entries
        if normalize_display_text(str(entry["root"])).lower() not in {"미션 설명", "데이터", "분석 드릴다운", "데이터 확인", "eda"}
    ]
    if len(preferred_entries) >= min(4, limit):
        ranked_entries = preferred_entries[:limit]

    for entry in ranked_entries:
        root = str(entry["root"])
        root_section = entry["root_section"]
        child_items = list(entry["children"])

        if not child_items:
            child_items = build_track_code_focus_items(root_section, research_tab, limit=3)
        else:
            child_items.sort(key=lambda item: -int(item.get("score", 0)))
            child_items = child_items[:3]
            child_items.sort(key=lambda item: int(item.get("index", 0)))

        summary = str(entry["summary"]).strip()
        if not summary:
            summary = build_track_root_summary(
                root_label=root,
                root_section=root_section,
                child_items=child_items,
                research_tab=research_tab,
            )

        if child_items:
            child_labels = [str(item["label"]) for item in child_items if item.get("label")]
            practice = f"세부 흐름: {', '.join(child_labels[:3])}"
        else:
            practice = str(entry["practice"]) or describe_track_source_section(root_section, research_tab)

        notes.append(
            {
                "label": root,
                "summary": summary,
                "practice": practice,
                "children": child_items,
            }
        )

    return notes


def build_track_source_section(
    *,
    study_notes: list[dict[str, object]],
) -> str:
    sections: list[str] = []
    for note in study_notes:
        sections.append(
            "\n".join(
                [
                    f"### {note['label']}",
                    "",
                    note["summary"],
                    "",
                    f"- 읽을 포인트: {note['practice']}",
                ]
            )
        )
        for child in note.get("children", [])[:3]:
            child_label = normalize_display_text(str(child.get("label", "")))
            child_summary = normalize_display_text(str(child.get("summary", "")))
            if not child_label or not child_summary:
                continue
            sections.append(
                "\n".join(
                    [
                        f"#### {child_label}",
                        "",
                        child_summary,
                    ]
                )
            )
    return "\n\n".join(sections)


def build_track_flow_items_from_source_notes(
    study_notes: list[dict[str, object]],
    limit: int = 6,
) -> list[str]:
    items: list[str] = []
    for note in study_notes:
        child_labels = [normalize_display_text(str(item.get("label", ""))) for item in note.get("children", []) if item.get("label")]
        if child_labels:
            items.append(trim_text(f"{note['label']}: {', '.join(child_labels[:2])}", 150))
        elif note.get("summary"):
            items.append(trim_text(f"{note['label']}: {note['summary']}", 150))
        if len(items) >= limit:
            break
    return items[:limit]


def build_track_research_summary(
    *,
    title: str,
    track: str,
    study_notes: list[dict[str, object]],
    code_samples: list[dict[str, object]],
    artifact_summary: str,
) -> str:
    cleaned_title = normalize_display_text(title)
    section_labels = [normalize_display_text(str(note["label"])) for note in study_notes[:3] if note.get("label")]
    code_labels = unique_preserve_order([get_code_label(block, track) for block in code_samples])[:3]

    subject = cleaned_title
    if is_topic_sparse_title(cleaned_title) and section_labels:
        subject = f"{format_korean_list(section_labels[:2], limit=2, max_item_len=22)} 중심의 {track} 실험"

    lead = f"{subject}에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 {track} 학습 기록입니다"
    if section_labels:
        detail = f"본문은 {format_korean_list(section_labels, limit=3, max_item_len=22)} 순서로 핵심 장면을 먼저 훑고"
    else:
        detail = "본문은 실험의 큰 흐름을 먼저 훑고"
    if code_labels:
        detail += f", {format_korean_list(code_labels, limit=3, max_item_len=24)} 같은 코드로 실제 구현을 이어서 확인할 수 있습니다"
    else:
        detail += ", 아래 코드 블록에서 실제 구현 장면을 바로 확인할 수 있습니다"

    return " ".join(
        part
        for part in (
            ensure_sentence(lead),
            ensure_sentence(detail),
            artifact_summary,
        )
        if part
    )


def build_ml_source_notes(
    sections: list[dict[str, object]],
    title_keywords: list[str] | None = None,
    limit: int = 8,
) -> list[dict[str, object]]:
    title_keywords = title_keywords or []
    grouped: dict[str, dict[str, object]] = {}

    for index, section in enumerate(sections):
        path = [clean_section_label(item) for item in section.get("path", []) if clean_section_label(item)]
        if not path:
            continue

        root = path[0]
        if not root or is_auxiliary_section(root) or is_generic_label(root):
            continue

        entry = grouped.get(root)
        if entry is None:
            entry = {
                "root": root,
                "index": index,
                "root_section": section,
                "summary": "",
                "summary_score": -10_000,
                "practice": "",
                "children": [],
            }
            grouped[root] = entry

        level = int(section.get("level") or 9)
        summary = get_ml_section_summary(section, max_len=190)
        score = score_ml_source_section(section, title_keywords=title_keywords) + (30 if level == 1 else 0)
        if len(path) == 1 and summary and score > int(entry["summary_score"]):
            entry["summary"] = summary
            entry["summary_score"] = score
            entry["practice"] = describe_ml_source_section(section)

        if len(path) >= 2:
            child_label = format_section_path(path[1:], max_depth=2)
            child_summary = get_ml_section_summary(section, max_len=160)
            if not child_summary:
                code_focus = build_ml_code_focus_items(section, limit=1)
                if code_focus:
                    child_summary = code_focus[0]["summary"]

            existing_labels = {str(item["label"]).lower() for item in entry["children"]}
            if child_label and child_label.lower() not in existing_labels and not is_auxiliary_section(child_label):
                selected_child_blocks = select_ml_code_blocks(
                    list(section.get("code_blocks", [])),
                    limit=1,
                    title_keywords=title_keywords,
                )
                entry["children"].append(
                    {
                        "index": index,
                        "label": child_label,
                        "summary": child_summary or describe_ml_source_section(section),
                        "score": score_ml_source_section(section, title_keywords=title_keywords),
                        "code_blocks": selected_child_blocks,
                    }
                )

    notes: list[dict[str, object]] = []
    ranked_entries = sorted(
        grouped.values(),
        key=lambda entry: (-int(entry["summary_score"]), int(entry["index"])),
    )[:limit]

    preferred_entries = [
        entry
        for entry in ranked_entries
        if not any(token in normalize_display_text(str(entry["root"])).lower() for token in ML_LOW_PRIORITY_ROOT_TOKENS)
    ]
    if preferred_entries:
        ranked_entries = preferred_entries[:limit]
    ranked_entries = sorted(ranked_entries, key=lambda entry: int(entry["index"]))

    for entry in ranked_entries:
        root = str(entry["root"])
        root_section = entry["root_section"]
        child_items = list(entry["children"])

        if not child_items:
            child_items = build_ml_code_focus_items(root_section, limit=3)
        else:
            child_items.sort(key=lambda item: -int(item.get("score", 0)))
            child_items = child_items[:4]
            child_items.sort(key=lambda item: int(item.get("index", 0)))

        summary = str(entry["summary"]).strip()
        if not summary:
            summary = build_ml_root_summary(
                root_label=root,
                root_section=root_section,
                child_items=child_items,
            )

        if child_items:
            child_labels = [str(item["label"]) for item in child_items if item.get("label")]
            practice = f"세부 흐름: {', '.join(child_labels[:3])}"
        else:
            practice = str(entry["practice"]) or "이 장의 설명을 먼저 읽고 아래 코드 섹션으로 내려가면 흐름이 더 자연스럽습니다."

        notes.append(
            {
                "label": root,
                "summary": summary,
                "practice": practice,
                "children": child_items,
                "code_blocks": select_ml_code_blocks(
                    list(root_section.get("code_blocks", [])),
                    limit=1,
                    title_keywords=title_keywords,
                ) if not child_items else [],
            }
        )

    if notes:
        return notes

    ranked: list[dict[str, object]] = []
    for index, section in enumerate(sections):
        label = format_section_path(section.get("path", []), max_depth=2)
        summary = summarize_section_content(section, max_len=190)
        if not label or not summary or is_auxiliary_section(label):
            continue
        ranked.append(
            {
                "index": index,
                "label": label,
                "summary": summary,
                "practice": describe_ml_source_section(section),
                "score": score_ml_source_section(section, title_keywords=title_keywords),
            }
        )

    ranked.sort(key=lambda item: (-int(item["score"]), int(item["index"])))
    return [
        {
            "label": str(item["label"]),
            "summary": str(item["summary"]),
            "practice": str(item["practice"]),
            "children": [],
        }
        for item in ranked[:limit]
    ]


def should_skip_focus_item(text: str) -> bool:
    normalized = normalize_display_text(text)
    if not normalized:
        return True
    return any(normalized.startswith(prefix) for prefix in LOW_SIGNAL_PREFIXES)


def parse_front_matter(path: Path) -> tuple[dict[str, object], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines

    data: dict[str, object] = {}
    current_list_key: str | None = None
    body_start = 0

    for index in range(1, len(lines)):
        stripped = lines[index].strip()
        if stripped == "---":
            body_start = index + 1
            break

        key_match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", stripped)
        if key_match and not stripped.startswith("- "):
            key = key_match.group(1)
            raw_value = key_match.group(2)
            if raw_value == "":
                data[key] = []
                current_list_key = key
            else:
                data[key] = strip_yaml_value(raw_value)
                current_list_key = None
            continue

        if current_list_key and stripped.startswith("- "):
            value = strip_yaml_value(stripped[2:])
            existing = data.get(current_list_key, [])
            if not isinstance(existing, list):
                existing = [str(existing)]
            existing.append(value)
            data[current_list_key] = existing
            continue

        current_list_key = None

    return data, lines[body_start:]


def collect_existing_title_overrides(output_dir: Path) -> dict[str, str]:
    overrides: dict[str, str] = {}
    for path in sorted(output_dir.glob("imported-*.md")):
        metadata, _ = parse_front_matter(path)
        source_path = normalize_display_text(str(metadata.get("source_path") or ""))
        title = normalize_display_text(str(metadata.get("title") or ""))
        if source_path and title:
            overrides[source_path] = title
    return overrides


def get_research_kind(name: str) -> str:
    lower_name = name.lower()
    if "스프린트" in name or "sprint" in lower_name:
        return "Sprint Mission"
    if "미션" in name or "mission" in lower_name:
        return "Mission"
    if any(keyword in name for keyword in ("실습", "코드실습", "코딩실습")):
        return "Practice"
    if any(keyword in name for keyword in ("공유", "강사공유")):
        return "Shared Note"
    if "sample" in lower_name or "샘플" in name:
        return "Sample Code"
    return "Archive Note"


def to_kebab(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "archive-note"


def get_clean_title(*candidates: str) -> str:
    for candidate in candidates:
        title = clean_markdown_text(candidate)
        if not title:
            continue
        title = re.sub(r"^\d{6,8}[_-]*", "", title)
        title = re.sub(r"^\d+-\d+\s*", "", title)
        title = re.sub(r"^\[[^\]]+\]\s*", "", title)
        title = re.sub(r"^\([^)]+\)\s*", "", title)
        title = title.replace("_", " ")
        title = compact_spaces(title)
        if title:
            return title
    return "Research Archive Note"


def parse_note_structure(lines: list[str]) -> dict[str, object]:
    headings: list[str] = []
    paragraphs: list[str] = []
    code_blocks: list[dict[str, object]] = []
    sections: list[dict[str, object]] = []

    current_heading = "Overview"
    current_level = 0
    current_path: list[str] = []
    current_paragraph: list[str] = []
    in_code_block = False
    block_info = ""
    block_heading = current_heading
    block_lines: list[str] = []
    block_has_output = False
    block_path: list[str] = []
    current_section: dict[str, object] = {
        "heading": current_heading,
        "level": current_level,
        "path": list(current_path),
        "path_text": format_section_path(current_path, max_depth=3),
        "paragraphs": [],
        "code_blocks": [],
    }
    heading_stack: list[tuple[int, str]] = []

    def section_has_content(section: dict[str, object]) -> bool:
        return bool(section["paragraphs"]) or bool(section["code_blocks"]) or normalize_display_text(str(section["heading"])) not in {"", "Overview"}

    def flush_paragraph() -> None:
        if not current_paragraph:
            return
        text = clean_markdown_text(" ".join(current_paragraph))
        current_paragraph.clear()
        if text:
            paragraphs.append(text)
            cast_paragraphs = current_section["paragraphs"]
            if isinstance(cast_paragraphs, list):
                cast_paragraphs.append(text)

    def flush_section() -> None:
        if section_has_content(current_section):
            sections.append(
                {
                    "heading": current_section["heading"],
                    "level": current_section.get("level", 0),
                    "path": list(current_section.get("path", [])),
                    "path_text": current_section.get("path_text", ""),
                    "paragraphs": list(current_section["paragraphs"]),
                    "code_blocks": list(current_section["code_blocks"]),
                }
            )

    for raw_line in lines:
        stripped = raw_line.strip()
        fence_match = CODE_FENCE_RE.match(stripped)
        if fence_match:
            if not in_code_block:
                flush_paragraph()
                in_code_block = True
                block_info = fence_match.group("info").strip()
                block_heading = current_heading
                block_path = list(current_path)
                block_lines = []
                block_has_output = any(
                    token in block_info for token in ("executionInfo=", "outputId=", "colab=")
                )
            else:
                code_blocks.append(
                    {
                        "info": block_info,
                        "lang": get_code_language(block_info),
                        "heading": block_heading,
                        "path": list(block_path),
                        "path_text": format_section_path(block_path, max_depth=3),
                        "body": "\n".join(block_lines).rstrip(),
                        "has_output": block_has_output,
                        "context": current_section["paragraphs"][-1] if current_section["paragraphs"] else "",
                    }
                )
                cast_code_blocks = current_section["code_blocks"]
                if isinstance(cast_code_blocks, list):
                    cast_code_blocks.append(code_blocks[-1])
                in_code_block = False
                block_info = ""
                block_lines = []
                block_has_output = False
                block_path = []
            continue

        if in_code_block:
            block_lines.append(raw_line.rstrip("\n"))
            continue

        if not stripped:
            flush_paragraph()
            continue

        if stripped.startswith("<!--"):
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            continue

        if re.fullmatch(r"[-\s]{3,}", stripped):
            flush_paragraph()
            continue

        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            flush_paragraph()
            flush_section()
            heading_level = len(heading_match.group(1))
            heading_text = clean_markdown_text(heading_match.group(2))
            if heading_text:
                headings.append(heading_text)
                while heading_stack and heading_stack[-1][0] >= heading_level:
                    heading_stack.pop()
                heading_stack.append((heading_level, heading_text))
                current_heading = heading_text
                current_level = heading_level
                current_path = [title for _, title in heading_stack]
                current_section = {
                    "heading": heading_text,
                    "level": current_level,
                    "path": list(current_path),
                    "path_text": format_section_path(current_path, max_depth=3),
                    "paragraphs": [],
                    "code_blocks": [],
                }
            continue

        quote_text = stripped.lstrip("> ").strip()
        if quote_text:
            current_paragraph.append(quote_text)

    flush_paragraph()
    flush_section()

    return {
        "headings": unique_preserve_order(headings),
        "paragraphs": paragraphs,
        "code_blocks": code_blocks,
        "sections": sections,
    }


def get_code_language(info: str) -> str:
    token = info.split()[0] if info else ""
    token = token.strip("{}")
    return token or "text"


def unique_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for item in items:
        normalized = item.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        unique.append(normalized)
    return unique


def trim_text(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def unique_cleaned_items(items: list[str], *, limit: int | None = None) -> list[str]:
    cleaned_items: list[str] = []
    seen: set[str] = set()
    for item in items:
        cleaned = normalize_display_text(item)
        if not cleaned:
            continue
        lower_cleaned = cleaned.lower()
        if lower_cleaned in seen:
            continue
        seen.add(lower_cleaned)
        cleaned_items.append(cleaned)
        if limit is not None and len(cleaned_items) >= limit:
            break
    return cleaned_items


def select_intro_paragraphs(
    sections: list[dict[str, object]],
    paragraphs: list[str],
    limit: int,
    title_keywords: list[str] | None = None,
) -> list[str]:
    ranked_sections: list[tuple[int, int, str]] = []
    title_keywords = title_keywords or []

    for index, section in enumerate(sections):
        summary = summarize_section_content(section, max_len=190)
        if not summary:
            continue
        label = format_section_path(section.get("path", []), max_depth=3)
        level = int(section.get("level") or 9)
        score = {1: 50, 2: 34, 3: 18, 4: 8}.get(level, 0)
        score += score_section_for_title(section, title_keywords)
        if "미션 설명" in label:
            score += 40
        if "데이터 설명" in label or label == "데이터":
            score += 26
        if is_auxiliary_section(label):
            score -= 120
        ranked_sections.append((score, index, summary))

    candidates: list[str] = []
    if ranked_sections:
        ranked_sections.sort(key=lambda item: (-item[0], item[1]))
        candidates.extend(summary for _, _, summary in ranked_sections[:limit])

    for section in sections:
        summary = summarize_section_content(section, max_len=190)
        if summary:
            candidates.append(summary)

    if not candidates:
        for paragraph in paragraphs:
            normalized = normalize_display_text(paragraph)
            if not is_meaningful_sentence(normalized):
                continue
            candidates.append(trim_text(normalized, 190))

    return unique_cleaned_items(candidates, limit=limit)


def select_focus_items(
    sections: list[dict[str, object]],
    metadata_items: list[str],
    headings: list[str],
    title: str,
    limit: int,
    title_keywords: list[str] | None = None,
) -> list[str]:
    normalized_title = normalize_display_text(title).lower()
    title_keywords = title_keywords or []
    candidates: list[tuple[int, int, str]] = []

    for index, section in enumerate(sections):
        section_score = score_section_for_title(section, title_keywords)
        for paragraph in section.get("paragraphs", []):
            normalized = normalize_display_text(str(paragraph))
            if normalized and normalized.lower() != normalized_title and is_meaningful_sentence(normalized):
                score = section_score + score_text_against_keywords(normalized, title_keywords) + 8
                candidates.append((score, index, trim_text(normalized, 150)))
                break

        heading = condense_focus_item(str(section.get("heading", "")), max_len=42)
        if heading and heading.lower() != normalized_title and not is_generic_label(heading):
            score = section_score + score_text_against_keywords(heading, title_keywords) + 6
            candidates.append((score, index, heading))

    for offset, item in enumerate(metadata_items + headings, start=len(sections)):
        normalized = condense_focus_item(item, max_len=52)
        if not normalized or normalized.lower() == normalized_title:
            continue
        if is_generic_label(normalized):
            continue
        if should_skip_focus_item(normalized):
            continue
        score = score_text_against_keywords(normalized, title_keywords)
        candidates.append((score, offset, normalized))

    candidates.sort(key=lambda item: (-item[0], item[1]))
    return unique_cleaned_items([item[2] for item in candidates], limit=limit)


def build_section_summaries(
    sections: list[dict[str, object]],
    metadata_items: list[str],
    limit: int,
    title_keywords: list[str] | None = None,
) -> list[dict[str, str]]:
    summaries: list[dict[str, str]] = []
    seen_titles: set[str] = set()
    title_keywords = title_keywords or []
    ranked_sections: list[tuple[int, int, str, str]] = []

    for index, section in enumerate(sections):
        title = format_section_path(section.get("path", []), max_depth=2)
        if not title:
            raw_title = str(section.get("heading", ""))
            title = normalize_section_title(raw_title)

        summary_text = summarize_section_content(section, max_len=220)
        if not summary_text or is_auxiliary_section(title):
            continue
        if not title:
            title = "Key Step"
        score = score_section_for_title(section, title_keywords)
        score += score_text_against_keywords(title, title_keywords)
        ranked_sections.append((score, index, title, summary_text or trim_text(title, 180)))

    ranked_sections.sort(key=lambda item: (-item[0], item[1]))
    for _, _, title, summary_text in ranked_sections:
        title_key = title.lower()
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)
        summaries.append({"title": title, "summary": summary_text})
        if len(summaries) >= limit:
            return summaries

    for item in metadata_items:
        normalized = normalize_display_text(item)
        if not normalized or is_generic_label(normalized) or not is_meaningful_sentence(normalized):
            continue
        title = trim_text(normalized, 72)
        key = title.lower()
        if key in seen_titles:
            continue
        seen_titles.add(key)
        summaries.append({"title": "Key Step", "summary": trim_text(normalized, 200)})
        if len(summaries) >= limit:
            break

    return summaries


def build_flow_items(
    section_summaries: list[dict[str, str]],
    focus_items: list[str],
    metadata_items: list[str],
    limit: int,
) -> list[str]:
    items: list[str] = []
    for entry in section_summaries:
        combined = entry["title"]
        if entry["summary"] and entry["summary"].lower() != entry["title"].lower():
            combined = f"{entry['title']}: {entry['summary']}"
        items.append(trim_text(combined, 170))

    if not items:
        items.extend(focus_items)
    if not items:
        items.extend(unique_cleaned_items(metadata_items, limit=limit))

    return unique_cleaned_items(items, limit=limit)


def build_ml_flow_items_from_code_samples(code_samples: list[dict[str, object]]) -> list[str]:
    steps: list[str] = []
    for block in code_samples:
        stage = get_code_stage_label(block, "ML")
        label = condense_focus_item(get_code_label(block, "ML"), max_len=52)
        if stage and label:
            steps.append(f"{stage}: {label}")
        elif label:
            steps.append(label)
    return unique_cleaned_items(steps, limit=6)


def build_artifact_summary(
    source_formats: list[str],
    code_block_count: int,
    execution_block_count: int,
    libraries: list[str],
) -> str:
    format_text = "/".join(source_formats) if source_formats else "원본 파일"
    library_text = format_korean_list(libraries[:4])
    summary = f"`{format_text}` 원본과 {code_block_count}개 코드 블록, {execution_block_count}개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다"
    if library_text:
        summary += f". 주요 스택은 {library_text}입니다"
    return ensure_sentence(summary)


def build_research_summary(
    title: str,
    track: str,
    kind: str,
    intro_paragraphs: list[str],
    focus_items: list[str],
    artifact_summary: str,
) -> str:
    condensed_focus = unique_cleaned_items([condense_focus_item(item, max_len=28) for item in focus_items], limit=3)
    if intro_paragraphs:
        lead = intro_paragraphs[0]
    elif condensed_focus:
        lead = f"{format_korean_list(condensed_focus, limit=3, max_item_len=28)} 중심으로 구현 과정을 정리한 {title} 기록입니다"
    else:
        lead = f"{title}에서 다룬 구현 흐름과 참고 소스를 다시 볼 수 있게 정리한 {track} 아카이브 노트입니다"

    if len(intro_paragraphs) > 1:
        detail = intro_paragraphs[1]
    elif track == "ML":
        detail = "이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다"
    elif condensed_focus:
        detail = f"페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다"
    else:
        detail = "문제 맥락과 구현 흔적을 한 화면에서 빠르게 파악할 수 있도록 핵심 정보부터 배치했습니다"

    return " ".join(
        part
        for part in (
            ensure_sentence(lead),
            ensure_sentence(detail),
            artifact_summary,
        )
        if part
    )


def build_excerpt(
    research_summary: str,
    focus_items: list[str],
    title: str,
) -> str:
    if research_summary:
        return trim_text(research_summary, 170)
    if focus_items:
        return trim_text(f"{title}: {format_korean_list(focus_items, limit=3, max_item_len=34)}", 170)
    return trim_text(f"{title} 구현 기록과 참고 소스를 함께 남긴 research note.", 170)


def score_code_block(block: dict[str, object]) -> int:
    body = str(block["body"])
    lines = [line for line in body.splitlines() if line.strip()]
    score = min(len(lines), 30)

    important_patterns = (
        r"\bclass\b",
        r"\bdef\b",
        r"\bfor epoch\b",
        r"\bDataLoader\b",
        r"\bDataset\b",
        r"\btrain\b",
        r"\bfit\b",
        r"\boptimizer\b",
        r"\btorch\b",
        r"\bsklearn\b",
        r"\btransformers\b",
    )
    for pattern in important_patterns:
        if re.search(pattern, body):
            score += 6

    if bool(block["has_output"]):
        score += 2

    if str(block["lang"]) in {"python", "bash", "sh", "sql", "yaml"}:
        score += 2

    if is_import_heavy_block(body):
        score -= 18

    if is_low_signal_code_block(body):
        score -= 26

    return score


GENERIC_ML_HEADINGS = {
    "overview",
    "archive note",
    "미션 설명",
    "파일 설명",
    "데이터 설명",
    "데이터 확인",
    "공유 시스템 이해",
    "기본 답안",
    "예시",
    "예제",
    "실습",
}

MODEL_NAME_PATTERNS = [
    ("XGBoost", ("xgbregressor", "xgbclassifier", "xgboost")),
    ("RandomForest", ("randomforestregressor", "randomforestclassifier")),
    ("DecisionTree", ("decisiontreeclassifier", "decisiontreeregressor")),
    ("LogisticRegression", ("logisticregression",)),
    ("LinearRegression", ("linearregression",)),
    ("Ridge", ("ridge(", "ridgecv")),
    ("Lasso", ("lasso(", "lassocv")),
    ("SVM", ("svc(", "svr(", "linearsvc", "linearsvr", "svm")),
    ("KNN", ("kneighborsclassifier", "kneighborsregressor", "knn")),
    ("Bagging", ("baggingclassifier", "baggingregressor")),
    ("AdaBoost", ("adaboostclassifier", "adaboostregressor")),
    ("Voting", ("votingclassifier", "votingregressor")),
    ("Stacking", ("stackingclassifier", "stackingregressor")),
    ("LightGBM", ("lgbmclassifier", "lgbmregressor", "lightgbm")),
    ("CatBoost", ("catboostclassifier", "catboostregressor", "catboost")),
    ("PCA", ("pca(", "principalcomponentanalysis")),
    ("KMeans", ("kmeans(",)),
]


def is_generic_ml_heading(heading: str) -> bool:
    normalized = normalize_display_text(heading).lower()
    if not normalized:
        return True
    if normalized in GENERIC_ML_HEADINGS:
        return True
    if any(token in normalized for token in ("주의사항", "tip", "추가할 사항", "결론")):
        return True
    if re.fullmatch(r"\(?\d+\)?\s*\d+차 모델링", normalized):
        return True
    if re.fullmatch(r"\(?\d+\)?\s*차 모델링", normalized):
        return True
    if normalized.startswith("(") and any(token in normalized for token in ("모델링", "파생변수", "데이터 타입 변환", "전처리")):
        return True
    if normalized.endswith("의미") or normalized.endswith("정리") or normalized.endswith("결과"):
        return True
    if re.fullmatch(r"\(\d+\)\s*.+", normalized):
        return False
    return normalized.endswith("이해") or normalized.endswith("설명")


def is_basic_python_practice_block(body: str) -> bool:
    lower = body.lower()
    advanced_tokens = (
        "pd.read_csv",
        "pandas",
        "dataframe",
        "train_test_split",
        "sklearn",
        "randomforest",
        "decisiontree",
        "logisticregression",
        "linearregression",
        "labelencoder",
        "standardscaler",
        "minmaxscaler",
        "xgb",
        "lightgbm",
        "catboost",
        "np.",
        "numpy",
        "plt.",
        "sns.",
        "kmeans",
        "pca(",
        "roc_auc",
        "accuracy_score",
        "mean_squared_error",
    )
    if any(token in lower for token in advanced_tokens):
        return False
    return any(token in lower for token in ("class ", "def ", "with open(", "import csv", "import datetime", "import time"))


def extract_first_symbol_name(body: str, symbol: str) -> str:
    pattern = r"class\s+([A-Za-z_][A-Za-z0-9_]*)" if symbol == "class" else r"def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\("
    match = re.search(pattern, body)
    return match.group(1) if match else ""


def detect_model_names(body: str) -> list[str]:
    lower = body.lower()
    models: list[str] = []
    for label, patterns in MODEL_NAME_PATTERNS:
        if any(pattern in lower for pattern in patterns):
            models.append(label)
    return unique_preserve_order(models)


def infer_ml_code_label(block: dict[str, object]) -> str:
    body = str(block["body"])
    lower = body.lower()
    stage = get_ml_stage(block)
    models = detect_model_names(body)
    function_name = extract_first_symbol_name(body, "def")
    class_name = extract_first_symbol_name(body, "class")

    if stage == "data_load":
        if "train" in lower and "test" in lower and "read_csv" in lower:
            return "train/test CSV 불러오기"
        if "fetch_california_housing" in lower:
            return "California Housing 불러오기"
        if "load_iris" in lower:
            return "Iris 데이터 불러오기"
        if "fetch_" in lower or "load_" in lower:
            return "데이터셋 불러오기"
        if "read_csv" in lower:
            return "CSV 데이터 불러오기"
        if "read_excel" in lower:
            return "엑셀 데이터 불러오기"
    if stage == "preprocessing":
        if "labelencoder" in lower:
            return "LabelEncoder 전처리"
        if "standardscaler" in lower:
            return "StandardScaler 스케일링"
        if "minmaxscaler" in lower:
            return "MinMaxScaler 스케일링"
        if "train_test_split" in lower:
            return "학습/검증 데이터 분리"
        if "fillna" in lower or "dropna" in lower:
            return "결측치 정리"
    if stage == "feature_engineering":
        if is_ml_feature_list_block(body):
            return "모델 입력 컬럼 선택"
        if "pd.to_datetime" in lower or ".dt." in lower:
            return "datetime 파생 변수 생성"
        if any(token in lower for token in ("is_rush_hour", "is_morning", "is_night", "is_workhour", "is_weekend")):
            return "시간대 파생 변수 생성"
        if any(token in lower for token in ("humidity_ideal", "weather_ideal", "humidity_bin")):
            return "날씨 파생 변수 생성"
        if any(token in lower for token in ("was_contacted_before", "had_prev_success", "is_target_", "few_contacts", "low_euribor3m", "neg_emp_var_rate")):
            return "고객/캠페인 파생 변수 생성"
        if "get_dummies" in lower:
            return "범주형 원-핫 인코딩"
        if "smote(" in lower:
            return "SMOTE 데이터 재구성"
        return "파생 변수 추가"
    if stage == "modeling":
        if models:
            return f"{' / '.join(models[:2])} 모델 구성"
        return "모델 정의"
    if stage == "training":
        if "gridsearchcv" in lower:
            return "GridSearchCV 모델 학습"
        if models:
            return f"{models[0]} 모델 학습"
        return "모델 학습 루프"
    if stage == "evaluation":
        if "classification_report" in lower:
            return "분류 리포트 점검"
        if "results.append" in lower or "pd.dataframe(results" in lower:
            return "모델 성능 비교표 정리"
        if "rmsle" in lower:
            return "RMSLE 기준 성능 평가"
        if any(token in lower for token in ("accuracy_score", "f1_score", "roc_auc", "classification_report", "confusion_matrix")):
            return "분류 성능 평가"
        if any(token in lower for token in ("mean_squared_error", "rmse", "mae")):
            return "회귀 성능 평가"
        return "예측 결과 점검"
    if stage == "result_save":
        if "submission" in lower and "to_csv" in lower:
            return "submission 저장"
        return "예측 결과 저장"
    if stage == "visualization":
        return "데이터 분포 시각화"
    if stage == "class_design" and class_name:
        return f"{class_name} 클래스 구현"
    if stage == "function_practice" and function_name:
        return f"{function_name} 함수 구현"
    if class_name:
        return f"{class_name} 클래스 구현"
    if function_name:
        return f"{function_name} 함수 구현"
    return ""


def get_code_label(block: dict[str, object], research_tab: str = "") -> str:
    heading = normalize_display_text(str(block["heading"]))
    if research_tab == "ML":
        inferred_label = infer_ml_code_label(block)
        stage = get_ml_stage(block)
        if heading and heading.lower() not in {"overview", "archive note"} and not is_generic_ml_heading(heading):
            if inferred_label and stage not in {"modeling", "class_design", "function_practice"}:
                return trim_text(inferred_label, 80)
            return trim_text(heading, 80)
        if inferred_label:
            return trim_text(inferred_label, 80)

    if heading and heading.lower() not in {"overview", "archive note"}:
        return heading

    for raw_line in str(block["body"]).splitlines():
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            return clean_markdown_text(stripped.lstrip("# ").strip())
        if stripped.startswith("//"):
            return clean_markdown_text(stripped.lstrip("/ ").strip())
        if stripped.startswith("class ") or stripped.startswith("def "):
            return trim_text(stripped.split(":")[0], 80)
        return trim_text(clean_markdown_text(stripped), 80)

    return "Code Highlight"


def extract_comment_clues(body: str, limit: int = 3) -> list[str]:
    clues: list[str] = []
    for raw_line in body.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            stripped = stripped.lstrip("#").strip()
        elif stripped.startswith("//"):
            stripped = stripped.lstrip("/").strip()
        else:
            continue

        stripped = stripped.replace("@title", "").strip()
        cleaned = normalize_display_text(stripped)
        if not cleaned:
            continue
        if cleaned.lower() in {"trimmed", "...", "imports"}:
            continue
        clues.append(cleaned)
        if len(clues) >= limit:
            break

    return unique_cleaned_items(clues, limit=limit)


def infer_code_purpose(block: dict[str, object]) -> str:
    body = str(block["body"])

    if re.search(r"class\s+\w+.*Dataset", body) or "torch.utils.data.Dataset" in body:
        return "원본 데이터를 모델이 바로 받을 수 있는 샘플 구조로 바꾸기 위해 커스텀 Dataset을 정의하는 부분입니다."
    if "DataLoader(" in body or "collate_fn" in body:
        return "학습과 평가가 배치 단위로 안정적으로 돌도록 DataLoader와 collate 구성을 잡는 부분입니다."
    if any(token in body for token in ("optimizer", "backward(", "loss_dict", "lr_scheduler", "for epoch", "epoch_loss")):
        return "손실 계산, 역전파, optimizer 또는 scheduler 업데이트가 이어지는 학습 루프입니다."
    if any(token in body for token in ("train_test_split", "fillna", "dropna", "StandardScaler", "MinMaxScaler", "LabelEncoder")):
        return "전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다."
    if any(token in body for token in ("Word2Vec", "FastText", "GloVe", "Embedding", "embedding", "Tokenizer")):
        return "토큰을 벡터 표현으로 바꾸는 임베딩 또는 벡터화 단계를 구성하는 코드입니다."
    if any(token in body for token in ("FAISS", "Chroma", "Retriever", "vectorstore", "similarity_search", "as_retriever")):
        return "RAG 검색 경로의 기반이 되는 인덱싱과 Retriever 구성을 담당하는 코드입니다."
    if any(token in body for token in ("ChatOpenAI", "PromptTemplate", "Runnable", "chain.invoke", "llm.invoke")):
        return "프롬프트와 모델 호출을 연결해 재현 가능한 추론 체인을 만드는 부분입니다."
    if any(token in body for token in ("accuracy_score", "f1_score", "classification_report", "confusion_matrix", "roc_auc", "mean_squared_error")):
        return "지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다."
    if any(token in body for token in ("model.eval()", "torch.no_grad()", "predict(", "inference")):
        return "학습된 모델로 추론을 수행하고 예측 결과를 점검하는 코드입니다."
    if any(token in body for token in ("Conv2d", "Linear(", "nn.Module", "transformer", "LSTM", "GRU")):
        return "실험의 중심이 되는 모델 아키텍처를 정의하는 코드입니다."
    return "원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다."


def infer_ml_code_purpose(block: dict[str, object]) -> str:
    body = str(block["body"])
    lower = body.lower()
    stage = get_ml_stage(block)
    models = detect_model_names(body)

    if stage == "data_load":
        return "실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다."
    if stage == "preprocessing":
        return "결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다."
    if stage == "feature_engineering":
        if "smote(" in lower:
            return "클래스 불균형을 완화하기 위해 학습 데이터를 재구성하는 단계입니다. 특히 훈련셋에만 적용해야 누수를 막을 수 있습니다."
        if is_ml_feature_list_block(body):
            return "앞에서 만든 파생 변수와 원본 컬럼 중 어떤 조합을 실제 모델 입력으로 사용할지 확정하는 코드입니다."
        return "원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다."
    if stage == "modeling":
        if models:
            return f"{' / '.join(models[:2])} 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다."
        return "실험의 중심이 되는 모델 구조를 정의하고 비교 기준을 세우는 코드입니다."
    if stage == "training":
        if "gridsearchcv" in lower or "cross_val_score" in lower:
            return "하이퍼파라미터 탐색이나 교차검증을 통해 단순 실행이 아니라 성능 비교까지 해본 학습 코드입니다."
        return "훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다."
    if stage == "evaluation":
        if "results.append" in lower or "pd.dataframe(results" in lower:
            return "모델별 지표를 한 표로 모아 어떤 조합이 가장 나은지 비교하는 단계입니다."
        return "예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다."
    if stage == "result_save":
        return "최종 모델로 test 데이터를 예측하고 제출용 파일 형태로 저장하는 마무리 코드입니다."
    if stage == "visualization":
        return "데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다."
    if stage == "class_design":
        return "문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다."
    if stage == "function_practice":
        return "입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다."
    if any(token in lower for token in ("strftime", "datetime.now", "timedelta", "random.randint", "random.choice", "random.shuffle", "uniform(", "time.sleep", "time.time")):
        return "파이썬 표준 라이브러리를 사용해 시간 계산, 난수 생성, 실행 흐름을 직접 확인하는 실습 코드입니다."
    if any(token in lower for token in ("np.array", "np.arange", "np.zeros", "np.mean", "numpy")):
        return "넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다."
    if any(token in lower for token in ("pd.read_csv", "dataframe", ".loc[", ".iloc[", "pandas")):
        return "판다스 DataFrame을 불러오고 열과 행을 다루는 기본 조작을 익히는 실습 코드입니다."
    fallback = infer_code_purpose(block)
    if fallback == "원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.":
        label = normalize_display_text(get_code_label(block, "ML"))
        if label:
            return f"{trim_text(label, 36)} 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다."
    return fallback


def describe_code_block(block: dict[str, object], research_tab: str = "") -> str:
    label = get_code_label(block, research_tab)
    comments = extract_comment_clues(str(block["body"]))
    context = normalize_display_text(str(block.get("context", "")))
    intro = ""
    if label and label.lower() not in {"code highlight", "overview"}:
        intro = f"`{label}`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다."

    if research_tab == "ML":
        comment_clues = [condense_focus_item(item, max_len=34) for item in comments[:2]]
        detail = infer_ml_code_purpose(block)
        if comment_clues:
            detail = f"{detail} 코드에는 {format_korean_list(comment_clues, limit=2, max_item_len=34)} 같은 처리 포인트도 함께 남아 있습니다."
    elif comments:
        detail = f"코드 안에서는 {format_korean_list(comments[:3])} 흐름이 주석과 함께 드러납니다."
    elif context and is_meaningful_sentence(context):
        detail = ensure_sentence(context)
    else:
        detail = infer_code_purpose(block)

    return " ".join(part for part in (intro, detail) if part)


def get_code_trim_marker(lang: str) -> str:
    if lang in {"python", "bash", "sh", "ruby"}:
        return "# ... trimmed ..."
    if lang in {"javascript", "typescript", "java", "c", "cpp", "csharp", "go", "rust"}:
        return "// ... trimmed ..."
    if lang in {"html", "xml"}:
        return "<!-- ... trimmed ... -->"
    return "..."


def trim_code_block(body: str, lang: str, max_lines: int = 28) -> str:
    lines = body.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    if len(lines) <= max_lines:
        return "\n".join(lines)

    trimmed = lines[:max_lines]
    trimmed.append(get_code_trim_marker(lang))
    return "\n".join(trimmed)


ML_STAGE_LABELS = {
    "setup": "환경 준비",
    "data_load": "데이터 불러오기",
    "preprocessing": "전처리",
    "feature_engineering": "피처 가공",
    "modeling": "모델 구성",
    "training": "학습",
    "evaluation": "평가",
    "result_save": "결과 저장",
    "visualization": "시각화",
    "class_design": "클래스 설계",
    "function_practice": "함수 실습",
    "other": "구현 코드",
}

ML_STAGE_PRIORITY = [
    "data_load",
    "preprocessing",
    "feature_engineering",
    "modeling",
    "training",
    "evaluation",
    "result_save",
    "class_design",
    "function_practice",
    "visualization",
    "other",
    "setup",
]

ML_STAGE_DISPLAY_PRIORITY = [
    "data_load",
    "preprocessing",
    "feature_engineering",
    "visualization",
    "modeling",
    "training",
    "evaluation",
    "result_save",
    "class_design",
    "function_practice",
    "other",
    "setup",
]


def get_code_lines(body: str) -> list[str]:
    return [line.strip() for line in body.splitlines() if line.strip()]


def is_import_heavy_block(body: str) -> bool:
    lines = get_code_lines(body)
    if not lines:
        return False
    import_like = 0
    for line in lines:
        if IMPORT_RE.match(line) or FROM_IMPORT_RE.match(line):
            import_like += 1
        elif line.startswith("!pip install") or line.startswith("pip install"):
            import_like += 1
    return import_like / max(len(lines), 1) >= 0.6


def is_ml_feature_list_block(body: str) -> bool:
    lower = body.lower()
    lines = get_code_lines(body)
    if not lines:
        return False
    if "def " in lower or "class " in lower:
        return False
    if "feature_names" not in lower and "features_" not in lower:
        return False
    if "[" not in body or "]" not in body:
        return False
    signal_tokens = (
        "train_test_split",
        ".fit(",
        ".predict(",
        "pd.cut(",
        ".map(",
        ".isin(",
        ".between(",
        "get_dummies",
        "labelencoder",
        "standardscaler",
        "smote(",
    )
    return not any(token in lower for token in signal_tokens)


def is_ml_prediction_only_block(body: str) -> bool:
    lower = body.lower()
    lines = get_code_lines(body)
    if not lines:
        return False
    if len(lines) > 3:
        return False
    return ".predict(" in lower and not any(
        token in lower
        for token in (
            "accuracy_score",
            "f1_score",
            "classification_report",
            "confusion_matrix",
            "roc_auc",
            "mean_squared_error",
            "rmse",
            "rmsle",
            "results.append",
            "pd.dataframe(results",
        )
    )


def get_ml_stage(block: dict[str, object]) -> str:
    body = str(block["body"]).lower()
    heading = normalize_display_text(str(block["heading"])).lower()

    if not body.strip():
        return "other"
    if is_import_heavy_block(str(block["body"])):
        return "setup"
    if is_ml_feature_list_block(str(block["body"])):
        return "other"
    if any(token in body for token in ("strftime", "datetime.now", "timedelta", "random.randint", "random.choice", "random.shuffle", "uniform(", "time.sleep", "time.time")):
        return "other"
    if "class " in body and is_basic_python_practice_block(str(block["body"])):
        return "class_design"
    if "def " in body and is_basic_python_practice_block(str(block["body"])):
        return "function_practice"
    if "submission" in body or "to_csv(" in body:
        return "result_save"
    if any(token in body for token in ("pd.read_csv", "read_csv(", "fetch_", "load_", "dataset_path", "train.csv", "test.csv")):
        return "data_load"
    if any(token in body for token in ("fillna", "dropna", "labelencoder", "standardscaler", "minmaxscaler", "clean_text", "stopwords", "tokenize", "train_test_split")):
        return "preprocessing"
    if "smote(" in body:
        return "feature_engineering"
    if any(token in body for token in ("get_dummies", ".dt.", "pd.to_datetime", "engineer", "pd.cut(", ".map(", "isin(", "between(", "weekday_name", "weekday_num", "humidity_bin", "weather_ideal")):
        return "feature_engineering"
    if any(token in body for token in (".fit(", "gridsearchcv", "cross_val_score", "train_model", "optimizer", "epoch")):
        return "training"
    if any(token in body for token in (".predict(", "accuracy_score", "f1_score", "roc_auc", "classification_report", "confusion_matrix", "rmsle", "mean_squared_error", "rmse", "results.append", "pd.dataframe(results")):
        return "evaluation"
    if any(token in body for token in ("randomforest", "xgb", "lightgbm", "catboost", "linearregression", "logisticregression", "decisiontree", "classifier(", "regressor(", "pipeline(")):
        return "modeling"
    if any(token in body for token in ("plt.", "sns.", "heatmap", "histplot", "boxplot", "scatterplot", "barplot")):
        return "visualization"
    if "class " in body and "__init__" in body:
        return "class_design"
    if "def " in body:
        return "function_practice"
    if any(token in heading for token in ("모델링", "회귀", "분류")):
        return "modeling"
    if any(token in heading for token in ("전처리", "결측치", "이상치")):
        return "preprocessing"
    if "시각화" in heading:
        return "visualization"
    return "other"


def get_code_stage_label(block: dict[str, object], research_tab: str) -> str:
    if research_tab == "ML":
        return ML_STAGE_LABELS.get(get_ml_stage(block), "구현 코드")
    return ""


def score_ml_block_for_stage(block: dict[str, object], stage: str) -> int:
    raw_body = str(block["body"])
    body = raw_body.lower()
    score = score_code_block(block)
    lines = get_code_lines(raw_body)

    bonus_map = {
        "setup": ("import ", "from ", "!pip install", "warnings.filterwarnings"),
        "data_load": ("read_csv(", "pd.read_csv", "fetch_", "train.csv", "test.csv"),
        "preprocessing": ("fillna", "dropna", "labelencoder", "standardscaler", "minmaxscaler", "clean_text", "astype("),
        "feature_engineering": ("get_dummies", "pd.to_datetime", ".dt.", "hour", "month", "dayofweek", "feature"),
        "modeling": ("randomforest", "xgb", "lightgbm", "catboost", "linearregression", "logisticregression", "decisiontree", "classifier(", "regressor("),
        "training": (".fit(", "gridsearchcv", "cross_val_score", "train_", "cv="),
        "evaluation": (".predict(", "accuracy_score", "f1_score", "roc_auc", "classification_report", "confusion_matrix", "rmsle", "mean_squared_error", "rmse"),
        "result_save": ("submission", "to_csv(", "savefig(", "pickle.dump(", "joblib.dump("),
        "visualization": ("plt.", "sns.", "heatmap", "histplot", "boxplot", "scatterplot", "barplot"),
        "class_design": ("class ", "__init__", "self."),
        "function_practice": ("def ", "return "),
    }
    for token in bonus_map.get(stage, ()):
        if token in body:
            score += 10

    if not lines:
        score -= 200
    if stage == "other":
        score -= 24
    if stage == "preprocessing" and "import " in body and is_import_heavy_block(str(block["body"])):
        score -= 20
    if stage == "preprocessing" and "train_test_split" in body and "smote(" in body:
        score += 12
    if stage == "feature_engineering" and "datetime" in body and "pd.to_datetime" not in body and ".dt." not in body:
        score -= 10
    if stage == "feature_engineering" and any(token in body for token in ("plt.", "sns.", "barplot", "histplot", "boxplot")) and "smote(" not in body:
        score -= 30
    if stage == "feature_engineering" and is_ml_feature_list_block(raw_body):
        score -= 65
    if stage == "feature_engineering" and "def " in body:
        score += 18
    if stage == "feature_engineering" and len(lines) <= 3 and "def " not in body and "df[\"" not in body and "df['" not in body and ".map(" not in body and ".isin(" not in body and ".between(" not in body and "pd.cut(" not in body:
        score -= 28
    if stage == "feature_engineering" and any(token in body for token in ("def add_", "df[\"", "df['", "pd.cut(", ".map(", ".isin(", ".between(")):
        score += 22
    if stage == "modeling" and "results.append" in body:
        score -= 40
    if stage == "modeling" and is_ml_feature_list_block(raw_body):
        score -= 40
    if stage == "evaluation" and "classification_report" not in body and "results.append" not in body and "mean_squared_error" not in body and "accuracy_score" not in body and ".predict(" in body:
        score -= 10
    if stage == "evaluation" and is_ml_prediction_only_block(raw_body):
        score -= 28
    if stage == "result_save" and "to_csv(" in body:
        score += 18

    return score


def select_ml_code_blocks(code_blocks: list[dict[str, object]], limit: int, title_keywords: list[str] | None = None) -> list[dict[str, object]]:
    title_keywords = title_keywords or []
    candidate_items = [
        (index, block)
        for index, block in enumerate(code_blocks)
        if get_code_lines(str(block["body"]))
    ]
    if not candidate_items:
        return []

    stage_best: dict[str, tuple[int, dict[str, object], int]] = {}
    ranked = sorted(
        candidate_items,
        key=lambda item: (-score_code_block_for_track(item[1], "ML", title_keywords), item[0]),
    )
    preferred_ranked = [
        (index, block)
        for index, block in ranked
        if get_ml_stage(block) not in {"setup", "other"}
    ]
    stage_ranked = preferred_ranked or ranked

    for index, block in stage_ranked:
        stage = get_ml_stage(block)
        stage_score = score_ml_block_for_stage(block, stage) + score_code_block_for_track(block, "ML", title_keywords)
        existing = stage_best.get(stage)
        if existing is None or stage_score > existing[2]:
            stage_best[stage] = (index, block, stage_score)

    selected_indexes: list[int] = []
    used_labels: set[str] = set()
    for stage in ML_STAGE_PRIORITY:
        if stage in stage_best:
            index, block, _ = stage_best[stage]
            label_key = normalize_display_text(get_code_label(block, "ML")).lower()
            if label_key and label_key in used_labels:
                continue
            selected_indexes.append(index)
            if label_key:
                used_labels.add(label_key)
        if len(selected_indexes) >= limit:
            break

    if len(selected_indexes) < limit:
        for index, block in stage_ranked:
            if index in selected_indexes:
                continue
            if is_ml_prediction_only_block(str(block["body"])):
                continue
            label_key = normalize_display_text(get_code_label(block, "ML")).lower()
            if label_key and label_key in used_labels:
                continue
            selected_indexes.append(index)
            if label_key:
                used_labels.add(label_key)
            if len(selected_indexes) >= limit:
                break

    if not preferred_ranked and len(selected_indexes) < min(limit, len(ranked)):
        for index, block in ranked:
            if index in selected_indexes:
                continue
            if is_ml_prediction_only_block(str(block["body"])):
                continue
            label_key = normalize_display_text(get_code_label(block, "ML")).lower()
            if label_key and label_key in used_labels:
                continue
            selected_indexes.append(index)
            if label_key:
                used_labels.add(label_key)
            if len(selected_indexes) >= limit:
                break

    ordered_unique_indexes: list[int] = []
    for index in selected_indexes:
        if index not in ordered_unique_indexes:
            ordered_unique_indexes.append(index)
    display_order = {stage: index for index, stage in enumerate(ML_STAGE_DISPLAY_PRIORITY)}
    ordered_unique_indexes.sort(
        key=lambda index: (
            display_order.get(get_ml_stage(code_blocks[index]), 999),
            index,
        )
    )
    return [code_blocks[index] for index in ordered_unique_indexes]


def select_code_blocks(
    code_blocks: list[dict[str, object]],
    research_tab: str,
    title_keywords: list[str] | None = None,
    limit: int = 2,
) -> list[dict[str, object]]:
    title_keywords = title_keywords or []
    if research_tab == "ML":
        return select_ml_code_blocks(code_blocks, limit=limit, title_keywords=title_keywords)

    ranked = sorted(
        enumerate(code_blocks),
        key=lambda item: (-score_code_block_for_track(item[1], research_tab, title_keywords), item[0]),
    )

    selected_indexes: list[int] = []
    used_headings: set[str] = set()

    for index, block in ranked:
        heading_key = normalize_display_text(str(block["heading"])).lower() or f"index-{index}"
        if heading_key in used_headings:
            continue
        selected_indexes.append(index)
        used_headings.add(heading_key)
        if len(selected_indexes) >= limit:
            break

    if len(selected_indexes) < limit:
        for index, _ in ranked:
            if index in selected_indexes:
                continue
            selected_indexes.append(index)
            if len(selected_indexes) >= limit:
                break

    selected_indexes.sort()
    return [code_blocks[index] for index in selected_indexes]


def extract_libraries(code_blocks: list[dict[str, object]]) -> list[str]:
    libraries: list[str] = []
    seen: set[str] = set()

    for block in code_blocks:
        body = str(block["body"])
        for line in body.splitlines():
            import_match = IMPORT_RE.match(line)
            if import_match:
                lib = import_match.group(1).split(".")[0]
                if lib not in seen:
                    seen.add(lib)
                    libraries.append(lib)
            from_match = FROM_IMPORT_RE.match(line)
            if from_match:
                lib = from_match.group(1).split(".")[0]
                if lib not in seen:
                    seen.add(lib)
                    libraries.append(lib)
        if len(libraries) >= 8:
            break

    return libraries[:8]


def get_companion_files(path: Path) -> list[Path]:
    files = sorted(
        candidate
        for candidate in path.parent.iterdir()
        if candidate.is_file() and candidate.stem == path.stem
    )
    if path not in files:
        files.append(path)
        files.sort()
    return files


def clean_reference_name(raw_value: str) -> str:
    cleaned = strip_yaml_value(raw_value).strip("'")
    if "://" in cleaned or cleaned.startswith("http"):
        return cleaned
    if "/" in cleaned or "\\" in cleaned:
        return Path(cleaned).name
    return cleaned


def format_inline_code_list(items: list[str], empty_text: str = "None") -> str:
    if not items:
        return empty_text
    return ", ".join(f"`{item}`" for item in items)


def format_yaml_list(name: str, items: list[str]) -> str:
    if not items:
        return f"{name}: []"
    lines = [f"{name}:"]
    for item in items:
        lines.append(f'  - "{escape_yaml(normalize_display_text(item))}"')
    return "\n".join(lines)


CONCEPT_RULES = [
    {
        "key": "rag",
        "patterns": ["retriever", "vectorstore", "faiss", "chroma", "similarity_search", "as_retriever", "rag"],
        "label": "RAG 검색 파이프라인",
        "need": "LLM이 외부 지식을 안정적으로 참조하게 하려면, 생성 전에 관련 문서를 정확히 찾아오는 검색 단계가 먼저 필요합니다.",
        "choice": "이 방식은 모델 파라미터만 믿지 않고 최신 문서나 도메인 지식을 붙일 수 있어서 실제 서비스형 QA에 적합합니다.",
        "principle": "문서를 청크로 나누고 임베딩한 뒤, 질문과 가까운 벡터를 검색해 프롬프트에 함께 넣는 구조로 동작합니다.",
    },
    {
        "key": "agent",
        "patterns": ["langgraph", "stategraph", "agent", "toolnode", "tools_condition"],
        "label": "에이전트 상태 흐름",
        "need": "단일 호출만으로 해결되지 않는 작업은 추론, 도구 호출, 중간 상태 관리가 이어지는 흐름 제어가 필요합니다.",
        "choice": "상태 그래프 기반 접근은 단계별 분기와 재시도를 명시적으로 관리할 수 있어 에이전트 실험을 설명하기 좋습니다.",
        "principle": "현재 상태를 노드 간에 전달하면서, 조건에 따라 다음 노드나 도구 호출을 결정하는 방식으로 실행 흐름이 이어집니다.",
    },
    {
        "key": "lora",
        "patterns": ["lora", "qlora", "peft", "peftmodel"],
        "label": "파라미터 효율 미세조정",
        "need": "대형 언어모델 전체를 다시 학습하는 비용이 크기 때문에, 적은 자원으로도 실험 가능한 미세조정 방식이 필요합니다.",
        "choice": "LoRA/QLoRA는 전체 가중치를 모두 바꾸지 않고 작은 적응 파라미터만 학습해 메모리와 시간을 크게 줄일 수 있습니다.",
        "principle": "기존 가중치는 고정하고 저차원 행렬 업데이트만 추가로 학습해, 적은 파라미터로도 모델 행동을 조정합니다.",
    },
    {
        "key": "detection",
        "patterns": ["mask r-cnn", "fasterrcnn", "masks_to_boxes", "bounding box", "intersection over union", "iou"],
        "label": "객체 탐지와 영역 단위 이해",
        "need": "이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.",
        "choice": "Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.",
        "principle": "모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.",
    },
    {
        "key": "segmentation",
        "patterns": ["segmentation", "unet", "dice", "pixel-wise"],
        "label": "픽셀 단위 분할",
        "need": "객체의 경계를 세밀하게 다뤄야 할 때는 이미지 전체를 한 번에 분류하는 방식만으로는 부족합니다.",
        "choice": "Segmentation은 픽셀마다 클래스를 붙여주기 때문에 의료영상, 장면 이해, 배경 제거처럼 경계가 중요한 문제에 잘 맞습니다.",
        "principle": "이미지 특징을 추출한 뒤 해상도를 복원하면서 각 픽셀 위치에 대한 클래스 확률을 예측합니다.",
    },
    {
        "key": "embedding",
        "patterns": ["word2vec", "fasttext", "glove", "embedding", "tokenizer"],
        "label": "임베딩과 표현 학습",
        "need": "텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.",
        "choice": "Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.",
        "principle": "자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.",
    },
    {
        "key": "rnn",
        "patterns": ["lstm", "gru", "nn.lstm", "nn.gru", "rnn"],
        "label": "순차 데이터 모델링",
        "need": "문장, 시계열처럼 순서가 중요한 데이터는 현재 입력만이 아니라 앞선 맥락까지 함께 봐야 합니다.",
        "choice": "LSTM/GRU는 기본 RNN보다 긴 문맥을 더 안정적으로 다룰 수 있어 텍스트 분류나 시계열 예측 실습에 자주 쓰입니다.",
        "principle": "이전 시점의 은닉 상태를 다음 입력과 함께 업데이트하며, 게이트 구조로 필요한 정보는 남기고 불필요한 정보는 줄입니다.",
    },
    {
        "key": "cnn",
        "patterns": ["conv2d", "maxpool", "resnet", "alexnet", "cnn"],
        "label": "합성곱 기반 특징 추출",
        "need": "이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.",
        "choice": "CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.",
        "principle": "작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.",
    },
    {
        "key": "dataset",
        "patterns": ["dataloader", "dataset", "collate_fn", "train_test_split", "batch_size"],
        "label": "데이터 파이프라인",
        "need": "모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.",
        "choice": "Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.",
        "principle": "각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.",
    },
    {
        "key": "preprocessing",
        "patterns": ["standardscaler", "minmaxscaler", "labelencoder", "fillna", "dropna", "tokenize", "clean_text", "stopwords"],
        "label": "전처리와 입력 정리",
        "need": "원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.",
        "choice": "전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.",
        "principle": "불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.",
    },
    {
        "key": "training",
        "patterns": ["optimizer", "backward(", "optimizer.step", "lr_scheduler", "epoch_loss", "loss_dict"],
        "label": "학습 루프와 최적화",
        "need": "모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.",
        "choice": "optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.",
        "principle": "예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.",
    },
    {
        "key": "evaluation",
        "patterns": ["accuracy_score", "classification_report", "f1_score", "roc_auc", "mean_squared_error", "confusion_matrix", "precision", "recall", "rmsle"],
        "label": "평가 지표 해석",
        "need": "정확도 하나만으로는 모델이 실제로 무엇을 잘하고 무엇을 놓치는지 충분히 설명할 수 없습니다.",
        "choice": "문제 유형에 맞는 지표를 함께 보면 불균형 데이터, 오차 크기, 재현율 같은 중요한 관점을 놓치지 않을 수 있습니다.",
        "principle": "예측 결과를 정답과 비교해 오차나 클래스별 성능을 수치화하고, 그 수치로 모델 선택과 개선 방향을 판단합니다.",
    },
    {
        "key": "llmchain",
        "patterns": ["prompttemplate", "chatopenai", "chain.invoke", "llm.invoke", "runnable"],
        "label": "프롬프트 체인 구성",
        "need": "LLM 호출을 재현 가능하게 만들려면 입력 조합, 프롬프트 템플릿, 후처리 순서를 구조화할 필요가 있습니다.",
        "choice": "체인 구조는 실험 중 프롬프트와 입력 변형을 비교하기 쉽고, 이후 RAG나 에이전트 단계로 확장하기도 좋습니다.",
        "principle": "질문과 컨텍스트를 정해진 템플릿에 넣고, 모델 호출 결과를 다음 단계 입력으로 넘기며 처리 흐름을 구성합니다.",
    },
    {
        "key": "oop",
        "patterns": ["class ", "__init__", "self.", "method"],
        "label": "클래스와 객체 모델링",
        "need": "코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.",
        "choice": "클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.",
        "principle": "클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.",
    },
]


CONCEPT_PRIORITY = {
    "rag": 0,
    "agent": 1,
    "lora": 2,
    "embedding": 3,
    "rnn": 4,
    "llmchain": 5,
    "detection": 6,
    "dataset": 7,
    "preprocessing": 8,
    "training": 9,
    "evaluation": 10,
    "cnn": 11,
    "segmentation": 12,
    "oop": 13,
}


TRACK_ALLOWED_CONCEPTS = {
    "ML": {"embedding", "rnn", "dataset", "preprocessing", "training", "evaluation", "oop"},
    "DL": {"detection", "segmentation", "cnn", "dataset", "training", "evaluation", "preprocessing"},
    "LLM": {"rag", "agent", "lora", "embedding", "rnn", "llmchain", "dataset", "preprocessing", "training", "evaluation"},
}


ML_STAGE_NOTE_TEMPLATES = {
    "data_load": {
        "label": "데이터 입력부터 다시 보기",
        "need": "실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.",
        "choice": "이 글에서는 `{label}` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.",
        "principle": "표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.",
    },
    "preprocessing": {
        "label": "전처리 코드를 남기는 이유",
        "need": "머신러닝에선 모델보다 먼저 입력 데이터의 결측치, 범주형 값, 스케일을 어떻게 다뤘는지가 성능을 크게 바꿉니다.",
        "choice": "그래서 `{label}` 같은 코드를 통해 실제로 어떤 정제 규칙을 적용했는지 문장보다 코드로 먼저 보여주도록 정리했습니다.",
        "principle": "원본 데이터를 모델이 다루기 쉬운 수치 형태로 바꾸면 같은 알고리즘이어도 학습 안정성과 해석 가능성이 함께 올라갑니다.",
    },
    "feature_engineering": {
        "label": "파생 변수를 직접 만든 부분",
        "need": "원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.",
        "choice": "이 글에서는 `{label}` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.",
        "principle": "좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.",
    },
    "modeling": {
        "label": "모델을 바꿔가며 비교한 이유",
        "need": "한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.",
        "choice": "그래서 `{label}`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.",
        "principle": "모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.",
    },
    "training": {
        "label": "학습 코드를 따로 보는 이유",
        "need": "모델 선언만으로는 끝나지 않고 fitting, 검증 분리, 하이퍼파라미터 탐색까지 봐야 실제로 해본 실습으로 읽힙니다.",
        "choice": "이 글에서는 `{label}` 코드를 남겨 학습 루프나 GridSearchCV처럼 성능을 끌어올리기 위해 손댄 지점을 보여줍니다.",
        "principle": "훈련 과정은 데이터에서 패턴을 찾도록 파라미터를 조정하는 단계이며, 검증이 함께 있어야 과적합 여부도 판단할 수 있습니다.",
    },
    "evaluation": {
        "label": "지표 계산까지 남긴 이유",
        "need": "예측을 했더라도 어떤 기준으로 잘했는지 판단하지 않으면 실험 비교가 성립하지 않습니다.",
        "choice": "그래서 `{label}` 코드를 통해 정확도, F1, RMSLE 같은 지표를 실제로 어떻게 계산했는지 함께 남겼습니다.",
        "principle": "평가 지표는 예측 결과를 수치화해 모델 선택과 개선 방향을 정하는 기준점 역할을 합니다.",
    },
    "class_design": {
        "label": "클래스로 문제를 쪼개 본 이유",
        "need": "상태와 동작이 함께 움직이는 문제는 함수만 나열하기보다 객체 단위로 묶어야 구조가 더 선명해집니다.",
        "choice": "이 글에서는 `{label}` 코드를 통해 생성자와 메서드를 어떻게 나눠 문제를 모델링했는지 바로 보이게 했습니다.",
        "principle": "클래스는 관련 데이터와 동작을 한 단위로 캡슐화해 재사용성과 확장성을 높여 줍니다.",
    },
    "function_practice": {
        "label": "함수 단위로 연습한 이유",
        "need": "기초 문제 풀이도 입력, 처리, 반환을 함수로 분리해 봐야 로직을 재사용하고 테스트하기 쉬워집니다.",
        "choice": "그래서 `{label}` 같은 코드를 앞쪽에 두고, 문제 해결 흐름이 함수 단위로 어떻게 정리됐는지 보여주도록 만들었습니다.",
        "principle": "함수는 반복되는 로직을 한 번 정의해 여러 입력에 적용할 수 있게 하며, 문제를 작은 단위로 나누는 기본 도구입니다.",
    },
    "visualization": {
        "label": "시각화를 같이 남긴 이유",
        "need": "숫자만 보면 놓치기 쉬운 분포와 이상치를 그래프로 확인해야 다음 전처리나 feature engineering 방향이 또렷해집니다.",
        "choice": "이 글에서는 `{label}` 코드를 통해 어떤 그래프를 보고 판단했는지 실습 흔적을 남겼습니다.",
        "principle": "시각화는 데이터 분포를 직관적으로 드러내 모델 선택과 변수 설계의 근거를 만들어 줍니다.",
    },
    "other": {
        "label": "구현 흐름을 코드로 남긴 이유",
        "need": "설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.",
        "choice": "그래서 `{label}` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.",
        "principle": "코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.",
    },
}


ML_STUDY_RULES = [
    {
        "key": "classification",
        "patterns": ("classifier", "accuracy_score", "precision_score", "recall_score", "f1_score", "roc_auc", "confusion_matrix", "logloss"),
        "label": "분류 문제",
        "summary": "분류는 입력 특성으로 클래스나 반응 여부를 예측하는 문제입니다. 모델은 각 샘플이 어떤 범주에 속하는지 확률 또는 라벨로 출력합니다.",
        "practice": "이 글에서는 가입 여부, 품종, 레이블 예측처럼 범주형 타깃을 다루는 실습 맥락으로 연결됩니다.",
    },
    {
        "key": "regression",
        "patterns": ("regressor", "rmsle", "rmse", "mae", "mse", "mean_squared_error", "mean_absolute_error", "r2_score"),
        "label": "회귀 문제",
        "summary": "회귀는 연속적인 수치를 예측하는 문제입니다. 예측값과 실제값의 차이를 오차로 계산해 모델 성능을 판단합니다.",
        "practice": "이 글에서는 수요량, 가격, 점수처럼 숫자 타깃을 예측하는 실습과 이어집니다.",
    },
    {
        "key": "tree_ensemble",
        "patterns": ("decisiontree", "randomforest", "bagging", "adaboost", "xgb", "xgboost", "votingclassifier", "stackingclassifier", "stackingregressor"),
        "label": "결정 트리와 앙상블",
        "summary": "결정 트리는 조건 분기로 예측 규칙을 만들고, 앙상블은 여러 모델의 예측을 묶어 편향과 분산을 함께 줄이는 접근입니다.",
        "practice": "이 글에서는 Decision Tree, RandomForest, XGBoost, Voting, Stacking 코드를 통해 여러 모델을 비교해 볼 수 있습니다.",
    },
    {
        "key": "linear_model",
        "patterns": ("linearregression", "logisticregression", "ridge", "lasso", "elasticnet"),
        "min_hits": 2,
        "label": "선형 모델과 정규화",
        "summary": "선형 모델은 입력 특성의 선형 결합으로 예측을 만들고, 정규화는 가중치 크기를 제어해 과적합을 줄이는 역할을 합니다.",
        "practice": "이 글에서는 LinearRegression, LogisticRegression, Ridge, Lasso 실습과 연결해 해석할 수 있습니다.",
    },
    {
        "key": "preprocessing",
        "patterns": ("labelencoder", "onehotencoder", "get_dummies", "fillna", "dropna", "standardscaler", "minmaxscaler", "train_test_split"),
        "label": "전처리와 입력 정리",
        "summary": "머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.",
        "practice": "이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.",
    },
    {
        "key": "feature_engineering",
        "patterns": ("pd.to_datetime", ".dt.", "feature", "is_", "engineer", "groupby(", "weekday", "hour", "month"),
        "label": "피처 엔지니어링",
        "summary": "피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.",
        "practice": "이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.",
    },
    {
        "key": "evaluation",
        "patterns": ("accuracy_score", "precision_score", "recall_score", "f1_score", "roc_auc", "classification_report", "rmsle", "rmse", "mae", "mean_squared_error"),
        "label": "평가 지표 해석",
        "summary": "평가 지표는 예측 결과를 수치화해 모델의 강점과 약점을 읽게 해주는 기준입니다. 문제 유형에 맞는 지표를 골라야 실험 비교가 가능합니다.",
        "practice": "이 글에서는 F1, Recall, Accuracy, RMSLE 같은 지표를 실제 코드에서 계산하는 흐름으로 연결됩니다.",
    },
    {
        "key": "dimensionality_reduction",
        "patterns": ("pca(", "principalcomponentanalysis", "explained_variance_ratio_", "svd"),
        "label": "차원 축소",
        "summary": "차원 축소는 많은 변수의 정보를 더 적은 축으로 압축해 시각화, 노이즈 감소, 계산 효율 개선에 활용하는 기법입니다.",
        "practice": "이 글에서는 PCA처럼 분산을 최대한 보존하는 축을 찾아 데이터를 다시 표현하는 실습과 이어집니다.",
    },
    {
        "key": "clustering",
        "patterns": ("kmeans(", "cluster", "silhouette", "elbow", "centroid"),
        "label": "군집화",
        "summary": "군집화는 정답 라벨 없이 비슷한 샘플끼리 묶어 데이터 구조를 탐색하는 비지도 학습 방법입니다.",
        "practice": "이 글에서는 KMeans, 군집 시각화, 클러스터 품질 점검 같은 흐름과 연결됩니다.",
    },
    {
        "key": "oop",
        "patterns": ("class ", "__init__", "self."),
        "label": "객체지향 설계",
        "summary": "객체지향은 관련 데이터와 동작을 하나의 객체로 묶어 문제를 구조적으로 표현하는 방식입니다.",
        "practice": "이 글에서는 클래스, 메서드, 상태 관리 같은 코드가 핵심 학습 포인트로 드러납니다.",
    },
    {
        "key": "function_design",
        "patterns": ("def ", "return ", "with open(", "import csv"),
        "label": "함수 분해와 로직 구성",
        "summary": "함수는 입력, 처리, 반환을 분리해 로직을 재사용하기 쉽게 만들고, 문제를 작은 단위로 나누는 기본 도구입니다.",
        "practice": "이 글에서는 문제 풀이를 함수 단위로 쪼개고 입출력을 나눠 보는 실습과 연결됩니다.",
    },
]

ML_STUDY_PRIORITY = {
    "classification": 1,
    "regression": 1,
    "tree_ensemble": 2,
    "linear_model": 2,
    "dimensionality_reduction": 2,
    "clustering": 2,
    "preprocessing": 3,
    "feature_engineering": 4,
    "evaluation": 5,
    "oop": 6,
    "function_design": 7,
}

ML_API_PATTERNS = [
    ("pd.read_csv", ("pd.read_csv", "read_csv(")),
    ("train_test_split", ("train_test_split",)),
    ("LabelEncoder", ("labelencoder",)),
    ("get_dummies", ("get_dummies",)),
    ("StandardScaler", ("standardscaler",)),
    ("MinMaxScaler", ("minmaxscaler",)),
    ("GridSearchCV", ("gridsearchcv",)),
    ("cross_val_score", ("cross_val_score",)),
    ("DecisionTree", ("decisiontree",)),
    ("RandomForest", ("randomforest",)),
    ("XGBoost", ("xgb", "xgboost")),
    ("AdaBoost", ("adaboost",)),
    ("Bagging", ("bagging",)),
    ("Voting", ("votingclassifier", "votingregressor")),
    ("Stacking", ("stackingclassifier", "stackingregressor")),
    ("LinearRegression", ("linearregression",)),
    ("LogisticRegression", ("logisticregression",)),
    ("Ridge", ("ridge(", "ridgecv")),
    ("Lasso", ("lasso(", "lassocv")),
    ("PCA", ("pca(",)),
    ("KMeans", ("kmeans(",)),
    ("accuracy_score", ("accuracy_score",)),
    ("precision_score", ("precision_score",)),
    ("recall_score", ("recall_score",)),
    ("f1_score", ("f1_score",)),
    ("RMSLE", ("mean_squared_log_error", "rmsle")),
    ("RMSE", ("rmse", "mean_squared_error")),
    ("matplotlib", ("plt.",)),
    ("seaborn", ("sns.",)),
]


def clean_ml_title_for_summary(title: str) -> str:
    cleaned = normalize_display_text(title)
    cleaned = re.sub(r"^\d+\s+", "", cleaned)
    cleaned = re.sub(r"\s*-\s*AI\s*\d.*$", "", cleaned)
    return compact_spaces(cleaned)


def condense_ml_problem_text(text: str, max_len: int = 120) -> str:
    normalized = normalize_display_text(text)
    if not normalized:
        return ""
    normalized = re.sub(r"[\U00010000-\U0010ffff]", "", normalized)
    normalized = re.sub(r"[📌🎯🚲🏦🧪]", "", normalized)
    parts = [compact_spaces(part) for part in re.split(r"\s+-\s+|\.\s+", normalized) if compact_spaces(part)]
    if not parts:
        return trim_text(normalized, max_len)
    condensed = ". ".join(parts[:2])
    return trim_text(condensed, max_len)


def build_ml_problem_summary(
    title: str,
    sections: list[dict[str, object]],
    intro_paragraphs: list[str],
    focus_items: list[str],
    title_keywords: list[str] | None = None,
) -> str:
    title_keywords = title_keywords or []
    outline_labels = build_ml_outline_labels(sections, limit=4)
    for section in sections:
        label = format_section_path(section.get("path", []), max_depth=3).lower()
        if "미션 설명" in label:
            summary = summarize_section_content(section, max_len=126)
            if summary:
                return condense_ml_problem_text(summary, max_len=126)
    ranked_sections = sorted(
        sections,
        key=lambda section: -score_section_for_title(section, title_keywords),
    )
    for section in ranked_sections:
        summary = summarize_section_content(section, max_len=126)
        if summary and score_section_for_title(section, title_keywords) > 0:
            return condense_ml_problem_text(summary, max_len=126)
    if outline_labels:
        cleaned_title = clean_ml_title_for_summary(title)
        lead = cleaned_title or "이 ML 실습"
        return f"{lead}에서 {format_korean_list(outline_labels, limit=3, max_item_len=18)} 흐름을 직접 따라가며 구현했습니다."
    for candidate in intro_paragraphs + focus_items:
        if is_meaningful_sentence(candidate):
            return condense_ml_problem_text(candidate, max_len=126)
    cleaned_title = clean_ml_title_for_summary(title)
    return f"{cleaned_title}를 중심으로 학습한 내용을 정리한 ML 실습입니다." if cleaned_title else "이 ML 실습에서 다룬 문제 설정을 정리했습니다."


def build_ml_data_summary(
    sections: list[dict[str, object]],
    section_summaries: list[dict[str, str]],
    intro_paragraphs: list[str],
    focus_items: list[str],
    title_keywords: list[str] | None = None,
) -> str:
    title_keywords = title_keywords or []
    outline_labels = build_ml_outline_labels(sections, limit=4)
    for section in sections:
        label = format_section_path(section.get("path", []), max_depth=3).lower()
        if "데이터 설명" in label or "파일 설명" in label or label == "데이터" or label.endswith(" > 데이터"):
            summary = summarize_section_content(section, max_len=126)
            if summary:
                return trim_text(summary, 126)
    for entry in section_summaries:
        title = normalize_display_text(entry["title"]).lower()
        summary = normalize_display_text(entry["summary"])
        if "데이터 설명" in title or "파일 설명" in title or title == "데이터" or "dataset" in title:
            return trim_text(summary, 126)
    for entry in section_summaries:
        title = normalize_display_text(entry["title"]).lower()
        summary = normalize_display_text(entry["summary"])
        if any(token in title for token in ("공식", "미션", "tip", "참고")):
            continue
        if any(token in summary.lower() for token in ("데이터", "csv", "dataset", "train", "test")):
            return trim_text(summary, 126)
    for candidate in intro_paragraphs[1:] + focus_items:
        normalized = condense_ml_problem_text(candidate, max_len=126)
        if any(token in normalized.lower() for token in ("데이터", "csv", "dataset", "train", "test")):
            return trim_text(normalized, 126)
    ranked_sections = sorted(
        sections,
        key=lambda section: -score_section_for_title(section, title_keywords),
    )
    for section in ranked_sections:
        summary = summarize_section_content(section, max_len=126)
        if not summary:
            continue
        if any(token in summary.lower() for token in ("데이터", "csv", "dataset", "train", "test")):
            return trim_text(summary, 126)
    if outline_labels:
        return f"특정 데이터셋 설명보다 {format_korean_list(outline_labels, limit=3, max_item_len=18)} 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다."
    return ""


def build_ml_study_notes(
    *,
    title: str,
    focus_items: list[str],
    section_summaries: list[dict[str, str]],
    paragraphs: list[str],
    code_blocks: list[dict[str, object]],
    libraries: list[str],
) -> list[dict[str, str]]:
    corpus_parts = [title]
    corpus_parts.extend(focus_items[:8])
    corpus_parts.extend(entry["title"] for entry in section_summaries[:6])
    corpus_parts.extend(entry["summary"] for entry in section_summaries[:6])
    corpus_parts.extend(paragraphs[:8])
    corpus_parts.extend(libraries[:8])
    corpus_parts.extend(str(block["heading"]) for block in code_blocks[:10])
    corpus_parts.extend(str(block["body"])[:900] for block in code_blocks[:8])
    corpus = "\n".join(corpus_parts).lower()

    notes: list[dict[str, str]] = []
    for rule in ML_STUDY_RULES:
        hit_count = sum(1 for pattern in rule["patterns"] if pattern in corpus)
        if hit_count >= int(rule.get("min_hits", 1)):
            notes.append(
                {
                    "key": rule["key"],
                    "label": rule["label"],
                    "summary": rule["summary"],
                    "practice": rule["practice"],
                }
            )

    if not notes:
        return [
            {
                "label": "구현 중심 학습",
                "summary": "이 글은 개념 설명과 함께 실제 코드를 통해 학습 흐름을 다시 따라가도록 정리된 ML 실습 기록입니다.",
                "practice": "데이터 입력, 처리, 모델링, 평가 가운데 실제로 손댄 단계를 중심으로 읽을 수 있습니다.",
            }
        ]

    notes.sort(key=lambda note: (ML_STUDY_PRIORITY.get(note["key"], 999), note["label"]))
    deduped: list[dict[str, str]] = []
    seen_labels: set[str] = set()
    for note in notes:
        label_key = note["label"].lower()
        if label_key in seen_labels:
            continue
        seen_labels.add(label_key)
        deduped.append(
            {
                "label": note["label"],
                "summary": note["summary"],
                "practice": note["practice"],
            }
        )
        if len(deduped) >= 4:
            break
    return deduped


def build_ml_research_summary(
    *,
    title: str,
    study_notes: list[dict[str, object]],
    code_samples: list[dict[str, object]],
    artifact_summary: str,
) -> str:
    cleaned_title = clean_ml_title_for_summary(title) or title
    section_labels = choose_ml_summary_labels(study_notes, limit=3)
    summary_stage_priority = (
        "training",
        "modeling",
        "evaluation",
        "result_save",
        "feature_engineering",
        "preprocessing",
        "data_load",
        "visualization",
    )
    prioritized_blocks = sorted(
        code_samples,
        key=lambda block: (
            summary_stage_priority.index(get_ml_stage(block))
            if get_ml_stage(block) in summary_stage_priority
            else len(summary_stage_priority),
            code_samples.index(block),
        ),
    )
    code_labels = unique_preserve_order([get_code_label(block, "ML") for block in prioritized_blocks])[:2]

    if section_labels:
        lead = f"{cleaned_title}의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다"
    else:
        lead = f"{cleaned_title}에서 다룬 문제 설정, 데이터 흐름, 구현 코드를 다시 볼 수 있게 정리한 ML 학습 기록입니다"

    if code_labels:
        prefix = f"본문은 {format_korean_list(section_labels, limit=3, max_item_len=18)} 순서로 큰 장을 먼저 훑고, " if section_labels else "본문은 큰 흐름을 먼저 훑고, "
        detail = f"{prefix}{format_korean_list(code_labels, limit=2, max_item_len=24)} 같은 코드로 실제 구현을 이어서 확인할 수 있습니다"
    else:
        detail = "본문은 원본 노트의 큰 장을 따라가며 문제 맥락을 정리하고, 아래에서 실제로 실행해 본 코드 흐름을 다시 확인할 수 있게 구성했습니다"

    return " ".join(
        part
        for part in (
            ensure_sentence(lead),
            ensure_sentence(detail),
            artifact_summary,
        )
        if part
    )


def extract_ml_api_terms(body: str, limit: int = 4) -> list[str]:
    lower = body.lower()
    items: list[str] = []
    for label, patterns in ML_API_PATTERNS:
        if any(pattern in lower for pattern in patterns):
            items.append(label)
        if len(items) >= limit:
            break
    return unique_preserve_order(items)[:limit]


def build_ml_implementation_steps(code_samples: list[dict[str, object]]) -> list[dict[str, object]]:
    steps: list[dict[str, object]] = []
    for index, block in enumerate(code_samples, start=1):
        stage_label = get_code_stage_label(block, "ML") or "구현 코드"
        title = get_code_label(block, "ML")
        purpose = infer_ml_code_purpose(block)
        apis = extract_ml_api_terms(str(block["body"]))
        clues = [condense_focus_item(item, max_len=34) for item in extract_comment_clues(str(block["body"]), limit=2)]
        steps.append(
            {
                "index": index,
                "stage": stage_label,
                "title": title,
                "purpose": purpose,
                "apis": apis,
                "clues": clues,
            }
        )
    return steps


def format_html_code_list(items: list[str]) -> str:
    if not items:
        return ""
    return " ".join(f"<code>{html.escape(item)}</code>" for item in items)


def build_ml_intro_html(
    *,
    problem_summary: str,
    data_summary: str,
    study_notes: list[dict[str, object]],
    outline_labels: list[str],
    flow_items: list[str],
    source_formats: list[str],
    code_block_count: int,
    execution_block_count: int,
    libraries: list[str],
) -> str:
    concept_labels = choose_ml_summary_labels(study_notes, limit=4)
    parsed_flow_items: list[tuple[str, str]] = []
    for item in flow_items:
        if ": " in item:
            stage, label = item.split(": ", 1)
            parsed_flow_items.append((stage.strip(), label.strip()))
        else:
            parsed_flow_items.append(("", item))

    implementation_focus: list[str] = []
    preferred_stage_groups = [
        {"데이터 불러오기", "전처리", "피처 가공"},
        {"모델 구성", "학습"},
        {"평가", "결과 저장"},
    ]
    used_labels: set[str] = set()
    for stage_group in preferred_stage_groups:
        for stage, label in parsed_flow_items:
            if not label or label in used_labels:
                continue
            if stage in stage_group:
                implementation_focus.append(label)
                used_labels.add(label)
                break
    for _, label in parsed_flow_items:
        if not label or label in used_labels:
            continue
        implementation_focus.append(label)
        used_labels.add(label)
        if len(implementation_focus) >= 3:
            break
    implementation_focus = unique_preserve_order(implementation_focus)[:3]
    library_summary = ", ".join(libraries[:4]) if libraries else "미확인"
    if len(libraries) > 4:
        library_summary += f" 외 {len(libraries) - 4}"
    rows = [
        ("문제 설정", problem_summary or "이 글에서 다룬 문제 설정과 목표를 짧게 요약했습니다."),
        ("원본 구조", " -> ".join(outline_labels) if outline_labels else "원본 마크다운의 큰 섹션 흐름을 기준으로 이 실습을 다시 읽을 수 있게 정리했습니다."),
        ("데이터 맥락", data_summary or "원본 노트에서 데이터를 설명한 부분을 기준으로 실습 맥락을 정리했습니다."),
        ("주요 장", " · ".join(concept_labels) if concept_labels else "이 글에서 필요한 개념을 먼저 읽고 코드로 이어갈 수 있게 정리했습니다."),
        ("구현 흐름", " -> ".join(implementation_focus) if implementation_focus else "데이터 처리부터 학습과 평가까지의 핵심 코드 흐름을 단계별로 보여줍니다."),
        ("자료", f'{" / ".join(source_formats) if source_formats else "source"} · 코드 {code_block_count} · 실행 {execution_block_count}'),
        ("주요 스택", library_summary),
    ]
    row_html = "\n".join(
        "\n".join(
            [
                '  <div class="research-overview__row">',
                f'    <div class="research-overview__label">{html.escape(label)}</div>',
                f'    <div class="research-overview__value">{html.escape(value)}</div>',
                "  </div>",
            ]
        )
        for label, value in rows
    )
    return "\n".join(
        [
            "## 글 한눈에 보기",
            "",
            '<div class="research-overview research-overview--intro">',
            row_html,
            "</div>",
        ]
    )


def render_ml_inline_code_block(block: dict[str, object]) -> str:
    lang = str(block["lang"])
    label = get_code_label(block, "ML")
    stage_label = get_code_stage_label(block, "ML")
    explanation = infer_ml_code_purpose(block)
    apis = extract_ml_api_terms(str(block["body"]))
    body = trim_code_block(str(block["body"]), lang, max_lines=24)
    intro_parts = [part for part in (stage_label, label) if part]
    lines = [f"**코드로 확인한 부분**: {' · '.join(intro_parts)}" if intro_parts else "**코드로 확인한 부분**"]
    if apis:
        lines.append(f"**핵심 API**: {format_inline_code_list(apis)}")
    lines.append(explanation)
    lines.append("")
    lines.append(f"```{lang}")
    lines.append(body)
    lines.append("```")
    return "\n".join(lines)


def build_ml_study_section(
    *,
    study_notes: list[dict[str, object]],
) -> str:
    sections: list[str] = []
    for note in study_notes:
        children = note.get("children", [])
        sections.append(
            "\n".join(
                [
                    f"### {note['label']}",
                    "",
                    note["summary"],
                    "",
                    f"- 읽을 포인트: {note['practice']}",
                ]
            )
        )
        if not children:
            for block in note.get("code_blocks", [])[:1]:
                sections.append(render_ml_inline_code_block(block))
        for child in children[:4]:
            child_label = normalize_display_text(str(child.get("label", "")))
            child_summary = normalize_display_text(str(child.get("summary", "")))
            if not child_label or not child_summary:
                continue
            sections.append(
                "\n".join(
                    [
                        f"#### {child_label}",
                        "",
                        child_summary,
                    ]
                )
            )
            for block in child.get("code_blocks", [])[:1]:
                sections.append(render_ml_inline_code_block(block))
    return "\n\n".join(sections)


def build_ml_implementation_section(steps: list[dict[str, object]]) -> str:
    sections: list[str] = []
    for step in steps:
        api_line = format_inline_code_list(step["apis"], empty_text="-")
        clue_line = " · ".join(step["clues"]) if step["clues"] else "-"
        sections.append(
            "\n".join(
                [
                    f"### {step['index']}. {step['title']}",
                    "",
                    f"- 단계: {step['stage']}",
                    f"- 구현 의도: {step['purpose']}",
                    f"- 핵심 API: {api_line}",
                    f"- 코드 포인트: {clue_line}",
                ]
            )
        )
    return "\n\n".join(sections)


def build_ml_learning_notes(code_samples: list[dict[str, object]]) -> list[dict[str, str]]:
    stage_to_block: dict[str, dict[str, object]] = {}
    for block in code_samples:
        stage = get_ml_stage(block)
        stage_to_block.setdefault(stage, block)

    notes: list[dict[str, str]] = []
    for stage in ML_STAGE_PRIORITY:
        template = ML_STAGE_NOTE_TEMPLATES.get(stage)
        block = stage_to_block.get(stage)
        if template is None or block is None:
            continue

        code_label = clean_markdown_text(get_code_label(block, "ML"))
        notes.append(
            {
                "label": template["label"],
                "need": template["need"],
                "choice": template["choice"].format(label=code_label),
                "principle": template["principle"],
            }
        )
        if len(notes) >= 4:
            break

    if notes:
        return notes

    fallback = ML_STAGE_NOTE_TEMPLATES["other"]
    return [
        {
            "label": fallback["label"],
            "need": fallback["need"],
            "choice": fallback["choice"].format(label="핵심 구현 코드"),
            "principle": fallback["principle"],
        }
    ]


def build_concept_notes(
    *,
    research_tab: str,
    title: str,
    focus_items: list[str],
    section_summaries: list[dict[str, str]],
    paragraphs: list[str],
    code_blocks: list[dict[str, object]],
    libraries: list[str],
) -> list[dict[str, str]]:
    corpus_parts = [research_tab, title]
    corpus_parts.extend(focus_items[:8])
    corpus_parts.extend(entry["title"] for entry in section_summaries[:6])
    corpus_parts.extend(entry["summary"] for entry in section_summaries[:6])
    corpus_parts.extend(paragraphs[:8])
    corpus_parts.extend(libraries[:8])
    corpus_parts.extend(str(block["heading"]) for block in code_blocks[:10])
    corpus_parts.extend(str(block["body"])[:900] for block in code_blocks[:8])
    corpus = "\n".join(corpus_parts).lower()

    notes: list[dict[str, str]] = []
    allowed = TRACK_ALLOWED_CONCEPTS.get(research_tab, set())
    for rule in CONCEPT_RULES:
        if allowed and rule["key"] not in allowed:
            continue
        if any(pattern.lower() in corpus for pattern in rule["patterns"]):
            notes.append(
                {
                    "key": rule["key"],
                    "label": rule["label"],
                    "need": rule["need"],
                    "choice": rule["choice"],
                    "principle": rule["principle"],
                }
            )

    if notes:
        notes.sort(key=lambda note: CONCEPT_PRIORITY.get(note["key"], 999))
        return [
            {
                "label": note["label"],
                "need": note["need"],
                "choice": note["choice"],
                "principle": note["principle"],
            }
            for note in notes[:3]
        ]

    if research_tab == "ML":
        return [
            {
                "label": "입력과 모델 연결",
                "need": "머신러닝 실습에서는 모델 선택만큼 입력 데이터를 어떤 형태로 정리하는지가 결과를 크게 좌우합니다.",
                "choice": "이 기록은 전처리와 모델링 코드를 같이 남겨, 학습한 개념이 실제 코드 흐름으로 어떻게 연결되는지 보게 합니다.",
                "principle": "데이터 정리, 특징 표현, 학습, 평가가 한 파이프라인으로 이어질 때 비로소 모델 동작을 해석할 수 있습니다.",
            }
        ]
    if research_tab == "DL":
        return [
            {
                "label": "표현 학습과 학습 루프",
                "need": "딥러닝은 모델 구조만 보는 것이 아니라 입력 텐서, 손실, optimizer가 함께 어떻게 맞물리는지 이해해야 합니다.",
                "choice": "그래서 이 아카이브는 모델 정의뿐 아니라 DataLoader와 학습 루프 코드를 같이 남기는 쪽으로 정리했습니다.",
                "principle": "입력이 층을 통과하며 표현으로 바뀌고, 손실의 기울기가 역전파되어 가중치가 조금씩 조정되는 구조입니다.",
            }
        ]
    return [
        {
            "label": "LLM 실험 구조화",
            "need": "LLM 실습은 프롬프트 한 줄보다 검색, 컨텍스트, 모델 호출 순서를 함께 봐야 실제 동작을 이해할 수 있습니다.",
            "choice": "그래서 이 기록은 체인 구성과 보조 코드까지 함께 남겨, 단순 결과보다 시스템 흐름을 읽을 수 있게 만들었습니다.",
            "principle": "입력 가공, 컨텍스트 주입, 모델 호출, 출력 후처리가 연결되면서 하나의 응답 파이프라인이 만들어집니다.",
        }
    ]


def build_content(
    *,
    title: str,
    date: str,
    research_tab: str,
    research_kind: str,
    source_title: str,
    source_path: str,
    excerpt: str,
    track_tag: str,
    kind_tag: str,
    code_block_count: int,
    execution_block_count: int,
    source_formats: list[str],
    companion_files: list[str],
    research_summary: str,
    artifact_summary: str,
    focus_items: list[str],
    section_summaries: list[dict[str, str]],
    concept_notes: list[dict[str, str]],
    ml_problem_summary: str,
    ml_data_summary: str,
    ml_study_notes: list[dict[str, str]],
    ml_source_notes: list[dict[str, str]],
    track_source_notes: list[dict[str, object]],
    ml_outline_labels: list[str],
    ml_implementation_steps: list[dict[str, object]],
    flow_items: list[str],
    code_samples: list[dict[str, object]],
    libraries: list[str],
    raw_note_markdown: str,
    preview_lines: list[str],
    related_notes: list[str],
    external_refs: list[str],
    note_type: str,
    updated_at: str,
) -> str:
    focus_display_items = unique_cleaned_items([condense_focus_item(item, max_len=60) for item in focus_items], limit=5)
    coverage_title = "원문 흐름대로 보기" if research_tab == "ML" else "What This Note Covers"
    flow_title = "구현 흐름" if research_tab == "ML" else "Implementation Flow"
    code_title = "코드로 확인한 내용" if research_tab == "ML" else "Code Highlights"
    concept_title = "Why These Steps Matter" if research_tab == "ML" else "Why This Matters"
    snapshot_rows = [
        ("Track", research_tab),
        ("Type", research_kind),
        ("Source Files", format_inline_code_list(source_formats)),
        ("Code Blocks", str(code_block_count)),
        ("Execution Cells", str(execution_block_count)),
        ("Libraries", format_inline_code_list(libraries, empty_text="Not detected")),
        ("Source Note", f"`{clean_markdown_text(source_title)}`"),
    ]

    snapshot_table = "\n".join(f"| {label} | {value} |" for label, value in snapshot_rows)

    if focus_display_items:
        focus_section = "\n".join(f"- {item}" for item in focus_display_items)
    else:
        focus_section = f"- 이 기록은 `{research_tab}` 트랙의 `{research_kind}` 아카이브로 정리되어 있습니다."

    if research_tab == "ML" and ml_source_notes:
        coverage_section = build_ml_study_section(study_notes=ml_source_notes)
    elif research_tab == "ML" and ml_study_notes:
        coverage_section = build_ml_study_section(study_notes=ml_study_notes)
    elif track_source_notes:
        coverage_section = build_track_source_section(study_notes=track_source_notes)
    elif section_summaries and any(entry["title"] != "Key Step" for entry in section_summaries):
        coverage_section = "\n\n".join(
            f"### {entry['title']}\n\n{entry['summary']}"
            for entry in section_summaries
        )
    else:
        coverage_section = focus_section

    if research_tab == "ML" and ml_implementation_steps:
        flow_section = build_ml_implementation_section(ml_implementation_steps)
    elif flow_items:
        flow_section = "\n".join(f"{index}. {item}" for index, item in enumerate(flow_items, start=1))
    else:
        flow_section = "1. 원본 노트의 문제 정의를 먼저 확인합니다.\n2. 핵심 코드 블록과 구현 단계를 따라갑니다.\n3. 필요하면 이 흐름을 별도 케이스 스터디로 확장합니다."

    if concept_notes:
        concept_section = "\n\n".join(
            "\n".join(
                [
                    f"### {note['label']}",
                    "",
                    f"- 왜 필요한가: {note['need']}",
                    f"- 왜 이 방식을 쓰는가: {note['choice']}",
                    f"- 원리: {note['principle']}",
                ]
            )
            for note in concept_notes
        )
    else:
        concept_section = "- 왜 필요한가: 이 기록은 구현 코드를 읽기 전에 핵심 개념을 빠르게 짚을 수 있도록 정리되어 있습니다.\n- 왜 이 방식을 쓰는가: 실습 노트와 코드 블록을 같이 남기면 개념과 구현을 한 번에 연결해서 볼 수 있습니다.\n- 원리: 입력, 처리, 학습 또는 추론, 평가 단계가 하나의 흐름으로 이어집니다."

    if code_samples:
        code_sections = []
        for block in code_samples:
            lang = str(block["lang"])
            label = get_code_label(block, research_tab)
            max_code_lines = 36 if research_tab == "ML" else 28
            body = trim_code_block(str(block["body"]), lang, max_lines=max_code_lines)
            stage_label = get_code_stage_label(block, research_tab)
            stage_line = f"**직접 해본 단계**: {stage_label}\n\n" if stage_label else ""
            if research_tab == "ML":
                api_terms = extract_ml_api_terms(str(block["body"]))
                api_line = f"**핵심 API**: {format_inline_code_list(api_terms)}\n\n" if api_terms else ""
                explanation = infer_ml_code_purpose(block)
                code_sections.append(f"### {label}\n\n{stage_line}{api_line}{explanation}\n\n```{lang}\n{body}\n```")
            else:
                explanation = describe_code_block(block, research_tab)
                code_sections.append(f"### {label}\n\n{stage_line}{explanation}\n\n```{lang}\n{body}\n```")
        code_section = "\n\n".join(code_sections)
    else:
        code_section = "실행 가능한 코드 블록은 없지만, 개념 정리나 참고 노트로서 맥락을 보존하고 있습니다."

    preview_block = "\n".join(f"> {line}" for line in preview_lines) if preview_lines else "> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다."

    bundle_lines = [
        f"- Source path: `{clean_markdown_text(source_path)}`",
        f"- Source formats: {format_inline_code_list(source_formats)}",
        f"- Companion files: {format_inline_code_list(companion_files)}",
        f"- Note type: `{note_type}`",
        f"- Last updated in the source vault: `{updated_at}`",
    ]

    if related_notes:
        bundle_lines.append(f"- Related notes: {format_inline_code_list(related_notes)}")
    if external_refs:
        bundle_lines.append(f"- External references: {format_inline_code_list(external_refs)}")

    bundle_section = "\n".join(bundle_lines)
    if research_tab != "ML" and track_source_notes:
        top_focus = [normalize_display_text(str(note["label"])) for note in track_source_notes[:3] if note.get("label")]
    else:
        top_focus = focus_display_items[:3]
    top_libraries = libraries[:5]
    if research_tab == "ML":
        intro_block = build_ml_intro_html(
            problem_summary=ml_problem_summary,
            data_summary=ml_data_summary,
            study_notes=ml_source_notes if ml_source_notes else ml_study_notes,
            outline_labels=ml_outline_labels,
            flow_items=flow_items,
            source_formats=source_formats,
            code_block_count=code_block_count,
            execution_block_count=execution_block_count,
            libraries=top_libraries,
        )
    else:
        intro_lines = [research_summary]
        if top_focus:
            intro_lines.append(f"**빠르게 볼 수 있는 포인트**: {format_korean_list(top_focus, limit=3, max_item_len=42)}.")
        intro_lines.append(f"**남겨둔 자료**: {artifact_summary}")
        if top_libraries:
            intro_lines.append(f"**주요 스택**: {format_inline_code_list(top_libraries)}")
        intro_block = "\n\n".join(intro_lines)
    artifact_line = "/".join(source_formats) if source_formats else "source"
    artifact_line = f"{artifact_line} · 코드 {code_block_count}개 · 실행 {execution_block_count}개"
    if research_tab == "ML":
        body_sections = raw_note_markdown.strip() or coverage_section
    else:
        body_sections = f"""## {coverage_title}

{coverage_section}

## {concept_title}

{concept_section}

## {flow_title}

{flow_section}

## {code_title}

{code_section}"""

    if research_tab == "ML":
        return f"""---
title: "{escape_yaml(title)}"
date: {date}
research_tab: "{research_tab}"
research_kind: "{research_kind}"
source_title: "{escape_yaml(source_title)}"
source_path: "{escape_yaml(source_path)}"
excerpt: "{escape_yaml(excerpt)}"
research_summary: "{escape_yaml(research_summary)}"
research_artifacts: "{escape_yaml(artifact_line)}"
code_block_count: {code_block_count}
execution_block_count: {execution_block_count}
{format_yaml_list("research_focus", top_focus)}
{format_yaml_list("research_stack", top_libraries)}
{format_yaml_list("source_formats", source_formats)}
tags:
  - research-archive
  - imported-note
  - {track_tag}
  - {kind_tag}
---

{intro_block}

{body_sections}
"""

    return f"""---
title: "{escape_yaml(title)}"
date: {date}
research_tab: "{research_tab}"
research_kind: "{research_kind}"
source_title: "{escape_yaml(source_title)}"
source_path: "{escape_yaml(source_path)}"
excerpt: "{escape_yaml(excerpt)}"
research_summary: "{escape_yaml(research_summary)}"
research_artifacts: "{escape_yaml(artifact_line)}"
code_block_count: {code_block_count}
execution_block_count: {execution_block_count}
{format_yaml_list("research_focus", top_focus)}
{format_yaml_list("research_stack", top_libraries)}
{format_yaml_list("source_formats", source_formats)}
tags:
  - research-archive
  - imported-note
  - {track_tag}
  - {kind_tag}
---

{intro_block}

## Snapshot

| Item | Value |
|------|-------|
{snapshot_table}

{body_sections}

## Source Bundle

{bundle_section}

## Note Preview

{preview_block}
"""


def build_note_payload(track: dict[str, str], file_path: Path, title_override: str | None = None) -> str:
    metadata, body_lines = parse_front_matter(file_path)
    structure = parse_note_structure(body_lines)
    raw_note_markdown = sanitize_raw_note_markdown("\n".join(body_lines).strip(), track["tab"])
    code_blocks = list(structure["code_blocks"])
    headings = list(structure["headings"])
    paragraphs = list(structure["paragraphs"])
    sections = list(structure["sections"])

    source_title = str(metadata.get("title") or file_path.stem)
    clean_title = normalize_display_text(title_override or "") or get_clean_title(source_title, file_path.stem)
    research_kind = get_research_kind(clean_title)
    title_keywords = build_title_anchor_keywords(clean_title, headings, sections, code_blocks)

    metadata_sections = metadata.get("section_keys", [])
    if not isinstance(metadata_sections, list):
        metadata_sections = []

    preview_lines = paragraphs[:2]
    intro_paragraphs = select_intro_paragraphs(sections, paragraphs, limit=2, title_keywords=title_keywords)
    focus_items = select_focus_items(sections, metadata_sections, headings, clean_title, limit=5, title_keywords=title_keywords)
    section_summaries = build_section_summaries(sections, metadata_sections, limit=4, title_keywords=title_keywords)
    flow_items = build_flow_items(section_summaries, focus_items, metadata_sections, limit=6)
    if track["tab"] == "ML":
        code_limit = min(max(len(code_blocks), 1), 7)
    else:
        code_limit = min(max(len(code_blocks), 1), 4)
    code_samples = select_code_blocks(code_blocks, research_tab=track["tab"], title_keywords=title_keywords, limit=code_limit)
    if track["tab"] == "ML":
        flow_items = build_ml_flow_items_from_code_samples(code_samples)
    libraries = extract_libraries(code_blocks)
    if track["tab"] == "ML":
        ml_problem_summary = build_ml_problem_summary(clean_title, sections, intro_paragraphs, focus_items, title_keywords=title_keywords)
        ml_data_summary = build_ml_data_summary(sections, section_summaries, intro_paragraphs, focus_items, title_keywords=title_keywords)
        ml_study_notes = build_ml_study_notes(
            title=clean_title,
            focus_items=focus_items,
            section_summaries=section_summaries,
            paragraphs=paragraphs,
            code_blocks=code_blocks,
            libraries=libraries,
        )
        ml_source_notes = build_ml_source_notes(sections, title_keywords=title_keywords)
        ml_outline_labels = build_ml_outline_labels(sections)
        ml_implementation_steps = build_ml_implementation_steps(code_samples)
        concept_notes = []
        track_source_notes: list[dict[str, object]] = []
    else:
        ml_problem_summary = ""
        ml_data_summary = ""
        ml_study_notes = []
        ml_source_notes = []
        ml_outline_labels = []
        ml_implementation_steps = []
        track_source_notes = build_track_source_notes(track["tab"], sections, title_keywords=title_keywords)
        if track_source_notes:
            flow_items = build_track_flow_items_from_source_notes(track_source_notes)
        concept_notes = build_concept_notes(
            research_tab=track["tab"],
            title=clean_title,
            focus_items=focus_items,
            section_summaries=section_summaries,
            paragraphs=paragraphs,
            code_blocks=code_blocks,
            libraries=libraries,
        )

    companion_files = get_companion_files(file_path)
    source_formats = [candidate.suffix.lstrip(".").lower() or candidate.name.lower() for candidate in companion_files]
    related_notes_raw = metadata.get("related_notes_auto", [])
    external_refs_raw = metadata.get("external_ref_domains", [])

    if not isinstance(related_notes_raw, list):
        related_notes_raw = [str(related_notes_raw)] if related_notes_raw else []
    if not isinstance(external_refs_raw, list):
        external_refs_raw = [str(external_refs_raw)] if external_refs_raw else []

    related_notes = unique_preserve_order([clean_reference_name(item) for item in related_notes_raw])[:5]
    external_refs = unique_preserve_order([clean_reference_name(item) for item in external_refs_raw])[:5]

    updated_at = str(metadata.get("updated_at") or datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d"))
    note_type = clean_markdown_text(str(metadata.get("note_type_auto") or "research-note"))
    companion_file_names = [candidate.name for candidate in companion_files]
    artifact_summary = build_artifact_summary(
        source_formats,
        len(code_blocks),
        sum(1 for block in code_blocks if bool(block["has_output"])),
        libraries,
    )
    if track["tab"] == "ML":
        research_summary = build_ml_research_summary(
            title=clean_title,
            study_notes=ml_source_notes if ml_source_notes else ml_study_notes,
            code_samples=code_samples,
            artifact_summary=artifact_summary,
        )
    else:
        research_summary = build_track_research_summary(
            title=clean_title,
            track=track["tab"],
            study_notes=track_source_notes,
            code_samples=code_samples,
            artifact_summary=artifact_summary,
        )
    excerpt = build_excerpt(research_summary, focus_items, clean_title)
    source_path = file_path.relative_to(KNOWLEDGE_ROOT).as_posix()

    return build_content(
        title=clean_title,
        date=datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d"),
        research_tab=track["tab"],
        research_kind=research_kind,
        source_title=source_title,
        source_path=source_path,
        excerpt=excerpt,
        track_tag=track["tag"],
        kind_tag=to_kebab(research_kind),
        code_block_count=len(code_blocks),
        execution_block_count=sum(1 for block in code_blocks if bool(block["has_output"])),
        source_formats=source_formats,
        companion_files=companion_file_names,
        research_summary=research_summary,
        artifact_summary=artifact_summary,
        focus_items=focus_items,
        section_summaries=section_summaries,
        concept_notes=concept_notes,
        ml_problem_summary=ml_problem_summary,
        ml_data_summary=ml_data_summary,
        ml_study_notes=ml_study_notes,
        ml_source_notes=ml_source_notes,
        track_source_notes=track_source_notes,
        ml_outline_labels=ml_outline_labels,
        ml_implementation_steps=ml_implementation_steps,
        flow_items=flow_items,
        code_samples=code_samples,
        libraries=libraries,
        raw_note_markdown=raw_note_markdown,
        preview_lines=preview_lines,
        related_notes=related_notes,
        external_refs=external_refs,
        note_type=note_type,
        updated_at=updated_at,
    )


def main() -> None:
    summary: list[tuple[str, int, Path]] = []

    for track in TRACKS:
        output_dir = RESEARCH_ROOT / track["folder"]
        output_dir.mkdir(parents=True, exist_ok=True)
        title_overrides = collect_existing_title_overrides(output_dir)

        for old_file in output_dir.glob("imported-*.md"):
            old_file.unlink()

        files = sorted(track["source"].glob("*.md"))
        for index, file_path in enumerate(files, start=1):
            source_path = file_path.relative_to(KNOWLEDGE_ROOT).as_posix()
            content = build_note_payload(track, file_path, title_override=title_overrides.get(source_path))
            output_path = output_dir / f'imported-{track["tag"]}-{index:03d}.md'
            output_path.write_text(content, encoding="utf-8")

        summary.append((track["tab"], len(files), output_dir))

    for tab, count, output_dir in summary:
        print(f"{tab}: {count} files -> {output_dir}")


if __name__ == "__main__":
    main()
