from django.db import models
from django.core.exceptions import ValidationError

def validate_quantity_range(value):
    if not(0 <= value <=100):
        raise ValidationError("Quantity must be between 0 and 100")

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(blank=True, max_length=120)
    quantity = models.IntegerField(validators=[validate_quantity_range])