from django.db import models

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
    task_textbox = models.TextField(max_length=500, blank=True, null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
