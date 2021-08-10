from lib.models import BaseModel
from django.db import models


class Category(BaseModel):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.name)
