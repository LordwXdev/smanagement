#!/usr/bin/env python
"""
Seed script for School Management System.
Run from the backend folder: python seed.py
"""
import os, sys, random
from datetime import date, time, timedelta
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_management.settings")

import django
django.setup()

from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

from academics.models import AcademicYear, Grade, Section, Subject, ExamType, Exam, StudentGrade
from students.models import Student
from teachers.models import Teacher, TeacherAssignment
from attendance.models import Attendance
from fees.models import FeeStructure, Invoice, Payment
from communications.models import Message, Notification, Announcement
from timetables.models import TimeSlot, TimetableEntry
from reports.models import ReportCard

random.seed(42)

print("=" * 60)
print("  SEEDING DATABASE")
print("=" * 60)

# ── CLEAR ──
print("\n[1/12] Clearing old data...")
ReportCard.objects.all().delete()
TimetableEntry.objects.all().delete()
TimeSlot.objects.all().delete()
Announcement.objects.all().delete()
Notification.objects.all().delete()
Message.objects.all().delete()
Payment.objects.all().delete()
Invoice.objects.all().delete()
FeeStructure.objects.all().delete()
Attendance.objects.all().delete()
StudentGrade.objects.all().delete()
Exam.objects.all().delete()
ExamType.objects.all().delete()
TeacherAssignment.objects.all().delete()
Teacher.objects.all().delete()
Student.objects.all().delete()
Subject.objects.all().delete()
Section.objects.all().delete()
Grade.objects.all().delete()
AcademicYear.objects.all().delete()
User.objects.filter(is_superuser=False).delete()
print("  Done.")

# ── HELPER ──
def make_user(email, first, last, role):
    return User.objects.create_user(
        username=email.split("@")[0], email=email,
        first_name=first, last_name=last, role=role,
        password="School@2025", phone="+1 555-" + str(1000 + User.objects.count()),
    )

# ── USERS ──
print("\n[2/12] Creating users...")
admin_user = make_user("admin@lumiere.edu", "Margaret", "Davis", "school_admin")
accountant = make_user("finance@lumiere.edu", "Robert", "Clarke", "accountant")

teachers_info = [
    ("e.rodriguez@lumiere.edu", "Elena", "Rodriguez", "Sciences"),
    ("d.chen@lumiere.edu", "David", "Chen", "Mathematics"),
    ("s.williams@lumiere.edu", "Sarah", "Williams", "English"),
    ("j.okafor@lumiere.edu", "James", "Okafor", "Social Studies"),
    ("c.dubois@lumiere.edu", "Claire", "Dubois", "Languages"),
    ("m.park@lumiere.edu", "Michael", "Park", "Sciences"),
    ("a.kumar@lumiere.edu", "Anita", "Kumar", "Mathematics"),
    ("t.johnson@lumiere.edu", "Thomas", "Johnson", "Physical Education"),
]
teacher_users = []
for em, fn, ln, dept in teachers_info:
    teacher_users.append((make_user(em, fn, ln, "teacher"), dept))
print("  8 teachers")

parent_info = [
    ("p.johnson@gmail.com", "Marcus", "Johnson"),
    ("p.chen@gmail.com", "Wei", "Chen"),
    ("p.martinez@gmail.com", "Isabella", "Martinez"),
    ("p.williams@gmail.com", "Derek", "Williams"),
    ("p.patel@gmail.com", "Priya", "Patel"),
    ("p.kim@gmail.com", "Soo-jin", "Kim"),
    ("p.okafor@gmail.com", "Chioma", "Okafor"),
    ("p.liu@gmail.com", "Mei", "Liu"),
    ("p.brown@gmail.com", "Catherine", "Brown"),
    ("p.reyes@gmail.com", "Carlos", "Reyes"),
]
parents = []
for em, fn, ln in parent_info:
    parents.append(make_user(em, fn, ln, "parent"))
print("  10 parents")

