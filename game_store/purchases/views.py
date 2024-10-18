from django.shortcuts import render
from rest_framework import viewsets

from purchases.models import GamePurchase
from purchases.serializers import GamePurchaseSerializer


# Create your views here.


class GamePurchaseViewSet(viewsets.ModelViewSet):
    queryset = GamePurchase.objects.all()
    serializer_class = GamePurchaseSerializer
