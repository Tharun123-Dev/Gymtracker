from django.urls import path
from .views import workouts_api

urlpatterns = [
    path('workouts/', workouts_api),
]
