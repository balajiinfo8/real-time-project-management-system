from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project , Todo
from .serializers import ProjectSerializer , TodoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



# ==========================
# Project API
# ==========================
class ProjectListAPIView(APIView):

    # get all projects
    def get(self,request):
        projects =Project.objects.filter(owner=request.user).order_by("-created_at")
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    # create a new project
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailAPIView(APIView):

    # Get one Porject 
    def get(self,request,pk):
        project = get_object_or_404(Project,pk=pk,owner=request.user)

        serializer = ProjectSerializer(project)

        return Response(serializer.data)
    # Update One Project
    def put(self, request, pk):
        project = get_object_or_404(Project, pk=pk,owner=request.user)

        serializer = ProjectSerializer(
            project,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # delete on Projet
    def delete(self, request , pk):
        project = get_object_or_404(Project , pk=pk)

        project.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

# ==========================
# Todo API
# ==========================
class TodoListAPIView(APIView):

    # get all todos
    def get(self,request):
        todos = Todo.objects.filter(
            user=request.user
        ).order_by("-date")
        serializer = TodoSerializer(todos,many=True)
        return Response(serializer.data)

    # create a new todo
    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(APIView):

    # Get on Project
    def get(self , request , pk):
        todo = get_object_or_404(Todo ,pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    # Update On Project 
    def put(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(
            todo,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    # Delete On Project 
    def delete(self, request , pk):
        todo = get_object_or_404(Todo,pk=pk)
        todo.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )