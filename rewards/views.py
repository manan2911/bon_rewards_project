from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import User, Bill, Reward
from .serializers import UserSerializer, BillSerializer, RewardSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    @action(detail=True, methods=["post"])
    def pay(self, request, pk=None):
        """Mark bill as paid and check for rewards"""
        bill = self.get_object()
        if bill.status == "PAID":
            return Response({"message": "Bill already paid"}, status=status.HTTP_400_BAD_REQUEST)

        bill.payment_date = timezone.now().date()
        bill.status = "PAID"
        bill.save()

        # ✅ Check last 3 bills
        last_3_bills = Bill.objects.filter(user=bill.user, status="PAID").order_by("-due_date")[:3]
        if len(last_3_bills) == 3 and all(b.is_paid_on_time() for b in last_3_bills):
            reward = Reward.objects.create(user=bill.user)
            return Response({
                "message": "Bill paid successfully. Reward unlocked!",
                "reward": RewardSerializer(reward).data
            })

        return Response({"message": "Bill paid successfully. No reward earned this time."})


class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
