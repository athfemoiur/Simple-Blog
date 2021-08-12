from django.urls import reverse_lazy
from django.utils.text import slugify

from lib.models import BaseModel
from django.db import models


class Category(BaseModel):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    slug = models.SlugField(null=True, editable=False, default='')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('category-posts', kwargs={'pk': self.pk})
