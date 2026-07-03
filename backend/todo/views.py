from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView 
from rest_framework.response import Response
from .forms import TodoForm
from .models import Todo
from .models import Project
from .serializers import ProjectSerializer

# ===== LOGIN VIEW =====
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username and password")
    return render(request, 'todo/login.html')

# ===== REGISTER VIEW =====
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'todo/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, 'todo/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'todo/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'todo/register.html')


# ===== LOGOUT VIEW =====
def logout_view(request):
    logout(request)
    return redirect('login')


# ===== HOME / INDEX VIEW =====
@login_required
def index(request):
    item_list = Todo.objects.filter(user=request.user).order_by('-date')
    pending_count = item_list.filter(completed=False).count()
    completed_count = item_list.filter(completed=True).count()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect('home')
    else:
        form = TodoForm()

    pages = {
        "forms": form,
        "list": item_list,
        "title": "TODO ITEM",
        "pending_count": pending_count,
        "completed_count": completed_count,
    }
    return render(request, 'todo/index.html', pages)


# ===== EDIT TASK VIEW =====
@login_required
def edit_task(request, item_id):
    task = get_object_or_404(Todo, id=item_id, user=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('home')
    else:
        form = TodoForm(instance=task)

    return render(request, 'todo/edit.html', {
        'form': form,
        'task': task
    })


# ===== DELETE TASK VIEW =====
@login_required
def delete_task(request, item_id):
    task = get_object_or_404(Todo, id=item_id, user=request.user)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('home')


# ===== REMOVE VIEW =====
@login_required
def remove(request, item_id):
    task = get_object_or_404(Todo, id=item_id, user=request.user)
    task.delete()
    messages.info(request, "Item removed!")
    return redirect('home')


# ===== TOGGLE COMPLETE VIEW =====
@login_required
def toggle_complete(request, item_id):
    task = get_object_or_404(Todo, id=item_id, user=request.user)
    task.completed = not task.completed
    task.save()

    if task.completed:
        messages.success(request, f"✅ '{task.title}' marked as complete!")
    else:
        messages.info(request, f"🔄 '{task.title}' marked as pending.")
    return redirect('home')