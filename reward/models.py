from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    coins = models.IntegerField(default=0)


class ScheduledReward(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards')
    amount = models.IntegerField()
    execute_at = models.DateTimeField(auto_now_add=True)


class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)
