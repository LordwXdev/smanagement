from django.contrib import admin
from .models import Teacher, TeacherAssignment
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["employee_id","user","department","is_active"]
admin.site.register(TeacherAssignment)
