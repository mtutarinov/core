from celery import shared_task

from reward.models import ScheduledReward, RewardLog, User

@shared_task
def apply_reward(reward_id):
    reward = ScheduledReward.objects.get(id=reward_id)
    reward.user.coins += reward.amount
    reward.user.save()
    RewardLog.objects.create(user=reward.user, amount=reward.amount)

@shared_task
def create_reward_by_user_request(user_id, amount):
    user = User.objects.get(id=user_id)
    ScheduledReward.objects.create(user=user, amount=amount)

