from django.db.models.signals import post_save
from django.dispatch import receiver

from reward.models import ScheduledReward
from reward.tasks import apply_reward

@receiver(post_save, sender=ScheduledReward)
def schedule_reward(sender, instance, created, **kwargs):
    if created:
        apply_reward.delay(instance.id)
