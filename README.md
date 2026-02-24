# 🏥 Health Computing Arxiv Daily

[![Daily Update](https://github.com/Ezharjan/DailyHealthArxiv/workflows/Run%20Health%20Arxiv%20Papers%20Daily/badge.svg)](https://github.com/Ezharjan/DailyHealthArxiv/actions)
[![License](https://img.shields.io/github/license/Ezharjan/DailyHealthArxiv)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Ezharjan/DailyHealthArxiv)](https://github.com/Ezharjan/DailyHealthArxiv/commits/main)

> **Automatically tracking the latest research papers in Health Computing and Medical AI from arXiv**

📊 **12 Research Domains** | 🔄 **Daily Updates** | 🤖 **Fully Automated** | 🌐 **[Live Website](https://Ezharjan.github.io/DailyHealthArxiv/)**

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

**Health Computing Arxiv Daily** is an automated research paper tracking system that:

- 📰 **Fetches** latest papers from arXiv every 24 hours
- 🎯 **Filters** by 150+ health computing keywords across 12 domains
- 🔗 **Links** to code repositories when available
- 📊 **Organizes** papers by research domain
- 🌐 **Publishes** to a beautiful website with search

Perfect for researchers, clinicians, and AI enthusiasts who want to stay updated on:
- Medical imaging and analysis
- Clinical AI and electronic health records
- Foundation models for healthcare
- Drug discovery and bioinformatics
- Healthcare robotics
- Digital health and telemedicine
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
- ✅ 12 comprehensive health computing domains
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
git clone https://github.com/Ezharjan/DailyHealthArxiv.git
cd DailyHealthArxiv

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
- `docs/health-arxiv-daily.json` - Complete data
- `docs/health-arxiv-daily-web.json` - Web-optimized data

---

## ⚙️ Configuration

### Basic Settings

Edit `config.yaml`:

```yaml
# How many papers per topic
max_results: 15

# Your GitHub info (for deployment)
user_name: "YourGitHubUsername"
repo_name: "DailyHealthArxiv"

# Base directory (usually /docs for GitHub Pages)
base_url: "https://yourusername.github.io/DailyHealthArxiv/"
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
    "Wearable Health Devices":
        filters: 
            - "Wearable Sensor"
            - "Smart Watch Health"
            - "Fitness Tracker"
            - "Wearable Healthcare"
            - "Body Sensor Network"
```

### Adjusting Paper Count

- **5-10**: Focused, high-quality (faster)
- **15-20**: Balanced (recommended)
- **20+**: Comprehensive (may include tangential)

### Update Schedule

Edit `.github/workflows/health-arxiv-daily.yml`:

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
git commit -m "Initial commit: Health Computing Arxiv Daily"
git push origin main
```

#### 2. Update Configuration

**Edit `.github/workflows/health-arxiv-daily.yml`:**
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
2. "Run Health Arxiv Papers Daily"
3. "Run workflow"

Your site: `https://yourusername.github.io/DailyHealthArxiv/`

---

## 📚 Research Domains

Current tracking covers 12 comprehensive health computing domains:

<details>
<summary><strong>🖼️ Medical Image Analysis</strong></summary>

- Medical image segmentation
- Radiology AI
- Pathology image analysis
- Medical image registration
- CT/MRI/X-ray analysis
- 3D medical imaging
</details>

<details>
<summary><strong>🏥 Clinical AI & EHR</strong></summary>

- Electronic health records
- Clinical decision support
- Patient monitoring
- ICU prediction
- Hospital readmission
- Clinical workflow optimization
</details>

<details>
<summary><strong>🏗️ Foundation Models for Healthcare</strong></summary>

- Medical foundation models
- Healthcare large language models
- Vision-language models
- Multi-modal medical AI
- Transfer learning in medicine
</details>

<details>
<summary><strong>🤖 Medical AI & Diagnosis</strong></summary>

- Disease diagnosis
- Treatment recommendation
- Medical chatbots
- Symptom checking
- Differential diagnosis
- Prognosis prediction
</details>

<details>
<summary><strong>🧬 Drug Discovery & Bioinformatics</strong></summary>

- Drug design
- Molecular property prediction
- Protein structure
- Genomics
- Precision medicine
- Biomarker discovery
</details>

<details>
<summary><strong>🤖 Healthcare Robotics</strong></summary>

- Surgical robots
- Rehabilitation robotics
- Assistive devices
- Medical automation
- Prosthetics
- Robotic surgery
</details>

<details>
<summary><strong>🥽 VR/AR/XR for Healthcare</strong></summary>

- Medical VR/AR
- Surgical simulation
- Pain management VR
- Medical training
- Therapy applications
- Visualization
</details>

<details>
<summary><strong>💻 HCI & Digital Health</strong></summary>

- mHealth applications
- Telemedicine
- Health informatics
- Patient engagement
- Health apps
- Remote monitoring
</details>

<details>
<summary><strong>📊 Biosignal Processing</strong></summary>

- ECG/EEG analysis
- Sleep monitoring
- Vital signs
- Physiological signals
- Wearable sensors
- Signal processing
</details>

<details>
<summary><strong>🌍 Public Health & Epidemiology</strong></summary>

- Disease surveillance
- Outbreak prediction
- Health policy
- Population health
- Social determinants
- Healthcare access
</details>

<details>
<summary><strong>🧠 Mental Health & Neuroscience</strong></summary>

- Depression detection
- Cognitive assessment
- Brain-computer interfaces
- Neuroimaging
- Mental health apps
- Behavioral analysis
</details>

<details>
<summary><strong>📖 Medical NLP & Knowledge</strong></summary>

- Clinical NLP
- Medical text mining
- Knowledge graphs
- Information extraction
- Medical literature analysis
- Question answering
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
- Add specific domain terms: "clinical", "medical", "healthcare"
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

Found a bug? [Open an issue](https://github.com/Ezharjan/DailyHealthArxiv/issues) with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

### Suggesting Features

Have an idea? [Start a discussion](https://github.com/Ezharjan/DailyHealthArxiv/discussions) about:
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
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Ezharjan/DailyHealthArxiv/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Ezharjan/DailyHealthArxiv/discussions)
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

- 🌐 **Live Website**: https://Ezharjan.github.io/DailyHealthArxiv/
- 📦 **GitHub Repo**: https://github.com/Ezharjan/DailyHealthArxiv
- 📊 **JSON Data**: [health-arxiv-daily.json](docs/health-arxiv-daily.json)
- 📘 **Detailed Usage**: [docs/README.md](docs/README.md)

---

<div align="center">

## 🎉 Happy Researching!

**Stay updated with the latest in Health Computing and Medical AI**

Made with ❤️ for the research community

</div>

---
