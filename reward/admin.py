from django.contrib import admin
from reward.models import User, ScheduledReward, RewardLog

admin.site.register(User)
admin.site.register(ScheduledReward)
admin.site.register(RewardLog)
