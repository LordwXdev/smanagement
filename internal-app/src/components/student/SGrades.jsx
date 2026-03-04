"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getMyGrades } from "@/lib/api";
import { gradeColor, pctBar } from "@/lib/helpers";

export default function SGrades() {
  const [grades, setGrades] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getMyGrades().then((g) => { setGrades(Array.isArray(g) ? g : (g.results || [])); setLoading(false); }).catch(() => setLoading(false));
  }, []);

  if (loading) return <Loading />;

  return (
    <>
      <TopBar title="My Grades" subtitle={grades.length + " graded items"} />
      <div className="card">
        {grades.length === 0 ? <p style={{color:"#94a3b8",padding:20}}>No grades recorded yet.</p> : (
          <table className="data-table">
            <thead><tr><th>Assessment</th><th>Marks</th><th>Grade</th><th>%</th></tr></thead>
            <tbody>
              {grades.map((g, i) => (
                <tr key={i}>
                  <td className="td-bold">{g.student_name || "Exam"}</td>
                  <td className="mono-val">{g.marks_obtained}</td>
                  <td><span className={"badge " + gradeColor(g.letter_grade)}>{g.letter_grade}</span></td>
                  <td><div className="inline-bar"><div className="progress-bar" style={{flex:1}}><div className={"progress-fill " + pctBar(g.percentage)} style={{width:g.percentage+"%"}} /></div><span className="mono-val">{g.percentage}%</span></div></td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}
