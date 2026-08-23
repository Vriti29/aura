import React, { useEffect, useState } from "react";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

function RecommendationPanel({ problems, history, onSelectProblem }) {
  const [recommendationData, setRecommendationData] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchRecommendations = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API}/api/recommendations`);
      if (!response.ok) {
        throw new Error("Failed to fetch recommendations");
      }
      const data = await response.json();
      setRecommendationData(data);
    } catch (error) {
      console.error("Recommendation fetch error:", error);
      setRecommendationData(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRecommendations();
  }, [history]);

  if (!problems || problems.length === 0) {
    return null;
  }

  if (loading && !recommendationData) {
    return (
      <div
        className="profile-section"
        style={{
          marginTop: "24px",
          border: "1px solid #252b38",
          borderRadius: "16px",
          padding: "24px",
          background: "linear-gradient(145deg, #11151d, #0c0f15)",
        }}
      >
        <div
          style={{
            fontSize: "11px",
            letterSpacing: "2px",
            fontWeight: "700",
            color: "#7887a0",
            marginBottom: "8px",
          }}
        >
          AURA RECOMMENDATION ENGINE
        </div>
        <h2 style={{ margin: 0 }}>What should you solve next?</h2>
        <p style={{ color: "#8995aa", marginTop: "8px" }}>
          AURA is analyzing your solving history...
        </p>
      </div>
    );
  }

  const recommendations = recommendationData?.recommendations || [];
  const weakArea = recommendationData?.weak_area || null;
  const explanation =
    recommendationData?.explanation ||
    "Recommendations are based on your solving history.";

  if (recommendations.length === 0) {
    return (
      <div
        className="profile-section"
        style={{
          marginTop: "24px",
          border: "1px solid #252b38",
          borderRadius: "16px",
          padding: "24px",
          background: "linear-gradient(145deg, #11151d, #0c0f15)",
        }}
      >
        <div
          style={{
            fontSize: "11px",
            letterSpacing: "2px",
            fontWeight: "700",
            color: "#7887a0",
            marginBottom: "8px",
          }}
        >
          AURA RECOMMENDATION ENGINE
        </div>
        <h2 style={{ margin: 0 }}>What should you solve next?</h2>
        <p style={{ color: "#8995aa", marginTop: "8px" }}>
          Solve a few problems and AURA will personalize your recommendations.
        </p>
      </div>
    );
  }

  const getProblemObject = (recommendation) => {
    return (
      problems.find((problem) => problem.id === recommendation.id) ||
      recommendation
    );
  };

  return (
    <div
      className="profile-section"
      style={{
        marginTop: "24px",
        border: "1px solid #252b38",
        borderRadius: "16px",
        padding: "24px",
        background: "linear-gradient(145deg, #11151d, #0c0f15)",
      }}
    >
      {/* HEADER */}
      <div
        style={{
          fontSize: "11px",
          letterSpacing: "2px",
          fontWeight: "700",
          color: "#7887a0",
          marginBottom: "8px",
        }}
      >
        AURA RECOMMENDATION ENGINE
      </div>

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "flex-start",
          gap: "20px",
          marginBottom: "8px",
        }}
      >
        <div>
          <h2 style={{ margin: 0 }}>What should you solve next?</h2>
          <p
            style={{
              marginTop: "8px",
              color: "#8995aa",
              lineHeight: "1.6",
              maxWidth: "720px",
            }}
          >
            {explanation}
          </p>
        </div>

        {weakArea && (
          <div
            style={{
              border: "1px solid #303848",
              borderRadius: "10px",
              padding: "9px 12px",
              fontSize: "12px",
              color: "#aab5c8",
              whiteSpace: "nowrap",
            }}
          >
            Focus Area: <strong style={{ color: "#ffffff" }}>{weakArea}</strong>
          </div>
        )}
      </div>

      {/* RECOMMENDATION CARDS */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
          gap: "14px",
          marginTop: "22px",
        }}
      >
        {recommendations.map((recommendation, index) => {
          const problem = getProblemObject(recommendation);

          return (
            <button
              key={recommendation.id}
              onClick={() => onSelectProblem(problem)}
              style={{
                textAlign: "left",
                cursor: "pointer",
                border: "1px solid #252b38",
                borderRadius: "14px",
                padding: "18px",
                background: "#0d1118",
                color: "#ffffff",
                transition: "transform 0.15s ease, border-color 0.15s ease",
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = "translateY(-2px)";
                e.currentTarget.style.borderColor = "#4c596f";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = "translateY(0)";
                e.currentTarget.style.borderColor = "#252b38";
              }}
            >
              {/* CARD HEADER */}
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  marginBottom: "14px",
                }}
              >
                <span
                  style={{
                    fontSize: "10px",
                    letterSpacing: "1.5px",
                    fontWeight: "700",
                    color: index === 0 ? "#7c8cff" : "#77839a",
                  }}
                >
                  {index === 0 ? "★ TOP RECOMMENDATION" : "NEXT PRACTICE"}
                </span>

                <span
                  style={{
                    fontSize: "11px",
                    color: "#7e8ba1",
                    background: "#181d28",
                    padding: "3px 8px",
                    borderRadius: "6px",
                  }}
                >
                  {problem.difficulty}
                </span>
              </div>

              {/* TITLE */}
              <h3
                style={{
                  margin: "0 0 8px 0",
                  fontSize: "17px",
                }}
              >
                {problem.title}
              </h3>

              {/* TOPIC */}
              <div
                style={{
                  fontSize: "11px",
                  color: "#718097",
                  marginBottom: "12px",
                }}
              >
                {problem.topic}
              </div>

              {/* REASON */}
              <p
                style={{
                  margin: 0,
                  color: "#9aa6b8",
                  fontSize: "13px",
                  lineHeight: "1.5",
                  minHeight: "38px",
                }}
              >
                {recommendation.reason ||
                  "A problem recommended to develop your DSA pattern foundation."}
              </p>

              {/* ACTION */}
              <div
                style={{
                  marginTop: "16px",
                  fontSize: "12px",
                  color: "#7c8cff",
                  fontWeight: "600",
                }}
              >
                Practice this →
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
}

export default RecommendationPanel;