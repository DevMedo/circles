from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from .models import Circle,Student,Post,Replay

# Serializers define the API representation.
class ReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = '__all__'
# Serializers define the API representation.

# ViewSets define the view behavior.
class ReplayViewSet(viewsets.ModelViewSet):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer

class PostSerializer(serializers.ModelSerializer):
    replays = ReplaySerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# Serializers define the API representation.
class CircleSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Circle
        fields = '__all__'

# ViewSets define the view behavior.
class CircleViewSet(viewsets.ModelViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer


    # Serializers define the API representation.
class StudentSerializer(serializers.ModelSerializer):
    circles = CircleSerializer(many=True, read_only=True)
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

# ViewSets define the view behavior.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer