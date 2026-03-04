from django.contrib import admin
from .models import ReportCard
@admin.register(ReportCard)
class ReportCardAdmin(admin.ModelAdmin):
    list_display = ["student","academic_year","percentage","gpa","rank","is_published"]
