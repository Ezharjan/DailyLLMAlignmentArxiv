# Health Arxiv Daily - Usage Guide

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

---

## Overview

The Health Arxiv Daily project automatically tracks and organizes the latest research papers in health computing, medical AI, and related domains from arXiv. This guide explains how to use and customize the system.

---

## Usage

### Basic Commands

#### 1. Fetch Latest Papers

```bash
python daily_arxiv.py
```

This command:
- Queries arXiv based on keywords in `config.yaml`
- Fetches papers from relevant categories (cs.AI, cs.LG, cs.CV, cs.HC, cs.RO, etc.)
- Generates organized markdown files with paper information
- Creates JSON data files for persistence
- Updates both README and GitHub Pages version

**Output Files:**
- `README.md` - Main paper list
- `docs/index.md` - GitHub Pages version
- `docs/health-arxiv-daily.json` - Data storage
- `docs/health-arxiv-daily-web.json` - Web format data

#### 2. Update Paper Links

```bash
python daily_arxiv.py --update_paper_links
```

This command:
- Reads existing papers from JSON files
- Searches for associated GitHub repositories
- Updates code links where available
- Maintains paper metadata

Run this weekly to keep code links up-to-date.

#### 3. Custom Configuration

```bash
python daily_arxiv.py --config_path custom_config.yaml
```

Use a custom configuration file instead of the default `config.yaml`.

---

## Configuration

### config.yaml Structure

```yaml
# Basic Settings
base_url: "https://arxiv.paperswithcode.com/api/v0/papers/"
user_name: "YourGitHubUsername"
repo_name: "health-arxiv-daily"
max_results: 15  # Papers per topic

# Output Options
publish_readme: True   # Generate README.md
publish_gitpage: True  # Generate docs/index.md

# Display Options
show_authors: True
show_links: True
show_badge: True

# Keywords Configuration
keywords:
    "Topic Name": 
        filters: ["keyword1", "keyword2", "multi word phrase"]
```

### Adding Research Topics

To add a new research area:

```yaml
keywords:
    "Your New Topic":
        filters: ["specific term", "another term", "full phrase"]
```

**Best Practices:**
- Use specific, descriptive terms
- Include common synonyms
- Multi-word phrases are automatically quoted
- Filters use OR logic (matches any filter)

### Recommended Health Computing Keywords

The default configuration includes:

1. **Medical Image Analysis** - CT, MRI, X-ray, pathology
2. **Clinical AI & EHR** - Electronic health records, clinical NLP
3. **Foundation Models** - Medical LLMs, vision-language models
4. **Medical AI & Diagnosis** - Disease detection, CAD systems
5. **Drug Discovery** - Molecular design, bioinformatics
6. **Healthcare Robotics** - Surgical robots, assistive devices
7. **VR/AR/XR** - Medical visualization, surgical simulation
8. **HCI & Digital Health** - mHealth, telemedicine
9. **Biosignal Processing** - ECG, EEG, BCI
10. **Public Health** - Epidemiology, disease surveillance
11. **Mental Health** - Depression detection, neuroimaging
12. **Medical NLP** - Clinical text mining, knowledge graphs

---

## Examples

### Example 1: Focused Search

For a narrow focus on surgical robotics only:

```yaml
keywords:
    "Surgical Robotics":
        filters: ["Robot-Assisted Surgery", "Surgical Robot", 
                  "Robotic Surgery", "Surgical Automation",
                  "Minimally Invasive Surgery Robot"]
```

### Example 2: Broad Coverage

For comprehensive coverage of medical imaging:

```yaml
keywords:
    "Medical Imaging AI":
        filters: ["Medical Image", "Radiology AI", "Medical Imaging",
                  "CT Scan", "MRI", "X-ray", "Ultrasound",
                  "Pathology Image", "Histopathology",
                  "Medical Image Segmentation", "Medical Image Classification"]
```

### Example 3: Multiple Related Topics

