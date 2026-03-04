from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(["GET"])
@permission_classes([AllowAny])
def api_root(request):
    return Response({"message": "School Management System API v1.0",
        "endpoints": {
            "accounts": "/api/accounts/", "students": "/api/students/",
            "teachers": "/api/teachers/", "academics": "/api/academics/",
            "attendance": "/api/attendance/", "fees": "/api/fees/",
            "communications": "/api/communications/",
            "timetables": "/api/timetables/", "reports": "/api/reports/",
    }})

urlpatterns = [
    path("", api_root),
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/students/", include("students.urls")),
    path("api/teachers/", include("teachers.urls")),
    path("api/academics/", include("academics.urls")),
    path("api/attendance/", include("attendance.urls")),
    path("api/fees/", include("fees.urls")),
    path("api/communications/", include("communications.urls")),
    path("api/timetables/", include("timetables.urls")),
    path("api/reports/", include("reports.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "School Management System"
