from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .problems import PROBLEMS
# Using updated analyzer with full multi-problem knowledge base
from .analyzer import analyze_code
from .executor import run_cpp
from .recommendation_engine import generate_recommendation
from .learning_tracker import LearningTracker


app = FastAPI(title="AURA API", version="0.1.0")


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# AURA LEARNING HISTORY
# ============================================================

learning_tracker = LearningTracker()


# ============================================================
# REQUEST MODELS
# ============================================================

class Submission(BaseModel):
    problem_id: str
    code: str


class CodeSubmission(BaseModel):
    code: str
    problem_statement: str = ""


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "name": "AURA",
        "status": "running",
        "version": "0.1.0"
    }


# ============================================================
# PROBLEMS
# ============================================================

@app.get("/api/problems")
def get_problems():
    return list(PROBLEMS.values())


@app.get("/api/problems/{problem_id}")
def get_problem(problem_id: str):
    problem = PROBLEMS.get(problem_id)
    if not problem:
        return {"error": "Problem not found"}
    return problem


# ============================================================
# ANALYZE PROBLEM SOLUTION
# ============================================================

@app.post("/api/analyze")
def analyze(submission: Submission):
    problem = PROBLEMS.get(submission.problem_id)
    if not problem:
        return {"error": "Problem not found"}

    # 1. Run C++ code against test cases
    execution = run_cpp(
        submission.code,
        problem["test_cases"],
        timeout_seconds=2
    )

    # 2. Analyze code with problem-aware analyzer
    analysis = analyze_code(
        submission.code,
        execution,
        submission.problem_id,
        problem["description"]
    )

    # 3. Save learning attempt
    learning_tracker.record_attempt(
        submission.problem_id,
        problem["title"],
        analysis
    )

    # 4. Get complete learning history
    history = learning_tracker.get_attempts()

    # 5. Generate personalized recommendation
    recommendation = generate_recommendation(
        history=history,
        problems=PROBLEMS,
        limit=3
    )

    # 6. Return full payload
    return {
        "problem": problem["title"],
        "execution": execution,
        "analysis": analysis,
        "recommendation": recommendation,
        "learning_profile": learning_tracker.get_profile()
    }


# ============================================================
# ANALYZE ANY CODE
# ============================================================

@app.post("/api/analyze-code")
def analyze_code_only(submission: CodeSubmission):
    analysis = analyze_code(
        submission.code,
        {
            "status": "not_executed",
            "passed": 0,
            "total": 0,
            "error": None
        },
        "generic",
        submission.problem_statement
    )

    return {
        "analysis": analysis
    }


# ============================================================
# AURA ANALYSIS HISTORY
# ============================================================

@app.get("/api/history")
def get_history():
    return {
        "history": learning_tracker.get_attempts(),
        "profile": learning_tracker.get_profile()
    }


# ============================================================
# AURA RECOMMENDATIONS
# ============================================================

@app.get("/api/recommendations")
def get_recommendations():
    history = learning_tracker.get_attempts()
    recommendation = generate_recommendation(
        history=history,
        problems=PROBLEMS,
        limit=3
    )
    return recommendation