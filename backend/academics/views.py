from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSchoolAdmin, IsAdminOrReadOnly, IsTeacherOrStudent
from .models import AcademicYear, Grade, Section, Subject, ExamType, Exam, StudentGrade
from .serializers import AcademicYearSerializer, GradeSerializer, SectionSerializer, SubjectSerializer, ExamTypeSerializer, ExamSerializer, StudentGradeSerializer

class AcademicYearViewSet(viewsets.ModelViewSet):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAdminOrReadOnly]
    @action(detail=True, methods=["post"], permission_classes=[IsSchoolAdmin])
    def set_current(self, request, pk=None):
        y = self.get_object(); y.is_current = True; y.save()
        return Response({"detail": f"{y.name} set as current."})

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all(); serializer_class = GradeSerializer; permission_classes = [IsAdminOrReadOnly]

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all(); serializer_class = SectionSerializer; permission_classes = [IsAdminOrReadOnly]; filterset_fields = ["grade","academic_year"]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all(); serializer_class = SubjectSerializer; permission_classes = [IsAdminOrReadOnly]; filterset_fields = ["grade","teacher","is_elective"]

class ExamTypeViewSet(viewsets.ModelViewSet):
    queryset = ExamType.objects.all(); serializer_class = ExamTypeSerializer; permission_classes = [IsAdminOrReadOnly]

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all(); serializer_class = ExamSerializer; permission_classes = [IsTeacherOrStudent]; filterset_fields = ["subject","section","academic_year"]

class StudentGradeViewSet(viewsets.ModelViewSet):
    queryset = StudentGrade.objects.all()
    serializer_class = StudentGradeSerializer
    permission_classes = [IsTeacherOrStudent]
    filterset_fields = ["student","exam"]

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def my_grades(self, request):
        g = StudentGrade.objects.filter(student=request.user)
        return Response(self.get_serializer(g, many=True).data)
