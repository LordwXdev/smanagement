import uuid
from django.db import models
class ReportCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name="report_cards")
    academic_year = models.ForeignKey("academics.AcademicYear", on_delete=models.CASCADE)
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE)
    total_marks = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    obtained_marks = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    rank = models.IntegerField(null=True, blank=True)
    teacher_comments = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    generated_at = models.DateTimeField(auto_now_add=True)
    class Meta: unique_together = ["student","academic_year"]
    def calculate(self):
        from academics.models import StudentGrade
        grades = StudentGrade.objects.filter(student=self.student.user, exam__academic_year=self.academic_year)
        if grades.exists():
            self.total_marks = sum(float(g.exam.total_marks) for g in grades)
            self.obtained_marks = sum(float(g.marks_obtained) for g in grades)
            self.percentage = (self.obtained_marks/self.total_marks*100) if self.total_marks else 0
            self.gpa = sum(g.grade_point for g in grades)/grades.count()
            self.save()
