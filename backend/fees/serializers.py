from rest_framework import serializers
from .models import FeeStructure, Invoice, Payment
class FeeStructureSerializer(serializers.ModelSerializer):
    class Meta: model = FeeStructure; fields = "__all__"
class PaymentSerializer(serializers.ModelSerializer):
    class Meta: model = Payment; fields = "__all__"; read_only_fields = ["received_by"]
    def create(self, validated_data):
        validated_data["received_by"] = self.context["request"].user
        return super().create(validated_data)
class InvoiceSerializer(serializers.ModelSerializer):
    balance = serializers.ReadOnlyField()
    payments = PaymentSerializer(many=True, read_only=True)
    class Meta: model = Invoice; fields = "__all__"
