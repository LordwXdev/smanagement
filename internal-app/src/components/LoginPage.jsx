"use client";
import { useState } from "react";
import { login, getProfile } from "@/lib/api";

export default function LoginPage({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!email || !password) { setError("Enter email and password."); return; }
    setError(""); setLoading(true);
    try {
      await login(email, password);
      const user = await getProfile();
      onLogin(user);
    } catch (err) {
      const msg = err.response?.data?.detail || "Invalid credentials.";
      setError(msg);
    }
    setLoading(false);
  };

  const handleDemo = async (demoEmail) => {
    setError(""); setLoading(true);
    try {
      await login(demoEmail, "School@2025");
      const user = await getProfile();
      onLogin(user);
    } catch (err) {
      setError("Demo login failed. Is the backend running with seed data?");
    }
    setLoading(false);
  };

  return (
    <div className="login-page">
      <div className="login-bg-pattern" />
      <div className="login-card">
        <div className="login-crest">L</div>
        <h1 className="login-title">School Portal</h1>
        <p className="login-sub">Sign in with your school credentials</p>

        {error && <div className="login-error">{error}</div>}

        <div className="login-fields">
          <label className="login-label">Email</label>
          <input className="login-input" type="email" placeholder="you@lumiere.edu"
            value={email} onChange={(e) => setEmail(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSubmit()} />
          <label className="login-label">Password</label>
          <input className="login-input" type="password" placeholder="Enter password"
            value={password} onChange={(e) => setPassword(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSubmit()} />
          <button className="login-btn" onClick={handleSubmit} disabled={loading}>
            {loading ? "Signing in..." : "Sign In"}
          </button>
        </div>

        <div className="login-divider"><span>Demo Access</span></div>

        <div className="demo-btns">
          <button className="demo-btn demo-student" onClick={() => handleDemo("amara.j@lumiere.edu")} disabled={loading}>
            <span className="demo-icon">&#127891;</span>
            <span><strong>Student Demo</strong><br/><small>amara.j@lumiere.edu</small></span>
          </button>
          <button className="demo-btn demo-teacher" onClick={() => handleDemo("e.rodriguez@lumiere.edu")} disabled={loading}>
            <span className="demo-icon">&#128203;</span>
            <span><strong>Teacher Demo</strong><br/><small>e.rodriguez@lumiere.edu</small></span>
          </button>
        </div>
      </div>
    </div>
  );
}
