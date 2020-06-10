from django.db import models

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return f"Photo no:- {self.id}"

