from django.db import models
from location.models import Location
import datetime

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    profitCenterNumber = models.ForeignKey(Location, on_delete=models.CASCADE)
    task = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.profitCenterNumber} | {self.task}'
   