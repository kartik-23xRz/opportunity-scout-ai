# Opportunity Scout AI

A beginner-friendly Agentic AI demo that searches for internship opportunities, evaluates relevance to a student's profile, and drafts an application email.

## Features
- Student profile input
- Live web search using Tavily
- LangGraph workflow with separate profile, search and evaluation nodes
- Gemini-powered analysis and structured output
- Skill relevance score and eligibility notes
- Original listing links and editable application email draft

> This is a demonstration assistant. Search snippets can be incomplete or outdated. Always open the original listing and verify availability, eligibility and deadlines before applying.

## Tech stack
Python, Streamlit, LangGraph, Gemini API, Tavily Search API.

## Run locally

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment:

   **Windows PowerShell**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and add your API keys:
   ```env
   GEMINI_API_KEY=your_key
   TAVILY_API_KEY=your_key
   ```

5. Run:
   ```bash
   streamlit run app.py
   ```

## API keys
- Gemini: https://aistudio.google.com/apikey
- Tavily: https://app.tavily.com/

Never commit `.env` or publish API keys.

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository and upload the project files. Keep `app.py`, `requirements.txt`, `README.md`, and `src/` at the repository root.
2. Visit https://share.streamlit.io/ and sign in with GitHub.
3. Choose **Create app**, select your repository and branch, and set the main file path to `app.py`.
4. Open **Advanced settings / Secrets** and add:
   ```toml
   GEMINI_API_KEY = "your_gemini_key"
   TAVILY_API_KEY = "your_tavily_key"
   ```
5. Deploy. Wait for the build to finish, then test a search.

## Project workflow
1. Understand the student profile and create a search query.
2. Search the web using Tavily.
3. Evaluate search results using Gemini.
4. Return ranked opportunities and an application email draft.

## Limitations
- Search results are leads, not guaranteed active vacancies.
- Eligibility is only as reliable as the source material returned by search.
- The match score is an estimate of skill relevance, not the probability of selection.
- The agent does not submit applications automatically.
