from django.db import models
from django.utils.text import slugify
from category.models import Category
from lib.models import BaseModel
from user.models import User


class Post(BaseModel):
    DRAFT = 0
    PUBLISHED = 1
    ARCHIVED = 2

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (ARCHIVED, 'Archived')
    )

    author = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', blank=True, editable=False)
    body = models.TextField()
    categories = models.ManyToManyField(Category, related_name='posts')
    attachment = models.FileField(upload_to='posts/attachments/', null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
