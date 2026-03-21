from __future__ import annotations

from datetime import datetime
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
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
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


def normalize_display_text(text: str) -> str:
    cleaned = clean_markdown_text(text)
    cleaned = cleaned.replace("**", "").replace("__", "")
    cleaned = re.sub(r"^\d+(?:\.\d+)*[\.\)]\s+", "", cleaned)
    cleaned = re.sub(r"^[A-Za-z]\.\s*", "", cleaned)
    cleaned = cleaned.strip(":- ")
    return compact_spaces(cleaned)


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
    "지침": "Problem Brief",
    "데이터셋 설명": "Dataset Context",
    "가이드라인": "Implementation Guide",
    "환경준비": "Environment Setup",
    "import": "Imports",
    "gpu 설정": "Runtime Setup",
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
    current_paragraph: list[str] = []
    in_code_block = False
    block_info = ""
    block_heading = current_heading
    block_lines: list[str] = []
    block_has_output = False
    current_section: dict[str, object] = {
        "heading": current_heading,
        "paragraphs": [],
        "code_blocks": [],
    }

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
            continue

        if in_code_block:
            block_lines.append(raw_line.rstrip("\n"))
            continue

        if not stripped:
            flush_paragraph()
            continue

        if stripped.startswith("<!--"):
            continue

        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            flush_paragraph()
            flush_section()
            heading_text = clean_markdown_text(heading_match.group(2))
            if heading_text:
                headings.append(heading_text)
                current_heading = heading_text
                current_section = {
                    "heading": heading_text,
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
) -> list[str]:
    candidates: list[str] = []

    for section in sections:
        for paragraph in section.get("paragraphs", []):
            normalized = normalize_display_text(str(paragraph))
            if not is_meaningful_sentence(normalized):
                continue
            candidates.append(trim_text(normalized, 190))
            break

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
) -> list[str]:
    normalized_title = normalize_display_text(title).lower()
    candidates: list[str] = []

    for section in sections:
        for paragraph in section.get("paragraphs", []):
            normalized = normalize_display_text(str(paragraph))
            if normalized and normalized.lower() != normalized_title and is_meaningful_sentence(normalized):
                candidates.append(trim_text(normalized, 150))
                break

        heading = condense_focus_item(str(section.get("heading", "")), max_len=42)
        if heading and heading.lower() != normalized_title and not is_generic_label(heading):
            candidates.append(heading)

    for item in metadata_items + headings:
        normalized = condense_focus_item(item, max_len=52)
        if not normalized or normalized.lower() == normalized_title:
            continue
        if is_generic_label(normalized):
            continue
        if should_skip_focus_item(normalized):
            continue
        candidates.append(normalized)

    return unique_cleaned_items(candidates, limit=limit)


def build_section_summaries(
    sections: list[dict[str, object]],
    metadata_items: list[str],
    limit: int,
) -> list[dict[str, str]]:
    summaries: list[dict[str, str]] = []
    seen_titles: set[str] = set()

    for section in sections:
        raw_title = str(section.get("heading", ""))
        title = normalize_section_title(raw_title)
        summary_text = ""

        for paragraph in section.get("paragraphs", []):
            normalized = normalize_display_text(str(paragraph))
            if is_meaningful_sentence(normalized):
                summary_text = trim_text(normalized, 220)
                break

        if not summary_text:
            continue
        if not title:
            title = "Key Step"

        title_key = title.lower()
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)
        summaries.append({"title": title, "summary": summary_text or trim_text(title, 180)})
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
        lead = research_summary.split(". ")[0]
        return trim_text(lead, 170)
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

    return score


def get_code_label(block: dict[str, object]) -> str:
    heading = normalize_display_text(str(block["heading"]))
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


def describe_code_block(block: dict[str, object]) -> str:
    label = get_code_label(block)
    comments = extract_comment_clues(str(block["body"]))
    context = normalize_display_text(str(block.get("context", "")))
    intro = ""
    if label and label.lower() not in {"code highlight", "overview"}:
        intro = f"`{label}`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다."

    if comments:
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


