from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=121)
    owner = models.CharField(max_length=121)
    created_at = models.DateTimeField(auto_now=True)
    finish_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
