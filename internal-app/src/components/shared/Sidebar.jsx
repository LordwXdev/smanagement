"use client";
export default function Sidebar({ user, role, tabs, activeTab, onTabChange, onLogout }) {
  return (
    <aside className={`sidebar sidebar-${role}`}>
      <div className="sidebar-header">
        <div className="sidebar-crest">L</div>
        <div className="sidebar-brand">Lumiere Portal</div>
      </div>
      <div className="sidebar-user">
        <div className="sidebar-avatar">{user.first_name[0]}{user.last_name[0]}</div>
        <div>
          <div className="sidebar-name">{user.first_name} {user.last_name}</div>
          <div className="sidebar-role">{role === "student" ? "Student" : "Teacher"}</div>
        </div>
      </div>
      <nav className="sidebar-nav">
        {tabs.map((t) => (
          <button key={t.id}
            className={`sidebar-item ${activeTab === t.id ? "active" : ""}`}
            onClick={() => onTabChange(t.id)}>
            <span className="sidebar-icon">{t.icon}</span>
            <span>{t.label}</span>
            {t.badge ? <span className="sidebar-badge">{t.badge}</span> : null}
          </button>
        ))}
      </nav>
      <button className="sidebar-logout" onClick={onLogout}>
        <span className="sidebar-icon">🚪</span> Sign Out
      </button>
    </aside>
  );
}
