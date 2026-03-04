import uuid
from django.db import models
from django.conf import settings

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    admission_number = models.CharField(max_length=30, unique=True)
    admission_date = models.DateField()
    section = models.ForeignKey("academics.Section", on_delete=models.SET_NULL, null=True, related_name="students")
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    blood_group = models.CharField(max_length=5, blank=True)
    allergies = models.TextField(blank=True)
    medical_conditions = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    is_graduated = models.BooleanField(default=False)
    previous_school = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: ordering = ["admission_number"]
    def __str__(self): return f"{self.user.get_full_name()} ({self.admission_number})"

class StudentDocument(models.Model):
    class DocType(models.TextChoices):
        BIRTH_CERT = "birth_certificate", "Birth Certificate"
        TRANSFER_CERT = "transfer_certificate", "Transfer Certificate"
        REPORT_CARD = "report_card", "Report Card"
        MEDICAL = "medical_record", "Medical Record"
        OTHER = "other", "Other"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="documents")
    doc_type = models.CharField(max_length=30, choices=DocType.choices)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="student_documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
