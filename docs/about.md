---
layout: default
title: About
nav_order: 2
description: "About LLM Alignment Arxiv Daily tracker"
permalink: /about
---

# About This Project

## 🎯 Purpose

The LLM Alignment Arxiv Daily tracker automatically monitors and organizes the latest research papers in LLM / VLM alignment, AI safety, and related alignment domains from arXiv.

## 🔄 How It Works

1. **Automated Fetching**: GitHub Actions runs every 24 hours to fetch new papers
2. **Smart Categorization**: Papers are organized into 12 research domains
3. **Code Links**: Automatically finds associated GitHub repositories
4. **Web Display**: Beautiful, searchable interface with sidebar navigation

## 📊 Coverage

We track papers from these arXiv categories:
- **cs.AI** - Artificial Intelligence
- **cs.LG** - Machine Learning
- **cs.CV** - Computer Vision (multimodal & VLM research)
- **cs.CL** - Computation and Language (LLMs and NLP alignment)
- **cs.HC** - Human-Computer Interaction (human oversight research)
- **cs.RO** - Robotics (multi-agent and safety research)
- **cs.CY** - Computers and Society (AI ethics and governance)

## 🚀 Features

### Automatic Updates
- Updates every 24 hours via GitHub Actions
- Fetches latest papers from arXiv API
- Updates code repository links weekly

### Smart Organization
- 12 specialized LLM alignment categories
- 150+ carefully curated alignment keywords
- Relevance-based filtering

### User-Friendly Interface
- Searchable paper database
- Sidebar navigation for easy browsing
- Responsive design for mobile/desktop [_mobile version suspended due to personal exhaustion_]

### Open Source
- Fully customizable configuration
- Easy to fork and adapt
- Documented codebase

## 🛠️ Technology Stack

- **Backend**: Python, arXiv API
- **Frontend**: Jekyll, GitHub Pages
- **Theme**: Just the Docs (customized)
- **Automation**: GitHub Actions
- **Deployment**: GitHub Pages (root directory)

## 📈 Statistics

- **12** Research Domains
- **150+** Keywords
- **Daily** Updates
- **15** Papers per topic (configurable)

## 🤝 Contributing

Contributions are welcome! Ways to contribute:

1. **Add Keywords**: Suggest new research topics
2. **Improve Filters**: Refine search queries
3. **Report Issues**: Found a bug? Let us know
4. **Documentation**: Help improve guides


## 📄 License

This project is provided for research and educational purposes, under MIT license.

## 🙏 Acknowledgments

- [arXiv](https://arxiv.org/) for open access to research
- [Papers with Code](https://paperswithcode.com/) for code links
- [Just the Docs](https://just-the-docs.github.io/just-the-docs/) theme

## 📧 Contact

- **GitHub**: [@Ezharjan](https://github.com/Ezharjan)
- **Email**: mysoft@111.com
- **Issues**: [Report here](https://github.com/Ezharjan/DailyLLMAlignmentArxiv/issues)

---

Last updated: {{ "now" | date: "%Y-%m-%d" }}
