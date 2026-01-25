from django.db import models
from django.contrib.auth.models import User

class MemberProfile(models.Model):
    GOAL_CHOICES = [
        ('loss', 'Weight Loss'),
        ('gain', 'Muscle Gain'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES)

    is_approved = models.BooleanField(default=False)
    assigned_trainer = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='members'
    )

class DailyWorkout(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    workout_details = models.TextField()

class Attendance(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=True)
