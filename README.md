# AURA: Adaptive Code Intelligence & DSA Optimization Engine

[![Live Application](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://aura-roan-tau.vercel.app)
[![API Engine](https://img.shields.io/badge/API_Engine-Render_Docker-46E3B7?style=for-the-badge&logo=render)](https://aura-backend-udu8.onrender.com/docs)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

A full-stack code evaluation and algorithmic intelligence platform that goes beyond standard pass/fail testing. **AURA** performs static structural analysis, asymptotic complexity estimation, dynamic execution profiling for C++, and adaptive problem recommendation based on individual problem-solving history.

---

## Live Links

- **Frontend Client:** [https://aura-roan-tau.vercel.app](https://aura-roan-tau.vercel.app)
- **Backend API Docs (Swagger UI):** [https://aura-backend-udu8.onrender.com/docs](https://aura-backend-udu8.onrender.com/docs)

---

## Core Features

* **Sandboxed Code Execution Engine:** Securely compiles and runs C++ code with configurable time limits, memory thresholds, and input injection.
* **Static Structural & Complexity Profiler:** Parses source code AST and token patterns to estimate Big-$O$ time complexity ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$) and detect algorithmic design patterns (e.g., Two Pointers, Hash Mapping, Sliding Window).
* **Code Smells & Anti-Pattern Detection:** Identifies inefficiencies such as unnecessary nested iterations, pass-by-value copies of standard containers, and redundant lookups.
* **Adaptive Learning Tracker:** Aggregates user problem-solving metrics and mastery scores across core algorithmic categories to deliver targeted practice recommendations.

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React, Vite, CSS |
| **Backend** | Python 3.11, FastAPI, Uvicorn, Pydantic |
| **Execution Toolchain** | Linux Debian Environment, `g++` (GCC), Docker Sandbox |
| **DevOps & Hosting** | Docker Containerization, Render (Backend API), Vercel (Edge CDN Frontend) |

---

## Architecture Overview

```text
  [ User Browser ]
         │
         ▼
[ Vercel Edge CDN ] ──── React SPA Interface
         │
    (REST API)
         │
         ▼
[ Render Docker Service ] ─── FastAPI Application
         │
   ┌─────┴────────────────────────────────┐
   ▼                                      ▼
[ Static Analyzer ]              [ Sandboxed Runner ]
- AST Pattern Detection          - GCC Compilation (`g++`)
- Complexity Estimation          - Memory / Time Limits
- Anti-Pattern Linting           - Test Case Validation
