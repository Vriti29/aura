import re

# ============================================================
# PROBLEM KNOWLEDGE BASE
# ============================================================

PROBLEM_KNOWLEDGE = {

    # --------------------------------------------------------
    # 1. TWO SUM
    # --------------------------------------------------------
    "two-sum": {
        "optimal_pattern": "Hashing / Lookup",
        "optimal_time": "O(n) expected",
        "optimal_space": "O(n)"
    },

    # --------------------------------------------------------
    # 2. MAXIMUM ELEMENT
    # --------------------------------------------------------
    "max-element": {
        "optimal_pattern": "Linear Scan / Traversal",
        "optimal_time": "O(n)",
        "optimal_space": "O(1)"
    },

    # --------------------------------------------------------
    # 3. BINARY SEARCH
    # --------------------------------------------------------
    "binary-search": {
        "optimal_pattern": "Binary Search",
        "optimal_time": "O(log n)",
        "optimal_space": "O(1)"
    },

    # --------------------------------------------------------
    # 4. BEST TIME TO BUY AND SELL STOCK
    # --------------------------------------------------------
    "best-time-stock": {
        "optimal_pattern": "Linear Scan / Traversal",
        "optimal_time": "O(n)",
        "optimal_space": "O(1)"
    },

    # --------------------------------------------------------
    # 5. MAXIMUM SUBARRAY
    # --------------------------------------------------------
    "maximum-subarray": {
        "optimal_pattern": "Linear Scan / Traversal",
        "optimal_time": "O(n)",
        "optimal_space": "O(1)"
    },
    # --------------------------------------------------------
    # 6. VALID ANAGRAM
    # --------------------------------------------------------
    "valid-anagram": {
        "optimal_pattern": "Hashing / Lookup",
        "optimal_time": "O(n)",
        "optimal_space": "O(n)"
    },

    # --------------------------------------------------------
    # 7. CONTAINS DUPLICATE
    # --------------------------------------------------------
    "contains-duplicate": {
        "optimal_pattern": "Hashing / Lookup",
        "optimal_time": "O(n) expected",
        "optimal_space": "O(n)"
    },

    # --------------------------------------------------------
    # 8. MOVE ZEROES
    # --------------------------------------------------------
    "move-zeroes": {
        "optimal_pattern": "Two Pointer",
        "optimal_time": "O(n)",
        "optimal_space": "O(1)"
    },

    # --------------------------------------------------------
    # 9. LONGEST SUBSTRING WITHOUT REPEATING
    # --------------------------------------------------------
    "longest-substring": {
        "optimal_pattern": "Sliding Window",
        "optimal_time": "O(n)",
        "optimal_space": "O(n)"
    },

    # --------------------------------------------------------
    # 10. SUBARRAY SUM EQUALS K
    # --------------------------------------------------------
    "subarray-sum-k": {
        "optimal_pattern": "Prefix / Cumulative",
        "optimal_time": "O(n)",
        "optimal_space": "O(n)"
    },

    # --------------------------------------------------------
    # 11. MERGE INTERVALS
    # --------------------------------------------------------
    "merge-intervals": {
        "optimal_pattern": "Sorting",
        "optimal_time": "O(n log n)",
        "optimal_space": "O(n)"
    },

    # --------------------------------------------------------
    # 12. NUMBER OF ISLANDS
    # --------------------------------------------------------
    "number-of-islands": {
        "optimal_pattern": "DFS / Graph Traversal",
        "optimal_time": "O(V + E)",
        "optimal_space": "O(V)"
    }
}
# ============================================================
# AURA EXPLANATION KNOWLEDGE
# ============================================================

