from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, TeacherAssignmentViewSet
router = DefaultRouter()
router.register("teachers", TeacherViewSet)
router.register("assignments", TeacherAssignmentViewSet)
urlpatterns = [path("", include(router.urls))]