def select_code_blocks(code_blocks: list[dict[str, object]], limit: int = 2) -> list[dict[str, object]]:
    ranked = sorted(
        enumerate(code_blocks),
        key=lambda item: (-score_code_block(item[1]), item[0]),
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
    files = sorted(candidate for candidate in path.parent.glob(f"{path.stem}.*") if candidate.is_file())
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
    for rule in CONCEPT_RULES:
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
    flow_items: list[str],
    code_samples: list[dict[str, object]],
    libraries: list[str],
    preview_lines: list[str],
    related_notes: list[str],
    external_refs: list[str],
    note_type: str,
    updated_at: str,
) -> str:
    focus_display_items = unique_cleaned_items([condense_focus_item(item, max_len=60) for item in focus_items], limit=5)
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

    if section_summaries and any(entry["title"] != "Key Step" for entry in section_summaries):
        coverage_section = "\n\n".join(
            f"### {entry['title']}\n\n{entry['summary']}"
            for entry in section_summaries
        )
    else:
        coverage_section = focus_section

    if flow_items:
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
            label = get_code_label(block)
            body = trim_code_block(str(block["body"]), lang)
            explanation = describe_code_block(block)
            code_sections.append(f"### {label}\n\n{explanation}\n\n```{lang}\n{body}\n```")
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
    top_focus = focus_display_items[:3]
    top_libraries = libraries[:5]
    intro_lines = [research_summary]
    if top_focus:
        intro_lines.append(f"**빠르게 볼 수 있는 포인트**: {format_korean_list(top_focus, limit=3, max_item_len=42)}.")
    intro_lines.append(f"**남겨둔 자료**: {artifact_summary}")
    if top_libraries:
        intro_lines.append(f"**주요 스택**: {format_inline_code_list(top_libraries)}")
    intro_block = "\n\n".join(intro_lines)
    artifact_line = "/".join(source_formats) if source_formats else "source"
    artifact_line = f"{artifact_line} · 코드 {code_block_count}개 · 실행 {execution_block_count}개"

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

## What This Note Covers

{coverage_section}

## Why This Matters

{concept_section}

## Implementation Flow

{flow_section}

## Code Highlights

{code_section}

## Source Bundle

{bundle_section}

## Note Preview

{preview_block}
"""


def build_note_payload(track: dict[str, str], file_path: Path) -> str:
    metadata, body_lines = parse_front_matter(file_path)
    structure = parse_note_structure(body_lines)
    code_blocks = list(structure["code_blocks"])
    headings = list(structure["headings"])
    paragraphs = list(structure["paragraphs"])
    sections = list(structure["sections"])

    source_title = str(metadata.get("title") or file_path.stem)
    clean_title = get_clean_title(source_title, file_path.stem)
    research_kind = get_research_kind(clean_title)

    metadata_sections = metadata.get("section_keys", [])
    if not isinstance(metadata_sections, list):
        metadata_sections = []

    preview_lines = paragraphs[:2]
    intro_paragraphs = select_intro_paragraphs(sections, paragraphs, limit=2)
    focus_items = select_focus_items(sections, metadata_sections, headings, clean_title, limit=5)
    section_summaries = build_section_summaries(sections, metadata_sections, limit=4)
    flow_items = build_flow_items(section_summaries, focus_items, metadata_sections, limit=6)
    code_limit = 3 if len(code_blocks) >= 3 else max(len(code_blocks), 1)
    code_samples = select_code_blocks(code_blocks, limit=code_limit)
    libraries = extract_libraries(code_blocks)
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
    research_summary = build_research_summary(
        clean_title,
        track["tab"],
        research_kind,
        intro_paragraphs,
        focus_items,
        artifact_summary,
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
        flow_items=flow_items,
        code_samples=code_samples,
        libraries=libraries,
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

        for old_file in output_dir.glob("imported-*.md"):
            old_file.unlink()

        files = sorted(track["source"].glob("*.md"))
        for index, file_path in enumerate(files, start=1):
            content = build_note_payload(track, file_path)
            output_path = output_dir / f'imported-{track["tag"]}-{index:03d}.md'
            output_path.write_text(content, encoding="utf-8")

        summary.append((track["tab"], len(files), output_dir))

    for tab, count, output_dir in summary:
        print(f"{tab}: {count} files -> {output_dir}")


if __name__ == "__main__":
    main()