EXPLANATIONS = {
    "two-sum": {

        "Brute Force / Pair Search": {
            "why": (
                "You're checking the array two elements at a time. "
                "That works, but in the worst case you end up checking "
                "almost every possible pair, which takes O(n²) time."
            ),

            "better": (
                "A hash map can keep track of the numbers you've already "
                "seen. For each number, check whether target - current "
                "number is already in the map."
            ),

            "tradeoff": (
                "The hash map needs O(n) extra space, but it brings the "
                "expected running time down from O(n²) to O(n)."
            ),

            "learning_point": (
                "If you're repeatedly searching for whether a value exists, "
                "a hash map is often a good way to avoid scanning again."
            )
        },

        "Hashing / Lookup": {
            "why": (
                "You're storing numbers you've already seen in a hash map "
                "and checking for the required complement as you go."
            ),

            "better": (
                "For Two Sum, this is the standard efficient approach. "
                "Each number is processed once and the hash map gives an "
                "expected O(1) lookup."
            ),

            "tradeoff": (
                "The solution uses O(n) extra space to get expected O(n) "
                "time."
            ),

            "learning_point": (
                "The main idea is simple: remember what you've seen so you "
                "don't have to search through it again."
            )
        }
    },
    # ========================================================
    # MAXIMUM ELEMENT
    # ========================================================

    "max-element": {

        "Linear Scan / Traversal": {

            "why": (
                "You're scanning the array from left to right and "
                "keeping track of the largest value seen so far."
            ),

            "better": (
                "For finding the maximum element, a linear scan is "
                "already optimal because every element must be checked "
                "at least once."
            ),

            "tradeoff": (
                "The solution uses O(1) extra space and O(n) time. "
                "There is no asymptotically faster approach because "
                "an unseen element could still be the maximum."
            ),

            "learning_point": (
                "When the answer depends on every element, a single "
                "linear traversal is often the optimal approach."
            )
        }
    },


    # ========================================================
    # BINARY SEARCH
    # ========================================================

    "binary-search": {

        "Binary Search": {

            "why": (
                "You're using the sorted order of the array to repeatedly "
                "divide the search range into two halves."
            ),

            "better": (
                "Binary search is already the optimal approach here. "
                "Instead of checking every element, each comparison "
                "eliminates roughly half of the remaining search space."
            ),

            "tradeoff": (
                "The iterative approach uses O(1) extra space and "
                "achieves O(log n) time. It relies on the array being sorted."
            ),

            "learning_point": (
                "Whenever the search space is sorted, ask whether one "
                "comparison can eliminate half of the possibilities."
            )
        },

        "Linear Scan / Traversal": {

            "why": (
                "You're checking the elements sequentially from left "
                "to right until the target is found."
            ),

            "better": (
                "Because the array is sorted, binary search can eliminate "
                "half of the remaining search space after each comparison."
            ),

            "tradeoff": (
                "Linear search uses O(1) extra space but can take O(n) time. "
                "Binary search uses the same O(1) extra space while reducing "
                "the expected search time to O(log n)."
            ),

            "learning_point": (
                "A sorted array is a strong signal to check whether "
                "binary search can replace a linear scan."
            )
        }
    }
}


# ============================================================
# EXPLANATION ENGINE
# ============================================================

