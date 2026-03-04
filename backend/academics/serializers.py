from rest_framework import serializers
from .models import AcademicYear, Grade, Section, Subject, ExamType, Exam, StudentGrade
class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta: model = AcademicYear; fields = "__all__"
class GradeSerializer(serializers.ModelSerializer):
    class Meta: model = Grade; fields = "__all__"
class SectionSerializer(serializers.ModelSerializer):
    grade_name = serializers.CharField(source="grade.name", read_only=True)
    class Meta: model = Section; fields = "__all__"
class SubjectSerializer(serializers.ModelSerializer):
    class Meta: model = Subject; fields = "__all__"
class ExamTypeSerializer(serializers.ModelSerializer):
    class Meta: model = ExamType; fields = "__all__"
class ExamSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    class Meta: model = Exam; fields = "__all__"
class StudentGradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.get_full_name", read_only=True)
    percentage = serializers.ReadOnlyField()
    letter_grade = serializers.ReadOnlyField()
    grade_point = serializers.ReadOnlyField()
    class Meta: model = StudentGrade; fields = "__all__"; read_only_fields = ["graded_by"]
    def create(self, validated_data):
        validated_data["graded_by"] = self.context["request"].user
        return super().create(validated_data)
