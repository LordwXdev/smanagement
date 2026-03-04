import uuid
from django.db import models
from django.conf import settings
class FeeStructure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    grade = models.ForeignKey("academics.Grade", on_delete=models.CASCADE, related_name="fee_structures")
    academic_year = models.ForeignKey("academics.AcademicYear", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()
    description = models.TextField(blank=True)
class Invoice(models.Model):
    class Status(models.TextChoices):
        PENDING="pending","Pending"; PARTIAL="partial","Partial"; PAID="paid","Paid"; OVERDUE="overdue","Overdue"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_number = models.CharField(max_length=30, unique=True)
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name="invoices")
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING)
    due_date = models.DateField()
    issued_date = models.DateField(auto_now_add=True)
    @property
    def balance(self): return self.amount - self.amount_paid
class Payment(models.Model):
    class Method(models.TextChoices):
        CASH="cash","Cash"; BANK="bank_transfer","Bank Transfer"; CARD="card","Card"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=Method.choices)
    transaction_id = models.CharField(max_length=100, blank=True)
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        inv = self.invoice
        inv.amount_paid = sum(p.amount for p in inv.payments.all())
        inv.status = "paid" if inv.amount_paid >= inv.amount else ("partial" if inv.amount_paid > 0 else "pending")
        inv.save()
