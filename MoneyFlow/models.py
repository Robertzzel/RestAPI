from django.db import models

# Create your models here.

class Produs(models.Model):
    nume = models.CharField(max_length=255)
    pret = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return self.nume