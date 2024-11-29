from django.db import models

class PerformanceCars(models.Model):
    modelName=models.CharField(max_length=225)
    brand=models.CharField(max_length=225)
    engine=models.CharField(max_length=225)
    horsepower=models.FloatField()
    torque=models.IntegerField()
    acceleration=models.FloatField()

    