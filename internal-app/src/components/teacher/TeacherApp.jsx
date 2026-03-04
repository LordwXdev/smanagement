"use client";
import { useState } from "react";
import Sidebar from "@/components/shared/Sidebar";
import TDashboard from "./TDashboard";
import TStudents from "./TStudents";
import TAttendance from "./TAttendance";
import TGrading from "./TGrading";
import TTimetable from "./TTimetable";
import TMessages from "./TMessages";

const TABS = [
  { id: "dashboard", icon: "\ud83d\udcca", label: "Dashboard" },
  { id: "students", icon: "\ud83d\udc65", label: "Students" },
  { id: "attendance", icon: "\u2705", label: "Attendance" },
  { id: "grading", icon: "\ud83d\udcdd", label: "Grading" },
  { id: "timetable", icon: "\ud83d\udcc5", label: "Timetable" },
  { id: "messages", icon: "\ud83d\udcac", label: "Messages" },
];

export default function TeacherApp({ session, onLogout }) {
  const [tab, setTab] = useState("dashboard");
  const views = {
    dashboard: <TDashboard user={session.user} />,
    students: <TStudents />,
    attendance: <TAttendance />,
    grading: <TGrading />,
    timetable: <TTimetable />,
    messages: <TMessages />,
  };
  return (
    <div className="app-layout">
      <Sidebar user={session.user} role="teacher" tabs={TABS} activeTab={tab} onTabChange={setTab} onLogout={onLogout} />
      <main className="app-main">{views[tab]}</main>
    </div>
  );
}
