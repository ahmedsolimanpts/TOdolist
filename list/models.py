from django.db import models
from django.utils.timezone import now
# Create your models here.
class List(models.Model):
    status_choices = (("Done",'done'),('Pause','pause'))
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=20,
                              choices=status_choices,
                              )
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=now)
    day = models.DateField()