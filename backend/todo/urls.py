from django.urls import path
from . import views
from .api_views import ProjectListAPIView , TodoListAPIView

urlpatterns = [

    # ==========================
    # Authentication
    # ==========================
    path('', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),

    # ==========================
    # Template Views
    # ==========================
    path('home/', views.index, name="home"),
    path('edit/<int:item_id>/', views.edit_task, name='edit'),
    path('delete/<int:item_id>/', views.delete_task, name='delete'),
    path('remove/<int:item_id>/', views.remove, name='remove'),
    path('toggle/<int:item_id>/', views.toggle_complete, name='toggle'),
]