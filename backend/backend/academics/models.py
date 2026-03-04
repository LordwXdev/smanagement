import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class AcademicYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["-start_date"]
    def __str__(self): return self.name
    def save(self, *args, **kwargs):
        if self.is_current: AcademicYear.objects.filter(is_current=True).update(is_current=False)
        super().save(*args, **kwargs)

class Grade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    level = models.IntegerField(unique=True)
    description = models.TextField(blank=True)
    class Meta: ordering = ["level"]
    def __str__(self): return self.name

class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="sections")
    capacity = models.IntegerField(default=40)
    class_teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name="sections")
    class Meta:
        unique_together = ["name","grade","academic_year"]
        ordering = ["grade__level","name"]
    def __str__(self): return f"{self.grade.name} - {self.name}"

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="subjects")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    credit_hours = models.IntegerField(default=3)
    is_elective = models.BooleanField(default=False)
    class Meta: ordering = ["grade__level","name"]
    def __str__(self): return f"{self.code} - {self.name}"

class ExamType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    def __str__(self): return self.name

class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="exams")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="exams")
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_marks = models.DecimalField(max_digits=6, decimal_places=2, default=100)
    pass_marks = models.DecimalField(max_digits=6, decimal_places=2, default=40)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["-date"]
    def __str__(self): return f"{self.name} - {self.subject.name}"

class StudentGrade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="grades")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="student_grades")
    marks_obtained = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    remarks = models.TextField(blank=True)
    graded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="graded_exams")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: unique_together = ["student","exam"]
    @property
    def percentage(self):
        if self.exam.total_marks: return round(float(self.marks_obtained)/float(self.exam.total_marks)*100, 2)
        return 0
    @property
    def letter_grade(self):
        p = self.percentage
        if p >= 90: return "A+"
        if p >= 80: return "A"
        if p >= 70: return "B"
        if p >= 60: return "C"
        if p >= 50: return "D"
        return "F"
    @property
    def grade_point(self):
        p = self.percentage
        if p >= 90: return 4.0
        if p >= 80: return 3.5
        if p >= 70: return 3.0
        if p >= 60: return 2.5
        if p >= 50: return 2.0
        return 0.0
