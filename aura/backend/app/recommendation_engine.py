# ============================================================
# AURA RECOMMENDATION ENGINE (Adaptive Progression 2.0)
# ============================================================

from collections import Counter
from .problems import PROBLEMS


# ============================================================
# PROBLEM -> PATTERN MAPPING
# ============================================================

PROBLEM_PATTERNS = {
    "two-sum": [
        "Hashing / Lookup"
    ],
    "max-element": [
        "Linear Scan / Traversal"
    ],
    "binary-search": [
        "Binary Search"
    ],
    "best-time-stock": [
        "Linear Scan / Traversal"
    ],
    "maximum-subarray": [
        "Dynamic Programming",
        "Linear Scan / Traversal"
    ],
    "valid-anagram": [
        "Hashing / Lookup"
    ],
    "contains-duplicate": [
        "Hashing / Lookup"
    ],
    "move-zeroes": [
        "Two Pointer"
    ],
    "longest-substring": [
        "Sliding Window",
        "Hashing / Lookup"
    ],
    "subarray-sum-k": [
        "Prefix / Cumulative",
        "Hashing / Lookup"
    ],
    "merge-intervals": [
        "Sorting",
        "Linear Scan / Traversal"
    ],
    "number-of-islands": [
        "DFS / Graph Traversal"
    ]
}


# ============================================================
# PATTERN PROGRESSION MAP (Skill Tree Transitions)
# ============================================================

PATTERN_PROGRESSION = {
    "Hashing / Lookup": ["Prefix / Cumulative", "Sliding Window"],
    "Linear Scan / Traversal": ["Two Pointer", "Binary Search", "Dynamic Programming"],
    "Binary Search": ["Two Pointer"],
    "Two Pointer": ["Sliding Window", "Sorting"],
    "Sliding Window": ["Prefix / Cumulative"],
    "Prefix / Cumulative": ["Dynamic Programming"],
    "Sorting": ["Two Pointer", "Intervals"],
    "DFS / Graph Traversal": ["BFS / Graph Traversal", "Dynamic Programming"]
}


