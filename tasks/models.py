from django.db import models

# Create your models here.
class Tasks(models.Model):
    name=models.CharField(max_length=50);
    description=models.TextField(blank=True);
    