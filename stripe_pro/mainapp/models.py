from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='item name', max_length=128, unique=True)
    description = models.TextField(verbose_name='description of the item', blank=True)
    price = models.DecimalField(verbose_name='price of the item', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name