from django.contrib import admin

from tasks.models import Tasks, TaskComment

admin.site.register(Tasks)
admin.site.register(TaskComment)
