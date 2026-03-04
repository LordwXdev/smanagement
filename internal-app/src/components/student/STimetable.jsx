"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getTimetable } from "@/lib/api";
import { DAYS, DAY_SHORT } from "@/lib/helpers";

export default function STimetable({ profile }) {
  const [tt, setTt] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (profile && profile.section) {
      getTimetable(profile.section).then((data) => { setTt(data || {}); setLoading(false); }).catch(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, [profile]);

  if (loading) return <Loading />;

  const hasTt = Object.keys(tt).length > 0;

  return (
    <>
      <TopBar title="My Timetable" subtitle="Weekly schedule" />
      {!hasTt ? (
        <div className="card"><p style={{color:"#94a3b8",padding:20}}>No timetable data available for your section.</p></div>
      ) : (
        <div className="timetable-grid">
          {DAYS.map((d) => (
            <div key={d} className="tt-day">
              <div className="tt-day-name">{DAY_SHORT[d]}</div>
              {(tt[d] || []).map((e, i) => (
                <div key={i} className="tt-block student-block">
                  <div className="tt-time">{e.time_slot_detail || ""}</div>
                  <div className="tt-subject">{e.subject_name}</div>
                  <div className="tt-detail">{e.teacher_name} &middot; {e.room}</div>
                </div>
              ))}
              {(!tt[d] || tt[d].length === 0) && <div style={{color:"#94a3b8",fontSize:13,padding:12,textAlign:"center"}}>No classes</div>}
            </div>
          ))}
        </div>
      )}
    </>
  );
}
