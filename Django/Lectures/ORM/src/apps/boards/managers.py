from django.db import models


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('comments', 'comments__created_by').filter()
