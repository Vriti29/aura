
import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";
import RecommendationPanel from "./RecommendationPanel";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

function App() {
  const [problems, setProblems] = useState([]);
  const [selected, setSelected] = useState(null);
  const [code, setCode] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showLibrary, setShowLibrary] = useState(false);
  const [analyzeAnyCode, setAnalyzeAnyCode] = useState(false);
  const [problemStatement, setProblemStatement] = useState("");
  const [showProfile, setShowProfile] = useState(false);
  const [history, setHistory] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("aura_history")) || [];
    } catch {
      return [];
    }
  });
  const [learningProfile, setLearningProfile] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("aura_learning_profile")) || null;
    } catch {
      return null;
    }
  });

  useEffect(() => {
    fetch(`${API}/api/problems`)
      .then((r) => r.json())
      .then((data) => {
        setProblems(data);
        if (data[0]) {
          setSelected(data[0]);
          setCode(data[0].starter_code);
        }
      });
  }, []);

  useEffect(() => {
    refreshLearningHistory();
  }, []);

  useEffect(() => {
    function handleRecommendedProblem(event) {
      const problem = event.detail;
      if (!problem) return;

      setShowProfile(false);
      setAnalyzeAnyCode(false);
      setSelected(problem);
      setCode(problem.starter_code);
      setProblemStatement("");
      setResult(null);
    }

    window.addEventListener("aura-select-problem", handleRecommendedProblem);
    return () => {
      window.removeEventListener("aura-select-problem", handleRecommendedProblem);
    };
  }, []);

  function chooseProblem(problem) {
    setShowProfile(false);
    setAnalyzeAnyCode(false);
    setSelected(problem);
    setCode(problem.starter_code);
    setProblemStatement("");
    setResult(null);
  }

  function openAnalyzeAnyCode() {
    setAnalyzeAnyCode(true);
    setSelected(null);
    setCode("");
    setResult(null);
  }

  async function refreshLearningHistory() {
    try {
      const response = await fetch(`${API}/api/history`);
      if (!response.ok) throw new Error("Failed to fetch learning history");
      const data = await response.json();

      const backendHistory = (data.history || []).map((item) => ({
        id: `${item.problem_id}-${item.timestamp}`,
        problemId: item.problem_id,
        problemTitle: item.problem_title,
        pattern: item.pattern || "Unknown",
        complexity: item.complexity || "Unknown",
        spaceComplexity: item.space_complexity || "Unknown",
        correctness: item.correctness_score || 0,
        optimalPattern: item.optimal_pattern || "Unknown",
        isOptimal: item.is_optimal,
        timestamp: item.timestamp,
      }));

      setHistory(backendHistory);
      setLearningProfile(data.profile);

      localStorage.setItem("aura_history", JSON.stringify(backendHistory));
      localStorage.setItem("aura_learning_profile", JSON.stringify(data.profile));
    } catch (error) {
      console.error("Could not refresh AURA learning history:", error);
    }
  }

  async function analyze() {
    setLoading(true);
    setResult(null);

    try {
      let response;
      if (analyzeAnyCode) {
        response = await fetch(`${API}/api/analyze-code`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            code: code,
            problem_statement: problemStatement,
          }),
        });
      } else {
        response = await fetch(`${API}/api/analyze`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            problem_id: selected.id,
            code: code,
          }),
        });
      }

      const data = await response.json();
      setResult(data);

      if (data.learning_profile) {
        setLearningProfile(data.learning_profile);
      }
      if (data.analysis) {
        await refreshLearningHistory();
      }
    } catch (error) {
      setResult({ error: "Could not connect to AURA backend." });
    }

    setLoading(false);
  }

  const problemProgress = learningProfile?.problem_progress || {};

  return (
    <div className="app">
      {/* SIDEBAR */}
      <aside className="sidebar">
        <div className="brand">AURA<span>.</span></div>
        <div className="tagline">Code intelligence for DSA.</div>

        <button className="library-button" onClick={() => setShowLibrary(true)}>
          Problem Library
        </button>
        <button className="library-button analyze-any-button" onClick={openAnalyzeAnyCode}>
          Analyze Any Code
        </button>
        <button
          className="library-button"
          onClick={() => {
            setShowProfile(true);
            setShowLibrary(false);
            setAnalyzeAnyCode(false);
            setResult(null);
          }}
        >
          AURA Profile
        </button>

        <div className="section-title">PROBLEMS</div>

        {problems.map((p) => {
          const progress = problemProgress[p.id];
          const isOptimal = progress?.is_optimal;
          const isSolved = progress?.solved;

          return (
            <button
              key={p.id}
              className={`problem ${selected?.id === p.id ? "active" : ""}`}
              onClick={() => chooseProblem(p)}
            >
              <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
                <span>{p.title}</span>
                {isOptimal && (
                  <span style={{ color: "#72e0a0", fontSize: "11px" }}>✓</span>
                )}
                {!isOptimal && isSolved && (
                  <span style={{ color: "#ffd28b", fontSize: "11px" }}>▲</span>
                )}
              </div>
              <small>{p.difficulty}</small>
            </button>
          );
        })}
      </aside>

      {/* PROBLEM LIBRARY */}
      {showLibrary && (
        <div className="library-overlay" onClick={() => setShowLibrary(false)}>
          <div className="library-modal" onClick={(e) => e.stopPropagation()}>
            <div className="library-header">
              <div>
                <div className="eyebrow">AURA LIBRARY</div>
                <h2>Problem Library</h2>
                <p>Select a DSA problem to practice, analyze, and master.</p>
              </div>

              <button className="library-close" onClick={() => setShowLibrary(false)}>
                ✕
              </button>
            </div>

            <div className="library-grid">
              {problems.map((p) => {
                const progress = problemProgress[p.id];
                const isOptimal = progress?.is_optimal;
                const isSolved = progress?.solved;

                return (
                  <button
                    key={p.id}
                    className="library-card"
                    onClick={() => {
                      chooseProblem(p);
                      setShowLibrary(false);
                    }}
                  >
                    <div className="library-card-top">
                      <strong>{p.title}</strong>
                      <div style={{ display: "flex", gap: "8px", alignItems: "center" }}>
                        {isOptimal && (
                          <span style={{ color: "#72e0a0", fontSize: "11px", fontWeight: "700" }}>
                            MASTERED
                          </span>
                        )}
                        {!isOptimal && isSolved && (
                          <span style={{ color: "#ffd28b", fontSize: "11px", fontWeight: "700" }}>
                            OPTIMIZATION AVAILABLE
                          </span>
                        )}
                        <small>{p.difficulty}</small>
                      </div>
                    </div>

                    <span>{p.topic}</span>
                    <p>{p.description}</p>
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* MAIN CONTENT */}
      <main className="main">
        {showProfile ? (
          <Profile
            history={history}
            learningProfile={learningProfile}
            problems={problems}
          />
        ) : (
          <>
            <header>
              <div>
                <div className="eyebrow">CODE INTELLIGENCE</div>
                <h1>{analyzeAnyCode ? "Analyze Any Code" : selected?.title || "Loading..."}</h1>
                <p>
                  {analyzeAnyCode
                    ? "Paste any C++ DSA solution and let AURA analyze its complexity, pattern, and optimization."
                    : selected?.description}
                </p>
              </div>

              <div className="topic">
                {analyzeAnyCode ? "DSA Code Analysis" : selected?.topic}
              </div>
            </header>

            <section className="workspace">
              {analyzeAnyCode && (
                <div className="problem-input">
                  <label>Problem Statement</label>
                  <textarea
                    placeholder="Paste the DSA problem statement here..."
                    value={problemStatement}
                    onChange={(e) => setProblemStatement(e.target.value)}
                  />
                </div>
              )}

              {/* CODE EDITOR */}
              <div className="editor-card">
                <div className="card-header">
                  <span>{analyzeAnyCode ? "your-code.cpp" : "solution.cpp"}</span>
                  <button
                    onClick={analyze}
                    disabled={(!selected && !analyzeAnyCode) || loading}
                  >
                    {loading ? "Analyzing..." : "Analyze Code →"}
                  </button>
                </div>

                <textarea
                  value={code}
                  onChange={(e) => setCode(e.target.value)}
                  spellCheck="false"
                />
              </div>

              {/* ANALYSIS */}
              <div className="analysis-card">
                <div className="card-header">
                  <span>AURA ANALYSIS</span>
                </div>

                {!result && (
                  <div className="empty">
                    {analyzeAnyCode
                      ? "Paste any C++ code and analyze its complexity, pattern, and optimization."
                      : "Submit your code to receive correctness, complexity, and pattern analysis."}
                  </div>
                )}

                {result?.error && <pre className="error">{result.error}</pre>}

                {result?.analysis && (
                  <div className="metrics">
                    <Metric
                      label="Correctness"
                      value={
                        result.execution
                          ? `${result.execution.passed}/${result.execution.total} tests passed`
                          : "Not evaluated"
                      }
                    />

                    {result.execution?.results && (
                      <div className="test-results">
                        <div className="test-results-title">TEST RESULTS</div>
                        {result.execution.results.map((test, index) => (
                          <div
                            key={index}
                            className={`test-result ${test.passed ? "passed" : "failed"}`}
                          >
                            <div className="test-result-header">
                              <strong>
                                {test.passed ? "✓" : "✗"} Test {index + 1}
                              </strong>
                            </div>
                            <div className="test-detail">
                              <span>Expected:</span>
                              <code>{test.expected}</code>
                            </div>
                            <div className="test-detail">
                              <span>Actual:</span>
                              <code>{test.actual || "(no output)"}</code>
                            </div>
                            {test.stderr && (
                              <div className="test-detail">
                                <span>Error:</span>
                                <code>{test.stderr}</code>
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    )}

                    <Metric label="Time Complexity" value={result.analysis.complexity} />
                    <Metric label="Space Complexity" value={result.analysis.space_complexity} />
                    <Metric label="Pattern" value={result.analysis.pattern} />
                    <Metric label="Code Quality" value={result.analysis.code_quality} />

                    {/* APPROACH */}
                    <div className="approach-card">
                      <div className="approach-title">YOUR APPROACH</div>
                      <p>
                        {result.analysis.explanation_engine?.why ||
                          `AURA detected a ${result.analysis.pattern} approach.`}
                      </p>
                      <div className="approach-complexity">
                        <span>Time: <strong>{result.analysis.complexity}</strong></span>
                        <span>Space: <strong>{result.analysis.space_complexity}</strong></span>
                      </div>
                    </div>

                    {/* OPTIMIZATION ENGINE */}
                    {result.analysis?.optimization_engine && (
                      <div className="optimization-engine">
                        <div className="optimization-title">OPTIMIZATION ENGINE</div>
                        <div className="optimization-grid">
                          <div className="optimization-item">
                            <span>Current Approach</span>
                            <strong>{result.analysis.pattern}</strong>
                          </div>
                          <div className="optimization-item">
                            <span>Recommended Approach</span>
                            <strong>
                              {result.analysis.optimization_engine.optimal_pattern}
                            </strong>
                          </div>
                          <div className="optimization-item">
                            <span>Current Complexity</span>
                            <strong>{result.analysis.complexity}</strong>
                          </div>
                          <div className="optimization-item">
                            <span>Optimal Time</span>
                            <strong>
                              {result.analysis.optimization_engine.optimal_time}
                            </strong>
                          </div>
                        </div>

                        <div className="optimization-message">
                          {result.analysis.optimization}
                        </div>
                      </div>
                    )}

                    {/* EXPLANATION */}
                    {result.analysis?.explanation_engine && (
                      <div className="explanation-engine">
                        <div className="explanation-title">WHY THIS APPROACH?</div>
                        <div className="explanation-section">
                          <div className="explanation-label">Mechanism & Details</div>
                          <p>{result.analysis.explanation_engine.better}</p>
                        </div>
                        <div className="explanation-section">
                          <div className="explanation-label">Time-Space Trade-off</div>
                          <p>{result.analysis.explanation_engine.tradeoff}</p>
                        </div>
                        <div className="learning-point">
                          <strong>DSA Takeaway:</strong>{" "}
                          {result.analysis.explanation_engine.learning_point}
                        </div>
                      </div>
                    )}

                    {/* COACH HINTS */}
                    {result.analysis?.coach?.hints?.length > 0 && (
                      <div className="coach-engine">
                        <div className="coach-title">🧠 AURA COACH</div>
                        <div className="coach-subtitle">
                          Guided hints to help you improve your solution
                        </div>
                        <div className="coach-hints">
                          {result.analysis.coach.hints.map((hint, index) => (
                            <div className="coach-hint" key={index}>
                              <span className="coach-number">{index + 1}</span>
                              <span>{hint}</span>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                )}

                {result?.execution?.error && (
                  <pre className="error">{result.execution.error}</pre>
                )}
              </div>
            </section>
          </>
        )}
      </main>
    </div>
  );
}

function Metric({ label, value }) {
  return (
    <div className="metric">
      <div className="metric-label">{label}</div>
      <div className="metric-value">{value}</div>
    </div>
  );
}

function Profile({ history, learningProfile, problems }) {
  const total = learningProfile?.problems_attempted ?? 0;
  const solved = learningProfile?.problems_solved ?? 0;
  const successRate = learningProfile?.success_rate ?? 0;
  const totalSubmissions = learningProfile?.total_submissions ?? history.length;
  const patternCount = learningProfile?.pattern_usage || {};
  const strongestPattern = learningProfile?.strongest_pattern || "No data yet";
  const optimizationOpportunities = learningProfile?.optimization_opportunities || {};

  const topWeakness =
    Object.entries(optimizationOpportunities).sort((a, b) => b[1] - a[1])[0]?.[0] || null;
  const inefficientAttempts = Object.values(optimizationOpportunities).reduce(
    (sum, count) => sum + count,
    0
  );

  const skillAreas = {
    Arrays: {
      patterns: [
        "Linear Scan / Traversal",
        "Brute Force / Pair Search",
        "Two Pointer",
        "Sliding Window",
        "Prefix / Cumulative",
      ],
      score: 0,
      attempts: 0,
      status: "Not started",
    },
    Hashing: {
      patterns: ["Hashing / Lookup"],
      score: 0,
      attempts: 0,
      status: "Not started",
    },
    "Binary Search": {
      patterns: ["Binary Search"],
      score: 0,
      attempts: 0,
      status: "Not started",
    },
    DP: {
      patterns: ["Dynamic Programming", "DP", "Recursion"],
      score: 0,
      attempts: 0,
      status: "Not started",
    },
    Graphs: {
      patterns: [
        "Graph Traversal",
        "BFS / DFS",
        "BFS / Graph Traversal",
        "DFS / Graph Traversal",
        "Graphs",
      ],
      score: 0,
      attempts: 0,
      status: "Not started",
    },
  };

  Object.entries(skillAreas).forEach(([area, data]) => {
    const related = history.filter(
      (item) => data.patterns.includes(item.pattern) || item.topic === area
    );

    data.attempts = related.length;
    if (related.length === 0) {
      data.score = 0;
      data.status = "Not started";
      return;
    }

    const optimalCount = related.filter((item) => item.isOptimal === true).length;
    data.score = Math.round((optimalCount / related.length) * 100);

    if (data.score >= 80) data.status = "Strong";
    else if (data.score >= 60) data.status = "Developing";
    else data.status = "Needs Practice";
  });

  const startedSkills = Object.entries(skillAreas).filter(([, data]) => data.attempts > 0);
  const weakAreas = startedSkills
    .filter(([, data]) => data.score < 60)
    .sort((a, b) => a[1].score - b[1].score);
  const strongAreas = startedSkills
    .filter(([, data]) => data.score >= 80)
    .sort((a, b) => b[1].score - a[1].score);

  return (
    <div className="profile-page">
      <div className="eyebrow">AURA LEARNING PROFILE</div>
      <h1>Your DSA Progress</h1>
      <p>AURA tracks your problem-solving patterns and identifies areas that need practice.</p>

      <div className="profile-grid">
        <div className="profile-card">
          <span>Problems Attempted</span>
          <strong>{total}</strong>
        </div>
        <div className="profile-card">
          <span>Problems Solved</span>
          <strong>{solved}</strong>
        </div>
        <div className="profile-card">
          <span>Success Rate</span>
          <strong>{successRate}%</strong>
        </div>
        <div className="profile-card">
          <span>Strongest Pattern</span>
          <strong>{strongestPattern}</strong>
        </div>
        <div className="profile-card">
          <span>Total Submissions</span>
          <strong>{totalSubmissions}</strong>
        </div>
      </div>

      {topWeakness && (
        <div className="weakness-card">
          <div className="weakness-label">🧠 AURA INSIGHT</div>
          <h2>Focus Area: {topWeakness}</h2>
          <p>AURA detected that your previous solutions could be improved using this pattern.</p>
          <div className="weakness-stat">
            <strong>{inefficientAttempts}</strong>
            <span>optimization opportunities detected</span>
          </div>
        </div>
      )}

      {/* DASHBOARD */}
      <div className="profile-section dashboard-section">
        <div className="eyebrow">AURA LEARNING DASHBOARD</div>
        <h2>Your Skill Areas</h2>
        <p className="dashboard-description">
          AURA estimates your strength from the approaches you've used and how often you reached an optimal solution.
        </p>

        <div className="skill-dashboard">
          {Object.entries(skillAreas).map(([area, data]) => {
            const started = data.attempts > 0;
            return (
              <div className="skill-row" key={area}>
                <div className="skill-header">
                  <span>{area}</span>
                  <strong>{started ? `${data.score}%` : "Not started"}</strong>
                </div>

                {started ? (
                  <>
                    <div className="skill-bar">
                      <div
                        className="skill-bar-fill"
                        style={{ width: `${data.score}%` }}
                      />
                    </div>
                    <div className="skill-meta">
                      <span>{data.attempts} attempt{data.attempts !== 1 ? "s" : ""}</span>
                      <span>{data.status}</span>
                    </div>
                  </>
                ) : (
                  <div className="skill-not-started">No attempts yet</div>
                )}
              </div>
            );
          })}
        </div>

        {startedSkills.length > 0 && (
          <div className="learning-insight">
            <div className="eyebrow">AURA INSIGHT</div>
            {weakAreas.length > 0 ? (
              <>
                <h3>Areas That Need Practice</h3>
                <p>AURA found that some skill areas have fewer optimal solutions than others.</p>
                <div className="weak-area-list">
                  {weakAreas.slice(0, 3).map(([area, data]) => (
                    <div className="weak-area-item" key={area}>
                      <div>
                        <strong>{area}</strong>
                        <small>{data.attempts} attempt{data.attempts !== 1 ? "s" : ""}</small>
                      </div>
                      <strong>{data.score}%</strong>
                    </div>
                  ))}
                </div>
              </>
            ) : (
              <>
                <h3>Strong Performance</h3>
                <p>AURA currently sees no major weak skill area among the topics you've practiced.</p>
              </>
            )}
          </div>
        )}

        {strongAreas.length > 0 && (
          <div className="learning-strength">
            <div className="eyebrow">YOUR STRENGTHS</div>
            <div className="strength-list">
              {strongAreas.slice(0, 3).map(([area, data]) => (
                <div className="strength-item" key={area}>
                  <span>{area}</span>
                  <strong>{data.score}%</strong>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      <RecommendationPanel
        problems={problems}
        history={history}
        onSelectProblem={(problem) => {
          window.dispatchEvent(
            new CustomEvent("aura-select-problem", { detail: problem })
          );
        }}
      />

      <div className="profile-section">
        <h2>Pattern Usage</h2>
        {Object.entries(patternCount).length === 0 ? (
          <p>Solve some problems to build your profile.</p>
        ) : (
          Object.entries(patternCount).map(([pattern, count]) => (
            <div className="pattern-row" key={pattern}>
              <span>{pattern}</span>
              <strong>{count}</strong>
            </div>
          ))
        )}
      </div>

      <div className="profile-section">
        <div className="section-heading-row">
          <div>
            <div className="eyebrow">LEARNING HISTORY</div>
            <h2>My Analyses</h2>
          </div>
          <span className="history-count">{history.length} submissions</span>
        </div>

        {history.length === 0 ? (
          <p>No analyses yet. Solve a problem to start building your history.</p>
        ) : (
          <div className="analysis-history">
            {history.slice(0, 10).map((item) => {
              const solved = item.correctness === 100;
              const hasOptimization =
                item.isOptimal === false &&
                item.optimalPattern &&
                item.optimalPattern !== "Unknown";

              return (
                <div className="analysis-history-card" key={item.id}>
                  <div className="analysis-history-header">
                    <div>
                      <strong className="analysis-problem-title">
                        {item.problemTitle}
                      </strong>
                      <small>{new Date(item.timestamp).toLocaleString()}</small>
                    </div>

                    <span
                      className={`analysis-status ${
                        solved ? "status-solved" : "status-failed"
                      }`}
                    >
                      {solved ? "✓ Solved" : "✗ Needs Work"}
                    </span>
                  </div>

                  <div className="analysis-details">
                    <div className="analysis-detail">
                      <span>Approach</span>
                      <strong>{item.pattern}</strong>
                    </div>
                    <div className="analysis-detail">
                      <span>Time</span>
                      <strong>{item.complexity}</strong>
                    </div>
                    <div className="analysis-detail">
                      <span>Space</span>
                      <strong>{item.spaceComplexity}</strong>
                    </div>
                    <div className="analysis-detail">
                      <span>Correctness</span>
                      <strong>{item.correctness}%</strong>
                    </div>
                  </div>

                  {hasOptimization ? (
                    <div className="analysis-optimization">
                      <div className="optimization-history-label">
                        OPTIMIZATION AVAILABLE
                      </div>
                      <div className="optimization-history-flow">
                        <div>
                          <span>Your Approach</span>
                          <strong>{item.pattern}</strong>
                          <small>{item.complexity}</small>
                        </div>
                        <div className="optimization-history-arrow">→</div>
                        <div>
                          <span>Recommended</span>
                          <strong>{item.optimalPattern}</strong>
                          <small>{item.optimalTime}</small>
                        </div>
                      </div>
                    </div>
                  ) : (
                    <div className="analysis-optimal">
                      ✓ Optimal approach detected
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

createRoot(document.getElementById("root")).render(<App />);