import axios from "axios";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

const api = axios.create({ baseURL: API_URL, headers: { "Content-Type": "application/json" } });

api.interceptors.request.use((config) => {
  if (typeof window !== "undefined") {
    const token = localStorage.getItem("access_token");
    if (token) config.headers.Authorization = "Bearer " + token;
  }
  return config;
});

api.interceptors.response.use(
  (res) => res,
  async (err) => {
    const orig = err.config;
    if (err.response && err.response.status === 401 && !orig._retry) {
      orig._retry = true;
      const refresh = typeof window !== "undefined" ? localStorage.getItem("refresh_token") : null;
      if (refresh) {
        try {
          const { data } = await axios.post(API_URL + "/accounts/token/refresh/", { refresh });
          localStorage.setItem("access_token", data.access);
          orig.headers.Authorization = "Bearer " + data.access;
          return api(orig);
        } catch (e) {
          localStorage.removeItem("access_token");
          localStorage.removeItem("refresh_token");
          window.location.href = "/";
        }
      }
    }
    return Promise.reject(err);
  }
);

// ── Auth ──
export async function login(email, password) {
  const { data } = await api.post("/accounts/login/", { email, password });
  localStorage.setItem("access_token", data.access);
  localStorage.setItem("refresh_token", data.refresh);
  return data;
}

export async function getProfile() {
  const { data } = await api.get("/accounts/profile/");
  return data;
}

export function logout() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
}

// ── Student endpoints ──
export async function getStudentProfile() {
  const { data } = await api.get("/students/students/my_profile/");
  return data;
}

export async function getMyGrades() {
  const { data } = await api.get("/academics/student-grades/my_grades/");
  return data;
}

export async function getMyAttendance(studentId) {
  const { data } = await api.get("/attendance/attendance/", { params: { student: studentId } });
  return data;
}

export async function getMyInvoices(studentId) {
  const { data } = await api.get("/fees/invoices/", { params: { student: studentId } });
  return data;
}

export async function getMyMessages() {
  const { data } = await api.get("/communications/messages/inbox/");
  return data;
}

export async function getAnnouncements() {
  const { data } = await api.get("/communications/announcements/");
  return data;
}

export async function getNotifications() {
  const { data } = await api.get("/communications/notifications/");
  return data;
}

export async function getTimetable(sectionId) {
  const { data } = await api.get("/timetables/entries/section_timetable/", { params: { section: sectionId } });
  return data;
}

export async function getMyReports() {
  const { data } = await api.get("/reports/report-cards/my_reports/");
  return data;
}

// ── Teacher endpoints ──
export async function getTeacherProfile() {
  const { data } = await api.get("/teachers/teachers/", { params: { search: "" } });
  return data;
}

export async function getTeacherAssignments() {
  const { data } = await api.get("/teachers/assignments/");
  return data;
}

export async function getAllStudents(sectionId) {
  const { data } = await api.get("/students/students/", { params: sectionId ? { section: sectionId } : {} });
  return data;
}

export async function getSections() {
  const { data } = await api.get("/academics/sections/");
  return data;
}

export async function getSubjects() {
  const { data } = await api.get("/academics/subjects/");
  return data;
}

export async function getExams(params) {
  const { data } = await api.get("/academics/exams/", { params });
  return data;
}

export async function getStudentGrades(params) {
  const { data } = await api.get("/academics/student-grades/", { params });
  return data;
}

export async function getAttendanceRecords(params) {
  const { data } = await api.get("/attendance/attendance/", { params });
  return data;
}

export async function bulkMarkAttendance(payload) {
  const { data } = await api.post("/attendance/attendance/bulk_mark/", payload);
  return data;
}

export async function getTeacherMessages() {
  const { data } = await api.get("/communications/messages/inbox/");
  return data;
}

export async function getTeacherTimetable() {
  const { data } = await api.get("/timetables/entries/");
  return data;
}

export default api;
