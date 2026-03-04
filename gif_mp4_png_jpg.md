# GitHub Blog 시각 자료 적용 가이드 (MP4, GIF, PNG, JPG)

이 문서는 현재 레포(`Sichanvisit.github.io`) 기준으로, 프로젝트 글에 시각 자료를 넣는 실전 가이드다.

## 1) 핵심 원칙

- 카드 썸네일: `PNG/JPG/WebP` 같은 정적 이미지 사용
- 본문 데모: `MP4` 우선 사용 (용량/속도 이점)
- GitHub README: 필요하면 `GIF` 사용

현재 카드 템플릿은 `header.teaser`를 썸네일로 읽는다.  
즉, 카드 영역에는 동영상이 아니라 이미지 파일을 넣는 것이 맞다.

## 2) 폴더 구조 (이 레포 기준)

```text
assets/
  images/
    portfolio/
      advanced-thumb.jpg
      rag-thumb.jpg
  videos/
    advanced-demo.mp4
    rag-demo.mp4
```

- 썸네일 이미지: `assets/images/portfolio/`
- 본문 데모 영상: `assets/videos/`

## 3) 변환 명령 (Windows + ffmpeg)

### MP4 최적화 (블로그 본문용)

```bash
ffmpeg -i "input.mp4" -vf "fps=24,scale=960:-2" -c:v libx264 -crf 26 -preset medium -movflags +faststart -an "demo_blog.mp4"
```

- `crf 23~28`: 숫자 클수록 용량 작아짐
- `-an`: 오디오 제거
- `+faststart`: 웹 스트리밍 시작 빠르게

### GIF 생성 (README용)

```bash
ffmpeg -i "input.mp4" -vf "fps=12,scale=720:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" "demo_readme.gif"
```

## 4) 포트폴리오 카드에 적용 (front matter)

`_portfolio/*.md` 파일 상단에 아래처럼 넣는다.

```yaml
---
title: "Project Name"
date: 2026-03-04
priority: 1
excerpt: "프로젝트 요약"
header:
  teaser: /assets/images/portfolio/advanced-thumb.jpg
frontend_url: "https://your-frontend-page.com"
github_url: "https://github.com/your/repo"
---
```

설명:
- `header.teaser`: 카드 썸네일 이미지
- `frontend_url`: 카드 클릭/버튼에서 프론트 페이지로 이동
- `github_url`: GitHub 버튼 노출

## 5) 본문에 MP4/GIF 넣는 방법

### MP4 권장 (포트폴리오 글 본문)

```html
<video controls autoplay loop muted playsinline style="width:100%; max-width: 960px; border-radius: 12px;">
  <source src="/assets/videos/advanced-demo.mp4" type="video/mp4">
</video>
```

### GIF 삽입

```markdown
![demo](/assets/images/portfolio/advanced-demo.gif)
```

## 6) 지금 블로그에 바로 적용 순서

1. 썸네일 이미지 준비: `assets/images/portfolio/*.jpg`
2. 데모 영상 변환: `ffmpeg`로 `assets/videos/*.mp4` 생성
3. 각 `_portfolio/*.md`에 `header.teaser`, `frontend_url` 추가
4. 각 글 본문에 `<video>` 블록 삽입
5. 커밋 후 푸시

## 7) 빠른 체크리스트

- 카드 이미지가 너무 크면: 가로 1200px 이하로 리사이즈
- MP4 하나당 2~8MB 정도 유지
- GIF는 가능하면 README 전용으로만 사용
- 모바일 확인: `playsinline`, `muted` 유지

