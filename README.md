# ADV Lab 05 — Git Basics for a Python Project

**Student:** Prabhas P Simha  
**USN:** 24SSDS415036  
**GitHub:** [Pubby-15](https://github.com/Pubby-15)  
**Repository:** [Pubby-15/ADV-Lab-05](https://github.com/Pubby-15/ADV-Lab-05)

## Project overview

This repository follows the Git Basics lab reference. The Python application is a **County Development Dashboard** built with Streamlit, Pandas, and Plotly. It uses Plotly's bundled Gapminder sample data and includes a year slider, continent filter, three key metrics, and a GDP-per-capita versus life-expectancy scatter chart.

## Main files

- `app.py` — dashboard application.
- `requirements.txt` — Streamlit, Pandas, and Plotly.
- `.gitignore` — excludes temporary files, local environments, and local data.
- `24SSDS415036_LAB4_Code.ipynb` — reference-aligned, step-by-step Git workflow notebook.
- `24SSDS415036_LAB4_Report.md` — report source in Markdown.
- `evidence/` — repository, code, commit, pull-request, and dashboard evidence illustrations.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Git workflow

The notebook walks through Git identity setup, cloning the existing repository, creating or checking project files, adding ignore rules, staging, committing, pushing, editing the dashboard, and creating/pushing the feature branch. It requests a GitHub token through a hidden prompt; do not store a token in the notebook, source files, or remote URL.

## Branch and pull request

- Main branch: `main`
- Feature branch: `feature/experiment`
- Pull request: [#1 — Add experiment feature](https://github.com/Pubby-15/ADV-Lab-05/pull/1) (open; not merged)

## Deployment

The app is prepared for Streamlit Community Cloud. Deployment is **pending** until the repository is selected, `app.py` is deployed, and a working public URL is verified at [share.streamlit.io](https://share.streamlit.io/).

## Evidence note

The actual profile image in the Word report is the screenshot supplied by the student. The repository, source-file, commit-history, and pull-request evidence illustrations in `evidence/` are reconstructed from GitHub API responses that were checked on 31 October 2026; they are not direct browser screenshots.
