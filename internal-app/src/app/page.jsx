"use client";
import { useState, useEffect } from "react";
import LoginPage from "@/components/LoginPage";
import StudentApp from "@/components/student/StudentApp";
import TeacherApp from "@/components/teacher/TeacherApp";
import { getProfile, logout as doLogout } from "@/lib/api";

export default function Home() {
  const [session, setSession] = useState(null);
  const [checking, setChecking] = useState(true);

  useEffect(() => {
    const token = typeof window !== "undefined" ? localStorage.getItem("access_token") : null;
    if (token) {
      getProfile().then((user) => {
        setSession({ role: user.role, user });
        setChecking(false);
      }).catch(() => { setChecking(false); });
    } else {
      setChecking(false);
    }
  }, []);

  const handleLogin = (user) => {
    setSession({ role: user.role, user });
  };

  const handleLogout = () => {
    doLogout();
    setSession(null);
  };

  if (checking) return (
    <div style={{minHeight:"100vh",display:"flex",alignItems:"center",justifyContent:"center",background:"#0a1628"}}>
      <div style={{color:"#c8a44e",fontSize:18}}>Loading...</div>
    </div>
  );

  if (!session) return <LoginPage onLogin={handleLogin} />;
  if (session.role === "student") return <StudentApp session={session} onLogout={handleLogout} />;
  if (session.role === "teacher") return <TeacherApp session={session} onLogout={handleLogout} />;

  return (
    <div style={{minHeight:"100vh",display:"flex",alignItems:"center",justifyContent:"center",background:"#0a1628",color:"white",flexDirection:"column",gap:16}}>
      <h2>Role not supported: {session.role}</h2>
      <p>This portal is for students and teachers only.</p>
      <button onClick={handleLogout} style={{padding:"10px 24px",background:"#c8a44e",border:"none",borderRadius:8,fontWeight:700,cursor:"pointer"}}>Sign Out</button>
    </div>
  );
}
