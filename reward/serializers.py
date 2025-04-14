from rest_framework import serializers

from reward.models import User, ScheduledReward

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'coins')

class ScheduledRewardSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduledReward
        fields = ('user', 'amount', 'execute_at')