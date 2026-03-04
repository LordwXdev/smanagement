from rest_framework import serializers
from .models import TimeSlot, TimetableEntry
class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta: model = TimeSlot; fields = "__all__"
class TimetableEntrySerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    teacher_name = serializers.CharField(source="teacher.get_full_name", read_only=True)
    class Meta: model = TimetableEntry; fields = "__all__"
