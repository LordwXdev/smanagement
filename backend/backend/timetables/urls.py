from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimeSlotViewSet, TimetableEntryViewSet
router = DefaultRouter()
router.register("time-slots", TimeSlotViewSet)
router.register("entries", TimetableEntryViewSet)
urlpatterns = [path("", include(router.urls))]
