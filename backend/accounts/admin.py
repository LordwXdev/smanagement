from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, AuditLog
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["email","first_name","last_name","role","is_active","created_at"]
    list_filter = ["role","is_active"]
    fieldsets = BaseUserAdmin.fieldsets + (("Extended", {"fields": ("role","phone","address","profile_photo","date_of_birth")}),)
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ["user","action","model_name","timestamp"]
    readonly_fields = ["user","action","model_name","object_id","details","ip_address","timestamp"]
