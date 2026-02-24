# 🤖 LLM Alignment Arxiv Daily

[![Daily Update](https://github.com/Ezharjan/DailyLLMAlignmentArxiv/workflows/Run%20LLM%20Alignment%20Arxiv%20Papers%20Daily/badge.svg)](https://github.com/Ezharjan/DailyLLMAlignmentArxiv/actions)
[![License](https://img.shields.io/github/license/Ezharjan/DailyLLMAlignmentArxiv)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Ezharjan/DailyLLMAlignmentArxiv)](https://github.com/Ezharjan/DailyLLMAlignmentArxiv/commits/main)

> **Automatically tracking the latest research papers in LLM / VLM Alignment, AI Safety, and related domains from arXiv**

📊 **12 Research Domains** | 🔄 **Daily Updates** | 🤖 **Fully Automated** | 🌐 **[Live Website](https://Ezharjan.github.io/DailyLLMAlignmentArxiv/)**

---

## 📋 Table of Contents

- [🎯 About](#-about)
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [🎓 Usage](#-usage)
- [⚙️ Configuration](#️-configuration)
- [🌐 Deployment](#-deployment)
- [📚 Research Domains](#-research-domains)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🤝 Contributing](#-contributing)

---

## 🎯 About

**LLM Alignment Arxiv Daily** is an automated research paper tracking system that:

- 📰 **Fetches** latest papers from arXiv every 24 hours
- 🎯 **Filters** by 150+ alignment keywords across 12 domains
- 🔗 **Links** to code repositories when available
- 📊 **Organizes** papers by research domain
- 🌐 **Publishes** to a beautiful website with search

Perfect for researchers, AI safety experts, and alignment enthusiasts who want to stay updated on:
- Deception and collusion in LLMs
- Coherence and self-improvement
- Reward hacking prevention
- AI safety mechanisms
- Constitutional AI
- And more!

**Last Updated**: Auto-generated daily at 9:00 AM UTC

---

## ✨ Features

### 🤖 Fully Automated
- ✅ Daily arXiv paper fetching via GitHub Actions
- ✅ Automatic commit and website deployment
- ✅ Weekly code repository link updates
- ✅ Zero manual intervention required

### 🎨 Beautiful Web Interface
- ✅ Modern Jekyll theme with search
- ✅ Mobile-responsive design
- ✅ Dark/light mode support
- ✅ Sidebar navigation by domain
- ✅ Quick stats dashboard

### 🔍 Smart Organization
- ✅ 12 comprehensive alignment domains
- ✅ 150+ curated research keywords
- ✅ Automatic categorization
- ✅ Code repository detection
- ✅ JSON data export

### ⚡ Easy Customization
- ✅ Simple YAML configuration
- ✅ Add your own topics/keywords
- ✅ Adjustable paper count
- ✅ Configurable update schedule
- ✅ Interactive local testing

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip
- Git (for GitHub deployment)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Ezharjan/DailyLLMAlignmentArxiv.git
cd DailyLLMAlignmentArxiv

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run interactive test
python test_local.py
# Choose option 1 for quick test

# 4. Check results
cat README.md
```

That's it! The script will fetch papers and generate the paper list.

---

## 🎓 Usage

### Local Testing

#### Interactive Mode (Recommended)
```bash
python test_local.py
```

**Options:**
1. **Quick test** - 2 topics, 5 papers (30 seconds)
2. **Full test** - All 12 topics (2-5 minutes)
3. **Update links** - Refresh code repository links

#### Direct Execution
```bash
# Fetch all papers
python daily_arxiv.py

# Update code links only
python daily_arxiv.py --update_paper_links
```

### Generated Files
- `README.md` - Main paper list (table format)
- `docs/index.md` - Web-friendly version
- `docs/alignment-arxiv-daily.json` - Complete data
- `docs/alignment-arxiv-daily-web.json` - Web-optimized data

---

## ⚙️ Configuration

### Basic Settings

Edit `config.yaml`:

```yaml
# How many papers per topic
max_results: 15

# Your GitHub info (for deployment)
user_name: "YourGitHubUsername"
repo_name: "DailyLLMAlignmentArxiv"

# Base directory (usually /docs for GitHub Pages)
base_url: "https://yourusername.github.io/DailyLLMAlignmentArxiv/"
```

### Adding Research Topics

```yaml
keywords:
    "Your Topic Name":
        filters: ["keyword 1", "keyword 2", "multi word phrase"]
```

**Example:**

```yaml
keywords:
    "Deception in LLMs":
        filters: 
            - "LLM Deception"
            - "Language Model Deception"
            - "AI Deception"
            - "Misleading LLMs"
            - "Deceptive AI"
```

### Adjusting Paper Count

- **5-10**: Focused, high-quality (faster)
- **15-20**: Balanced (recommended)
- **20+**: Comprehensive (may include tangential)

### Update Schedule

Edit `.github/workflows/alignment-arxiv-daily.yml`:

```yaml
schedule:
  - cron: "0 2 * * *"  # Daily at 2 AM UTC
```

Change to:
- `"0 */12 * * *"` - Every 12 hours
- `"0 0 */2 * *"` - Every 2 days
- `"0 0 * * 1,4"` - Monday & Thursday

Use [crontab.guru](https://crontab.guru/) for custom schedules.

---

## 🌐 Deployment

### GitHub Pages (Recommended)

#### 1. Fork or Create Repository
```bash
git add .
git commit -m "Initial commit: LLM Alignment Arxiv Daily"
git push origin main
```

#### 2. Update Configuration

**Edit `.github/workflows/alignment-arxiv-daily.yml`:**
```yaml
env:
  GITHUB_USER_NAME: YourUsername  # Change this
  GITHUB_USER_EMAIL: your@email.com
```

**Edit `config.yaml`:**
```yaml
user_name: "YourUsername"  # Change this
```

#### 3. Enable GitHub Actions
1. Settings → Actions → General
2. Workflow permissions: **Read and write**
3. Save

#### 4. Enable GitHub Pages
1. Settings → Pages
2. Source: **Deploy from branch**
3. Branch: `main`, Folder: `/docs`
4. Save

#### 5. Trigger First Run
1. Actions tab
2. "Run LLM Alignment Arxiv Papers Daily"
3. "Run workflow"

Your site: `https://yourusername.github.io/DailyLLMAlignmentArxiv/`

---

## 📚 Research Domains

Current tracking covers 12 comprehensive LLM alignment domains:

<details>
<summary><strong>🕵️ Deception in LLMs</strong></summary>

- LLM deception mechanisms
- Misleading language models
- AI manipulation techniques
- Deceptive AI behaviors
- Alignment deception
</details>

<details>
<summary><strong>🤝 Collusion in LLMs</strong></summary>

- LLM collusion strategies
- Multi-agent AI cooperation
- Collaborative AI systems
- Alignment collusion
- Teamwork in AI
</details>

<details>
<summary><strong>🔗 Coherence in LLMs</strong></summary>

- Language model coherence
- Self-improvement coherence
- Consistency in AI
- Coherent AI systems
- Alignment coherence
</details>

<details>
<summary><strong>🎯 Reward Hacking</strong></summary>

- Reward tampering techniques
- Spontaneous reward hacking
- Iterative self-refinement hacking
- AI reward manipulation
- Safety reward hacking
</details>

<details>
<summary><strong>⚖️ AI Alignment Techniques</strong></summary>

- Value alignment methods
- Human-AI alignment
- Constitutional AI
- Alignment training
- Safety alignment
</details>

<details>
<summary><strong>🔍 Unsupervised Elicitation</strong></summary>

- LLM elicitation techniques
- Unsupervised learning alignment
- AI capability elicitation
- Elicitation methods
- Alignment elicitation
</details>

<details>
<summary><strong>🚀 Self-Improvement in AI</strong></summary>

- AI self-improvement
- Recursive improvement
- Iterative refinement
- Self-enhancing AI
- Coherence optimization
</details>

<details>
<summary><strong>👁️ VLM Alignment</strong></summary>

- Vision-language model alignment
- Multimodal alignment
- Vision-language safety
- Visual AI alignment
- Image-text alignment
</details>

<details>
<summary><strong>🛡️ AI Safety Mechanisms</strong></summary>

- LLM safety protocols
- Alignment safety
- Safe AI development
- AI risk mitigation
- Safety training
</details>

<details>
<summary><strong>⚔️ Adversarial Attacks on Alignment</strong></summary>

- Alignment vulnerabilities
- Jailbreaking LLMs
- Prompt injection
- AI adversarial attacks
- Alignment robustness
</details>

<details>
<summary><strong>👀 Scalable Oversight</strong></summary>

- AI oversight methods
- Scalable supervision
- Human oversight
- AI monitoring
- Alignment verification
</details>

<details>
<summary><strong>📜 Constitutional AI</strong></summary>

- AI constitutions
- Self-constitutional AI
- Rule-based alignment
- AI ethics
- Principled AI
</details>

---

## 🛠️ Troubleshooting

### Installation Issues

**"Import arxiv could not be resolved"**
```bash
pip install arxiv requests pyyaml
```

**"Python not found"**
```bash
# Install Python 3.7+ from python.org
# Verify: python --version
```

### Paper Fetching Issues

**"No papers found"**
- Check internet connection
- Increase `max_results` in config.yaml (try 20)
- Use broader keywords

**"Papers not relevant"**
- Edit config.yaml keywords
- Add specific domain terms: "alignment", "safety", "deception", "coherence"
- Review and refine filters

**"SSL/Connection errors"**
- Handled gracefully with warnings
- Papers save even if code link fetch fails
- Check firewall/proxy settings if persistent

### GitHub Actions Issues

**"Workflow not running"**
1. Enable Actions (Settings → Actions)
2. Grant write permissions
3. Check YAML syntax
4. View Actions tab for errors

**"Permission denied"**
- Settings → Actions → General
- Workflow permissions: **Read and write**

**"Website not updating"**
- Wait 2-5 minutes after Action completes
- Check Pages settings (should show "Active")
- Clear browser cache

### Data Quality Issues

**"Too many irrelevant papers"**
- Reduce `max_results` (try 10)
- Use more specific keywords
- Add negative filters (if needed)

**"Missing important papers"**
- Increase `max_results` (try 20-25)
- Add broader synonym keywords
- Check arXiv categories are correct

---

## 🤝 Contributing

We welcome contributions! Here's how:

### Adding Keywords

1. Fork the repository
2. Edit `config.yaml`
3. Test locally: `python test_local.py`
4. Submit pull request

### Reporting Issues

Found a bug? [Open an issue](https://github.com/Ezharjan/DailyLLMAlignmentArxiv/issues) with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

### Suggesting Features

Have an idea? [Start a discussion](https://github.com/Ezharjan/DailyLLMAlignmentArxiv/discussions) about:
- New research domains
- UI improvements
- Additional features
- Integration ideas

---

## 📊 Statistics

- **Research Domains**: 12
- **Keywords**: 150+
- **Papers per Day**: ~50-100 (varies)
- **Update Frequency**: Every 24 hours
- **Auto-update Schedule**: 9:00 AM UTC
- **Link Updates**: Weekly (Mondays)

---

## 📞 Support

- 📖 **Documentation**: See files in this repo
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Ezharjan/DailyLLMAlignmentArxiv/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Ezharjan/DailyLLMAlignmentArxiv/discussions)
- 📧 **Email**: mysoft@111.com

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file.

---

## 🙏 Acknowledgments

- arXiv API for paper access
- Papers with Code for repository links
- GitHub Actions for automation
- Jekyll and Just the Docs theme

---

## 🔗 Links

- 🌐 **Live Website**: https://Ezharjan.github.io/DailyLLMAlignmentArxiv/
- 📦 **GitHub Repo**: https://github.com/Ezharjan/DailyLLMAlignmentArxiv
- 📊 **JSON Data**: [alignment-arxiv-daily.json](docs/alignment-arxiv-daily.json)
- 📘 **Detailed Usage**: [docs/README.md](docs/README.md)

---

<div align="center">

## 🎉 Happy Researching!

**Stay updated with the latest in LLM / VLM Alignment and AI Safety**

Made with ❤️ for the research community

</div>

---
