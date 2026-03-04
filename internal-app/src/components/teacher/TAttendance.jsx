"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getAllStudents, getSections, bulkMarkAttendance } from "@/lib/api";

export default function TAttendance() {
  const [sections, setSections] = useState([]);
  const [selectedSection, setSelectedSection] = useState(null);
  const [students, setStudents] = useState([]);
  const [records, setRecords] = useState({});
  const [loading, setLoading] = useState(true);
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    getSections().then((d) => {
      const list = Array.isArray(d) ? d : (d.results || []);
      setSections(list);
      if (list.length > 0) setSelectedSection(list[0].id);
      setLoading(false);
    }).catch(() => setLoading(false));
  }, []);

  useEffect(() => {
    if (selectedSection) {
      getAllStudents(selectedSection).then((d) => {
        const list = Array.isArray(d) ? d : (d.results || []);
        setStudents(list);
        const r = {};
        list.forEach(s => { r[s.id] = "present"; });
        setRecords(r);
        setSaved(false);
      }).catch(() => {});
    }
  }, [selectedSection]);

  const toggle = (id, status) => { setRecords({...records, [id]: status}); setSaved(false); };

  const handleSave = async () => {
    const today = new Date().toISOString().split("T")[0];
    const payload = {
      section_id: selectedSection,
      date: today,
      records: Object.entries(records).map(([sid, status]) => ({ student_id: sid, status })),
    };
    try {
      await bulkMarkAttendance(payload);
      setSaved(true);
    } catch (e) {
      alert("Failed to save: " + (e.response?.data?.detail || e.message));
    }
  };

  if (loading) return <Loading />;

  return (
    <>
      <TopBar title="Mark Attendance" subtitle="Select a section and mark" />
      <div className="filter-row">
        {sections.map(s => (
          <button key={s.id} className={"filter-chip " + (selectedSection === s.id ? "active" : "")}
            onClick={() => setSelectedSection(s.id)}>{s.grade_name} - {s.name}</button>
        ))}
      </div>
      <div className="card">
        <div className="attendance-header">
          <span>{Object.values(records).filter(v => v === "present").length} present / {students.length} total</span>
          <button className="action-btn" onClick={handleSave}>{saved ? "Saved!" : "Save Attendance"}</button>
        </div>
        {students.map((s) => (
          <div key={s.id} className="attendance-row">
            <span className="td-bold">{s.full_name}</span>
            <div className="attendance-btns">
              {["present","absent","late","excused"].map(st => (
                <button key={st} className={"att-btn " + (records[s.id] === st ? "att-" + st : "")}
                  onClick={() => toggle(s.id, st)}>{st}</button>
              ))}
            </div>
          </div>
        ))}
      </div>
    </>
  );
}
