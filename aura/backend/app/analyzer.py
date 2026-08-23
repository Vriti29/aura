import re

# ============================================================
# PROBLEM KNOWLEDGE BASE
# ============================================================

PROBLEM_KNOWLEDGE = {
    "two-sum": {
        "optimal_pattern": "Hashing / Lookup",
        "optimal_time": "O(n) expected",
        "optimal_space": "O(n)"
    },
    "max-element": {
        "optimal_pattern": "Linear Scan / Traversal",
        "optimal_time": "O(n)",
        "optimal_space": "O(1)"
    },
    "binary-search": {
        "optimal_pattern": "Binary Search",
        "optimal_time": "O(log n)",
        "optimal_space": "O(1)"
    },
    "best-time-stock": {
        "optimal_pattern": "Linear Scan / Traversal",
        "optimal_time": "O(n)",
        "optimal_space": "O(1)"
    },
    "maximum-subarray": {
        "optimal_pattern": "Linear Scan / Traversal",
        "optimal_time": "O(n)",
        "optimal_space": "O(1)"
    },
    "valid-anagram": {
        "optimal_pattern": "Hashing / Lookup",
        "optimal_time": "O(n) expected",
        "optimal_space": "O(n)"
    },
    "contains-duplicate": {
        "optimal_pattern": "Hashing / Lookup",
        "optimal_time": "O(n) expected",
        "optimal_space": "O(n)"
    },
    "move-zeroes": {
        "optimal_pattern": "Two Pointer",
        "optimal_time": "O(n)",
        "optimal_space": "O(1)"
    },
    "longest-substring": {
        "optimal_pattern": "Sliding Window",
        "optimal_time": "O(n)",
        "optimal_space": "O(n)"
    },
    "subarray-sum-k": {
        "optimal_pattern": "Prefix / Cumulative",
        "optimal_time": "O(n)",
        "optimal_space": "O(n)"
    },
    "merge-intervals": {
        "optimal_pattern": "Sorting",
        "optimal_time": "O(n log n)",
        "optimal_space": "O(n)"
    },
    "number-of-islands": {
        "optimal_pattern": "DFS / Graph Traversal",
        "optimal_time": "O(V + E)",
        "optimal_space": "O(V)"
    }
}

# ============================================================
# EXPLANATION KNOWLEDGE BASE
# ============================================================

EXPLANATIONS = {
    "two-sum": {
        "Brute Force / Pair Search": {
            "why": "You are checking every pair using nested loops, which requires O(n²) time.",
            "better": "Use a hash map to store seen numbers. For each number, lookup target - num in expected O(1) time.",
            "tradeoff": "Requires O(n) extra space to reduce runtime from O(n²) to expected O(n).",
            "learning_point": "Use hash lookups to eliminate quadratic pair comparisons."
        },
        "Hashing / Lookup": {
            "why": "You store previously seen numbers in a hash map and check for complements on the fly.",
            "better": "This is the optimal standard approach.",
            "tradeoff": "Uses O(n) space for expected O(n) time.",
            "learning_point": "State retention via hashing reduces search complexity from O(n) to O(1)."
        }
    },
    "move-zeroes": {
        "Two Pointer": {
            "why": "You maintain a write pointer while iterating through the array.",
            "better": "This processes the array in a single in-place pass with O(1) space.",
            "tradeoff": "Optimal in-place modification.",
            "learning_point": "Two-pointer partitioning avoids allocating secondary arrays."
        }
    },
    "longest-substring": {
        "Sliding Window": {
            "why": "You maintain a dynamic window that expands with right and contracts with left on duplicates.",
            "better": "Reuses character frequencies without rescanning substrings.",
            "tradeoff": "Uses O(min(m, n)) space with linear O(n) runtime.",
            "learning_point": "Sliding window efficiently optimizes contiguous substring/subarray bounds."
        }
    },
    "subarray-sum-k": {
        "Prefix / Cumulative": {
            "why": "You compute cumulative running sums and check if (current_sum - k) occurred previously.",
            "better": "Avoids O(n²) nested range summations.",
            "tradeoff": "Uses O(n) space for running sum frequency hash map.",
            "learning_point": "Prefix sums combined with hashing convert range-sum queries to O(1) lookups."
        }
    },
    "number-of-islands": {
        "DFS / Graph Traversal": {
            "why": "You traverse connected components using depth-first search (DFS) or breadth-first search (BFS).",
            "better": "Visits each grid cell at most once, running in linear O(R * C) time.",
            "tradeoff": "Uses O(R * C) recursion stack/visited memory.",
            "learning_point": "Flood-fill grid exploration maps directly to connected components in graph theory."
        }
    }
}

