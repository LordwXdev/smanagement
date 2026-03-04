from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from accounts.permissions import IsSchoolAdmin
from .models import Message, Notification, Announcement
from .serializers import MessageSerializer, NotificationSerializer, AnnouncementSerializer
class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer; permission_classes = [IsAuthenticated]
    def get_queryset(self):
        u = self.request.user
        return Message.objects.filter(sender=u) | Message.objects.filter(recipient=u)
    @action(detail=False)
    def inbox(self, r): return Response(self.get_serializer(Message.objects.filter(recipient=r.user), many=True).data)
    @action(detail=True, methods=["post"])
    def mark_read(self, r, pk=None):
        m = self.get_object(); m.is_read=True; m.read_at=timezone.now(); m.save()
        return Response({"detail":"Read."})
class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer; permission_classes = [IsAuthenticated]
    def get_queryset(self): return Notification.objects.filter(user=self.request.user)
    @action(detail=False, methods=["post"])
    def mark_all_read(self, r):
        Notification.objects.filter(user=r.user, is_read=False).update(is_read=True)
        return Response({"detail":"Done."})
    @action(detail=False)
    def unread_count(self, r): return Response({"count": Notification.objects.filter(user=r.user, is_read=False).count()})
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.filter(is_active=True); serializer_class = AnnouncementSerializer
    def get_permissions(self):
        if self.action in ["create","update","partial_update","destroy"]: return [IsSchoolAdmin()]
        return [IsAuthenticated()]