def get_explanation(problem_id, pattern):

    # --------------------------------------------------------
    # Problem-specific explanation
    # --------------------------------------------------------


    
    # Use problem-specific explanation when available
    if problem_id in EXPLANATIONS:
        problem_explanations = EXPLANATIONS[problem_id]

        if pattern in problem_explanations:
            return problem_explanations[pattern]
    # --------------------------------------------------------
    # Generic fallback
    # --------------------------------------------------------

    explanations = {

        "Linear Scan / Traversal": {
            "why": (
                "Your code processes the input sequentially, "
                "examining each element once to build the result."
            ),

            "better": (
                "A linear scan is already efficient when the required "
                "information must be obtained by examining the input."
            ),

            "tradeoff": (
                "This approach uses constant extra space, but requires "
                "one pass through the input, giving O(n) time."
            ),

            "learning_point": (
                "When every element needs to be inspected at least once, "
                "a single linear traversal is often the simplest optimal approach."
            )
        },

        "Hashing / Lookup": {
            "why": (
                "Your code uses a hash-based data structure to store "
                "information and perform fast lookups."
            ),

            "better": (
                "Hashing can avoid repeatedly searching through the input "
                "and usually provides expected O(1) lookup time."
            ),

            "tradeoff": (
                "The faster lookups require additional memory, typically O(n)."
            ),

            "learning_point": (
                "Ask whether previously seen information can be stored "
                "so that future searches become faster."
            )
        },

        "Binary Search": {
            "why": (
                "Your code repeatedly divides the search range and "
                "eliminates half of the remaining possibilities."
            ),

            "better": (
                "Binary search is highly efficient when the input or "
                "search space satisfies the required ordering condition."
            ),

            "tradeoff": (
                "Binary search achieves O(log n) time, but it requires "
                "the search space to support the necessary ordering property."
            ),

            "learning_point": (
                "Look for situations where each step can eliminate "
                "roughly half of the remaining search space."
            )
        },

        "Two Pointer": {
            "why": (
                "Your code maintains two positions in the input and "
                "moves them strategically instead of repeatedly scanning "
                "the same elements."
            ),

            "better": (
                "Two pointers can reduce repeated comparisons and often "
                "process the input in a single linear pass."
            ),

            "tradeoff": (
                "The approach usually achieves O(n) time and O(1) extra "
                "space, but it depends on the structure of the problem."
            ),

            "learning_point": (
                "When working with sequences, check whether two moving "
                "indices can replace repeated nested searches."
            )
        },
        "Sliding Window": {
            "why": (
                "Your code maintains a window over a sequence and updates "
                "the window incrementally instead of recalculating the "
                "entire window each time."
            ),

            "better": (
                "Sliding Window reuses information from the previous window. "
                "Instead of calculating each window from scratch, it adds "
                "the new element and removes the element that leaves the window."
            ),

            "tradeoff": (
                "This approach can reduce repeated work and achieve O(n) time "
                "with O(1) extra space when only a few running variables are needed."
            ),

            "learning_point": (
                "When solving problems involving contiguous subarrays or "
                "substrings, check whether a moving window can avoid "
                "recomputing overlapping ranges."
            )
        },

        "Brute Force / Pair Search": {
            "why": (
                "Your code checks multiple combinations of elements, "
                "which causes repeated comparisons."
            ),

            "better": (
                "Look for a way to avoid checking the same combinations "
                "repeatedly. Depending on the problem, hashing, sorting, "
                "two pointers, or another data structure may help."
            ),

            "tradeoff": (
                "Brute force is usually simple to understand, but repeated "
                "comparisons can increase the running time to O(n²) or more."
            ),

            "learning_point": (
                "Whenever you see nested loops, ask whether the inner work "
                "can be eliminated, stored, or performed more efficiently."
            )
        },
        "BFS / Graph Traversal": {
            "why": (
                "Your code explores the graph level by level using a queue "
                "and keeps track of visited vertices."
            ),

            "better": (
                "BFS processes each reachable vertex and edge once, giving "
                "O(V + E) time with an adjacency-list representation."
            ),

            "tradeoff": (
                "BFS uses a queue and visited structure, requiring O(V) "
                "additional space in the worst case."
            ),

            "learning_point": (
                "When a graph problem requires level-by-level exploration "
                "or shortest paths in an unweighted graph, BFS is a strong "
                "pattern to consider."
            )
        },

        "DFS / Graph Traversal": {
            "why": (
                "Your code explores the graph by going as deep as possible "
                "before backtracking, while tracking visited vertices."
            ),

            "better": (
                "DFS processes each reachable vertex and edge once, giving "
                "O(V + E) time with an adjacency-list representation."
            ),

            "tradeoff": (
                "DFS requires O(V) space for the visited structure and, "
                "when implemented recursively, the call stack."
            ),

            "learning_point": (
                "When a graph problem involves exploring connected components, "
                "paths, cycles, or reachability, DFS is an important pattern to consider."
            )
        },

        "Recursion": {
            "why": (
                "Your code solves the problem by breaking it into smaller "
                "subproblems through recursive calls."
            ),

            "better": (
                "Check whether recursive calls repeat the same subproblems. "
                "If they do, memoization, dynamic programming, or an "
                "iterative approach may reduce repeated work."
            ),

            "tradeoff": (
                "Recursion can make the solution easier to express, but "
                "recursive calls consume call-stack space."
            ),

            "learning_point": (
                "Identify the base case, the smaller subproblem, and whether "
                "the same subproblem is solved more than once."
            )
        }
    }

    # Generic pattern explanation
    if pattern in explanations:
        return explanations[pattern]

    # Final fallback
    return {
        "why": (
            f"AURA detected a {pattern} approach in your code "
            "based on its structural characteristics."
        ),

        "better": (
            "No generic alternative was identified. Review the detected "
            "complexity and look for repeated work or unnecessary operations."
        ),

        "tradeoff": (
            "The time-space trade-off depends on the specific operations "
            "performed by this approach."
        ),

        "learning_point": (
            "Focus on identifying repeated work and determining whether "
            "the same result can be obtained with fewer operations."
        )
    }

# ============================================================
# CODE STRUCTURE ANALYSIS
# ============================================================

