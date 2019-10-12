from django.contrib import admin
from django.urls import path,re_path,include
from app import views
from django.contrib.auth.models import User
from app.models import Post
from rest_framework import routers, serializers, viewsets
from app.serializers import CircleViewSet,StudentViewSet,PostViewSet,ReplayViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'students', StudentViewSet)
router.register(r'circles', CircleViewSet)
router.register(r'replays', ReplayViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]

