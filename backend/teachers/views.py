from rest_framework import viewsets
from accounts.permissions import IsSchoolAdmin, IsAdminOrReadOnly
from .models import Teacher, TeacherAssignment
from .serializers import TeacherSerializer, TeacherAssignmentSerializer
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related("user").prefetch_related("assignments").all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ["department","is_active"]
    search_fields = ["user__first_name","user__last_name","employee_id"]
class TeacherAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TeacherAssignment.objects.all()
    serializer_class = TeacherAssignmentSerializer
    permission_classes = [IsSchoolAdmin]
