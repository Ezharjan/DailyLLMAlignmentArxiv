# LLM Alignment Arxiv Daily - Mobile Edition

A lightweight, mobile-optimized interface for browsing daily LLM alignment papers from arXiv.

## Features

- **Mobile-First Design**: Optimized for touch and vertical scrolling
- **Real-Time Data**: Automatically fetches latest papers from `../alignment-arxiv-daily.json`
- **Category Filtering**: Horizontal swipe navigation for paper categories
- **Search**: Instant client-side search across titles and authors
- **Clean UI**: No overlapping elements, simple card-based layout
- **Fast Loading**: Minimal dependencies, pure HTML/CSS/JS

## How It Works

The mobile site automatically reads paper data from the parent directory's JSON file (`alignment-arxiv-daily.json`), which is updated daily via GitHub Actions. No server-side processing needed.

## Access

Open `mobile/index.html` in any browser or deploy to:
- GitHub Pages: `https://ezharjan.github.io/DailyLLMAlignmentArxiv/mobile/`
- Local: `file:///path/to/docs/mobile/index.html`

## Compatibility

- iOS Safari 12+
- Chrome/Edge Mobile
- Firefox Mobile
- Any modern mobile browser with ES6 support

## Structure

```
mobile/
├── index.html       # Single-page mobile app (self-contained)
└── README.md        # This file
```

No build process required. The entire mobile site is a single HTML file with inline CSS and JavaScript.
