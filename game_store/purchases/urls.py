from django.urls import path, include
from rest_framework.routers import DefaultRouter

from purchases.views import GamePurchaseViewSet

router = DefaultRouter()
router.register(r'game_purchases', GamePurchaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
