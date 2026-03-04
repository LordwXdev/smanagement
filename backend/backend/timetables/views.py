from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSchoolAdmin, IsAdminOrReadOnly
from .models import TimeSlot, TimetableEntry
from .serializers import TimeSlotSerializer, TimetableEntrySerializer

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all(); serializer_class = TimeSlotSerializer; permission_classes = [IsSchoolAdmin]

class TimetableEntryViewSet(viewsets.ModelViewSet):
    queryset = TimetableEntry.objects.select_related("subject","teacher","section","time_slot").all()
    serializer_class = TimetableEntrySerializer
    filterset_fields = ["section","teacher","day","academic_year"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsSchoolAdmin()]
        return [IsAuthenticated()]

    @action(detail=False, permission_classes=[IsAuthenticated])
    def section_timetable(self, request):
        s = request.query_params.get("section")
        if not s: return Response({"detail":"section required."}, status=status.HTTP_400_BAD_REQUEST)
        entries = TimetableEntry.objects.filter(section_id=s).order_by("day","time_slot__start_time")
        tt = {}
        for e in self.get_serializer(entries, many=True).data:
            tt.setdefault(e["day"], []).append(e)
        return Response(tt)
