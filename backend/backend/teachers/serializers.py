from rest_framework import serializers
from .models import Teacher, TeacherAssignment
class TeacherAssignmentSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    class Meta: model = TeacherAssignment; fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.get_full_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    assignments = TeacherAssignmentSerializer(many=True, read_only=True)
    class Meta: model = Teacher; fields = "__all__"
