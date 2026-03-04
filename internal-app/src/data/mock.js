// ─── STUDENT MOCK ───
export const MOCK_STUDENT = {
  user: { first_name: "Amara", last_name: "Johnson", email: "amara@lumiere.edu", role: "student" },
  admission_number: "LIA-2022-0847",
  grade: "Grade 10",
  section: "Section A",
  gpa: 3.78,
  attendance_rate: 96.2,
  rank: 12,
  total_students: 156,
};

export const STUDENT_COURSES = [
  { id: 1, name: "AP Biology", code: "BIO-301", teacher: "Dr. Elena Rodriguez", grade: "A", pct: 93, schedule: "Mon/Wed/Fri 8:00-9:15", room: "Lab 2" },
  { id: 2, name: "AP Calculus AB", code: "MAT-401", teacher: "Mr. David Chen", grade: "A-", pct: 91, schedule: "Tue/Thu 8:00-9:30", room: "Room 204" },
  { id: 3, name: "English Literature", code: "ENG-201", teacher: "Ms. Sarah Williams", grade: "B+", pct: 87, schedule: "Mon/Wed/Fri 9:30-10:45", room: "Room 108" },
  { id: 4, name: "World History", code: "HIS-202", teacher: "Mr. James Okafor", grade: "A", pct: 95, schedule: "Tue/Thu 10:00-11:30", room: "Room 115" },
  { id: 5, name: "French III", code: "FRN-301", teacher: "Mme. Claire Dubois", grade: "B+", pct: 88, schedule: "Mon/Wed 11:00-12:15", room: "Room 210" },
  { id: 6, name: "Physics", code: "PHY-301", teacher: "Dr. Michael Park", grade: "A-", pct: 90, schedule: "Tue/Thu 1:00-2:30", room: "Lab 3" },
];

export const STUDENT_GRADES = [
  { subject: "AP Biology", exam: "Lab Report #4", score: "47/50", pct: 94, date: "Nov 12" },
  { subject: "AP Calculus AB", exam: "Chapter 5 Test", score: "88/100", pct: 88, date: "Nov 10" },
  { subject: "World History", exam: "Essay: Cold War", score: "95/100", pct: 95, date: "Nov 8" },
  { subject: "French III", exam: "Oral Exam", score: "85/100", pct: 85, date: "Nov 5" },
  { subject: "Physics", exam: "Midterm Exam", score: "92/100", pct: 92, date: "Nov 1" },
  { subject: "English Literature", exam: "Essay: Hamlet", score: "84/100", pct: 84, date: "Oct 28" },
  { subject: "AP Biology", exam: "Chapter 8 Quiz", score: "18/20", pct: 90, date: "Oct 25" },
  { subject: "AP Calculus AB", exam: "Integration Quiz", score: "45/50", pct: 90, date: "Oct 22" },
];

export const STUDENT_TIMETABLE = {
  monday: [
    { time: "8:00-9:15", subject: "AP Biology", teacher: "Dr. Rodriguez", room: "Lab 2" },
    { time: "9:30-10:45", subject: "English Lit.", teacher: "Ms. Williams", room: "108" },
    { time: "11:00-12:15", subject: "French III", teacher: "Mme. Dubois", room: "210" },
    { time: "1:00-2:00", subject: "Study Hall", teacher: "-", room: "Library" },
  ],
  tuesday: [
    { time: "8:00-9:30", subject: "AP Calculus AB", teacher: "Mr. Chen", room: "204" },
    { time: "10:00-11:30", subject: "World History", teacher: "Mr. Okafor", room: "115" },
    { time: "1:00-2:30", subject: "Physics", teacher: "Dr. Park", room: "Lab 3" },
  ],
  wednesday: [
    { time: "8:00-9:15", subject: "AP Biology", teacher: "Dr. Rodriguez", room: "Lab 2" },
    { time: "9:30-10:45", subject: "English Lit.", teacher: "Ms. Williams", room: "108" },
    { time: "11:00-12:15", subject: "French III", teacher: "Mme. Dubois", room: "210" },
    { time: "1:00-2:30", subject: "Robotics Club", teacher: "Mr. Chen", room: "STEM Lab" },
  ],
  thursday: [
    { time: "8:00-9:30", subject: "AP Calculus AB", teacher: "Mr. Chen", room: "204" },
    { time: "10:00-11:30", subject: "World History", teacher: "Mr. Okafor", room: "115" },
    { time: "1:00-2:30", subject: "Physics", teacher: "Dr. Park", room: "Lab 3" },
  ],
  friday: [
    { time: "8:00-9:15", subject: "AP Biology", teacher: "Dr. Rodriguez", room: "Lab 2" },
    { time: "9:30-10:45", subject: "English Lit.", teacher: "Ms. Williams", room: "108" },
    { time: "11:00-12:00", subject: "Assembly", teacher: "-", room: "Auditorium" },
  ],
};

