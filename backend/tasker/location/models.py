from django.db import models

# Create your models here. This code defines how the SQL DB is setup.
class Location(models.Model):
    profitCenterNumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zipCode = models.IntegerField()

    def __str__(self):
        return self.name
    