"use client";
import { useState, useEffect } from "react";
import TopBar from "@/components/shared/TopBar";
import Loading from "@/components/shared/Loading";
import { getMyInvoices } from "@/lib/api";
import { statusColor, currency } from "@/lib/helpers";

export default function SFees({ profile }) {
  const [invoices, setInvoices] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (profile && profile.id) {
      getMyInvoices(profile.id).then((d) => { setInvoices(Array.isArray(d) ? d : (d.results || [])); setLoading(false); }).catch(() => setLoading(false));
    } else { setLoading(false); }
  }, [profile]);

  if (loading) return <Loading />;

  const totalBilled = invoices.reduce((s, inv) => s + parseFloat(inv.amount || 0), 0);
  const totalPaid = invoices.reduce((s, inv) => s + parseFloat(inv.amount_paid || 0), 0);

  return (
    <>
      <TopBar title="Fees & Payments" subtitle="Your billing summary" />
      <div className="stat-row">
        <div className="stat-box"><div className="stat-num">{currency(totalBilled)}</div><div className="stat-label">Total Billed</div></div>
        <div className="stat-box"><div className="stat-num">{currency(totalPaid)}</div><div className="stat-label">Paid</div></div>
        <div className="stat-box"><div className="stat-num">{currency(totalBilled - totalPaid)}</div><div className="stat-label">Balance</div></div>
      </div>
      <div className="card">
        {invoices.length === 0 ? <p style={{color:"#94a3b8",padding:20}}>No invoices found.</p> : (
          <table className="data-table">
            <thead><tr><th>Invoice</th><th>Amount</th><th>Paid</th><th>Due</th><th>Status</th></tr></thead>
            <tbody>
              {invoices.map((inv, i) => (
                <tr key={i}>
                  <td className="td-bold">{inv.invoice_number}</td>
                  <td className="mono-val">{currency(parseFloat(inv.amount))}</td>
                  <td className="mono-val">{currency(parseFloat(inv.amount_paid))}</td>
                  <td className="td-muted">{inv.due_date}</td>
                  <td><span className={"badge-pill " + statusColor(inv.status)}>{inv.status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}
