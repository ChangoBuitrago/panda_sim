from django.db import models

class Read(models.Model):
    active_power = models.FloatField(blank=True, null=True)
    reactive_power = models.FloatField(blank=True, null=True) 
    latest_status = models.DateTimeField(auto_now=True, blank=True, null=True)