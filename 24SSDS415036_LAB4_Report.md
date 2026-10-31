# LAB 4 — Git Basics for a Python Project

**Student:** Prabhas P Simha  
**USN:** 24SSDS415036  
**Programme:** Data Science and Analytics  
**University:** Ramaiah University of Applied Sciences, Bengaluru  
**GitHub:** [Pubby-15](https://github.com/Pubby-15)  
**Repository:** [Pubby-15/ADV-Lab-05](https://github.com/Pubby-15/ADV-Lab-05)  
**Date:** 31 October 2026

## Abstract
This lab demonstrates how Git tracks changes in a Python project and how GitHub hosts the project remotely. A Streamlit dashboard is used as the example application. The work covers repository setup, staging, commits, remote synchronization, branching, dependency management, and preparation for cloud deployment. The dashboard uses the Gapminder sample dataset included with Plotly, so a separate CSV download is not required.

## Problem statement
Software projects change frequently. Without version control, it is difficult to identify changes, restore earlier versions, or experiment without affecting the stable application. The objective is to apply Git version control to a Python project, publish its source to GitHub, and prepare a Streamlit dashboard for deployment.

## Learning objectives
- Understand the Git working directory, staging area, commits, and history.
- Create a `.gitignore` file to exclude temporary files and secrets.
- Connect a local repository to GitHub and push changes securely.
- Practice the add, commit, and push workflow.
- Create a feature branch and keep experimental changes separate from `main`.
- Prepare a Streamlit application and its dependencies for cloud deployment.

## Tools and technologies
| Tool | Purpose |
|---|---|
| Python | Dashboard application language |
| Git | Tracks changes and maintains commit history |
| GitHub | Remote repository and collaboration |
| Streamlit | Interactive web dashboard |
| Pandas and Plotly | Data handling and visualizations |
| Google Colab / Jupyter | Notebook environment |

## Procedure and code

### Task 1 — Configure Git identity
```bash
git config --global user.name "Prabhas P Simha"
git config --global user.email "YOUR_GITHUB_EMAIL"
git config --global --list
```
Git uses this information to identify the author of each commit.

### Task 2 — Project structure
```text
ADV-Lab-05/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── 24SSDS415036_LAB4_Code.ipynb
├── 24SSDS415036_LAB4_Report.md
└── feature_demo.py
```
The application contains the dashboard, `requirements.txt` lists dependencies, and the README explains the project. The notebook documents the workflow.

### Task 3 — Add a .gitignore file
```gitignore
.env
.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
/data/
*.csv
```
These rules prevent secrets, local environments, cache files, and local datasets from entering version control.

### Task 4 — Initialize, stage, and commit
```bash
git init -b main
git add .
git status
git commit -m "Add Streamlit dashboard project"
git log --oneline
```
The commands create a repository, stage files, inspect the staging area, save a commit, and display its history. When working from a cloned repository, cloning has already initialized Git.

### Task 5 — Connect the GitHub remote and push
The project is associated with the existing public repository **Pubby-15/ADV-Lab-05**.

```bash
git branch -M main
git remote add origin https://github.com/Pubby-15/ADV-Lab-05.git
git push -u origin main
```

A GitHub Personal Access Token or another supported authentication method may be used for HTTPS pushes. Never store a token in a notebook, source file, README, or remote URL. The companion notebook uses a hidden prompt for token input.

### Task 6 — Everyday Git workflow
```bash
git status
git add app.py
git commit -m "Update dashboard"
git push origin main
git log --oneline
```
After editing a file, stage the intended change, create a descriptive commit, and push it to GitHub.

### Task 7 — Feature branch
```bash
git branch
git switch -c feature/experiment
git add feature_demo.py
git commit -m "Add feature branch demonstration"
git push -u origin feature/experiment
```
A feature branch isolates new work from the stable branch. A pull request can be opened on GitHub to propose merging the feature into `main`.

## Streamlit dashboard

The Global Development Dashboard loads Plotly's bundled Gapminder dataset. It contains a year selector and continent filter. Key indicators include country count, median life expectancy, total population, and median GDP per capita. The application displays a scatter plot of GDP per capita against life expectancy and a bar chart of average life expectancy by continent.

### Dependencies
```text
streamlit>=1.40
pandas>=2.0
plotly>=5.20
```

### Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### Interpretation
The scatter plot allows country-level comparison, while the bar chart summarizes average life expectancy by continent. The data is a bundled demonstration dataset and should not be treated as a current official statistical release.

## GitHub repository and evidence
The repository is available at: https://github.com/Pubby-15/ADV-Lab-05

The supplied GitHub profile screenshot shows the Pubby-15 account and the ADV-Lab-05 repository. It is a profile-identification screenshot supplied before the files in this lab were added, not a screenshot of the final repository contents. The latest file list can be checked directly through the repository URL.

## Streamlit Community Cloud deployment
1. Open [Streamlit Community Cloud](https://share.streamlit.io/) and sign in using GitHub.
2. Create a new app and select `Pubby-15/ADV-Lab-05`.
3. Choose the `main` branch and set `app.py` as the main application file.
4. Deploy and allow the platform to install the listed dependencies.
5. Copy the generated `.streamlit.app` URL after a successful deployment.

**Deployment status: Pending.** The source and dependency files are prepared in GitHub, but a live URL has not been published or verified as part of this lab.

## Data insights and findings
- Git provides a history of project versions through commits.
- The staging area controls which files are included in a commit.
- `.gitignore` keeps secrets, caches, environments, and local data out of the repository.
- GitHub provides remote hosting and a collaboration point.
- Feature branches support experimentation without directly changing `main`.
- `requirements.txt` makes the Python environment easier to reproduce.
- Interactive filters help compare countries and regions across years.

## Recommendations / applications
1. Use version control from the beginning of every software or data science project.
2. Create small commits with meaningful messages.
3. Keep passwords, API keys, and tokens outside source files and public repositories.
4. Use feature branches for changes that need separate testing or review.
5. Maintain a README that explains setup, execution, and project structure.
6. Update dependencies whenever the application changes.
7. Review repository contents before making a public push.

## Conclusion
The lab demonstrates the basic Git workflow for a Python project and the role of GitHub as a remote repository. The dashboard source, dependency list, README, and ignore rules provide a structured project. The companion notebook contains reproducible commands for identity setup, staging, commits, remote push, and feature branching. The Streamlit application is prepared for deployment; publication remains a separate final step to complete and verify on Streamlit Community Cloud.

## Appendix — Important commands
| Command | Purpose |
|---|---|
| `git status` | Checks the working tree and staging area |
| `git add .` | Stages project changes |
| `git commit -m "message"` | Creates a commit |
| `git log --oneline` | Displays compact commit history |
| `git remote -v` | Shows configured remote repositories |
| `git push -u origin main` | Pushes main and sets upstream tracking |
| `git switch -c feature/experiment` | Creates and switches to a feature branch |
| `git push -u origin feature/experiment` | Publishes the feature branch |


## Pull request record
A feature demonstration file was pushed to the `feature/experiment` branch. [Pull Request #1](https://github.com/Pubby-15/ADV-Lab-05/pull/1) was opened against `main` and is awaiting review. It has not been merged.
