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

    current_heading = "Overview"
    current_paragraph: list[str] = []
    in_code_block = False
    block_info = ""
    block_heading = current_heading
    block_lines: list[str] = []
    block_has_output = False

    def flush_paragraph() -> None:
        if not current_paragraph:
            return
        text = clean_markdown_text(" ".join(current_paragraph))
        current_paragraph.clear()
        if text:
            paragraphs.append(text)

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
                    }
                )
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
            heading_text = clean_markdown_text(heading_match.group(2))
            if heading_text:
                headings.append(heading_text)
                current_heading = heading_text
            continue

        quote_text = stripped.lstrip("> ").strip()
        if quote_text:
            current_paragraph.append(quote_text)

    flush_paragraph()

    return {
        "headings": unique_preserve_order(headings),
        "paragraphs": paragraphs,
        "code_blocks": code_blocks,
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


def build_excerpt(
    paragraphs: list[str],
    headings: list[str],
    metadata_items: list[str],
    track: str,
    kind: str,
) -> str:
    for paragraph in paragraphs:
        if len(paragraph) >= 24:
            return trim_text(paragraph, 150)
    if headings:
        return trim_text(f"{track} {kind}: " + ", ".join(headings[:3]), 150)
    if metadata_items:
        return trim_text(f"{track} {kind}: " + ", ".join(metadata_items[:3]), 150)
    return f"{track} {kind} note with implementation details and archived source context."


def trim_text(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def select_focus_items(
    metadata_items: list[str],
    headings: list[str],
    title: str,
    limit: int,
) -> list[str]:
    source = metadata_items if metadata_items else headings
    cleaned_items: list[str] = []
    seen: set[str] = set()
    normalized_title = clean_markdown_text(title).lower()

    for item in source:
        cleaned = clean_markdown_text(item)
        if not cleaned:
            continue
        lower_cleaned = cleaned.lower()
        if lower_cleaned == normalized_title:
            continue
        if lower_cleaned in seen:
            continue
        seen.add(lower_cleaned)
        cleaned_items.append(cleaned)
        if len(cleaned_items) >= limit:
            break

    return cleaned_items


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
    heading = clean_markdown_text(str(block["heading"]))
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
    selected_indexes = sorted(index for index, _ in ranked[:limit])
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
    focus_items: list[str],
    flow_items: list[str],
    code_samples: list[dict[str, object]],
    libraries: list[str],
    preview_lines: list[str],
    related_notes: list[str],
    external_refs: list[str],
    note_type: str,
    updated_at: str,
) -> str:
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

    if focus_items:
        focus_section = "\n".join(f"- {item}" for item in focus_items)
    else:
        focus_section = f"- This archived note is categorized as `{research_kind}` under `{research_tab}`."

    if flow_items:
        flow_section = "\n".join(f"{index}. {item}" for index, item in enumerate(flow_items, start=1))
    else:
        flow_section = "1. Review the archived source note.\n2. Inspect the main implementation blocks.\n3. Reuse the extracted approach in a full project page if needed."

    if code_samples:
        code_sections = []
        for block in code_samples:
            lang = str(block["lang"])
            label = get_code_label(block)
            body = trim_code_block(str(block["body"]), lang)
            code_sections.append(f"### {label}\n\n```{lang}\n{body}\n```")
        code_section = "\n\n".join(code_sections)
    else:
        code_section = "No executable code block was detected in the source note. This entry is preserved as a concept or reference note."

    preview_block = "\n".join(f"> {line}" for line in preview_lines) if preview_lines else "> No prose preview was available in the source note."

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

## Snapshot

| Item | Value |
|------|-------|
{snapshot_table}

## What I Worked On

{focus_section}

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

    source_title = str(metadata.get("title") or file_path.stem)
    clean_title = get_clean_title(source_title, file_path.stem)
    research_kind = get_research_kind(clean_title)

    metadata_sections = metadata.get("section_keys", [])
    if not isinstance(metadata_sections, list):
        metadata_sections = []

    preview_lines = paragraphs[:2]
    focus_items = select_focus_items(metadata_sections, headings, clean_title, limit=5)
    flow_items = select_focus_items(metadata_sections, headings, clean_title, limit=6)
    code_samples = select_code_blocks(code_blocks, limit=2)
    libraries = extract_libraries(code_blocks)

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
    excerpt = build_excerpt(paragraphs, headings, focus_items, track["tab"], research_kind)
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
        focus_items=focus_items,
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
