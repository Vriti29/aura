import json
import os
from collections import Counter
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "learning_history.json")


class LearningTracker:

    def __init__(self):
        self.attempts = []
        self._load_from_disk()

    def _load_from_disk(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.attempts = json.load(f)
            except Exception:
                self.attempts = []

    def _save_to_disk(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.attempts, f, indent=2)
        except Exception as e:
            print(f"Failed to persist learning history: {e}")

    def record_attempt(self, problem_id, problem_title, analysis):
        pattern = analysis.get("pattern", "Unknown")
        complexity = analysis.get("complexity", "Unknown")
        space_complexity = analysis.get("space_complexity", "Unknown")
        correctness_score = analysis.get("correctness_score", 0)
        optimization_engine = analysis.get("optimization_engine", {})

        optimal_pattern = (
            optimization_engine.get("optimal_pattern")
            if isinstance(optimization_engine, dict)
            else None
        )
        is_optimal = (
            optimization_engine.get("is_optimal")
            if isinstance(optimization_engine, dict)
            else None
        )

        attempt = {
            "problem_id": problem_id,
            "problem_title": problem_title,
            "pattern": pattern,
            "complexity": complexity,
            "space_complexity": space_complexity,
            "correctness_score": correctness_score,
            "optimal_pattern": optimal_pattern,
            "is_optimal": is_optimal,
            "timestamp": datetime.now().isoformat()
        }

        self.attempts.append(attempt)
        self._save_to_disk()
        return attempt

    def get_attempts(self):
        return self.attempts

    def get_total_attempts(self):
        return len(self.attempts)

    def get_unique_problem_ids(self):
        return list(dict.fromkeys(a["problem_id"] for a in self.attempts))

    def get_unique_problem_count(self):
        return len(self.get_unique_problem_ids())

    def get_solved_count(self):
        solved = set()
        for attempt in self.attempts:
            score = attempt.get("correctness_score", 0)
            if score == 100 or score == 3:
                solved.add(attempt["problem_id"])
        return len(solved)

    def get_success_rate(self):
        total = self.get_unique_problem_count()
        if total == 0:
            return 0
        solved = self.get_solved_count()
        return round((solved / total) * 100)

    def get_latest_attempts(self):
        latest = {}
        for attempt in self.attempts:
            latest[attempt["problem_id"]] = attempt
        return list(latest.values())

    def get_best_attempts(self):
        best = {}
        for attempt in self.attempts:
            pid = attempt["problem_id"]
            score = attempt.get("correctness_score", 0)
            is_optimal = attempt.get("is_optimal")

            rank = 1
            if score in (100, 3):
                rank = 3 if is_optimal is True else 2

            if pid not in best or rank > best[pid]["rank"]:
                best[pid] = {"attempt": attempt, "rank": rank}

        return [item["attempt"] for item in best.values()]

    def get_pattern_usage(self):
        patterns = [
            a.get("pattern")
            for a in self.get_best_attempts()
            if a.get("pattern")
        ]
        return dict(Counter(patterns))

    def get_strongest_pattern(self):
        usage = self.get_pattern_usage()
        if not usage:
            return None
        return max(usage, key=usage.get)

    def get_optimization_opportunities(self):
        opps = []
        for attempt in self.get_latest_attempts():
            if attempt.get("is_optimal") is False:
                opt = attempt.get("optimal_pattern")
                if opt:
                    opps.append(opt)
        return dict(Counter(opps))

    def get_problem_progress(self):
        progress = {}
        for pid in self.get_unique_problem_ids():
            attempts = [a for a in self.attempts if a["problem_id"] == pid]
            latest = attempts[-1]
            solved = any(a.get("correctness_score", 0) in (100, 3) for a in attempts)
            optimal = any(
                a.get("correctness_score", 0) in (100, 3) and a.get("is_optimal") is True
                for a in attempts
            )

            progress[pid] = {
                "problem_title": latest["problem_title"],
                "attempt_count": len(attempts),
                "latest_pattern": latest.get("pattern"),
                "latest_complexity": latest.get("complexity"),
                "latest_is_optimal": latest.get("is_optimal"),
                "solved": solved,
                "is_optimal": optimal
            }
        return progress

    def get_profile(self):
        return {
            "problems_attempted": self.get_unique_problem_count(),
            "problems_solved": self.get_solved_count(),
            "success_rate": self.get_success_rate(),
            "total_submissions": self.get_total_attempts(),
            "strongest_pattern": self.get_strongest_pattern(),
            "pattern_usage": self.get_pattern_usage(),
            "optimization_opportunities": self.get_optimization_opportunities(),
            "problem_progress": self.get_problem_progress(),
            "recent_attempts": self.attempts[-10:]
        }