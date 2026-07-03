from rest_framework import serializers
from .models import Todo , Project

# convert data into json 
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            "owner",
            "created_at",
            "updated_at",
        ]

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'user',
            'project',
            'title',
            'details',
            'date',
            'completed',
        ]
        read_only_fields = [
            "user",
            "date",
        ]