def analyze_code_structure(code: str):

    structure = {}

    # --------------------------------------------------------
    # Loop information
    # --------------------------------------------------------


    loop_matches = list(
        re.finditer(r"\b(for|while)\s*\(", code)
    )

    loop_count = len(loop_matches)

    structure["loop_count"] = loop_count

    # Detect actual nesting using brace depth.
    # Two sequential loops are NOT nested.

    def get_brace_depth(position):
        return code[:position].count("{") - code[:position].count("}")

    loop_depths = [
        get_brace_depth(match.start())
        for match in loop_matches
    ]

    structure["has_nested_loops"] = any(
        loop_depths[j] > loop_depths[i]
        for i in range(len(loop_depths))
        for j in range(i + 1, len(loop_depths))
    )

    # --------------------------------------------------------
    # Data structures
    # --------------------------------------------------------

    structure["has_unordered_map"] = (
        "unordered_map" in code
        or "unordered_set" in code
    )

    structure["has_ordered_map"] = (
        bool(re.search(r"\bmap\s*<", code))
        or bool(re.search(r"\bset\s*<", code))
    )

    # --------------------------------------------------------
    # Sorting
    # --------------------------------------------------------

    structure["has_sorting"] = bool(
        re.search(r"\bsort\s*\(", code)
        or re.search(r"\bstable_sort\s*\(", code)
    )

    # --------------------------------------------------------
    # Two-pointer signals
    # --------------------------------------------------------

    structure["has_left_pointer"] = bool(
        re.search(r"\b(left|l)\b", code)
    )

    structure["has_right_pointer"] = bool(
        re.search(r"\b(right|r)\b", code)
    )

    structure["has_two_pointers"] = (
        structure["has_left_pointer"]
        and structure["has_right_pointer"]
    )
    # --------------------------------------------------------
    # Sliding Window signals
    # --------------------------------------------------------

    structure["has_sliding_window"] = (
        bool(
            re.search(
                r"\b\w+\s*\+=\s*\w+\s*\[\s*i\s*\]",
                code
            )
        )
        and
        bool(
            re.search(
                r"\b\w+\s*-=\s*\w+\s*\[\s*i\s*-\s*\w+\s*\]",
                code
            )
        )
    )

    # --------------------------------------------------------
    # Binary search signals
    # --------------------------------------------------------

    structure["has_mid"] = bool(
        re.search(r"\b(mid|middle)\b", code)
    )

    structure["has_binary_search_update"] = bool(
        re.search(
            r"(left|l)\s*=\s*(mid|middle)\s*\+\s*1",
            code
        )
        or
        re.search(
            r"(right|r)\s*=\s*(mid|middle)\s*-\s*1",
            code
        )
        or
        re.search(
            r"(high|hi)\s*=\s*(mid|middle)\s*-\s*1",
            code
        )
        or
        re.search(
            r"(low|lo)\s*=\s*(mid|middle)\s*\+\s*1",
            code
        )
    )

    structure["has_binary_search"] = (
        structure["has_mid"]
        and structure["has_binary_search_update"]
    )

    # --------------------------------------------------------
    # Prefix / cumulative signals
    # --------------------------------------------------------

    structure["has_prefix_signal"] = bool(
        re.search(
            r"\b(prefix|pref|prefixSum|psum|cumulative)\b",
            code,
            re.IGNORECASE
        )
    )

    # --------------------------------------------------------
    # Pair-comparison signals
    # --------------------------------------------------------

    structure["has_pair_sum"] = bool(
        re.search(
            r"\[[a-zA-Z_]\w*\]\s*\+\s*\[[a-zA-Z_]\w*\]",
            code
        )
        or
        re.search(
            r"\b\w+\s*\[\s*i\s*\]\s*\+\s*\w+\s*\[\s*j\s*\]",
            code
        )
    )

    structure["has_pair_comparison"] = bool(
        re.search(
            r"\b\w+\s*\[\s*i\s*\]\s*"
            r"(==|!=|<=|>=|<|>)\s*"
            r"\w+\s*\[\s*j\s*\]",
            code
        )
        or
        re.search(
            r"\b\w+\s*\[\s*j\s*\]\s*"
            r"(==|!=|<=|>=|<|>)\s*"
            r"\w+\s*\[\s*i\s*\]",
            code
        )
    )

    # --------------------------------------------------------
    # Membership / lookup signals
    # --------------------------------------------------------

    structure["has_lookup_operation"] = bool(
        re.search(
            r"\.find\s*\(",
            code
        )
        or
        re.search(
            r"\.count\s*\(",
            code
        )
        or
        "unordered_map" in code
        or
        "unordered_set" in code
    )
    # --------------------------------------------------------
    # Graph / DFS signals
    # --------------------------------------------------------

    structure["has_graph_adjacency"] = bool(
        re.search(
            r"vector\s*<\s*vector\s*<",
            code
        )
    )

    structure["has_visited"] = bool(
        re.search(
            r"\bvisited\b",
            code,
            re.IGNORECASE
        )
    )

    structure["has_graph_neighbors"] = bool(
        re.search(
            r"\bgraph\s*\[",
            code
        )
    )

    structure["has_queue"] = bool(
        re.search(
            r"\bqueue\s*<",
            code
        )
    )

    structure["has_dfs_structure"] = (
        structure["has_graph_adjacency"]
        and
        structure["has_visited"]
        and
        structure["has_graph_neighbors"]
        and
        not structure["has_queue"]
    )
    structure["has_bfs_structure"] = (
        structure["has_graph_adjacency"]
        and
        structure["has_visited"]
        and
        structure["has_graph_neighbors"]
        and
        structure["has_queue"]
    )

    # --------------------------------------------------------
    # Recursion
    # --------------------------------------------------------

    function_names = re.findall(
        r"\b(?:int|void|bool|long\s+long|string|double)\s+"
        r"(\w+)\s*\([^;{}]*\)\s*\{",
        code
    )

    structure["has_recursion"] = False

    for name in function_names:

        occurrences = len(
            re.findall(
                rf"\b{name}\s*\(",
                code
            )
        )

        # One occurrence is the function definition itself.
        if occurrences > 1:
            structure["has_recursion"] = True
            break

    return structure

