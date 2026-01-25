from django.urls import path
from .views import member_api

urlpatterns = [
    path('api/member/<int:member_id>/', member_api),
]
