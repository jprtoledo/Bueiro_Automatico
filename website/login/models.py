from django.db import models

# Create your models here.

class datalog(models.Model):
    is_active = models.CharField(max_length=50)
    device_name = models.CharField(max_length=255)
    last_occurrence = models.DateTimeField(auto_now=True)
    objects = models.Manager()