def get_explanation(problem_id, pattern):
    if problem_id in EXPLANATIONS and pattern in EXPLANATIONS[problem_id]:
        return EXPLANATIONS[problem_id][pattern]

    generic = {
        "Linear Scan / Traversal": {
            "why": "Your code inspects each element once sequentially.",
            "better": "Linear scanning is optimal when all elements must be checked.",
            "tradeoff": "Uses O(1) space and O(n) time.",
            "learning_point": "Single-pass scans are standard for reduction operations."
        },
        "Hashing / Lookup": {
            "why": "Your code uses a hash table for fast element lookups.",
            "better": "Avoids repeated scans by leveraging O(1) expected lookup time.",
            "tradeoff": "Trades O(n) memory for runtime speed.",
            "learning_point": "Use hash tables to cache previously computed values."
        },
        "Binary Search": {
            "why": "Your code halves the search interval each iteration.",
            "better": "Optimal O(log n) search on sorted arrays.",
            "tradeoff": "Requires sorted order.",
            "learning_point": "Divide-and-conquer on monotonic intervals guarantees logarithmic search."
        },
        "Two Pointer": {
            "why": "Your code coordinates two indices across the sequence.",
            "better": "Avoids nested rescanning by moving pointers conditionally.",
            "tradeoff": "Uses O(1) space and O(n) time.",
            "learning_point": "Pointer convergence or partition scans reduce quadratic operations."
        },
        "Sliding Window": {
            "why": "Your code updates a contiguous interval dynamically.",
            "better": "Avoids recomputing overlapping ranges.",
            "tradeoff": "Achieves O(n) time with linear space.",
            "learning_point": "Maintain running state across adjacent windows."
        },
        "Prefix / Cumulative": {
            "why": "Your code tracks running cumulative sums.",
            "better": "Enables O(1) range sum evaluation.",
            "tradeoff": "Requires O(n) lookup memory.",
            "learning_point": "Prefix arrays convert range queries into differences of prefixes."
        },
        "Sorting": {
            "why": "Your code orders the data before processing.",
            "better": "Simplifies greedy choices and interval merges.",
            "tradeoff": "Requires O(n log n) comparison time.",
            "learning_point": "Sorting structures data for linear greedy sweeps."
        },
        "DFS / Graph Traversal": {
            "why": "Your code explores connected graph/grid nodes recursively.",
            "better": "Visits each vertex and edge once in O(V + E) time.",
            "tradeoff": "Requires call stack or visited tracking.",
            "learning_point": "Depth-first search isolates connected components."
        }
    }

    return generic.get(pattern, {
        "why": f"AURA detected a {pattern} approach.",
        "better": "Review your data structures to minimize redundant passes.",
        "tradeoff": "Analyze the time and space complexity trade-offs.",
        "learning_point": "Look for opportunities to eliminate repeated computation."
    })


# ============================================================
# CODE STRUCTURE ANALYSIS
# ============================================================