# ============================================================
# PATTERN DETECTION
# ============================================================

def detect_pattern(code: str):

    structure = analyze_code_structure(code)

    # --------------------------------------------------------
    # Most specific patterns first
    # --------------------------------------------------------

    if structure["has_binary_search"]:
        return (
            "Binary Search",
            "O(log n)",
            "O(1)"
        )

    if structure["has_unordered_map"]:
        return (
            "Hashing / Lookup",
            "O(n) expected",
            "O(n)"
        )

    if structure["has_ordered_map"]:
        return (
            "Ordered Map / Set",
            "O(n log n)",
            "O(n)"
        )

    if structure["has_sliding_window"]:
        return (
            "Sliding Window",
            "O(n)",
            "O(1)"
        )

    if structure["has_two_pointers"]:
        return (
            "Two Pointer",
            "O(n)",
            "O(1)"
        )
    if structure["has_sorting"]:
        return (
            "Sorting",
            "O(n log n)",
            "O(1) or O(n)"
        )

    if structure["has_prefix_signal"]:
        return (
            "Prefix / Cumulative",
            "O(n)",
            "O(n)"
        )
    if structure["has_bfs_structure"]:
        return (
            "BFS / Graph Traversal",
            "O(V + E)",
            "O(V)"
        )

    if structure["has_dfs_structure"]:
        return (
            "DFS / Graph Traversal",
            "O(V + E)",
            "O(V)"
        )

    if structure["has_recursion"]:
        return (
            "Recursion",
            "Depends on recursive structure",
            "Depends on recursion depth"
        )
    # --------------------------------------------------------
    # Nested loops
    # --------------------------------------------------------

    if structure["has_nested_loops"]:

        if structure["has_pair_sum"] or structure["has_pair_comparison"]:
            return (
                "Brute Force / Pair Search",
                "O(n²)",
                "O(1)"
            )

        return (
            "Brute Force / Nested Loops",
            "O(n²)",
            "O(1)"
        )

    # --------------------------------------------------------
    # Single traversal
    # --------------------------------------------------------

    if structure["loop_count"] > 0:
        return (
            "Linear Scan / Traversal",
            "O(n)",
            "O(1)"
        )

    return (
        "Constant-Time / Simple Logic",
        "O(1)",
        "O(1)"
    )
# ============================================================
# OPTIMIZATION ENGINE
# ============================================================
# ============================================================
# PROBLEM IDENTIFICATION
# ============================================================