export const STUDENT_ATTENDANCE = [
  { date: "Nov 12", status: "present" }, { date: "Nov 11", status: "present" },
  { date: "Nov 10", status: "present" }, { date: "Nov 9", status: "late" },
  { date: "Nov 8", status: "present" }, { date: "Nov 7", status: "present" },
  { date: "Nov 6", status: "present" }, { date: "Nov 5", status: "present" },
  { date: "Nov 4", status: "absent" },  { date: "Nov 1", status: "present" },
];

export const STUDENT_FEES = [
  { item: "Tuition - Semester 2", amount: 12500, paid: 12500, status: "paid", due: "Jan 15" },
  { item: "Lab Fees", amount: 350, paid: 350, status: "paid", due: "Sep 1" },
  { item: "Activity Fee", amount: 200, paid: 0, status: "pending", due: "Dec 1" },
  { item: "Library Fee", amount: 75, paid: 75, status: "paid", due: "Sep 1" },
];

export const STUDENT_ANNOUNCEMENTS = [
  { title: "Winter Concert Rehearsal", date: "Nov 18", msg: "All choir members attend auditorium 3:30 PM.", type: "event" },
  { title: "Science Fair Registration", date: "Nov 15", msg: "Deadline Nov 30th. Register online.", type: "academic" },
  { title: "Early Dismissal Friday", date: "Nov 14", msg: "School dismisses 1:00 PM.", type: "general" },
  { title: "AP Exam Prep Sessions", date: "Nov 12", msg: "Free tutoring available Tuesdays after school.", type: "academic" },
];

export const STUDENT_MESSAGES = [
  { id: 1, from: "Ms. Williams", subject: "Hamlet Essay Feedback", preview: "Great analysis! A few notes...", date: "Nov 11", read: false },
  { id: 2, from: "Mr. Chen", subject: "Extra Credit Opportunity", preview: "Math competition next week...", date: "Nov 9", read: true },
  { id: 3, from: "Admin Office", subject: "Activity Fee Reminder", preview: "Please submit by Dec 1...", date: "Nov 8", read: true },
];

// ─── TEACHER MOCK ───
export const MOCK_TEACHER = {
  user: { first_name: "Elena", last_name: "Rodriguez", email: "e.rodriguez@lumiere.edu", role: "teacher" },
  employee_id: "TCH-2019-042",
  department: "Sciences",
  subjects: ["AP Biology", "Biology Honors"],
  sections: ["Grade 10-A", "Grade 10-B", "Grade 11-A"],
  total_students: 87,
};

export const TEACHER_CLASSES = [
  { id: 1, name: "AP Biology", section: "Grade 10-A", students: 28, room: "Lab 2", schedule: "Mon/Wed/Fri 8:00-9:15", avg_grade: 88.5 },
  { id: 2, name: "AP Biology", section: "Grade 10-B", students: 26, room: "Lab 2", schedule: "Mon/Wed/Fri 10:00-11:15", avg_grade: 85.2 },
  { id: 3, name: "Biology Honors", section: "Grade 11-A", students: 33, room: "Lab 1", schedule: "Tue/Thu 9:00-10:30", avg_grade: 82.7 },
];

