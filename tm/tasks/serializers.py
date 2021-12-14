from django.contrib.auth.models import User
from rest_framework import serializers

from tasks.models import TasksModel


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksModel
        exclude = ()

    executor = UserSerializer(many=False)
    author = UserSerializer(many=False)


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksModel
        fields = ['title', 'description', 'executor']


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksModel
        exclude = ('id',)
