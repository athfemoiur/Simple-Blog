from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView

from post.forms import PostForm
from post.models import Post


class AddPostView(FormView):
    form_class = PostForm
    template_name = 'post/add_post.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('user-post-list', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect(self.get_success_url())


class UserPostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    extra_context = {'access': False}

    def get_queryset(self):
        queryset = super().get_queryset().filter(author_id=self.kwargs['pk'])
        if not self.extra_context['access']:
            queryset = queryset.filter(status=1)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        self.extra_context['access'] = False
        if self.request.user.pk == self.kwargs['pk']:
            self.extra_context['access'] = True
        return super().dispatch(request, *args, **kwargs)


class PostListView(ListView):
    model = Post
    template_name = 'post/all_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.prefetch_related('categories').filter(status=1)
        return query_set


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post/update_post.html'
    fields = ('title', 'status', 'body', 'attachment', 'categories')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if self.kwargs['pk'] not in [post.pk for post in self.request.user.posts.all()]:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('user-post-list', kwargs={'pk': self.request.user.pk})


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    context_object_name = 'post'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if self.kwargs['pk'] not in [post.pk for post in self.request.user.posts.all()]:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('user-post-list', kwargs={'pk': self.request.user.pk})


@require_GET
def search_post(request):
    title = request.GET['title']
    posts = Post.objects.filter(status=1, title__icontains=title)
    return render(request, 'post/search_posts.html', {'title': title, 'posts': posts})
