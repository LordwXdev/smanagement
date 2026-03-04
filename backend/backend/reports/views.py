from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from accounts.permissions import IsSchoolAdmin, IsAdminOrReadOnly
from students.models import Student
from academics.models import AcademicYear
from .models import ReportCard
from .serializers import ReportCardSerializer
class ReportCardViewSet(viewsets.ModelViewSet):
    queryset = ReportCard.objects.select_related("student__user","academic_year").all()
    serializer_class = ReportCardSerializer; permission_classes = [IsAdminOrReadOnly]; filterset_fields = ["student","academic_year","is_published"]
    @action(detail=False, methods=["post"], permission_classes=[IsSchoolAdmin])
    def generate(self, request):
        sid, aid = request.data.get("section"), request.data.get("academic_year")
        if not all([sid,aid]): return Response({"detail":"section and academic_year required."}, status=status.HTTP_400_BAD_REQUEST)
        students = Student.objects.filter(section_id=sid)
        ay = AcademicYear.objects.get(id=aid)
        for s in students:
            r, _ = ReportCard.objects.get_or_create(student=s, academic_year=ay, defaults={"section_id":sid})
            r.calculate()
        for rank, r in enumerate(ReportCard.objects.filter(academic_year=ay, section_id=sid).order_by("-percentage"), 1):
            r.rank = rank; r.save()
        return Response({"detail": f"Generated {students.count()} report cards."})
    @action(detail=False)
    def my_reports(self, request):
        u = request.user
        if u.role == "student": qs = ReportCard.objects.filter(student__user=u, is_published=True)
        elif u.role == "parent": qs = ReportCard.objects.filter(student__parent=u, is_published=True)
        else: qs = ReportCard.objects.none()
        return Response(self.get_serializer(qs, many=True).data)
