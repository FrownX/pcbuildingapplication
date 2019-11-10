from django.db import models
from django.conf import settings
from PIL import Image
# Create your models here.

class Cpu(models.Model):
    partname=models.CharField(max_length=120)
    price=models.CharField(max_length=120,null=True)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.partname