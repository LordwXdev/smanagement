from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, r, v):
        return r.user.is_authenticated and r.user.role == "super_admin"

class IsSchoolAdmin(BasePermission):
    def has_permission(self, r, v):
        return r.user.is_authenticated and r.user.role in ("super_admin", "school_admin")

class IsTeacher(BasePermission):
    def has_permission(self, r, v):
        return r.user.is_authenticated and r.user.role in ("super_admin", "school_admin", "teacher")

class IsTeacherOrStudent(BasePermission):
    """Teachers get full access, students get read-only."""
    def has_permission(self, r, v):
        if not r.user.is_authenticated:
            return False
        if r.user.role in ("super_admin", "school_admin", "teacher"):
            return True
        if r.user.role in ("student", "parent") and r.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return False

class IsStudent(BasePermission):
    def has_permission(self, r, v):
        return r.user.is_authenticated and r.user.role == "student"

class IsParent(BasePermission):
    def has_permission(self, r, v):
        return r.user.is_authenticated and r.user.role == "parent"

class IsAccountant(BasePermission):
    def has_permission(self, r, v):
        return r.user.is_authenticated and r.user.role in ("super_admin", "school_admin", "accountant")

class IsAccountantOrStudent(BasePermission):
    """Accountants get full access, students can view their own invoices."""
    def has_permission(self, r, v):
        if not r.user.is_authenticated:
            return False
        if r.user.role in ("super_admin", "school_admin", "accountant"):
            return True
        if r.user.role in ("student", "parent") and r.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return False

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, r, v):
        if r.method in ("GET", "HEAD", "OPTIONS"):
            return r.user.is_authenticated
        return r.user.is_authenticated and r.user.role in ("super_admin", "school_admin")
