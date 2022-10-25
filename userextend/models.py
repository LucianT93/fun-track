from django.contrib.auth.models import User
from django.db import models

class UserExtend(User):
    is_manager=models.BooleanField()
    is_employee = models.BooleanField(default=True)
    experience = models.IntegerField(defaul=0)
    gold = models.IntegerField(default=0)
