from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from reward.views import ProfileView, RewardView, RewardRequest

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/profile/', ProfileView.as_view()),
    path('api/rewards/', RewardView.as_view()),
    path('api/rewards/request/', RewardRequest.as_view())
]