export const TEACHER_STUDENTS = [
  { id: 1, name: "Amara Johnson", admission: "LIA-2022-0847", section: "10-A", grade: "A", pct: 93, attendance: 96 },
  { id: 2, name: "Liam Chen", admission: "LIA-2022-0901", section: "10-A", grade: "A-", pct: 91, attendance: 98 },
  { id: 3, name: "Sofia Martinez", admission: "LIA-2022-0855", section: "10-A", grade: "B+", pct: 87, attendance: 94 },
  { id: 4, name: "Noah Williams", admission: "LIA-2022-0812", section: "10-A", grade: "B", pct: 83, attendance: 91 },
  { id: 5, name: "Ava Patel", admission: "LIA-2022-0876", section: "10-A", grade: "A", pct: 95, attendance: 100 },
  { id: 6, name: "Ethan Kim", admission: "LIA-2022-0834", section: "10-B", grade: "B+", pct: 88, attendance: 93 },
  { id: 7, name: "Mia Okafor", admission: "LIA-2022-0889", section: "10-B", grade: "A-", pct: 90, attendance: 97 },
  { id: 8, name: "James Liu", admission: "LIA-2022-0867", section: "10-B", grade: "C+", pct: 78, attendance: 85 },
  { id: 9, name: "Olivia Brown", admission: "LIA-2022-0823", section: "11-A", grade: "B", pct: 82, attendance: 92 },
  { id: 10, name: "Daniel Reyes", admission: "LIA-2022-0845", section: "11-A", grade: "A-", pct: 89, attendance: 96 },
];

export const TEACHER_ATTENDANCE_TODAY = [
  { id: 1, name: "Amara Johnson", status: "present" },
  { id: 2, name: "Liam Chen", status: "present" },
  { id: 3, name: "Sofia Martinez", status: "present" },
  { id: 4, name: "Noah Williams", status: "absent" },
  { id: 5, name: "Ava Patel", status: "present" },
];

export const TEACHER_RECENT_GRADES = [
  { student: "Amara Johnson", exam: "Lab Report #4", score: "47/50", submitted: "Nov 12" },
  { student: "Liam Chen", exam: "Lab Report #4", score: "45/50", submitted: "Nov 12" },
  { student: "Ava Patel", exam: "Lab Report #4", score: "49/50", submitted: "Nov 12" },
  { student: "Sofia Martinez", exam: "Lab Report #4", score: "42/50", submitted: "Nov 11" },
  { student: "Noah Williams", exam: "Lab Report #4", score: "38/50", submitted: "Nov 13" },
];

export const TEACHER_TIMETABLE = {
  monday: [
    { time: "8:00-9:15", subject: "AP Biology", section: "10-A", room: "Lab 2" },
    { time: "10:00-11:15", subject: "AP Biology", section: "10-B", room: "Lab 2" },
    { time: "1:00-2:00", subject: "Office Hours", section: "-", room: "Faculty 12" },
  ],
  tuesday: [
    { time: "9:00-10:30", subject: "Biology Honors", section: "11-A", room: "Lab 1" },
    { time: "11:00-12:00", subject: "Dept. Meeting", section: "-", room: "Conf. Room" },
    { time: "2:00-3:00", subject: "Lab Prep", section: "-", room: "Lab 2" },
  ],
  wednesday: [
    { time: "8:00-9:15", subject: "AP Biology", section: "10-A", room: "Lab 2" },
    { time: "10:00-11:15", subject: "AP Biology", section: "10-B", room: "Lab 2" },
  ],
  thursday: [
    { time: "9:00-10:30", subject: "Biology Honors", section: "11-A", room: "Lab 1" },
    { time: "1:00-3:00", subject: "Science Fair Advising", section: "-", room: "Lab 2" },
  ],
  friday: [
    { time: "8:00-9:15", subject: "AP Biology", section: "10-A", room: "Lab 2" },
    { time: "10:00-11:15", subject: "AP Biology", section: "10-B", room: "Lab 2" },
    { time: "2:00-3:00", subject: "Staff Meeting", section: "-", room: "Auditorium" },
  ],
};

export const TEACHER_MESSAGES = [
  { id: 1, from: "Principal Davis", subject: "AP Curriculum Review", preview: "Please review the updated...", date: "Nov 12", read: false },
  { id: 2, from: "Mr. Chen", subject: "Joint STEM Project", preview: "Should we combine the robotics...", date: "Nov 10", read: false },
  { id: 3, from: "Amara Johnson", subject: "Lab Report Question", preview: "I had a question about...", date: "Nov 9", read: true },
  { id: 4, from: "Admin Office", subject: "Grade Submission Deadline", preview: "Reminder: semester grades due...", date: "Nov 8", read: true },
];

export const TEACHER_ANNOUNCEMENTS = [
  { title: "Grade Submission Deadline", date: "Nov 20", msg: "All semester grades due by Nov 22nd.", type: "deadline" },
  { title: "Professional Development Day", date: "Nov 25", msg: "No classes. Faculty training in auditorium.", type: "event" },
  { title: "Science Fair Judging", date: "Dec 5", msg: "Volunteer judges needed. Sign up in faculty lounge.", type: "event" },
];
