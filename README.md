# ADV Lab 05 — Git Basics for a Python Project

**Student:** Prabhas P Simha  
**USN:** 24SSDS415036  
**GitHub:** [Pubby-15](https://github.com/Pubby-15)  
**Repository:** [Pubby-15/ADV-Lab-05](https://github.com/Pubby-15/ADV-Lab-05)

## Project overview

This lab demonstrates Git version control for a small Python project and prepares a Streamlit dashboard for deployment. The dashboard uses Plotly's bundled Gapminder sample dataset to explore GDP per capita, population, and life expectancy across countries and years.

## Files

- `app.py` — Streamlit dashboard application.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local secrets, virtual environments, caches, and local data files.
- `24SSDS415036_LAB4_Code.ipynb` — step-by-step notebook for Git setup, commits, remote push, branching, and deployment preparation.
- `24SSDS415036_LAB4_Report.docx` — lab report. A PDF copy is also included for convenient viewing.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Git workflow

```bash
git status
git add app.py
git commit -m "Update dashboard"
git push origin main
```

The notebook shows a secure interactive GitHub token prompt for a Colab HTTPS push. Never paste a token into source code, a notebook cell, or a public repository.

## Deployment

The app is prepared for Streamlit Community Cloud. Deployment is not yet published. Connect this repository on [Streamlit Community Cloud](https://share.streamlit.io/), select the `main` branch, and set `app.py` as the main application file.