def identify_problem(problem_statement: str):

    if not problem_statement:
        return "generic"

    text = problem_statement.lower()

    # --------------------------------------------------------
    # Two Sum
    # --------------------------------------------------------
    if (
        "two numbers" in text
        and "sum" in text
        and "target" in text
    ):
        return "two-sum"

    # --------------------------------------------------------
    # Maximum Element
    # --------------------------------------------------------
    if (
        ("maximum" in text or "largest" in text)
        and "array" in text
    ):
        return "max-element"

    # --------------------------------------------------------
    # Binary Search
    # --------------------------------------------------------
    if (
        "binary search" in text
        or (
            "sorted array" in text
            and "search" in text
        )
    ):
        return "binary-search"

    # --------------------------------------------------------
    # Best Time to Buy and Sell Stock
    # --------------------------------------------------------
    if (
        "buy" in text
        and "sell" in text
        and "stock" in text
    ):
        return "best-time-stock"

    # --------------------------------------------------------
    # Maximum Subarray
    # --------------------------------------------------------
    if (
        "maximum subarray" in text
        or "maximum sum subarray" in text
        or "largest sum contiguous" in text
    ):
        return "maximum-subarray"

    # --------------------------------------------------------
    # Valid Anagram
    # --------------------------------------------------------
    if (
        "valid anagram" in text
        or (
            "anagram" in text
            and "string" in text
        )
    ):
        return "valid-anagram"

    # --------------------------------------------------------
    # Contains Duplicate
    # --------------------------------------------------------
    if (
        "contains duplicate" in text
        or "duplicate" in text
        and "array" in text
    ):
        return "contains-duplicate"

    # --------------------------------------------------------
    # Move Zeroes
    # --------------------------------------------------------
    if (
        "move zeroes" in text
        or "move zeros" in text
    ):
        return "move-zeroes"

    # --------------------------------------------------------
    # Longest Substring Without Repeating
    # --------------------------------------------------------
    if (
        "longest substring" in text
        and (
            "without repeating" in text
            or "unique characters" in text
        )
    ):
        return "longest-substring"

    # --------------------------------------------------------
    # Subarray Sum Equals K
    # --------------------------------------------------------
    if (
        "subarray sum" in text
        and (
            "equals k" in text
            or "equal k" in text
            or "target k" in text
        )
    ):
        return "subarray-sum-k"

    # --------------------------------------------------------
    # Merge Intervals
    # --------------------------------------------------------
    if (
        "merge intervals" in text
        or "overlapping intervals" in text
    ):
        return "merge-intervals"

    # --------------------------------------------------------
    # Number of Islands
    # --------------------------------------------------------
    if (
        "number of islands" in text
        or (
            "island" in text
            and (
                "grid" in text
                or "matrix" in text
            )
        )
    ):
        return "number-of-islands"

    return "generic"

