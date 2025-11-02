from django.db import models
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField(default=4.0)
    delivery_time = models.CharField(max_length=20, default="30-40 mins")
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)

    def __str__(self):
        return self.name
