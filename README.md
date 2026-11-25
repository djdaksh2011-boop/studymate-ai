# StudyMate AI — Intelligent Study Companion

**Problem:** Students spend excessive time turning long notes into concise revision material and structured practice.

**Solution:** A privacy-friendly learning assistant that extracts important sentences, identifies keywords, generates rule-based flashcards and fill-in-the-blank questions, and builds a personalized revision schedule.

## Features
- Notes upload (.txt) or paste
- Frequency-weighted extractive summarization
- Keyword extraction
- Definition-based flashcards
- Cloze-style quizzes with reveal answers
- Multi-day study planner and downloadable exports

## Quick start
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```
Open the local URL shown by Streamlit. Python 3.10+ recommended.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Technology
Python, Streamlit, regex, Counter. **AI disclosure:** The NLP is deterministic and extractive; this version does not call a generative model or external AI API. Do not describe it as LLM-powered.

## Architecture
User -> Streamlit UI -> NLP engine -> Summary / Keywords / Flashcards / Quiz / Plan -> UI / Export

## Limitations
English-focused; heuristic summarization can miss nuance; flashcards require definitional sentence structures; quizzes are fill-in-the-blank rather than multiple-choice; text files only; no cloud sync or generative AI. Do not upload confidential material to public deployments without reviewing privacy and hosting arrangements.

## Demo script
1. Paste sample machine-learning notes.
2. Click Analyze notes; inspect keywords and download summary.
3. Open Practice Lab; reveal flashcard and quiz answers.
4. Generate a seven-day revision plan and export CSV.

## Competition note
This is a pre-event preparation prototype. Confirm event rules before using any pre-built solution in a timed challenge. Adapt and build original qualifying-round work only as permitted by organizers.

## License
MIT (see LICENSE).
