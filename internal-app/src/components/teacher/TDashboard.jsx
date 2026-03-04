"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getAllStudents, getAnnouncements, getTeacherAssignments } from "@/lib/api";

export default function TDashboard({ user }) {
  const [students, setStudents] = useState([]);
  const [announcements, setAnnouncements] = useState([]);
  const [assignments, setAssignments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      getAllStudents().catch(() => ({ results: [] })),
      getAnnouncements().catch(() => ({ results: [] })),
      getTeacherAssignments().catch(() => ({ results: [] })),
    ]).then(([s, a, ta]) => {
      setStudents(Array.isArray(s) ? s : (s.results || []));
      setAnnouncements(Array.isArray(a) ? a : (a.results || []));
      setAssignments(Array.isArray(ta) ? ta : (ta.results || []));
      setLoading(false);
    });
  }, []);

  if (loading) return <Loading />;

  return (
    <>
      <TopBar title={"Welcome, " + user.first_name + "!"} subtitle="Teacher Dashboard" />
      <div className="stat-row">
        <div className="stat-box"><div className="stat-num">{assignments.length}</div><div className="stat-label">Assignments</div></div>
        <div className="stat-box"><div className="stat-num">{students.length}</div><div className="stat-label">Total Students</div></div>
      </div>
      <div className="dash-grid">
        <div className="card">
          <div className="card-title">My Assignments</div>
          {assignments.length === 0 ? <p style={{color:"#94a3b8",padding:12}}>No assignments found.</p> :
            assignments.slice(0, 8).map((a, i) => (
              <div key={i} className="list-row">
                <div><div className="list-primary">{a.subject_name || "Subject"}</div></div>
              </div>
            ))
          }
        </div>
        <div className="card">
          <div className="card-title">Announcements</div>
          {announcements.length === 0 ? <p style={{color:"#94a3b8",padding:12}}>No announcements.</p> :
            (Array.isArray(announcements) ? announcements : []).slice(0, 5).map((a, i) => (
              <div key={i} className="announce-item">
                <div className="announce-title">{a.title}</div>
                <div className="announce-msg">{a.content}</div>
              </div>
            ))
          }
        </div>
      </div>
    </>
  );
}
