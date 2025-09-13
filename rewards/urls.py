from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BillViewSet, RewardViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("bills", BillViewSet)
router.register("rewards", RewardViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
