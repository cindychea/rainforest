from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price_in_cents = models.IntegerField(null=True)

    def __str__(self):
        return self.name