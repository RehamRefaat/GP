from django.db import models
from django.contrib.auth.models import User

class Operation(models.Model):
    Input = models.ImageField(upload_to='input')
    Output = models.CharField(max_length=255)
    CNV=models.CharField(max_length=8,default="0")
    DME=models.CharField(max_length=8,default="0")
    Drusen=models.CharField(max_length=8,default="0")
    NormalOCT = models.CharField(max_length=8, default="0")
    MacularDegeneration = models.CharField(max_length=8, default="0")
    Cataract = models.CharField(max_length=8, default="0")
    Diabetes = models.CharField(max_length=8, default="0")
    Glaucoma = models.CharField(max_length=8, default="0")
    Hypertension = models.CharField(max_length=8, default="0")
    PathologicalMyopia = models.CharField(max_length=8, default="0")
    NormalMacular = models.CharField(max_length=8, default="0")
    Other = models.CharField(max_length=8, default="0")
    ProcessName = models.CharField(max_length=65, default="OCT")
    Date = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)
    def __str__(self):
        return str(self.pk)