class RecommendationEngine:

    def __init__(self, problems=None):
        if problems is None:
            problems = PROBLEMS
        self.problems = problems

    # ========================================================
    # GET ATTEMPTS FOR A PROBLEM
    # ========================================================

    def _get_problem_attempts(self, history, problem_id):
        return [
            attempt
            for attempt in history
            if attempt.get("problem_id") == problem_id
        ]

    # ========================================================
    # CHECK WHETHER PROBLEM WAS MASTERED
    # ========================================================

    def _is_problem_mastered(self, history, problem_id):
        attempts = self._get_problem_attempts(history, problem_id)
        if not attempts:
            return False

        for attempt in attempts:
            correctness = attempt.get("correctness_score", 0)
            is_optimal = attempt.get("is_optimal", False)

            if correctness in (100, 3) and is_optimal is True:
                return True

        return False

    # ========================================================
    # GET MASTERED PATTERNS
    # ========================================================

    def get_mastered_patterns(self, history):
        mastered = set()
        for attempt in history:
            correctness = attempt.get("correctness_score", 0)
            is_optimal = attempt.get("is_optimal", False)
            pattern = attempt.get("pattern")
            if correctness in (100, 3) and is_optimal is True and pattern:
                mastered.add(pattern)
        return list(mastered)

    # ========================================================
    # FIND WEAK PATTERNS
    # ========================================================

    def get_weak_patterns(self, history):
        pattern_stats = {}

        for attempt in history:
            pattern = attempt.get("pattern")
            if not pattern:
                continue

            if pattern not in pattern_stats:
                pattern_stats[pattern] = {
                    "attempts": 0,
                    "optimal": 0
                }

            pattern_stats[pattern]["attempts"] += 1
            if attempt.get("is_optimal") is True:
                pattern_stats[pattern]["optimal"] += 1

        weaknesses = []
        for pattern, data in pattern_stats.items():
            attempts = data["attempts"]
            optimal = data["optimal"]
            if attempts == 0:
                continue

            score = (optimal / attempts) * 100
            weaknesses.append({
                "pattern": pattern,
                "score": round(score),
                "attempts": attempts
            })

        weaknesses.sort(key=lambda x: x["score"])
        return weaknesses

    # ========================================================
    # FIND OPTIMIZATION OPPORTUNITIES
    # ========================================================

    def get_optimization_patterns(self, history):
        opportunities = Counter()

        for attempt in history:
            if attempt.get("is_optimal") is False:
                optimal_pattern = attempt.get("optimal_pattern")
                if optimal_pattern:
                    opportunities[optimal_pattern] += 1

        return dict(opportunities)

    # ========================================================
    # SCORE PROBLEM & BUILD REASON
    # ========================================================

    def _score_problem(
        self,
        problem,
        history,
        weak_patterns,
        optimization_patterns,
        mastered_patterns
    ):
        problem_id = problem.get("id")

        # 1. Never recommend a problem already solved optimally
        if self._is_problem_mastered(history, problem_id):
            return None, ""

        score = 30  # Baseline for unmastered
        reason = "Expands your overall DSA pattern coverage."
        patterns = PROBLEM_PATTERNS.get(problem_id, [])
        difficulty = problem.get("difficulty", "Easy")

        # 2. Optimization reinforcement bonus (Highest Priority)
        for pattern, count in optimization_patterns.items():
            if pattern in patterns:
                score += count * 35
                reason = f"Reinforces the {pattern} pattern that you previously missed."
                break

        # 3. Weak pattern bonus
        for weak in weak_patterns:
            if weak["pattern"] in patterns and weak["score"] < 60:
                score += (60 - weak["score"])
                reason = f"Targets {weak['pattern']} to improve your success rate in this area."
                break

        # 4. Pattern progression bonus (Leveling Up)
        for mastered in mastered_patterns:
            next_steps = PATTERN_PROGRESSION.get(mastered, [])
            for next_step in next_steps:
                if next_step in patterns:
                    score += 25
                    if difficulty == "Medium":
                        score += 10
                        reason = f"Medium-level progression building upon your mastery of {mastered}."
                    else:
                        reason = f"Progression step advancing your foundation in {mastered}."
                    break

        # 5. Never attempted bonus
        attempts = self._get_problem_attempts(history, problem_id)
        if len(attempts) == 0:
            score += 15

        # 6. Base difficulty weighting
        if difficulty == "Easy":
            score += 10
        elif difficulty == "Medium":
            score += 5

        return score, reason

    # ========================================================
    # MAIN RECOMMENDATION FUNCTION
    # ========================================================

    def recommend(self, history=None, limit=3):
        if history is None:
            history = []

        weak_patterns = self.get_weak_patterns(history)
        optimization_patterns = self.get_optimization_patterns(history)
        mastered_patterns = self.get_mastered_patterns(history)

        scored_problems = []

        for problem_id, problem in self.problems.items():
            score, reason = self._score_problem(
                problem,
                history,
                weak_patterns,
                optimization_patterns,
                mastered_patterns
            )

            if score is None:
                continue

            scored_problems.append({
                "problem": problem,
                "score": score,
                "reason": reason
            })

        # Sort descending by calculated recommendation score
        scored_problems.sort(key=lambda x: x["score"], reverse=True)

        recommendations = []
        for item in scored_problems[:limit]:
            p = item["problem"]
            recommendations.append({
                "id": p.get("id"),
                "title": p.get("title"),
                "difficulty": p.get("difficulty"),
                "topic": p.get("topic"),
                "score": item["score"],
                "reason": item["reason"]
            })

        # Generate intelligent contextual explanation
        weak_area = weak_patterns[0]["pattern"] if weak_patterns else None

        if optimization_patterns:
            top_opt = list(optimization_patterns.keys())[0]
            explanation = (
                f"AURA detected opportunities to apply {top_opt}. "
                "Recommendations prioritize problems that help you practice this optimal pattern."
            )
        elif mastered_patterns:
            top_mastered = mastered_patterns[0]
            explanation = (
                f"Based on your mastery of {top_mastered}, "
                "AURA is recommending next-stage patterns to build your problem-solving range."
            )
        elif weak_area:
            explanation = (
                f"AURA identified {weak_area} as an area needing reinforcement. "
                "Recommendations prioritize high-yield practice in this pattern."
            )
        else:
            explanation = (
                "Recommendations are tailored to build broad algorithmic coverage across core DSA patterns."
            )

        return {
            "weak_area": weak_area,
            "recommendations": recommendations,
            "weak_patterns": weak_patterns,
            "optimization_patterns": optimization_patterns,
            "explanation": explanation
        }


# ============================================================
# HELPER / BACKWARD COMPATIBILITY
# ============================================================

def get_recommendations(problems, history, limit=3):
    engine = RecommendationEngine(problems)
    return engine.recommend(history, limit)


def generate_recommendation(history=None, problems=None, limit=3):
    if history is None:
        history = []
    if problems is None:
        problems = PROBLEMS

    engine = RecommendationEngine(problems)
    return engine.recommend(history=history, limit=limit)