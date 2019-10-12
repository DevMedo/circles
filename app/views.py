from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Post,Student,Circle,Replay
from .serializers import PostSerializer,StudentSerializer,CircleSerializer,ReplaySerializer
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

def addOne(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.points += 1
    post.save()
    return HttpResponse('<h1 style="color:green"> added </h1>')

def studentsPosts(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return HttpResponse(student.posts)

@csrf_exempt 
def home(request):
    if request.method == "POST":
        return HttpResponse('<h1 style="color:green">Homepage POST REQUEST ACCESS SUCCESSED</h1>')

    elif request.method == "GET":
        return HttpResponse('<h1 style="color:blue">Homepage GET REQUEST ACCESS SUCCESSED</h1>')


class CircleList(APIView):
    def get(self,request):
        circles = Circle.objects.all()
        serializer= CircleSerializer(circles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = CircleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CircleDetail(APIView):
    def get(self, request, pk):
        circle = get_object_or_404(Circle, pk=pk)
        serializer = CircleSerializer(circle)
        
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        circle = get_object_or_404(Circle, pk=pk)
        serializer = CircleSerializer(circle,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        circle = get_object_or_404(Circle, pk=pk)
        circle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################################################################

class StudentList(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer= StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data , status=status.HTTP_200_OK)
        
    def get_posts(self,request,pk):
        student = get_object_or_404(Student, pk=pk)
        posts = student.posts.objects.all()
        serializer= PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_circles(self,request,pk):
        student = get_object_or_404(Student, pk=pk)
        circles = student.circles.objects.all()
        serializer= CircleSerializer(circles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################################################################

class PostList(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializer= PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get_replay(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        replay = post.replay
        serializer = ReplaySerializer(replay)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################################################################

class ReplayList(APIView):
    def get(self,request):
        replays = Replay.objects.all()
        serializer= ReplaySerializer(Replay, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplayDetail(APIView):
    def get(self, request, pk):
        replay = get_object_or_404(Replay, pk=pk)
        serializer = ReplaySerializer(replay)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        replay = get_object_or_404(Post, pk=pk)
        serializer = ReplaySerializer(replay,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        replay = get_object_or_404(Replay, pk=pk)
        replay.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################################################################
