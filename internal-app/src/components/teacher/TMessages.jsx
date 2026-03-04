"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getTeacherMessages } from "@/lib/api";

export default function TMessages() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getTeacherMessages().then((d) => { setMessages(Array.isArray(d) ? d : (d.results || [])); setLoading(false); }).catch(() => setLoading(false));
  }, []);

  if (loading) return <Loading />;

  return (
    <>
      <TopBar title="Messages" subtitle="Your inbox" />
      <div className="card">
        {messages.length === 0 ? <p style={{color:"#94a3b8",padding:20}}>No messages.</p> :
          messages.map((m, i) => (
            <div key={i} className={"msg-row " + (!m.is_read ? "msg-unread" : "")}>
              <div className="msg-dot-col">{!m.is_read && <span className="msg-dot" />}</div>
              <div className="msg-content">
                <div className="msg-from">{m.sender_name || "Unknown"}</div>
                <div className="msg-subject">{m.subject}</div>
                <div className="msg-preview">{(m.body || "").slice(0, 80)}</div>
              </div>
            </div>
          ))
        }
      </div>
    </>
  );
}
