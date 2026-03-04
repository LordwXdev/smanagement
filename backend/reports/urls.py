from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportCardViewSet
router = DefaultRouter()
router.register("report-cards", ReportCardViewSet)
urlpatterns = [path("", include(router.urls))]
