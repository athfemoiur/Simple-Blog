from category.models import Category
from django import template

register = template.Library()


@register.simple_tag
def get_all_categories():
    return Category.objects.all()
