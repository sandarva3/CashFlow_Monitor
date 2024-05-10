from django.db import models
from Trace.models import CustomUser

class Event(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.TextField(max_length=125)
    wintegrate = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Eventitems(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(default=None, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name
