from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeeStructureViewSet, InvoiceViewSet, PaymentViewSet
router = DefaultRouter()
router.register("fee-structures", FeeStructureViewSet)
router.register("invoices", InvoiceViewSet)
router.register("payments", PaymentViewSet)
urlpatterns = [path("", include(router.urls))]
