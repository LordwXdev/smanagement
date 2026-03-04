"use client";
import { STUDENT_COURSES } from "@/data/mock";
import { gradeColor, pctBar } from "@/lib/helpers";
import TopBar from "@/components/shared/TopBar";

export default function SCourses() {
  return (
    <>
      <TopBar title="My Courses" subtitle="Current semester enrollment" />
      <div className="course-grid">
        {STUDENT_COURSES.map((c,i) => (
          <div key={i} className="course-card">
            <div className="course-card-head">
              <span className="course-code">{c.code}</span>
              <span className={`badge ${gradeColor(c.grade)}`}>{c.grade} ({c.pct}%)</span>
            </div>
            <div className="course-card-name">{c.name}</div>
            <div className="course-card-teacher">{c.teacher}</div>
            <div className="course-card-meta">
              <span>🕐 {c.schedule}</span>
              <span>📍 {c.room}</span>
            </div>
            <div className="progress-bar"><div className={`progress-fill ${pctBar(c.pct)}`} style={{width: c.pct+"%"}} /></div>
          </div>
        ))}
      </div>
    </>
  );
}
