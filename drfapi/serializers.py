from rest_framework import serializers

from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'logo_url', 'description', 'order', 'tasks']
