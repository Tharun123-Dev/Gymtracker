from django.urls import path
from .views import gym_users

urlpatterns = [
    path('api/gym-users/', gym_users),
]

