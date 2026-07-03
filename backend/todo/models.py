from django.db import models
from django.contrib.auth.models import User

# The Project Management System 
class Project(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="projects"
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # return project name 
    def __str__(self):
        return self.name 
    

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project,
            on_delete=models.CASCADE,
            related_name="todos",
            null=True,
            blank=True
        )
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
  

    def __str__(self):
        return self.title


