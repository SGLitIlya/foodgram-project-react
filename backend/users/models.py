from django.contrib.auth.models import AbstractUser
from django.db import models

from core import constants


class User(AbstractUser):
    """Модель пользователя."""

    email = models.EmailField(
        'Электронная почта',
        unique=True,
    )

    first_name = models.CharField(
        'Имя',
        max_length=constants.FIRST_NAME_MAX_LEN,
    )

    last_name = models.CharField(
        'Фамилия',
        max_length=constants.LAST_NAME_MAX_LEN,
    )

    followers = models.ManyToManyField(
        'self',
        through='FollowRelationship',
        related_name='following',
        symmetrical=False,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class FollowRelationship(models.Model):
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+'
    )
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+'
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                name='%(app_label)s_%(class)s_unique_relationships',
                fields=['from_user', 'to_user'],
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_prevent_self_follow',
                check=~models.Q(from_user=models.F('to_user')),
            ),
        ]

    def __str__(self):
        return f'Подписка от {self.from_user} на {self.to_user}.'