student_info = [
    ("amara.j@lumiere.edu", "Amara", "Johnson", 0),
    ("liam.c@lumiere.edu", "Liam", "Chen", 1),
    ("sofia.m@lumiere.edu", "Sofia", "Martinez", 2),
    ("noah.w@lumiere.edu", "Noah", "Williams", 3),
    ("ava.p@lumiere.edu", "Ava", "Patel", 4),
    ("ethan.k@lumiere.edu", "Ethan", "Kim", 5),
    ("mia.o@lumiere.edu", "Mia", "Okafor", 6),
    ("james.l@lumiere.edu", "James", "Liu", 7),
    ("olivia.b@lumiere.edu", "Olivia", "Brown", 8),
    ("daniel.r@lumiere.edu", "Daniel", "Reyes", 9),
    ("emma.t@lumiere.edu", "Emma", "Taylor", 0),
    ("lucas.g@lumiere.edu", "Lucas", "Garcia", 1),
    ("zara.a@lumiere.edu", "Zara", "Ahmed", 2),
    ("ryan.n@lumiere.edu", "Ryan", "Nguyen", 3),
    ("chloe.d@lumiere.edu", "Chloe", "Davis", 4),
]
student_users = []
for em, fn, ln, pi in student_info:
    student_users.append((make_user(em, fn, ln, "student"), parents[pi]))
print("  15 students")

# ── ACADEMIC YEAR ──
print("\n[3/12] Creating academic year...")
ay = AcademicYear.objects.create(name="2025-2026", start_date=date(2025, 9, 1), end_date=date(2026, 6, 15), is_current=True)
print("  2025-2026 (current)")

# ── GRADES & SECTIONS ──
print("\n[4/12] Creating grades and sections...")
grades = {}
for lv, nm in [(9, "Grade 9"), (10, "Grade 10"), (11, "Grade 11"), (12, "Grade 12")]:
    grades[lv] = Grade.objects.create(name=nm, level=lv)

sections = {}
for lv in grades:
    for sn in ["A", "B"]:
        idx = (lv - 9) * 2 + (0 if sn == "A" else 1)
        ct = teacher_users[idx % len(teacher_users)][0]
        sections[(lv, sn)] = Section.objects.create(name=sn, grade=grades[lv], capacity=30, class_teacher=ct, academic_year=ay)
print("  4 grades, 8 sections")

# ── TEACHER PROFILES ──
print("\n[5/12] Creating teacher profiles...")
teacher_objs = []
for i, (u, dept) in enumerate(teacher_users):
    t = Teacher.objects.create(
        user=u, employee_id="TCH-2019-" + str(40 + i).zfill(3),
        department=dept, qualification="Ph.D." if i < 2 else "M.Ed.",
        experience_years=8 + i, specialization=dept,
        joining_date=date(2019, 8, 15), salary=Decimal(str(65000 + i * 3000)),
    )
    teacher_objs.append(t)
print("  8 teacher profiles")

# ── SUBJECTS ──
print("\n[6/12] Creating subjects...")
subjects_config = [
    ("AP Biology", "BIO-301", 10, 0, 4),
    ("AP Calculus AB", "MAT-401", 10, 1, 4),
    ("English Literature", "ENG-201", 10, 2, 3),
    ("World History", "HIS-202", 10, 3, 3),
    ("French III", "FRN-301", 10, 4, 3),
    ("Physics", "PHY-301", 10, 5, 4),
    ("Biology Honors", "BIO-201", 11, 0, 4),
    ("Calculus BC", "MAT-402", 11, 1, 4),
    ("American Lit", "ENG-301", 11, 2, 3),
    ("AP US History", "HIS-301", 11, 3, 4),
    ("Chemistry", "CHM-201", 9, 5, 3),
    ("Algebra II", "MAT-201", 9, 6, 3),
]
subject_objs = []
for nm, code, glv, tidx, cr in subjects_config:
    s = Subject.objects.create(name=nm, code=code, grade=grades[glv], teacher=teacher_users[tidx][0], credit_hours=cr)
    subject_objs.append(s)
print("  " + str(len(subject_objs)) + " subjects")

# ── STUDENT PROFILES ──
print("\n[7/12] Creating student profiles...")
sec_map = [
    (10,"A"),(10,"A"),(10,"A"),(10,"A"),(10,"A"),
    (10,"B"),(10,"B"),(10,"B"),
    (11,"A"),(11,"A"),
    (10,"A"),(10,"A"),(10,"B"),(10,"B"),(10,"B"),
]
student_objs = []
for i, (u, parent) in enumerate(student_users):
    lv, sn = sec_map[i]
    s = Student.objects.create(
        user=u, admission_number="LIA-2022-" + str(847 + i).zfill(4),
        admission_date=date(2022, 8, 20), section=sections[(lv, sn)],
        parent=parent, blood_group=["A+","B+","O+","AB+","O-"][i % 5],
        emergency_contact_name=parent.get_full_name(), emergency_contact_phone=parent.phone,
    )
    student_objs.append(s)
print("  15 student profiles")