def get_optimization(
    pattern,
    complexity,
    space_complexity,
    code,
    problem_id=""
):
    problem_info = PROBLEM_KNOWLEDGE.get(problem_id)

    if problem_info:
        optimal_pattern = problem_info["optimal_pattern"]
        optimal_time = problem_info["optimal_time"]
        optimal_space = problem_info["optimal_space"]

        if pattern == optimal_pattern:
            return {
                "is_optimal": True,
                "current_approach": pattern,
                "optimal_pattern": optimal_pattern,
                "current_time": complexity,
                "optimal_time": optimal_time,
                "optimal_space": optimal_space,
                "improvement": "No major asymptotic improvement detected.",
                "message": (
                    f"{pattern} is an appropriate approach for this problem "
                    f"with {complexity} time complexity."
                )
            }

        return {
            "current_approach": pattern,
            "optimal_pattern": optimal_pattern,
            "current_time": complexity,
            "optimal_time": optimal_time,
            "optimal_space": optimal_space,
            "improvement": (
                f"Consider {optimal_pattern} to target "
                f"{optimal_time} time complexity."
            ),
            "message": (
                f"The detected approach is {pattern}, while this problem "
                f"is better suited to {optimal_pattern}."
            )
        }

    # --------------------------------------------------------
    # Linear Scan
    # --------------------------------------------------------

    if pattern == "Linear Scan / Traversal":
        return {
            "is_optimal": True,
            "optimal_pattern": "Linear Scan / Traversal",
            "optimal_time": "O(n)",
            "optimal_space": "O(1)",
            "improvement": "No major asymptotic improvement detected.",
            "recommendation": (
                "A single pass through the input is already an efficient "
                "approach when the required information must be obtained "
                "by examining the elements."
            )
        }

    # --------------------------------------------------------
    # Hashing
    # --------------------------------------------------------

    if pattern == "Hashing / Lookup":
        return {
            "is_optimal": True,
            "optimal_pattern": "Hashing / Lookup",
            "optimal_time": "O(n) expected",
            "optimal_space": "O(n)",
            "improvement": "No major asymptotic improvement detected.",
            "recommendation": (
                "The code uses fast lookups to avoid repeatedly scanning "
                "previously processed data."
            )
        }

    # --------------------------------------------------------
    # Binary Search
    # --------------------------------------------------------

    if pattern == "Binary Search":
        return {
            "is_optimal": True,
            "optimal_pattern": "Binary Search",
            "optimal_time": "O(log n)",
            "optimal_space": "O(1)",
            "improvement": "No major asymptotic improvement detected.",
            "recommendation": (
                "The search space is reduced at each step, giving "
                "logarithmic time when the required ordering condition holds."
            )
        }

    # --------------------------------------------------------
    # Two Pointer
    # --------------------------------------------------------

    if pattern == "Two Pointer":
        return {
            "is_optimal": True,
            "optimal_pattern": "Two Pointer",
            "optimal_time": "O(n)",
            "optimal_space": "O(1)",
            "improvement": "No major asymptotic improvement detected.",
            "recommendation": (
                "The code uses multiple moving positions to process the "
                "input without repeatedly scanning the same elements."
            )
        }
    # --------------------------------------------------------
    # Sliding Window
    # --------------------------------------------------------

    if pattern == "Sliding Window":
        return {
            "is_optimal": True,
            "optimal_pattern": "Sliding Window",
            "optimal_time": "O(n)",
            "optimal_space": "O(1)",
            "improvement": "No major asymptotic improvement detected.",
            "recommendation": (
                "Sliding Window efficiently updates the current window "
                "instead of recalculating overlapping ranges."
            )
        }
    # --------------------------------------------------------
    # BFS / DFS Graph Traversal
    # --------------------------------------------------------

    if pattern in (
        "BFS / Graph Traversal",
        "DFS / Graph Traversal"
    ):
        return {
            "is_optimal": True,
            "optimal_pattern": pattern,
            "optimal_time": "O(V + E)",
            "optimal_space": "O(V)",
            "improvement": "No major asymptotic improvement detected.",
            "recommendation": (
                f"{pattern} is an efficient graph traversal approach "
                "with O(V + E) time complexity when each vertex and edge "
                "is processed once."
            )
        }

    # --------------------------------------------------------
    # Nested loops / Brute Force
    # --------------------------------------------------------

    if pattern == "Brute Force / Pair Search":
        return {
            "is_optimal": False,
            "optimal_pattern": "Hashing / Lookup",
            "optimal_time": "O(n) expected",
            "optimal_space": "O(n)",
            "improvement": (
                "Repeated pair comparisons can be reduced by "
                "using a faster lookup strategy."
            ),
            "recommendation": (
                "The code checks every possible pair, which leads to "
                "O(n²) time. A hash-based lookup can store previously "
                "seen values and avoid repeatedly comparing pairs."
            )
        }
        

    if pattern == "Brute Force / Nested Loops":

        return {
            "is_optimal": None,
            "optimal_pattern": "Problem-dependent",
            "optimal_time": "Problem-dependent",
            "optimal_space": "Problem-dependent",
            "improvement": (
                "Nested loops do not automatically mean the algorithm "
                "can be improved."
            ),
            "recommendation": (
                "Check whether the inner computation is repeated "
                "unnecessarily. Depending on the operation, techniques "
                "such as hashing, prefix information, sorting, binary "
                "search, or a different data structure may reduce the work."
            )
        }
    # --------------------------------------------------------
    # Recursion
    # --------------------------------------------------------

    if pattern == "Recursion":
        return {
            "is_optimal": False,
            "optimal_pattern": "Problem-dependent",
            "optimal_time": "Problem-dependent",
            "optimal_space": "Problem-dependent",
            "improvement": (
                "The recursive structure may or may not be optimal."
            ),
            "recommendation": (
                "Check whether recursive calls repeat the same subproblems. "
                "If they do, consider memoization, dynamic programming, "
                "pruning, or an iterative approach."
            )
    }
                
    # --------------------------------------------------------
    # Generic fallback
    # --------------------------------------------------------

    return {
        "is_optimal": None,
        "optimal_pattern": "Problem-dependent",
        "optimal_time": "Unknown",
        "optimal_space": "Unknown",
        "improvement": "No reliable generic optimization detected.",
        "recommendation": (
            "Review the detected complexity and look for repeated work, "
            "unnecessary operations, or opportunities to use a more "
            "appropriate data structure or algorithm."
        )
    }        
      
# ============================================================
# COACH / HINT ENGINE
# ============================================================

