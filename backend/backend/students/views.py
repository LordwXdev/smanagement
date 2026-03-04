from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from accounts.permissions import IsAdminOrReadOnly
from .models import Student, StudentDocument
from .serializers import StudentSerializer, StudentDocumentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("user","section","parent").all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ["section","section__grade","is_graduated"]
    search_fields = ["user__first_name","user__last_name","admission_number"]
    @action(detail=False, methods=["get"])
    def my_profile(self, request):
        try:
            s = Student.objects.get(user=request.user)
            return Response(self.get_serializer(s).data)
        except Student.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)

class StudentDocumentViewSet(viewsets.ModelViewSet):
    queryset = StudentDocument.objects.all()
    serializer_class = StudentDocumentSerializer
    permission_classes = [IsAdminOrReadOnly]
