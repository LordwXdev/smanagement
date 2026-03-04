from django.contrib import admin
from .models import Student, StudentDocument
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["admission_number","user","section","is_graduated"]
    list_filter = ["section__grade","is_graduated"]
    search_fields = ["admission_number","user__first_name"]
admin.site.register(StudentDocument)
