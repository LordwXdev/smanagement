from rest_framework import serializers
from .models import Message, Notification, Announcement
class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source="sender.get_full_name", read_only=True)
    class Meta: model = Message; fields = "__all__"; read_only_fields = ["sender","is_read"]
    def create(self, validated_data):
        validated_data["sender"] = self.context["request"].user
        return super().create(validated_data)
class NotificationSerializer(serializers.ModelSerializer):
    class Meta: model = Notification; fields = "__all__"
class AnnouncementSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.get_full_name", read_only=True)
    class Meta: model = Announcement; fields = "__all__"; read_only_fields = ["author"]
    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
