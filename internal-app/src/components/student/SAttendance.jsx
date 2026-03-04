"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getMyAttendance } from "@/lib/api";
import { statusColor } from "@/lib/helpers";

export default function SAttendance({ profile }) {
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (profile && profile.id) {
      getMyAttendance(profile.id).then((d) => { setRecords(Array.isArray(d) ? d : (d.results || [])); setLoading(false); }).catch(() => setLoading(false));
    } else { setLoading(false); }
  }, [profile]);

  if (loading) return <Loading />;

  const present = records.filter(r => r.status === "present").length;
  const total = records.length;
  const rate = total > 0 ? Math.round(present / total * 100) : 0;

  return (
    <>
      <TopBar title="Attendance" subtitle="Your attendance record" />
      <div className="stat-row">
        <div className="stat-box"><div className="stat-num">{rate}%</div><div className="stat-label">Attendance Rate</div></div>
        <div className="stat-box"><div className="stat-num">{present}/{total}</div><div className="stat-label">Present Days</div></div>
      </div>
      <div className="card">
        <div className="card-title">Records</div>
        {records.length === 0 ? <p style={{color:"#94a3b8",padding:12}}>No attendance records.</p> : (
          <table className="data-table">
            <thead><tr><th>Date</th><th>Status</th></tr></thead>
            <tbody>
              {records.slice(0, 30).map((r, i) => (
                <tr key={i}>
                  <td className="td-muted">{r.date}</td>
                  <td><span className={"badge-pill " + statusColor(r.status)}>{r.status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}
