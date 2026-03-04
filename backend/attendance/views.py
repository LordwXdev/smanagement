from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from accounts.permissions import IsTeacher, IsTeacherOrStudent
from students.models import Student
from .models import Attendance
from .serializers import AttendanceSerializer, BulkAttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    filterset_fields = ["student","section","date","status"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy", "bulk_mark"]:
            return [IsTeacher()]
        return [IsTeacherOrStudent()]

    def get_queryset(self):
        user = self.request.user
        qs = Attendance.objects.select_related("student","student__user").all()
        # Students only see their own attendance
        if user.role == "student":
            qs = qs.filter(student__user=user)
        elif user.role == "parent":
            qs = qs.filter(student__parent=user)
        return qs

    @action(detail=False, methods=["post"], permission_classes=[IsTeacher])
    def bulk_mark(self, request):
        s = BulkAttendanceSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        d = s.validated_data
        for rec in d["records"]:
            Attendance.objects.update_or_create(
                student_id=rec["student_id"], date=d["date"],
                defaults={"section_id": d["section_id"], "status": rec.get("status","present"), "marked_by": request.user})
        return Response({"detail": f"Marked {len(d['records'])} records."})

    @action(detail=False, methods=["get"], permission_classes=[IsTeacher])
    def report(self, request):
        sec = request.query_params.get("section")
        df = request.query_params.get("from")
        dt = request.query_params.get("to")
        if not all([sec, df, dt]):
            return Response({"detail": "section, from, to required."}, status=status.HTTP_400_BAD_REQUEST)
        report = []
        for s in Student.objects.filter(section_id=sec):
            recs = Attendance.objects.filter(student=s, date__range=[df, dt])
            agg = recs.aggregate(present=Count("id",filter=Q(status="present")), absent=Count("id",filter=Q(status="absent")), total=Count("id"))
            agg["student_name"] = s.user.get_full_name()
            agg["rate"] = round(agg["present"]/max(agg["total"],1)*100, 1)
            report.append(agg)
        return Response(report)