```yaml
keywords:
    "AI for Mental Health":
        filters: ["Mental Health AI", "Depression Detection", 
                  "Anxiety Detection", "Psychiatric AI"]
    
    "Neuroscience AI":
        filters: ["Neuroimaging", "Brain Imaging", "fMRI Analysis",
                  "Alzheimer Detection", "Neurodegenerative Disease"]
```

### Example 4: Emerging Areas

```yaml
keywords:
    "Foundation Models for Medicine":
        filters: ["Medical Foundation Model", "Med-LLM", 
                  "Clinical Large Language Model",
                  "Medical Vision-Language Model",
                  "Healthcare GPT", "BioGPT"]
```

---

## Troubleshooting

### Common Issues

#### 1. No Papers Found

**Problem:** Script runs but finds no papers

**Solutions:**
- Check keyword specificity (too narrow?)
- Verify arXiv categories are relevant
- Increase `max_results` in config
- Try broader filter terms

#### 2. Too Many Irrelevant Papers

**Problem:** Papers don't match health computing focus

**Solutions:**
- Use more specific filter terms
- Add domain-specific phrases (e.g., "clinical", "medical", "healthcare")
- Combine multiple specific terms
- Reduce `max_results` for quality over quantity

#### 3. Missing Code Links

**Problem:** Papers show "null" for code links

**Solutions:**
- Run `python daily_arxiv.py --update_paper_links` weekly
- Some papers don't have public code
- Links are found via Papers with Code API
- Manual GitHub search may find unlisted repositories

#### 4. Duplicate Papers Across Topics

**Problem:** Same paper appears in multiple sections

**Solutions:**
- This is expected behavior (papers can fit multiple topics)
- Papers are deduplicated within each topic
- Cross-topic duplication helps discoverability

#### 5. Script Timeout

**Problem:** Script takes too long or times out

**Solutions:**
- Reduce `max_results` per topic
- Limit number of keywords in config
- Run specific topics separately
- Check internet connection

#### 6. GitHub Actions Not Running

**Problem:** Automatic updates not working

**Solutions:**
- Check Actions tab for error messages
- Verify workflows are enabled in repository settings
- Ensure GitHub token has write permissions
- Check cron schedule syntax

---

## Advanced Usage

### Filtering by arXiv Category

arXiv papers are categorized. Relevant categories for health computing:

- **cs.AI** - Core AI algorithms
- **cs.LG** - Machine learning methods
- **cs.CV** - Medical image analysis
- **cs.CL** - Clinical NLP
- **cs.HC** - Health interface design
- **cs.RO** - Healthcare robotics
- **cs.CY** - Health equity and social impact

### Query Construction

The script builds arXiv queries as:

```
(filter1) OR (filter2) OR (filter3) ...
```

Multi-word filters are automatically quoted:
- `Medical Imaging` → `"Medical Imaging"`

### Output Format Customization

Edit `daily_arxiv.py` function `json_to_md()` to customize:
- Table headers
- Markdown styling
- Badge display
- Table of contents

### Scheduling

Modify `.github/workflows/health-arxiv-daily.yml`:

```yaml
schedule:
    - cron: "0 2 * * *"  # Minute Hour Day Month Weekday
```

Examples:
- `"0 2 * * *"` - Daily at 2 AM UTC
- `"0 */8 * * *"` - Every 8 hours
- `"0 0 * * 1"` - Weekly on Monday
- `"0 0 1,15 * *"` - Twice monthly (1st and 15th)

---

## Performance Tips

1. **Optimize max_results**: 10-20 papers per topic is usually sufficient
2. **Strategic keywords**: Use 8-15 well-chosen topics
3. **Specific filters**: 3-8 filters per topic works well
4. **Update frequency**: Daily for active areas, weekly for stable areas
5. **Link updates**: Weekly is sufficient for code link maintenance

---

## Contact & Support

- **Issues**: Open a GitHub issue
- **Questions**: Check existing issues or create new one
- **Contributions**: PRs welcome for new health computing topics

---

## Additional Resources

- [arXiv API Documentation](https://arxiv.org/help/api/)
- [Papers with Code](https://paperswithcode.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Cron Syntax Guide](https://crontab.guru/)

---

Last Updated: October 2025
