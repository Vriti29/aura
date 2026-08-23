PROBLEMS = {

    # ============================================================
    # 1. TWO SUM
    # ============================================================

    "two-sum": {
        "id": "two-sum",
        "title": "Two Sum",
        "difficulty": "Easy",
        "topic": "Arrays / Hashing",
        "description": "Given an array of integers and a target, return indices of two numbers whose sum equals the target.",
        "input_format": "n, followed by n integers, followed by target",
        "output_format": "two indices separated by a space",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "4\n2 7 11 15\n9\n", "expected": "0 1"},
            {"input": "3\n3 2 4\n6\n", "expected": "1 2"},
            {"input": "2\n3 3\n6\n", "expected": "0 1"}
        ]
    },

    # ============================================================
    # 2. MAXIMUM ELEMENT
    # ============================================================

    "max-element": {
        "id": "max-element",
        "title": "Find Maximum Element",
        "difficulty": "Easy",
        "topic": "Arrays",
        "description": "Given an array of integers, print its maximum element.",
        "input_format": "n followed by n integers",
        "output_format": "maximum value",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "5\n1 8 3 7 2\n", "expected": "8"},
            {"input": "1\n-4\n", "expected": "-4"},
            {"input": "4\n-8 -2 -10 -3\n", "expected": "-2"}
        ]
    },

    # ============================================================
    # 3. BINARY SEARCH
    # ============================================================

    "binary-search": {
        "id": "binary-search",
        "title": "Binary Search",
        "difficulty": "Easy",
        "topic": "Binary Search",
        "description": "Given a sorted array and a target value, find the index of the target using binary search. Return -1 if the target is not present.",
        "input_format": "n followed by n sorted integers, followed by target",
        "output_format": "index of target or -1",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {
                "input": "5\n1 3 5 7 9\n5\n",
                "expected": "2"
            },
            {
                "input": "6\n2 4 6 8 10 12\n10\n",
                "expected": "4"
            },
            {
                "input": "4\n1 3 5 7\n4\n",
                "expected": "-1"
            }
        ]
    },

    # ============================================================
    # 4. BEST TIME TO BUY AND SELL STOCK
    # ============================================================

    "best-time-stock": {
        "id": "best-time-stock",
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy",
        "topic": "Arrays",
        "description": "Given an array of stock prices, find the maximum profit possible by buying on one day and selling on a later day.",
        "input_format": "n followed by n stock prices",
        "output_format": "maximum profit",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "6\n7 1 5 3 6 4\n", "expected": "5"},
            {"input": "5\n7 6 4 3 1\n", "expected": "0"},
            {"input": "5\n2 4 1 7 5\n", "expected": "6"}
        ]
    },

    # ============================================================
    # 5. MAXIMUM SUBARRAY
    # ============================================================

    "maximum-subarray": {
        "id": "maximum-subarray",
        "title": "Maximum Subarray",
        "difficulty": "Medium",
        "topic": "Arrays / Dynamic Programming",
        "description": "Given an integer array, find the contiguous subarray with the largest sum and return its sum.",
        "input_format": "n followed by n integers",
        "output_format": "maximum subarray sum",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "9\n-2 1 -3 4 -1 2 1 -5 4\n", "expected": "6"},
            {"input": "5\n1 2 3 4 5\n", "expected": "15"},
            {"input": "3\n-5 -2 -8\n", "expected": "-2"}
        ]
    },

    # ============================================================
    # 6. VALID ANAGRAM
    # ============================================================

    "valid-anagram": {
        "id": "valid-anagram",
        "title": "Valid Anagram",
        "difficulty": "Easy",
        "topic": "Strings / Hashing",
        "description": "Given two strings, determine whether the second string is an anagram of the first string.",
        "input_format": "two strings",
        "output_format": "true or false",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "anagram\nnagaram\n", "expected": "true"},
            {"input": "rat\ncar\n", "expected": "false"},
            {"input": "listen\nsilent\n", "expected": "true"}
        ]
    },

    # ============================================================
    # 7. CONTAINS DUPLICATE
    # ============================================================

    "contains-duplicate": {
        "id": "contains-duplicate",
        "title": "Contains Duplicate",
        "difficulty": "Easy",
        "topic": "Arrays / Hashing",
        "description": "Given an integer array, determine whether any value appears at least twice.",
        "input_format": "n followed by n integers",
        "output_format": "true or false",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "4\n1 2 3 1\n", "expected": "true"},
            {"input": "4\n1 2 3 4\n", "expected": "false"},
            {"input": "5\n1 1 2 3 4\n", "expected": "true"}
        ]
    },

    # ============================================================
    # 8. MOVE ZEROES
    # ============================================================

    "move-zeroes": {
        "id": "move-zeroes",
        "title": "Move Zeroes",
        "difficulty": "Easy",
        "topic": "Arrays / Two Pointer",
        "description": "Move all zeroes in an array to the end while maintaining the relative order of the non-zero elements.",
        "input_format": "n followed by n integers",
        "output_format": "array after moving zeroes to the end",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "5\n0 1 0 3 12\n", "expected": "1 3 12 0 0"},
            {"input": "4\n0 0 1 2\n", "expected": "1 2 0 0"},
            {"input": "5\n1 2 3 4 5\n", "expected": "1 2 3 4 5"}
        ]
    },

    # ============================================================
    # 9. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
    # ============================================================

    "longest-substring": {
        "id": "longest-substring",
        "title": "Longest Substring Without Repeating",
        "difficulty": "Medium",
        "topic": "Strings / Sliding Window",
        "description": "Given a string, find the length of the longest substring without repeating characters.",
        "input_format": "a single string",
        "output_format": "length of longest substring",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "abcabcbb\n", "expected": "3"},
            {"input": "bbbbb\n", "expected": "1"},
            {"input": "pwwkew\n", "expected": "3"}
        ]
    },

    # ============================================================
    # 10. SUBARRAY SUM EQUALS K
    # ============================================================

    "subarray-sum-k": {
        "id": "subarray-sum-k",
        "title": "Subarray Sum Equals K",
        "difficulty": "Medium",
        "topic": "Arrays / Prefix Sum",
        "description": "Given an integer array and an integer k, find the total number of continuous subarrays whose sum equals k.",
        "input_format": "n followed by n integers, followed by k",
        "output_format": "number of subarrays",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {"input": "3\n1 1 1\n2\n", "expected": "2"},
            {"input": "3\n1 2 3\n3\n", "expected": "2"},
            {"input": "3\n1 -1 0\n0\n", "expected": "3"}
        ]
    },

    # ============================================================
    # 11. MERGE INTERVALS
    # ============================================================

    "merge-intervals": {
        "id": "merge-intervals",
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "topic": "Arrays / Sorting",
        "description": "Given a collection of intervals, merge all overlapping intervals.",
        "input_format": "n followed by n pairs representing intervals",
        "output_format": "merged intervals, one per line",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {
                "input": "4\n1 3\n2 6\n8 10\n15 18\n",
                "expected": "1 6\n8 10\n15 18"
            },
            {
                "input": "2\n1 4\n4 5\n",
                "expected": "1 5"
            },
            {
                "input": "3\n1 2\n3 4\n5 6\n",
                "expected": "1 2\n3 4\n5 6"
            }
        ]
    },

    # ============================================================
    # 12. NUMBER OF ISLANDS
    # ============================================================

    "number-of-islands": {
        "id": "number-of-islands",
        "title": "Number of Islands",
        "difficulty": "Medium",
        "topic": "Graphs / DFS",
        "description": "Given a grid containing land and water, count the number of connected islands. Cells connected horizontally or vertically belong to the same island.",
        "input_format": "rows and columns followed by the grid",
        "output_format": "number of islands",
        "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    // Write your solution here\n    return 0;\n}",
        "test_cases": [
            {
                "input": "4 5\n11000\n11000\n00100\n00011\n",
                "expected": "3"
            },
            {
                "input": "3 3\n111\n010\n111\n",
                "expected": "1"
            },
            {
                "input": "3 3\n000\n000\n000\n",
                "expected": "0"
            }
        ]
    }

}