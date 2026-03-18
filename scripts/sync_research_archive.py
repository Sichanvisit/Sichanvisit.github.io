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


def escape_yaml(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def sanitize_plain_text(text: str) -> str:
    clean = text.replace("|", "/")
    clean = re.sub(r"\s+", " ", clean)
    return clean.strip()


def to_kebab(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "archive-note"


def get_research_kind(name: str) -> str:
    if "스프린트" in name:
        return "Sprint Mission"
    if "Mission" in name or "미션" in name:
        return "Mission"
    if any(keyword in name for keyword in ("실습", "코드실습", "코딩실습")):
        return "Practice"
    if any(keyword in name for keyword in ("공유", "강사공유")):
        return "Shared Note"
    if "sample" in name.lower() or "샘플" in name:
        return "Sample Code"
    return "Archive Note"


def get_clean_title(base_name: str) -> str:
    title = base_name
    title = re.sub(r"^\d{6,8}[_-]*", "", title)
    title = re.sub(r"^\d+-\d+\s*", "", title)
    title = re.sub(r"^\[[^\]]+\]\s*", "", title)
    title = re.sub(r"^\([^)]+\)\s*", "", title)
    title = title.replace("_", " ")
    title = re.sub(r"\s*-\s*공유$", "", title)
    title = re.sub(r"\s*-\s*AI\s*5.*?강사 답안$", "", title)
    title = re.sub(r"\s*-\s*AI5.*?강사 답안$", "", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title or base_name


def strip_front_matter(lines: list[str]) -> list[str]:
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                return lines[index + 1 :]
    return lines


def get_snippet(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    lines = strip_front_matter(lines)
    collected: list[str] = []
    in_code_block = False

    for line in lines:
        trimmed = line.strip()
        if trimmed.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block or not trimmed:
            continue
        if trimmed.startswith("<!--"):
            continue
        if "data:image" in trimmed:
            continue

        trimmed = re.sub(r"^#+\s*", "", trimmed)
        trimmed = sanitize_plain_text(trimmed)
        if not trimmed:
            continue

        if len(trimmed) > 170:
            trimmed = trimmed[:167].rstrip() + "..."

        collected.append(trimmed)
        if len(collected) >= 2:
            break

    if not collected:
        return "원본 노트는 현재 내용 미리보기를 제공하지 않습니다."

    return " / ".join(collected)


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
    snippet: str,
) -> str:
    table_source_title = sanitize_plain_text(title)
    table_source_path = sanitize_plain_text(source_path)
    snippet_text = sanitize_plain_text(snippet)

    return f"""---
title: "{escape_yaml(title)}"
date: {date}
research_tab: "{research_tab}"
research_kind: "{research_kind}"
source_title: "{escape_yaml(source_title)}"
source_path: "{escape_yaml(source_path)}"
excerpt: "{escape_yaml(excerpt)}"
tags:
  - research-archive
  - imported-note
  - {track_tag}
  - {kind_tag}
---

## Archive Note

이 글은 개인 실습 저장소에 있던 원본 노트를 `research` 컬렉션에서 구별해 보기 쉽게 정리한 아카이브 엔트리입니다.  
대표 항목은 이후 별도 케이스 스터디로 확장하고, 현재 단계에서는 전체 실습 흐름을 빠르게 탐색할 수 있도록 메타데이터 중심으로 정리했습니다.

| Item | Value |
|------|-------|
| Track | {research_tab} |
| Type | {research_kind} |
| Source Title | `{table_source_title}` |
| Source Path | `{table_source_path}` |

## Source Glimpse

> {snippet_text}

## Notes

- 원본 파일은 수업 실습, 스프린트 미션, 강사 공유, 샘플 코드 중 하나로 분류했습니다.
- 현재 공개 블로그에서는 구분과 탐색을 우선하고, 의미 있는 항목부터 순차적으로 본문을 더 다듬을 예정입니다.
- 같은 탭 안에서도 `type` 배지로 미션과 실습을 바로 구별할 수 있게 구성했습니다.
"""


def main() -> None:
    summary: list[tuple[str, int, Path]] = []

    for track in TRACKS:
        output_dir = RESEARCH_ROOT / track["folder"]
        output_dir.mkdir(parents=True, exist_ok=True)

        for old_file in output_dir.glob("imported-*.md"):
            old_file.unlink()

        files = sorted(track["source"].glob("*.md"))
        for index, file_path in enumerate(files, start=1):
            kind = get_research_kind(file_path.stem)
            date_text = datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d")
            content = build_content(
                title=get_clean_title(file_path.stem),
                date=date_text,
                research_tab=track["tab"],
                research_kind=kind,
                source_title=file_path.stem,
                source_path=file_path.relative_to(KNOWLEDGE_ROOT).as_posix(),
                excerpt=f'{track["tab"]} {kind} 아카이브 엔트리입니다. 원본 실습 노트를 공개 research 섹션에서 구별하기 쉽게 정리한 카드입니다.',
                track_tag=track["tag"],
                kind_tag=to_kebab(kind),
                snippet=get_snippet(file_path),
            )
            output_path = output_dir / f'imported-{track["tag"]}-{index:03d}.md'
            output_path.write_text(content, encoding="utf-8")

        summary.append((track["tab"], len(files), output_dir))

    for tab, count, output_dir in summary:
        print(f"{tab}: {count} files -> {output_dir}")


if __name__ == "__main__":
    main()
