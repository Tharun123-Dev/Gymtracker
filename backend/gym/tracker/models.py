from django.db import models

class GymUser(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    workout = models.CharField(max_length=100)

    def __str__(self):
        return self.name

