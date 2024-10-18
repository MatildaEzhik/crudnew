from django.db import models

# Create your models here.

class GamePurchase(models.Model):
    game_title = models.CharField(max_length=30)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.game_title