def get_hints(problem_id, pattern, complexity, execution=None):

    hints = []

    # --------------------------------------------------------
    # Two Sum
    # --------------------------------------------------------

    if problem_id == "two-sum":

        if pattern == "Brute Force / Pair Search":
            hints = [
                "Your solution checks many pairs repeatedly.",
                "Can you remember values you have already seen?",
                "What data structure gives fast lookup?",
                "Think about a hash map with expected O(1) lookup."
            ]

        elif pattern == "Hashing / Lookup":
            hints = [
                "Good choice! You are storing previously seen values.",
                "Check whether the required complement is already present.",
                "This gives expected O(n) time."
            ]

    # --------------------------------------------------------
    # Binary Search
    # --------------------------------------------------------

    elif problem_id == "binary-search":

        if pattern == "Linear Scan / Traversal":
            hints = [
                "The array is sorted.",
                "Do you really need to inspect every element?",
                "Can one comparison eliminate half of the search space?",
                "Think about Binary Search."
            ]

        elif pattern == "Binary Search":
            hints = [
                "Good choice!",
                "You are using the sorted property correctly.",
                "Each comparison eliminates roughly half of the search space."
            ]

    # --------------------------------------------------------
    # Maximum Element
    # --------------------------------------------------------

    elif problem_id == "max-element":

        hints = [
            "You need to inspect the elements to know which is largest.",
            "Can you keep track of the best value seen so far?",
            "A single traversal is sufficient."
        ]

    # --------------------------------------------------------
    # Generic
    # --------------------------------------------------------

    else:

        hints = [
            "Look at the repeated work in your solution.",
            "Ask whether previously computed information can be reused.",
            "Consider whether a different data structure can reduce the work."
        ]

    return hints
# ============================================================
# MAIN ANALYZER
# ============================================================

def analyze_code(
    code: str,
    execution: dict,
    problem_id: str = "",
    problem_statement: str = ""
):

    # --------------------------------------------------------
    # Detect pattern
    # --------------------------------------------------------

    pattern, complexity, space_complexity = detect_pattern(code)

    # --------------------------------------------------------
    # Identify problem
    # --------------------------------------------------------

    if not problem_id or problem_id == "generic":
        if problem_statement:
            problem_id = identify_problem(problem_statement)

    # --------------------------------------------------------
    # Correctness
    # --------------------------------------------------------

    if execution.get("status") == "accepted":

        correctness_score = 100

    elif execution.get("status") == "compile_error":

        correctness_score = 20

    elif execution.get("status") == "compile_timeout":

        correctness_score = 10

    else:

        total = execution.get("total", 1)
        passed = execution.get("passed", 0)

        correctness_score = (
            int((passed / total) * 100)
            if total
            else 0
        )

    # --------------------------------------------------------
    # Code quality
    # --------------------------------------------------------

    code_length = len(code)

    has_comments = (
        "//" in code
        or "/*" in code
    )

    if code_length < 4000 and has_comments:

        code_quality = "Readable and documented"

    elif code_length < 4000:

        code_quality = "Readable"

    else:

        code_quality = "Consider refactoring"

    # --------------------------------------------------------
    # Optimization
    # --------------------------------------------------------

    optimization = get_optimization(
    pattern,
    complexity,
    space_complexity,
    code,
    problem_id
    )
    explanation = get_explanation(
        problem_id,
        pattern
    )

    # --------------------------------------------------------
    # Final response
    # --------------------------------------------------------
    hints = get_hints(
        problem_id,
        pattern,
        complexity,
        execution
    )
    return {

        "correctness_score": correctness_score,

        "complexity": complexity,

        "space_complexity": space_complexity,

        "pattern": pattern,

        "code_quality": code_quality,

        "coach": {
            "hints": hints,
            "hint_count": len(hints)
        },

        "optimization": optimization.get(
            "recommendation",
            optimization.get("message", "No optimization recommendation available.")
        ),

        "next_step": (
            "Compare your current approach with "
            "the recommended approach and understand "
            "the time-space trade-off."
        ),

        "optimization_engine": {
            "is_optimal": optimization.get("is_optimal", False),
            "optimal_pattern": optimization.get("optimal_pattern", "Problem-dependent"),
            "optimal_time": optimization.get("optimal_time", "Unknown"),
            "optimal_space": optimization.get("optimal_space", "Unknown"),
            "improvement": optimization.get(
                "improvement",
                "No reliable generic optimization detected."
            )
        },
        "explanation_engine": {
            "why": explanation["why"],
            "better": explanation["better"],
            "tradeoff": explanation["tradeoff"],
            "learning_point": explanation["learning_point"]
        }
    }