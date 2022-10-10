from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.PositiveIntegerField(
        unique=True, 
        validators = [
        MaxValueValidator(101, "Quantity value cannot be greater than 100.")
        ]
    )
