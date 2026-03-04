from rest_framework import serializers
from .models import Attendance
class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    class Meta: model = Attendance; fields = "__all__"; read_only_fields = ["marked_by"]
    def get_student_name(self, obj): return obj.student.user.get_full_name()
    def create(self, validated_data):
        validated_data["marked_by"] = self.context["request"].user
        return super().create(validated_data)
class BulkAttendanceSerializer(serializers.Serializer):
    section_id = serializers.UUIDField()
    date = serializers.DateField()
    records = serializers.ListField(child=serializers.DictField())