# ── TEACHER ASSIGNMENTS ──
print("\n[8/12] Assigning teachers to sections...")
ac = 0
for subj in subject_objs:
    tidx = next(i for i, (u, d) in enumerate(teacher_users) if u == subj.teacher)
    for sn in ["A", "B"]:
        key = (subj.grade.level, sn)
        if key in sections:
            TeacherAssignment.objects.create(teacher=teacher_objs[tidx], subject=subj, section=sections[key], academic_year=ay)
            ac += 1
print("  " + str(ac) + " assignments")

# ── EXAMS & GRADES ──
print("\n[9/12] Creating exams and grading students...")
midterm = ExamType.objects.create(name="Midterm", weight=Decimal("30.00"))
final_type = ExamType.objects.create(name="Final", weight=Decimal("40.00"))
quiz_type = ExamType.objects.create(name="Quiz", weight=Decimal("15.00"))
lab_type = ExamType.objects.create(name="Lab Report", weight=Decimal("15.00"))

exam_objs = []
g10_subjects = [s for s in subject_objs if s.grade.level == 10]

for subj in g10_subjects:
    for sn in ["A", "B"]:
        key = (10, sn)
        if key not in sections:
            continue
        sec = sections[key]
        e1 = Exam.objects.create(
            name=subj.name + " Midterm", exam_type=midterm, subject=subj,
            section=sec, academic_year=ay, date=date(2025, 10, 15),
            start_time=time(9, 0), end_time=time(11, 0),
            total_marks=Decimal("100"), pass_marks=Decimal("40"),
        )
        exam_objs.append(e1)
        e2 = Exam.objects.create(
            name=subj.name + " Quiz 1", exam_type=quiz_type, subject=subj,
            section=sec, academic_year=ay, date=date(2025, 11, 5),
            start_time=time(9, 0), end_time=time(9, 30),
            total_marks=Decimal("50"), pass_marks=Decimal("20"),
        )
        exam_objs.append(e2)

gc = 0
for exam in exam_objs:
    for stu in Student.objects.filter(section=exam.section):
        base = random.randint(65, 98)
        marks = min(Decimal(str(base)) * exam.total_marks / Decimal("100"), exam.total_marks)
        StudentGrade.objects.create(student=stu.user, exam=exam, marks_obtained=marks.quantize(Decimal("0.01")), graded_by=exam.subject.teacher)
        gc += 1
print("  " + str(len(exam_objs)) + " exams, " + str(gc) + " grades")

# ── ATTENDANCE ──
print("\n[10/12] Creating attendance (30 days)...")
statuses = ["present"] * 17 + ["late"] * 2 + ["absent"]
atc = 0
for stu in student_objs:
    for day_off in range(30):
        d = date(2025, 10, 15) + timedelta(days=day_off)
        if d.weekday() >= 5:
            continue
        Attendance.objects.create(student=stu, section=stu.section, date=d, status=random.choice(statuses), marked_by=stu.section.class_teacher)
        atc += 1
print("  " + str(atc) + " records")

# ── FEES ──
print("\n[11/12] Creating fees and payments...")
fee_items = [
    ("Tuition - Semester 1", Decimal("12500.00"), date(2025, 9, 1)),
    ("Lab Fees", Decimal("350.00"), date(2025, 9, 1)),
    ("Activity Fee", Decimal("200.00"), date(2025, 12, 1)),
    ("Library Fee", Decimal("75.00"), date(2025, 9, 1)),
]
fee_structs = []
for nm, amt, due in fee_items:
    fee_structs.append(FeeStructure.objects.create(name=nm, grade=grades[10], academic_year=ay, amount=amt, due_date=due))

ic = 0
pc = 0
for stu in student_objs[:8]:
    for fs in fee_structs:
        ic += 1
        inv = Invoice.objects.create(
            invoice_number="INV-2025-" + str(ic).zfill(4),
            student=stu, fee_structure=fs, amount=fs.amount, due_date=fs.due_date,
        )
        if fs.name != "Activity Fee" or random.random() > 0.5:
            pc += 1
            Payment.objects.create(
                invoice=inv, amount=fs.amount,
                payment_method=random.choice(["cash", "bank_transfer", "card"]),
                transaction_id="TXN-" + str(pc).zfill(6),
                received_by=accountant,
            )
print("  " + str(ic) + " invoices, " + str(pc) + " payments")

