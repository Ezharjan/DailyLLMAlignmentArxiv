import os
import re
import json
import arxiv
import yaml
import logging
import argparse
import datetime
import requests

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
github_url = "https://api.github.com/search/repositories"
arxiv_url = "http://arxiv.org/"

def load_config(config_file:str) -> dict:
    '''
    config_file: input config file path
    return: a dict of configuration
    '''
    # Format filters for arxiv query with proper escaping
    def pretty_filters(**config) -> dict:
        keywords = dict()
        ESCAPE = '\"'
        OR = ' OR '
        
        def parse_filters(filters: list) -> str:
            ret = ''
            for idx in range(len(filters)):
                filter_term = filters[idx]
                # Escape multi-word phrases with quotes
                if len(filter_term.split()) > 1:
                    ret += (ESCAPE + filter_term + ESCAPE)
                else:
                    ret += filter_term
                # Add OR between filters
                if idx != len(filters) - 1:
                    ret += OR
            return ret
        for k,v in config['keywords'].items():
            keywords[k] = parse_filters(v['filters'])
        return keywords
    with open(config_file,'r', encoding='utf-8') as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
        config['kv'] = pretty_filters(**config)
        logging.info(f'config = {config}')
    return config

def get_authors(authors, first_author=False):
    """
    Extract author names from arxiv result.
    
    Args:
        authors: List of author objects
        first_author: If True, return only the first author
    
    Returns:
        String of author name(s)
    """
    if first_author:
        return str(authors[0])
    return ", ".join(str(author) for author in authors)


def sort_papers(papers):
    """
    Sort papers dictionary by keys in reverse order.
    
    Args:
        papers: Dictionary of papers with paper IDs as keys
    
    Returns:
        Sorted dictionary
    """
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output


def get_code_link(qword: str) -> str:
    """
    Search GitHub for code repositories related to the query.
    
    Args:
        qword: Query string (e.g., arxiv ID or paper title)
    
    Returns:
        GitHub repository URL if found, None otherwise
    """
    query = f"{qword}"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }
    try:
        r = requests.get(github_url, params=params, timeout=10)
        results = r.json()
        if results.get("total_count", 0) > 0:
            return results["items"][0]["html_url"]
    except Exception as e:
        logging.warning(f"GitHub search failed for '{qword}': {e}")
    return None

def get_daily_papers(topic, query="slam", max_results=2):
    """
    Fetch daily papers from arXiv and check for code repositories.
    
    Args:
        topic: Topic name/category
        query: ArXiv search query string
        max_results: Maximum number of papers to fetch
    
    Returns:
        Tuple of (data, data_web) dictionaries with paper information
    """
    content = dict()
    content_to_web = dict()
    
    search_engine = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    for result in search_engine.results():
        paper_id = result.get_short_id()
        paper_title = result.title
        paper_url = result.entry_id
        paper_abstract = result.summary.replace("\n", " ")
        paper_authors = get_authors(result.authors)
        paper_first_author = get_authors(result.authors, first_author=True)
        primary_category = result.primary_category
        publish_time = result.published.date()
        update_time = result.updated.date()
        comments = result.comment

        logging.info(f"Time = {update_time} title = {paper_title} author = {paper_first_author}")

        # Remove version suffix from paper ID (e.g., 2108.09112v1 -> 2108.09112)
        ver_pos = paper_id.find('v')
        paper_key = paper_id[0:ver_pos] if ver_pos != -1 else paper_id
        paper_url = arxiv_url + 'abs/' + paper_key

        try:
            # Try to fetch source code link from paperswithcode.com
            repo_url = None
            code_url = base_url + paper_id
            
            try:
                r = requests.get(code_url, timeout=10).json()
                if "official" in r and r["official"]:
                    repo_url = r["official"]["url"]
            except Exception as e:
                logging.warning(f"Could not fetch code link from paperswithcode.com for {paper_key}: {e}")
            
            # Fallback: Search GitHub if no code found on paperswithcode
            if repo_url is None:
                repo_url = get_code_link(paper_title)
                if repo_url is None:
                    repo_url = get_code_link(paper_key)
            
            # Format paper entry for README (table format)
            if repo_url is not None:
                content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|**[link]({})**|\n".format(
                    update_time, paper_title, paper_first_author, paper_key, paper_url, repo_url)
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({}), Code: **[{}]({})**".format(
                    update_time, paper_title, paper_first_author, paper_url, paper_url, repo_url, repo_url)
            else:
                # No code link found - leave Code column empty
                content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})||\n".format(
                    update_time, paper_title, paper_first_author, paper_key, paper_url)
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})".format(
                    update_time, paper_title, paper_first_author, paper_url, paper_url)

            # Add comments if available
            if comments:
                content_to_web[paper_key] += f", {comments}\n"
            else:
                content_to_web[paper_key] += "\n"

        except Exception as e:
            logging.error(f"Exception processing paper {paper_key}: {e}")
            # Save the paper entry even if there was an error
            content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})||\n".format(
                update_time, paper_title, paper_first_author, paper_key, paper_url)
            content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})\n".format(
                update_time, paper_title, paper_first_author, paper_url, paper_url)

    data = {topic: content}
    data_web = {topic: content_to_web}
    return data, data_web

