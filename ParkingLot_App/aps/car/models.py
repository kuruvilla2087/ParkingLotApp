from django.db import models
from datetime import datetime
# Create your models here.

class car(models.Model):
    regno = models.CharField(max_length=200)
    color = models.CharField(max_length=200, default='nocolor')
    status = models.CharField(max_length=200, default='in')
    slot = models.IntegerField(default=999)
    level = models.IntegerField(default=999)
    Time_in = models.DateTimeField(default=datetime.now)
    Date_out = models.DateTimeField()
    Charged_price = models.IntegerField()
    def __str__(self):
        return self.regno


class parking(models.Model):
    level = models.CharField(max_length=200)
    slot1 = models.IntegerField(default=0)
    slot2 = models.IntegerField(default=0)
    slot3 = models.IntegerField(default=0)
    slot4 = models.IntegerField(default=0)
    def __str_(self):
        return self.level
