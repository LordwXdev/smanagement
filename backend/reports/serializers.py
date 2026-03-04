from rest_framework import serializers
from .models import ReportCard
class ReportCardSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    class Meta: model = ReportCard; fields = "__all__"
    def get_student_name(self, obj): return obj.student.user.get_full_name()
