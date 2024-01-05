from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)


class Order(models.Model):
    items = models.ManyToManyField(Item)


class Discount(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Tax(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
