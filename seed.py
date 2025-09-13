import os
import django
from datetime import date, timedelta

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bon_rewards.settings")
django.setup()

from rewards.models import User, Bill, Reward


def run():
    # Clear old data
    User.objects.all().delete()
    Bill.objects.all().delete()
    Reward.objects.all().delete()

    today = date.today()

    # 1️⃣ User who has NOT paid bills on time
    late_user = User.objects.create(name="Late Payer", email="late@example.com")
    bill1 = Bill.objects.create(
        user=late_user, amount=1000, due_date=today - timedelta(days=5),
        payment_date=today, status="PAID"  # Paid late
    )
    bill2 = Bill.objects.create(
        user=late_user, amount=1200, due_date=today - timedelta(days=3),
        payment_date=None, status="PENDING"  # Not paid yet
    )
    bill3 = Bill.objects.create(
        user=late_user, amount=1500, due_date=today + timedelta(days=2)
    )

    # 2️⃣ User with 3 unpaid bills (like your current one)
    pending_user = User.objects.create(name="Pending Payer", email="pending@example.com")
    Bill.objects.create(user=pending_user, amount=1100, due_date=today + timedelta(days=2))
    Bill.objects.create(user=pending_user, amount=1300, due_date=today + timedelta(days=5))
    Bill.objects.create(user=pending_user, amount=1400, due_date=today + timedelta(days=8))

    # 3️⃣ User who should instantly get a reward (all last 3 bills paid on time)
    good_user = User.objects.create(name="OnTime Payer", email="ontime@example.com")
    Bill.objects.create(
        user=good_user, amount=900,
        due_date=today - timedelta(days=10),
        payment_date=today - timedelta(days=10), status="PAID"
    )
    Bill.objects.create(
        user=good_user, amount=1000,
        due_date=today - timedelta(days=7),
        payment_date=today - timedelta(days=7), status="PAID"
    )
    Bill.objects.create(
        user=good_user, amount=1100,
        due_date=today - timedelta(days=3),
        payment_date=today - timedelta(days=3), status="PAID"
    )

    # Trigger reward for good_user
    Reward.objects.create(user=good_user)

    print("✅ Seed data created:")
    print(" - 1 user with late/missed bills")
    print(" - 1 user with 3 pending bills")
    print(" - 1 user with 3 on-time payments (reward unlocked)")


if __name__ == "__main__":
    run()
