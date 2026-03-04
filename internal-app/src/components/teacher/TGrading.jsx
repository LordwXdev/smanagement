"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getStudentGrades } from "@/lib/api";
import { gradeColor } from "@/lib/helpers";

export default function TGrading() {
  const [grades, setGrades] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getStudentGrades({}).then((d) => { setGrades(Array.isArray(d) ? d : (d.results || [])); setLoading(false); }).catch(() => setLoading(false));
  }, []);

  if (loading) return <Loading />;

  return (
    <>
      <TopBar title="Grading" subtitle="View and manage student grades" />
      <div className="card">
        {grades.length === 0 ? <p style={{color:"#94a3b8",padding:20}}>No grades found.</p> : (
          <table className="data-table">
            <thead><tr><th>Student</th><th>Marks</th><th>Grade</th><th>%</th></tr></thead>
            <tbody>
              {grades.slice(0, 25).map((g, i) => (
                <tr key={i}>
                  <td className="td-bold">{g.student_name}</td>
                  <td className="mono-val">{g.marks_obtained}</td>
                  <td><span className={"badge " + gradeColor(g.letter_grade)}>{g.letter_grade}</span></td>
                  <td className="mono-val">{g.percentage}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}
