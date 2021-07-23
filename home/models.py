from django.db import models

# Create your models here.
class contactReport(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=13)
    subject = models.CharField(max_length=64)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)