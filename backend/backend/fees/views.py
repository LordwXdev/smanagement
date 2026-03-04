from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from accounts.permissions import IsAccountant, IsAdminOrReadOnly, IsAccountantOrStudent
from .models import FeeStructure, Invoice, Payment
from .serializers import FeeStructureSerializer, InvoiceSerializer, PaymentSerializer

class FeeStructureViewSet(viewsets.ModelViewSet):
    queryset = FeeStructure.objects.all(); serializer_class = FeeStructureSerializer; permission_classes = [IsAdminOrReadOnly]

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    filterset_fields = ["student","status"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAccountant()]
        return [IsAccountantOrStudent()]

    def get_queryset(self):
        user = self.request.user
        qs = Invoice.objects.select_related("student__user").all()
        if user.role == "student":
            qs = qs.filter(student__user=user)
        elif user.role == "parent":
            qs = qs.filter(student__parent=user)
        return qs

    @action(detail=False)
    def summary(self, request):
        billed = Invoice.objects.aggregate(t=Sum("amount"))["t"] or 0
        collected = Invoice.objects.aggregate(t=Sum("amount_paid"))["t"] or 0
        return Response({"total_billed": billed, "total_collected": collected, "pending": billed-collected})

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all(); serializer_class = PaymentSerializer; permission_classes = [IsAccountant]
