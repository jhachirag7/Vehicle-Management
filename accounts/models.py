from django.db import models

# Create your models here.

class Vehicle(models.Model):
    number = models.TextField(max_length=20)
    type = models.TextField(max_length=10)
    model=models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.number