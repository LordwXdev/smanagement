import uuid
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
class TimeSlot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    class Meta: ordering = ["start_time"]
class TimetableEntry(models.Model):
    DAY_CHOICES = [("monday","Monday"),("tuesday","Tuesday"),("wednesday","Wednesday"),("thursday","Thursday"),("friday","Friday"),("saturday","Saturday")]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE, related_name="timetable_entries")
    subject = models.ForeignKey("academics.Subject", on_delete=models.CASCADE)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="timetable_entries")
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    academic_year = models.ForeignKey("academics.AcademicYear", on_delete=models.CASCADE)
    room = models.CharField(max_length=50, blank=True)
    class Meta:
        unique_together = ["section","time_slot","day","academic_year"]
        ordering = ["day","time_slot__start_time"]
    def clean(self):
        if TimetableEntry.objects.filter(teacher=self.teacher, time_slot=self.time_slot, day=self.day, academic_year=self.academic_year).exclude(pk=self.pk).exists():
            raise ValidationError("Teacher conflict.")
    def save(self, *args, **kwargs): self.clean(); super().save(*args, **kwargs)
