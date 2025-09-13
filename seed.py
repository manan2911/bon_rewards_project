from rewards.models import User, Bill, Reward
from django.utils import timezone
from datetime import timedelta

# Clear old data
User.objects.all().delete()
Bill.objects.all().delete()
Reward.objects.all().delete()

# User 1: Has overdue bills
u1 = User.objects.create(name="Late Payer", email="late@example.com")
for i in range(3):
    Bill.objects.create(
        user=u1,
        amount=100 + i*50,
        due_date=timezone.now() - timedelta(days=10*(i+1)),
        payment_date=timezone.now() + timedelta(days=5),  # paid late
    )

# User 2: Has bills pending
u2 = User.objects.create(name="Pending Payer", email="pending@example.com")
for i in range(3):
    Bill.objects.create(
        user=u2,
        amount=200 + i*50,
        due_date=timezone.now() + timedelta(days=10*(i+1)),
    )

# User 3: Qualified for reward
u3 = User.objects.create(name="On-Time Payer", email="ontime@example.com")
for i in range(3):
    Bill.objects.create(
        user=u3,
        amount=150 + i*50,
        due_date=timezone.now() - timedelta(days=10*(i+1)),
        payment_date=timezone.now() - timedelta(days=10*(i+1)),  # paid on time
    )
Reward.objects.create(user=u3, reward_type="$10 Amazon Gift Card")

print("✅ Seed data created successfully!")
