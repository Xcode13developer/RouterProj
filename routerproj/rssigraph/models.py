from django.db import models

# Create your models here.
class Point(models.Model):
    #create a point model with x y date
    id = models.AutoField(primary_key=True)
    xPerHour = models.TextField()
    RSSIy = models.FloatField()
    RSRPy = models.FloatField()
    date = models.TextField()