def update_paper_links(filename):
    """
    Weekly update paper links in JSON file by re-checking for code repositories.
    
    Args:
        filename: Path to JSON file containing paper data
    """
    def parse_arxiv_string(s):
        """Parse paper entry string to extract components."""
        parts = s.split("|")
        date = parts[1].strip()
        title = parts[2].strip()
        authors = parts[3].strip()
        arxiv_id = parts[4].strip()
        code = parts[5].strip()
        # Remove version suffix
        arxiv_id = re.sub(r'v\d+', '', arxiv_id)
        return date, title, authors, arxiv_id, code

    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)

    json_data = m.copy()

    for keywords, v in json_data.items():
        logging.info(f'keywords = {keywords}')
        for paper_id, contents in v.items():
            contents = str(contents)

            update_time, paper_title, paper_first_author, paper_url, code_url = parse_arxiv_string(contents)

            contents = "|{}|{}|{}|{}|{}|\n".format(update_time, paper_title, paper_first_author, paper_url, code_url)
            json_data[keywords][paper_id] = str(contents)
            logging.info(f'paper_id = {paper_id}, contents = {contents}')

            # Check if code link is missing (empty or 'null')
            valid_link = False if (not code_url or code_url == 'null') else True
            if valid_link:
                continue
                
            # Try to fetch code link from paperswithcode.com
            try:
                code_api_url = base_url + paper_id
                r = requests.get(code_api_url, timeout=10).json()
                repo_url = None
                if "official" in r and r["official"]:
                    repo_url = r["official"]["url"]
                    if repo_url is not None:
                        new_cont = contents.replace('||', f'|**[link]({repo_url})**|').replace('|null|', f'|**[link]({repo_url})**|')
                        logging.info(f'ID = {paper_id}, updated with code link: {repo_url}')
                        json_data[keywords][paper_id] = str(new_cont)
            except Exception as e:
                logging.error(f"Exception updating paper {paper_id}: {e}")
                
    # Save updated data to JSON file
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

def update_json_file(filename, data_dict):
    """
    Update JSON file with new paper data.
    
    Args:
        filename: Path to JSON file
        data_dict: List of dictionaries containing paper data by keyword
    """
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)

    json_data = m.copy()

    # Update papers in each keyword category
    for data in data_dict:
        for keyword in data.keys():
            papers = data[keyword]

            if keyword in json_data.keys():
                json_data[keyword].update(papers)
            else:
                json_data[keyword] = papers

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

