import uuid
from django.contrib.auth import get_user_model
from django.db import models
from cities.models import Region, City
# from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Category(models.Model):

    title = models.CharField(
        verbose_name='Название категории',
        max_length=256
    )
    description = models.TextField(
        verbose_name='Описание категории',
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        help_text=(
                    'Идентификатор страницы для URL; разрешены символы '
                    'латиницы, цифры, дефис и подчёркивание.'
        ),
        unique=True
    )


class Vote(models.Model):
    option = models.ForeignKey(
        'VoteOption',
        related_name='Голос',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_voted = models.DateTimeField(auto_now=True)


class VoteOption(models.Model):
    poll = models.ForeignKey("Poll", on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)


class Poll(models.Model):

    SINGLE = 'S'
    MULTIPLE = 'M'
    POLL_MODES = [
        (SINGLE, 'Single choice'),
        (MULTIPLE, 'Multiple choices'),
    ]

    COMPLETED = 'CP'
    PUBLISHED = 'PB'
    UNDER_REVIEW = 'UR'
    REJECTED = 'RJ'
    POLL_STATUSES = [
        (UNDER_REVIEW, 'На модерации'),
        (PUBLISHED, 'Опубликовано'),
        (COMPLETED, 'Завершено'),
        (REJECTED, 'Отклонено')
    ]

    OPEN = 'O'
    PRIVATE = 'P'
    POLL_TYPES = [
        (PRIVATE, 'Приватное'),
        (OPEN, 'Открытое')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=200)
    essence = models.CharField(max_length=400)
    text = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='image/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mode = models.CharField(
        max_length=1,
        choices=POLL_MODES,
        default=SINGLE
    )
    type = models.CharField(
        max_length=2,
        choices=POLL_TYPES,
        default=OPEN
    )
    category = models.ManyToManyField(
        "Category",
        verbose_name=("Категория")
    )
    all_russia = models.BooleanField(
        default=False,
        verbose_name='Вся Россия'
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Область/Регион',
        related_name='user_profiles'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Город',
        related_name='user_profiles'
    )
    status = models.CharField(
        max_length=2,
        choices=POLL_STATUSES,
        default=UNDER_REVIEW
    )

    def __str__(self):
        return self.headline
