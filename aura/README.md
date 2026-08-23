# AURA — AI-Powered DSA & Code Intelligence Platform

AURA analyzes C++ submissions for correctness, complexity, edge cases, code quality, and personalized DSA progress.

## Milestone 1
- React dashboard
- FastAPI backend
- Problem API
- C++ submission API
- Basic local test-case execution
- Complexity heuristic
- Initial analysis response

## Run backend
```bash
cd backend
python -m venv .venv
# activate the environment
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run frontend
```bash
cd frontend
npm install
npm run dev
```

> The current C++ executor is intended for local development only. Do not expose raw subprocess execution to an untrusted public deployment. Later we will replace it with an isolated Docker sandbox.
