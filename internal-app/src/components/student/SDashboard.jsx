"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getMyGrades, getAnnouncements } from "@/lib/api";
import { gradeColor } from "@/lib/helpers";

export default function SDashboard({ user, profile }) {
  const [grades, setGrades] = useState([]);
  const [announcements, setAnnouncements] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      getMyGrades().catch(() => []),
      getAnnouncements().catch(() => ({ results: [] })),
    ]).then(([g, a]) => {
      setGrades(Array.isArray(g) ? g : (g.results || []));
      setAnnouncements(Array.isArray(a) ? a : (a.results || []));
      setLoading(false);
    });
  }, []);

  if (loading) return <Loading />;

  const name = user.first_name || "Student";

  return (
    <>
      <TopBar title={"Welcome back, " + name + "!"} subtitle={profile ? "Admission: " + profile.admission_number : ""} />
      <div className="stat-row">
        <div className="stat-box"><div className="stat-num">{grades.length}</div><div className="stat-label">Graded Items</div></div>
        <div className="stat-box"><div className="stat-num">{profile ? profile.admission_number : "-"}</div><div className="stat-label">Admission #</div></div>
      </div>
      <div className="dash-grid">
        <div className="card">
          <div className="card-title">Recent Grades</div>
          {grades.length === 0 && <p style={{color:"#94a3b8",padding:12}}>No grades yet.</p>}
          {grades.slice(0, 8).map((g, i) => (
            <div key={i} className="list-row">
              <div>
                <div className="list-primary">{g.student_name || "You"}</div>
                <div className="list-secondary">Marks: {g.marks_obtained} | {g.letter_grade}</div>
              </div>
              <span className={"badge " + gradeColor(g.letter_grade)}>{g.letter_grade} ({g.percentage}%)</span>
            </div>
          ))}
        </div>
        <div className="card">
          <div className="card-title">Announcements</div>
          {announcements.length === 0 && <p style={{color:"#94a3b8",padding:12}}>No announcements.</p>}
          {(Array.isArray(announcements) ? announcements : []).slice(0, 5).map((a, i) => (
            <div key={i} className="announce-item">
              <div className="announce-title">{a.title}</div>
              <div className="announce-msg">{a.content}</div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
