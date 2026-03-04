"use client";
import { TEACHER_CLASSES } from "@/data/mock";
import { pctBar } from "@/lib/helpers";
import TopBar from "@/components/shared/TopBar";

export default function TClasses() {
  return (
    <>
      <TopBar title="My Classes" subtitle="All active class sections" />
      <div className="course-grid">
        {TEACHER_CLASSES.map((c,i) => (
          <div key={i} className="course-card teacher-card">
            <div className="course-card-head">
              <span className="course-code">{c.section}</span>
              <span className="badge grade-b">{c.students} students</span>
            </div>
            <div className="course-card-name">{c.name}</div>
            <div className="course-card-meta">
              <span>🕐 {c.schedule}</span>
              <span>📍 {c.room}</span>
            </div>
            <div className="course-card-teacher">Class Average: {c.avg_grade}%</div>
            <div className="progress-bar"><div className={`progress-fill ${pctBar(c.avg_grade)}`} style={{width:c.avg_grade+"%"}} /></div>
          </div>
        ))}
      </div>
    </>
  );
}
