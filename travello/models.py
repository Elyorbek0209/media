from django.db import models

# Create your models here.

#Here our Destination Class

class Destination(models.Model):

 # Here we'll create 5 Variables below

   name = models.CharField(max_length=30)

   img = models.ImageField(upload_to='pics')

   desc = models.TextField()

   price = models.IntegerField()

   offer = models.BooleanField(default=False)














