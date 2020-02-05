from django.db import models

class Bond(models.Model):
    isin = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    ytm = models.FloatField(default=0)
    tenor = models.IntegerField(default=10)

    def __str__(self):
        return self.name