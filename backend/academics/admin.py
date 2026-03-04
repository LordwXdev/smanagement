from django.contrib import admin
from .models import AcademicYear, Grade, Section, Subject, ExamType, Exam, StudentGrade
@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin): list_display = ["name","start_date","end_date","is_current"]
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin): list_display = ["name","level"]
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin): list_display = ["__str__","grade","capacity"]
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin): list_display = ["code","name","grade","teacher"]
admin.site.register(ExamType)
admin.site.register(Exam)
admin.site.register(StudentGrade)
