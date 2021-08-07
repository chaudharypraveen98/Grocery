from django.contrib.auth.models import User
from django.db import models

ITEM_STATUS = (
    (1, "Bought"),
    (2, "NOT AVAILABLE"),
    (3, "PENDING")
)


class GroceryList(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    item_name = models.CharField(max_length=30)
    item_quantity = models.CharField(max_length=20)
    item_status = models.IntegerField(choices=ITEM_STATUS, default=3)
    date = models.DateField()

    def __str__(self):
        return self.item_name + self.item_quantity
