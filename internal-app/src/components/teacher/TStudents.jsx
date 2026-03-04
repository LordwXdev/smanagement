"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getAllStudents } from "@/lib/api";

export default function TStudents() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getAllStudents().then((d) => { setStudents(Array.isArray(d) ? d : (d.results || [])); setLoading(false); }).catch(() => setLoading(false));
  }, []);

  if (loading) return <Loading />;

  return (
    <>
      <TopBar title="Students" subtitle={students.length + " students"} />
      <div className="card">
        {students.length === 0 ? <p style={{color:"#94a3b8",padding:20}}>No students found.</p> : (
          <table className="data-table">
            <thead><tr><th>Name</th><th>Admission #</th><th>Email</th></tr></thead>
            <tbody>
              {students.map((s, i) => (
                <tr key={i}>
                  <td className="td-bold">{s.full_name}</td>
                  <td className="mono-val">{s.admission_number}</td>
                  <td className="td-muted">{s.email}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}
