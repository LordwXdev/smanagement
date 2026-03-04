export function gradeColor(g) {
  if (!g) return "";
  if (g.startsWith("A")) return "grade-a";
  if (g.startsWith("B")) return "grade-b";
  if (g.startsWith("C")) return "grade-c";
  return "grade-d";
}
export function statusColor(s) {
  const m = { present: "status-present", absent: "status-absent", late: "status-late", excused: "status-excused", paid: "status-present", pending: "status-late", overdue: "status-absent" };
  return m[s] || "";
}
export function pctBar(pct) {
  if (pct >= 90) return "bar-a";
  if (pct >= 80) return "bar-b";
  if (pct >= 70) return "bar-c";
  return "bar-d";
}
export function currency(n) { return "$" + n.toLocaleString(); }
export const DAYS = ["monday","tuesday","wednesday","thursday","friday"];
export const DAY_SHORT = { monday:"Mon", tuesday:"Tue", wednesday:"Wed", thursday:"Thu", friday:"Fri" };
