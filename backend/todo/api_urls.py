from django.urls import path
from .api_views import (
    ProjectListAPIView,
    ProjectDetailAPIView,
    TodoListAPIView,
    TodoDetailAPIView,
)

urlpatterns = [
    # ==========================
    # project API 
    # ==========================
    path("projects/",ProjectListAPIView.as_view(), name="project-list"),
    path("projects/<int:pk>/",ProjectDetailAPIView.as_view(),name="project-detail"),
    # ==========================
    # Todo Urls 
    # ==========================
    path("todos/", TodoListAPIView.as_view(), name="todo-list"),
    path("todos/<int:pk>/",TodoDetailAPIView.as_view(),name="todo-detail"),
]