from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Bill(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bills")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")

    def is_paid_on_time(self):
        """Check if this bill is paid on or before due date"""
        if self.payment_date:
            return self.payment_date <= self.due_date
        return False

    def __str__(self):
        return f"Bill {self.id} for {self.user.name}"


class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rewards")
    reward_type = models.CharField(max_length=100, default="$10 Amazon Gift Card")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.reward_type} → {self.user.name}"
