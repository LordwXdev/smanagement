from rest_framework import serializers
from .models import Student, StudentDocument
class StudentDocumentSerializer(serializers.ModelSerializer):
    class Meta: model = StudentDocument; fields = "__all__"
class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.get_full_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    documents = StudentDocumentSerializer(many=True, read_only=True)
    class Meta: model = Student; fields = "__all__"
