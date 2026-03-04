"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getTeacherTimetable } from "@/lib/api";
import { DAYS, DAY_SHORT } from "@/lib/helpers";

export default function TTimetable() {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getTeacherTimetable().then((d) => { setEntries(Array.isArray(d) ? d : (d.results || [])); setLoading(false); }).catch(() => setLoading(false));
  }, []);

  if (loading) return <Loading />;

  const byDay = {};
  entries.forEach(e => {
    const d = e.day || "unknown";
    if (!byDay[d]) byDay[d] = [];
    byDay[d].push(e);
  });

  return (
    <>
      <TopBar title="My Schedule" subtitle="Weekly teaching timetable" />
      <div className="timetable-grid">
        {DAYS.map(d => (
          <div key={d} className="tt-day">
            <div className="tt-day-name">{DAY_SHORT[d]}</div>
            {(byDay[d] || []).map((e, i) => (
              <div key={i} className="tt-block teacher-block">
                <div className="tt-subject">{e.subject_name}</div>
                <div className="tt-detail">{e.section_name || ""} &middot; {e.room}</div>
              </div>
            ))}
            {(!byDay[d] || byDay[d].length === 0) && <div style={{color:"#94a3b8",fontSize:13,padding:12,textAlign:"center"}}>No classes</div>}
          </div>
        ))}
      </div>
    </>
  );
}
