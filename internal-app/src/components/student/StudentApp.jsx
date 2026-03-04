"use client";
import { useState, useEffect } from "react";
import Sidebar from "@/components/shared/Sidebar";
import SDashboard from "./SDashboard";
import SGrades from "./SGrades";
import STimetable from "./STimetable";
import SAttendance from "./SAttendance";
import SFees from "./SFees";
import SMessages from "./SMessages";
import { getStudentProfile } from "@/lib/api";

const TABS = [
  { id: "dashboard", icon: "\ud83d\udcca", label: "Dashboard" },
  { id: "grades", icon: "\ud83d\udcdd", label: "Grades" },
  { id: "timetable", icon: "\ud83d\udcc5", label: "Timetable" },
  { id: "attendance", icon: "\u2705", label: "Attendance" },
  { id: "fees", icon: "\ud83d\udcb0", label: "Fees" },
  { id: "messages", icon: "\ud83d\udcac", label: "Messages" },
];

export default function StudentApp({ session, onLogout }) {
  const [tab, setTab] = useState("dashboard");
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    getStudentProfile().then(setProfile).catch(() => {});
  }, []);

  const views = {
    dashboard: <SDashboard user={session.user} profile={profile} />,
    grades: <SGrades />,
    timetable: <STimetable profile={profile} />,
    attendance: <SAttendance profile={profile} />,
    fees: <SFees profile={profile} />,
    messages: <SMessages />,
  };

  return (
    <div className="app-layout">
      <Sidebar user={session.user} role="student" tabs={TABS} activeTab={tab} onTabChange={setTab} onLogout={onLogout} />
      <main className="app-main">{views[tab]}</main>
    </div>
  );
}
