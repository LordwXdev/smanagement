from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, StudentDocumentViewSet
router = DefaultRouter()
router.register("students", StudentViewSet)
router.register("documents", StudentDocumentViewSet)
urlpatterns = [path("", include(router.urls))]
