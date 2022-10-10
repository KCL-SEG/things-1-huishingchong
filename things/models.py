from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        unique=False, 
        validators = [
            MinValueValidator(0, "Quantity value must be greater than 0."),
            MaxValueValidator(100, "Quantity value cannot be greater than 100.")
        ]
    )
