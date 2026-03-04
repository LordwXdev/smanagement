from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, NotificationViewSet, AnnouncementViewSet
router = DefaultRouter()
router.register("messages", MessageViewSet, basename="message")
router.register("notifications", NotificationViewSet, basename="notification")
router.register("announcements", AnnouncementViewSet)
urlpatterns = [path("", include(router.urls))]
