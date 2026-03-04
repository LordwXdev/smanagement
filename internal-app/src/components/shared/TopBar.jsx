"use client";
export default function TopBar({ title, subtitle }) {
  return (
    <div className="topbar">
      <div>
        <h1 className="topbar-title">{title}</h1>
        {subtitle && <p className="topbar-sub">{subtitle}</p>}
      </div>
    </div>
  );
}
