from django.urls import path, re_path
from . import views
from . import serializers
from rest_framework import routers

urlpatterns = [
    path('', views.home,name="homepage"),
]