def analyze_code_structure(code: str):
    structure = {}
    loop_matches = list(re.finditer(r"\b(for|while)\s*\(", code))
    structure["loop_count"] = len(loop_matches)

    def get_brace_depth(position):
        return code[:position].count("{") - code[:position].count("}")

    loop_depths = [get_brace_depth(m.start()) for m in loop_matches]
    structure["has_nested_loops"] = any(
        loop_depths[j] > loop_depths[i]
        for i in range(len(loop_depths))
        for j in range(i + 1, len(loop_depths))
    )

    structure["has_unordered_map"] = (
        "unordered_map" in code
        or "unordered_set" in code
        or bool(re.search(r"\bmap\s*<", code))
        or bool(re.search(r"\bset\s*<", code))
    )

    structure["has_sorting"] = bool(
        re.search(r"\bsort\s*\(", code) or re.search(r"\bstable_sort\s*\(", code)
    )

    structure["has_two_pointers"] = bool(
        (re.search(r"\b(left|l|slow|i)\b", code) and re.search(r"\b(right|r|fast|j)\b", code))
        and ("++" in code or "--" in code)
    )

    structure["has_sliding_window"] = bool(
        re.search(r"\b(window|start|left|l)\b", code)
        and ("max(" in code or "min(" in code or "unordered_map" in code or "unordered_set" in code)
        and ("while" in code or "for" in code)
    )

    structure["has_binary_search"] = bool(
        re.search(r"\b(mid|middle)\b", code)
        and (
            re.search(r"(left|l|low)\s*=\s*(mid|middle)\s*\+\s*1", code)
            or re.search(r"(right|r|high)\s*=\s*(mid|middle)\s*-\s*1", code)
        )
    )

    structure["has_prefix_signal"] = bool(
        re.search(r"\b(prefix|pref|prefixSum|psum|cumulative|sum)\b", code, re.IGNORECASE)
        and ("unordered_map" in code or "map<" in code)
    )

    structure["has_dfs_structure"] = bool(
        ("dfs(" in code or "bfs(" in code or "floodFill" in code)
        or ("vector<vector" in code.replace(" ", "") and ("visited" in code.lower() or "grid[" in code))
    )

    structure["has_pair_sum"] = bool(
        re.search(r"\[[a-zA-Z_]\w*\]\s*\+\s*\[[a-zA-Z_]\w*\]", code)
        or re.search(r"\b\w+\s*\[\s*i\s*\]\s*\+\s*\w+\s*\[\s*j\s*\]", code)
    )

    structure["has_pair_comparison"] = bool(
        re.search(r"\b\w+\s*\[\s*i\s*\]\s*(==|!=|<=|>=|<|>)\s*\w+\s*\[\s*j\s*\]", code)
    )

    return structure


# ============================================================
# PATTERN DETECTION
# ============================================================

def detect_pattern(code: str):
    structure = analyze_code_structure(code)

    if structure["has_dfs_structure"]:
        return "DFS / Graph Traversal", "O(V + E)", "O(V)"

    if structure["has_binary_search"]:
        return "Binary Search", "O(log n)", "O(1)"

    if structure["has_prefix_signal"]:
        return "Prefix / Cumulative", "O(n)", "O(n)"

    if structure["has_sliding_window"] and structure["has_unordered_map"]:
        return "Sliding Window", "O(n)", "O(n)"

    if structure["has_unordered_map"]:
        return "Hashing / Lookup", "O(n) expected", "O(n)"

    if structure["has_sorting"]:
        return "Sorting", "O(n log n)", "O(1) or O(n)"

    if structure["has_two_pointers"]:
        return "Two Pointer", "O(n)", "O(1)"

    if structure["has_nested_loops"]:
        if structure["has_pair_sum"] or structure["has_pair_comparison"]:
            return "Brute Force / Pair Search", "O(n²)", "O(1)"
        return "Brute Force / Nested Loops", "O(n²)", "O(1)"

    if structure["loop_count"] > 0:
        return "Linear Scan / Traversal", "O(n)", "O(1)"

    return "Constant-Time / Simple Logic", "O(1)", "O(1)"


# ============================================================
# OPTIMIZATION & CORRECTNESS
# ============================================================

def _normalize_complexity(c: str) -> str:
    if not c:
        return ""
    return c.lower().replace(" ", "").replace("expected", "").replace("orv", "")

def _complexity_matches(curr: str, opt: str) -> bool:
    if not curr or not opt:
        return True
    return _normalize_complexity(curr) == _normalize_complexity(opt)

