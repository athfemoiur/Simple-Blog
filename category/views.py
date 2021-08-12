from django.views.generic import ListView

from category.models import Category


class CategoryPostsView(ListView):
    model = Category
    template_name = 'category/category_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Category.objects.get(id=self.kwargs['pk']).posts.all()
