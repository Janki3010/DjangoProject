from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    PRODUCT_CATEGORY = [
        ('Electronic', 'Electronic'),
        ('Beauty', 'Beauty & Personal Care'),
        ('Games', 'Toys & Games '),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='myApp1/')
    date_added = models.DateTimeField(default=timezone.now())
    type = models.CharField(max_length=20, choices=PRODUCT_CATEGORY)


    def __str__(self):
        return self.name