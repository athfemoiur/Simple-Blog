from django.views.generic import ListView

from category.models import Category


class CategoryPostsView(ListView):
    model = Category
    template_name = 'category/category_posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['category'] = Category.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Category.objects.get(id=self.kwargs['pk']).posts.filter(status=1)
