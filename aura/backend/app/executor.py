import os
import shutil
import subprocess
import tempfile
from pathlib import Path


def normalize(value: str) -> str:
    return " ".join(value.strip().split())


def get_compiler_path() -> str:
    """Finds g++ compiler on Linux (Render/Docker) or Windows locally."""
    # 1. Standard system PATH (Linux / Render / Docker)
    system_gpp = shutil.which("g++")
    if system_gpp:
        return system_gpp

    # 2. Local Windows Fallbacks
    windows_paths = [
        r"C:\MinGW\bin\g++.exe",
        r"C:\msys64\mingw64\bin\g++.exe",
        r"C:\Program Files\mingw-w64\bin\g++.exe",
    ]
    for p in windows_paths:
        if os.path.exists(p):
            return p

    return "g++"


def run_cpp(code: str, test_cases: list, timeout_seconds: int = 2):
    results = []
    compiler = get_compiler_path()

    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "main.cpp"
        # On Linux/Render, binary is main; on Windows it is main.exe
        binary_name = "main.exe" if os.name == "nt" else "main"
        binary = Path(tmp) / binary_name

        src.write_text(code, encoding="utf-8")

        # Compile C++
        try:
            compile_result = subprocess.run(
                [
                    compiler,
                    "-std=c++17",
                    str(src),
                    "-O2",
                    "-o",
                    str(binary)
                ],
                capture_output=True,
                text=True,
                timeout=30
            )
        except subprocess.TimeoutExpired:
            return {
                "status": "compile_timeout",
                "passed": 0,
                "total": len(test_cases),
                "results": [],
                "error": "C++ compilation exceeded the limit."
            }

        if compile_result.returncode != 0:
            return {
                "status": "compile_error",
                "passed": 0,
                "total": len(test_cases),
                "results": [],
                "error": compile_result.stderr[-3000:]
            }

        # Run test cases
        for case in test_cases:
            try:
                run = subprocess.run(
                    [str(binary)],
                    input=case["input"],
                    capture_output=True,
                    text=True,
                    timeout=timeout_seconds
                )

                actual = normalize(run.stdout)
                expected = normalize(case["expected"])

                passed = (
                    run.returncode == 0
                    and actual == expected
                )

                results.append({
                    "passed": passed,
                    "input": case["input"],
                    "expected": expected,
                    "actual": actual,
                    "stderr": run.stderr[-1000:]
                })

            except subprocess.TimeoutExpired:
                results.append({
                    "passed": False,
                    "input": case["input"],
                    "expected": normalize(case["expected"]),
                    "actual": "",
                    "stderr": "Time limit exceeded"
                })

        passed = sum(r["passed"] for r in results)

        return {
            "status": "accepted" if passed == len(results) else "wrong_answer",
            "passed": passed,
            "total": len(results),
            "results": results
        }