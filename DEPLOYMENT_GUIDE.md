# Deploy StudyMate AI on Streamlit Community Cloud

1. Sign in to GitHub and create a new **public** repository named `studymate-ai` (do not initialize it with a README).
2. Extract the ZIP and upload **all files and folders**, including `app.py`, `requirements.txt`, `src/`, and `.streamlit/`, to the repository root. Commit changes.
3. Visit https://share.streamlit.io/ and sign in using GitHub.
4. Select **Create app** / **Deploy an app**, choose the repository, branch `main`, and entrypoint `app.py`.
5. Choose an available app URL and click **Deploy**. Wait for installation and check that the app opens.
6. Test the Notes intelligence, Practice lab, and Study planner tabs. Copy the public URL to your hackathon submission if permitted.

If deployment fails, check the app's build logs and verify `requirements.txt` and `app.py` are at the root. If your branch is named `master`, select `master` instead of `main`.

IMPORTANT: This is a deterministic NLP prototype, not an LLM-powered application. Confirm hackathon rules, including whether prebuilt projects are permitted, before submitting.