def json_to_md(filename, md_filename,
               task='',
               to_web=False,
               use_title=True,
               use_tc=True,
               show_badge=True,
               use_b2t=True):
    """
    Convert JSON paper data to Markdown format.
    
    Args:
        filename: Input JSON file path
        md_filename: Output Markdown file path
        task: Task description for logging
        to_web: Whether to format for web display
        use_title: Whether to include title section
        use_tc: Whether to include table of contents
        show_badge: Whether to include badges
        use_b2t: Whether to include back-to-top links
    """
    def pretty_math(s: str) -> str:
        """Format LaTeX math expressions with proper spacing."""
        match = re.search(r"\$.*\$", s)
        if match is None:
            return s
        math_start, math_end = match.span()
        space_trail = space_leading = ''
        if s[:math_start][-1] != ' ' and '*' != s[:math_start][-1]:
            space_trail = ' '
        if s[math_end:][0] != ' ' and '*' != s[math_end:][0]:
            space_leading = ' '
        ret = s[:math_start]
        ret += f'{space_trail}${match.group()[1:-1].strip()}${space_leading}'
        ret += s[math_end:]
        return ret

    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-', '.')

    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)

    # Create/clear the markdown file
    with open(md_filename, "w+", encoding='utf-8') as f:
        pass

    # Write paper data to markdown file
    with open(md_filename, "a+", encoding='utf-8') as f:

        if use_title and to_web:
            f.write("---\n")
            f.write("layout: papers\n")
            f.write("title: LLM Alignment Papers\n")
            f.write("nav_order: 1\n")
            f.write(f"last_updated: {DateNow}\n")
            f.write("---\n\n")

        if use_title:
            f.write("## Updated on " + DateNow + "\n")
        else:
            f.write("> Updated on " + DateNow + "\n")

        f.write("> Usage instructions: [here](./README.md)\n\n")

        # Add table of contents
        if use_tc:
            f.write("<details>\n")
            f.write("  <summary>Table of Contents</summary>\n")
            f.write("  <ol>\n")
            for keyword in data.keys():
                day_content = data[keyword]
                if not day_content:
                    continue
                kw = keyword.replace(' ', '-')
                f.write(f"    <li><a href=#{kw.lower()}>{keyword}</a></li>\n")
            f.write("  </ol>\n")
            f.write("</details>\n\n")

        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            
            # Write section header
            f.write(f"## {keyword}\n\n")

            if use_title:
                if to_web:
                    f.write("| Publish Date | Title | Authors | PDF | Code |\n")
                    f.write("|:---------|:-----------------------|:---------|:------|:------|\n")
                else:
                    f.write("|Publish Date|Title|Authors|PDF|Code|\n")
                    f.write("|---|---|---|---|---|\n")

            # Sort papers by date
            day_content = sort_papers(day_content)

            for _, v in day_content.items():
                if v is not None:
                    f.write(pretty_math(v))

            f.write("\n")

            # Add back to top link
            if use_b2t:
                top_info = f"#Updated on {DateNow}"
                top_info = top_info.replace(' ', '-').replace('.', '')
                f.write(f"<p align=right>(<a href={top_info.lower()}>back to top</a>)</p>\n\n")

        if show_badge:
            # Badge definitions
            f.write((f"[contributors-shield]: https://img.shields.io/github/"
                     f"contributors/DailyLLMAlignmentArxiv.svg?style=for-the-badge\n"))
            f.write((f"[contributors-url]: https://github.com/Ezharjan/"
                     f"ezharjan.github.io/graphs/contributors\n"))
            f.write((f"[forks-shield]: https://img.shields.io/github/forks/Ezharjan/"
                     f"ezharjan.github.io.svg?style=for-the-badge\n"))
            f.write((f"[forks-url]: https://github.com/Ezharjan/"
                     f"ezharjan.github.io/network/members\n"))
            f.write((f"[stars-shield]: https://img.shields.io/github/stars/Ezharjan/"
                     f"ezharjan.github.io.svg?style=for-the-badge\n"))
            f.write((f"[stars-url]: https://github.com/Ezharjan/"
                     f"ezharjan.github.io/stargazers\n"))
            f.write((f"[issues-shield]: https://img.shields.io/github/issues/Ezharjan/"
                     f"ezharjan.github.io.svg?style=for-the-badge\n"))
            f.write((f"[issues-url]: https://github.com/Ezharjan/"
                     f"ezharjan.github.io/issues\n\n"))

    logging.info(f"{task} finished")

def demo(**config):
    """
    Main function to fetch papers and generate markdown files.
    
    Args:
        **config: Configuration dictionary containing all settings
    """
    data_collector = []
    data_collector_web = []

    keywords = config['kv']
    max_results = config['max_results']
    publish_readme = config['publish_readme']
    publish_gitpage = config['publish_gitpage']
    show_badge = config['show_badge']

    b_update = config['update_paper_links']
    logging.info(f'Update Paper Link = {b_update}')
    
    if not config['update_paper_links']:
        logging.info("GET daily papers begin")
        for topic, keyword in keywords.items():
            logging.info(f"Keyword: {topic}")
            data, data_web = get_daily_papers(topic, query=keyword, max_results=max_results)
            data_collector.append(data)
            data_collector_web.append(data_web)
            print("\n")
        logging.info("GET daily papers end")

    # 1. Update README.md file
    if publish_readme:
        json_file = config['json_readme_path']
        md_file = config['md_readme_path']
        
        if config['update_paper_links']:
            update_paper_links(json_file)
        else:
            update_json_file(json_file, data_collector)
        
        json_to_md(json_file, md_file, task='Update Readme', show_badge=show_badge)

    # 2. Update docs/index.md file (for GitHub Pages)
    if publish_gitpage:
        json_file = config['json_gitpage_path']
        md_file = config['md_gitpage_path']
        
        if config['update_paper_links']:
            update_paper_links(json_file)
        else:
            update_json_file(json_file, data_collector)
        
        json_to_md(json_file, md_file, task='Update GitPage',
                   to_web=True, show_badge=show_badge,
                   use_tc=False, use_b2t=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='LLM Alignment Arxiv Daily - Fetch and organize latest papers'
    )
    parser.add_argument('--config_path', type=str, default='config.yaml',
                        help='Configuration file path')
    parser.add_argument('--update_paper_links', default=False,
                        action="store_true",
                        help='Update paper links for existing entries instead of fetching new papers')
    args = parser.parse_args()
    
    config = load_config(args.config_path)
    config = {**config, 'update_paper_links': args.update_paper_links}
    demo(**config)
