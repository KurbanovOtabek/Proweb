from rest_framework import serializers

from main.models import Task, Comment
from datetime import date


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at']
        # depth = 1

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Дата выполнения задачи не может быть в прошлом :)")
        return value


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
