from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    status_choices = (("Done",'done'),('Pause','pause'))
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=20,
                              choices=status_choices,
                              )
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=now)
    day = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)