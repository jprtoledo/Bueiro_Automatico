from django.db import models

# Create your models here.

class datalog(models.Model):
    device_name = models.CharField(max_length=250)
    is_active = models.CharField(max_length=50)
    last_occurrence = models.DateTimeField(auto_now=True)
    objects = models.Manager()


