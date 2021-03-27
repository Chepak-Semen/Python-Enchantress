from django.conf import settings
from django.db import models

# Create your models here.
from apps.boards.managers import TaskManager
from apps.users.models import TrelloUser
from common.models import BaseDateAuditModel


# class BoardUsers(models.Model):
#     board = models.ForeignKey(to='Board', on_delete=models.CASCADE)
#     user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Board(BaseDateAuditModel):
    name = models.CharField(max_length=36)
    # owner = models.ForeignKey(to=TrelloUser, on_delete=models.SET_NULL, null=True)
    # owner = models.ForeignKey(to='users.TrelloUser', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='boards'
    )
    users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)
    # users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='BoardUsers', blank=True)

    def __str__(self):
        return f'{self.name} ID: {self.pk}'

    class Meta:
        unique_together = (
            ("name", "owner"),
        )
        ordering = ('-created_at', )


class Task(BaseDateAuditModel):
    STATUS_OPEN = 'o'
    STATUS_ARCHIVED = 'd'
    STATUS_CHOICES = (
        (STATUS_OPEN, "Open"),
        (STATUS_ARCHIVED, "Archived"),
    )

    objects = TaskManager()

    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks'
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN,
        db_index=True
    )
    description = models.TextField(
        max_length=3000,
        null=True
    )

    def __str__(self):
        return self.name


class Comments(BaseDateAuditModel):
    message = models.TextField(max_length=1000)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='comments'
    )
    task = models.ForeignKey(
        to='Task',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return f"{self.message[:20]} BY {self.created_by.get_full_name()} ID: {self.created_by.pk}"
