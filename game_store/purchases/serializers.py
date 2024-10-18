from rest_framework import serializers

from purchases.models import GamePurchase


class GamePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePurchase
        fields = '__all__'
