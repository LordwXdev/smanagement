import uuid
from django.db import models
from django.conf import settings
class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="teacher_profile")
    employee_id = models.CharField(max_length=30, unique=True)
    department = models.CharField(max_length=100, blank=True)
    qualification = models.CharField(max_length=200, blank=True)
    experience_years = models.IntegerField(default=0)
    specialization = models.CharField(max_length=200, blank=True)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["employee_id"]
    def __str__(self): return f"{self.user.get_full_name()} ({self.employee_id})"
class TeacherAssignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="assignments")
    subject = models.ForeignKey("academics.Subject", on_delete=models.CASCADE)
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE)
    academic_year = models.ForeignKey("academics.AcademicYear", on_delete=models.CASCADE)
    class Meta: unique_together = ["teacher","subject","section","academic_year"]
