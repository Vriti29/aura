# AURA — DSA Code Evaluator & Recommendation Platform

A web-based DSA practice platform built with React, FastAPI, and C++ (`g++`).

AURA executes C++ code inside a Docker container, checks test cases, estimates time complexity (like $O(n)$ or $O(n^2)$), and gives personalized problem recommendations based on your submission history.

##  Live Links
- **Website (Frontend):** [aura-roan-tau.vercel.app](https://aura-roan-tau.vercel.app)
- **API Docs (Backend):** [aura-backend-udu8.onrender.com/docs](https://aura-backend-udu8.onrender.com/docs)

## Tech Stack
- **Frontend:** React, Vite, CSS
- **Backend:** Python, FastAPI, Uvicorn
- **Code Execution:** C++ (GCC / `g++`), Docker
- **Hosting:** Vercel (Frontend), Render (Backend)

## Key Features
1. **Code Execution:** Compiles and runs C++ code against sample test cases.
2. **Complexity Analysis:** Analyzes loops and recursion to estimate Big-O time complexity.
3. **Pattern Recognition:** Detects patterns like Two Pointers, Hash Maps, and Sliding Window.
4. **Adaptive Practice:** Suggests problems based on topics you need more practice in.

## Running Locally

### Backend
```bash
cd aura/backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
