from django.db import models
from rest_framework import serializers

from userextend.models import UserExtend


class Tasks(models.Model):
    difficulties = (('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard'))

    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    difficulty = models.CharField(choices=difficulties, max_length=10)
    experience = models.IntegerField()
    currency = models.IntegerField()

    task_creator = models.ForeignKey(UserExtend, on_delete=models.CASCADE)
    assigned_to = models.IntegerField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TaskComment(models.Model):
    creator = models.ForeignKey(UserExtend, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.creator} commented on {self.task.name}'
