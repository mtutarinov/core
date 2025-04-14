from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status

from reward.serializers import UserSerializer, ScheduledRewardSerializer
from reward.models import User, ScheduledReward
from reward.tasks import create_reward_by_user_request

class ProfileView(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.get(id=self.request.user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class RewardView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ScheduledRewardSerializer

    def get_queryset(self):
        return ScheduledReward.objects.filter(user=self.request.user)

class RewardRequest(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        user_request = ScheduledReward.objects.filter(execute_at__gte=today_start)
        if user_request.exists():
            return Response({'detail': 'Вы уже запрашивали награду сегодня'}, status=status.HTTP_400_BAD_REQUEST)
        create_reward_by_user_request.apply_async((self.request.user.id, self.request.data['amount']), countdown=300)
        return Response({'detail': 'Награда зачислена'})