# ── MESSAGES & ANNOUNCEMENTS ──
print("\n[12/12] Creating messages and announcements...")
msg_data = [
    (teacher_users[2][0], student_users[0][0], "Hamlet Essay Feedback", "Great analysis! A few notes on your thesis."),
    (teacher_users[1][0], student_users[0][0], "Extra Credit Opportunity", "Math competition next week, interested?"),
    (admin_user, teacher_users[0][0], "AP Curriculum Review", "Please review the updated AP Bio curriculum."),
    (teacher_users[1][0], teacher_users[0][0], "Joint STEM Project", "Should we combine robotics and biology?"),
    (student_users[0][0], teacher_users[0][0], "Lab Report Question", "Question about the enzyme lab methodology."),
]
for sender, recip, subj, body in msg_data:
    Message.objects.create(sender=sender, recipient=recip, subject=subj, body=body)

for stu in student_objs[:5]:
    Notification.objects.create(user=stu.user, notification_type="grade", title="New Grade Posted", message="Your AP Biology Midterm grade has been posted.")

Announcement.objects.create(title="Winter Concert Rehearsal", content="All choir members attend auditorium 3:30 PM Nov 18.", author=admin_user, target_roles=["student","teacher"], publish_date=timezone.now())
Announcement.objects.create(title="Science Fair Registration", content="Deadline Nov 30. See your science teacher.", author=teacher_users[0][0], target_roles=["student"], publish_date=timezone.now())
Announcement.objects.create(title="Grade Submission Deadline", content="All semester grades due Nov 22.", author=admin_user, target_roles=["teacher"], publish_date=timezone.now())
print("  5 messages, 3 announcements")

# ── TIMETABLE ──
print("\n[BONUS] Creating timetable...")
slot_info = [
    ("Period 1", time(8, 0), time(9, 15)),
    ("Period 2", time(9, 30), time(10, 45)),
    ("Period 3", time(11, 0), time(12, 15)),
    ("Lunch", time(12, 15), time(13, 0)),
    ("Period 4", time(13, 0), time(14, 15)),
    ("Period 5", time(14, 30), time(15, 30)),
]
slots = []
for nm, st, et in slot_info:
    slots.append(TimeSlot.objects.create(name=nm, start_time=st, end_time=et))

sec_10a = sections[(10, "A")]
tt_plan = [
    ("monday", 0, 0), ("monday", 1, 2), ("monday", 2, 4),
    ("tuesday", 0, 1), ("tuesday", 1, 3), ("tuesday", 3, 5),
    ("wednesday", 0, 0), ("wednesday", 1, 2), ("wednesday", 2, 4),
    ("thursday", 0, 1), ("thursday", 1, 3), ("thursday", 3, 5),
    ("friday", 0, 0), ("friday", 1, 2),
]
ttc = 0
for day, si, subi in tt_plan:
    if subi < len(g10_subjects) and si < len(slots):
        subj = g10_subjects[subi]
        TimetableEntry.objects.create(
            section=sec_10a, subject=subj, teacher=subj.teacher,
            time_slot=slots[si], day=day, academic_year=ay,
            room="Room " + str(200 + subi),
        )
        ttc += 1
print("  " + str(ttc) + " timetable entries")

# ── REPORT CARDS ──
print("\n[BONUS] Generating report cards...")
rc_count = 0
for stu in student_objs:
    if stu.section.grade.level == 10:
        rc, _ = ReportCard.objects.get_or_create(student=stu, academic_year=ay, defaults={"section": stu.section})
        rc.calculate()
        rc_count += 1

reps = ReportCard.objects.filter(academic_year=ay).order_by("-percentage")
for rank, r in enumerate(reps, 1):
    r.rank = rank
    r.save()
print("  " + str(rc_count) + " report cards")

# ── DONE ──
print("\n" + "=" * 60)
print("  SEED COMPLETE!")
print("=" * 60)
print("")
print("  Users:       " + str(User.objects.count()))
print("  Teachers:    " + str(Teacher.objects.count()))
print("  Students:    " + str(Student.objects.count()))
print("  Subjects:    " + str(Subject.objects.count()))
print("  Exams:       " + str(Exam.objects.count()))
print("  Grades:      " + str(StudentGrade.objects.count()))
print("  Attendance:  " + str(Attendance.objects.count()))
print("  Invoices:    " + str(Invoice.objects.count()))
print("  Messages:    " + str(Message.objects.count()))
print("  Timetable:   " + str(TimetableEntry.objects.count()) + " entries")
print("")
print("  LOGIN CREDENTIALS (password: School@2025):")
print("  -------------------------------------------")
print("  Admin:      admin@lumiere.edu")
print("  Accountant: finance@lumiere.edu")
print("  Teacher:    e.rodriguez@lumiere.edu")
print("  Student:    amara.j@lumiere.edu")
print("  Parent:     p.johnson@gmail.com")
print("")