def get_optimization(pattern, complexity, space_complexity, code, problem_id=""):
    problem_info = PROBLEM_KNOWLEDGE.get(problem_id)

    if problem_info:
        optimal_pattern = problem_info["optimal_pattern"]
        optimal_time = problem_info["optimal_time"]
        optimal_space = problem_info["optimal_space"]

        pattern_matches = (
            (pattern == optimal_pattern)
            or (pattern in ["Hashing / Lookup", "Linear Scan / Traversal"] and optimal_pattern in ["Hashing / Lookup", "Linear Scan / Traversal"] and problem_id == "valid-anagram")
            or (pattern in ["Sliding Window", "Hashing / Lookup"] and optimal_pattern == "Sliding Window")
            or (pattern in ["Prefix / Cumulative", "Hashing / Lookup"] and optimal_pattern == "Prefix / Cumulative")
        )
        time_matches = _complexity_matches(complexity, optimal_time)

        if pattern_matches:
            return {
                "is_optimal": True,
                "current_approach": pattern,
                "current_time": complexity,
                "current_space": space_complexity,
                "optimal_pattern": optimal_pattern,
                "optimal_time": optimal_time,
                "optimal_space": optimal_space,
                "improvement": "Optimal approach detected.",
                "recommendation": f"{pattern} is the optimal strategy for this problem.",
                "optimization_level": "Optimal"
            }

        return {
            "is_optimal": False,
            "current_approach": pattern,
            "current_time": complexity,
            "current_space": space_complexity,
            "optimal_pattern": optimal_pattern,
            "optimal_time": optimal_time,
            "optimal_space": optimal_space,
            "improvement": f"Switch from {pattern} to {optimal_pattern} to achieve {optimal_time}.",
            "recommendation": f"Optimal pattern is {optimal_pattern}.",
            "optimization_level": "Optimization Available"
        }

    return {
        "is_optimal": True if pattern in ["Hashing / Lookup", "Linear Scan / Traversal", "Binary Search", "Two Pointer", "Sliding Window", "Prefix / Cumulative", "DFS / Graph Traversal"] else False,
        "current_approach": pattern,
        "current_time": complexity,
        "current_space": space_complexity,
        "optimal_pattern": pattern,
        "optimal_time": complexity,
        "optimal_space": space_complexity,
        "improvement": "Approach is efficient.",
        "recommendation": f"{pattern} is a suitable strategy.",
        "optimization_level": "Likely Optimal"
    }


def get_hints(problem_id, pattern, complexity, execution=None):
    if problem_id in ["two-sum", "valid-anagram", "contains-duplicate"]:
        if "Brute Force" in pattern:
            return [
                "Your solution uses nested comparisons.",
                "Can you use a frequency table or hash map for O(1) lookup?",
                "This achieves expected O(n) runtime."
            ]
        return ["Great approach! You used an optimal lookup pattern."]
    
    if problem_id == "binary-search":
        if pattern == "Linear Scan / Traversal":
            return [
                "The array is sorted.",
                "Can you divide the search range in half each step?",
                "Think about Binary Search for O(log n) time."
            ]
        return ["Great job implementing binary search."]

    if problem_id == "longest-substring":
        return ["Maintain a hash map of character last-seen indices to slide the left boundary cleanly."]

    if problem_id == "subarray-sum-k":
        return ["Store cumulative prefix sums in a hash map to count previous occurrences of (sum - k)."]

    return ["Look at the structure of repeated operations to see if lookup caching or pointers can optimize time."]


def analyze_code(code: str, execution: dict, problem_id: str = "", problem_statement: str = ""):
    pattern, complexity, space_complexity = detect_pattern(code)
    status = execution.get("status", "unknown")
    passed = execution.get("passed", 0)
    total = execution.get("total", 0)

    correctness_score = 100 if status == "accepted" else (int((passed / total) * 100) if total > 0 else 0)

    optimization = get_optimization(pattern, complexity, space_complexity, code, problem_id)
    explanation = get_explanation(problem_id, pattern)
    hints = get_hints(problem_id, pattern, complexity, execution)

    return {
        "correctness_score": correctness_score,
        "complexity": complexity,
        "space_complexity": space_complexity,
        "pattern": pattern,
        "code_quality": "Readable and clean",
        "coach": {
            "hints": hints,
            "hint_count": len(hints)
        },
        "optimization": optimization.get("recommendation", "No optimization necessary."),
        "optimization_engine": {
            "is_optimal": optimization.get("is_optimal", False),
            "optimal_pattern": optimization.get("optimal_pattern", pattern),
            "optimal_time": optimization.get("optimal_time", complexity),
            "optimal_space": optimization.get("optimal_space", space_complexity),
            "improvement": optimization.get("improvement", "")
        },
        "explanation_engine": explanation
    }