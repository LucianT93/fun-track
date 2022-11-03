from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)
    experience = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile/', blank=True, null=True, default='profile/user-default.png')

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.first_name}  {self.last_name}'