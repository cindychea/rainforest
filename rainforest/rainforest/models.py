from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price_in_cents = models.IntegerField(null=True)
     

    def __str__(self):
        return self.name

    def price_in_dollars(self):
        dollars = self.price_in_cents / 100
        return "${:.2f}".format(dollars)

class Review(models.Model):
    name = models.CharField(max_length = 255)
    comment = models.TextField() 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')