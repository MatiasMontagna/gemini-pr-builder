# Gemini PR Builder

A CLI tool to automate the creation of GitHub pull requests with commit summaries using Gemini AI.

## Prerequisites
- Python 3.9.10+
- [GitHub CLI (`gh`)](https://cli.github.com/) installed and authorized
- `google-genai` Python package (`pip install google-genai`)
- Set the `GEMINI_API_KEY` environment variable with your Gemini API key

## Installation
1. Clone this repository.
2. Install dependencies:
   ```sh
   pip install google-genai
   ```

## Usage
Run the tool from your feature branch:
```sh
python main.py [main-branch-name]
```
- Optionally specify the main branch name (default: `main`).
- You will be prompted for additional PR context (optional).

## What it does
- Pushes your branch to GitHub
- Summarizes your commits using Gemini AI
- Creates a pull request with a commit summary in Spanish
- If a pull request template is present, it will be used for the PR body

---
Be sure your branch is up to date and all changes are committed before running the tool. 