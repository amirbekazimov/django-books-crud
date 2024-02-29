from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=100)
   # author = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   publish_date = models.DateField(null=True, blank=True)  
   user  = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
   
   # publish_date = models.DateField(null=True, blank=True)