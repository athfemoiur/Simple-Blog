from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class PostListView(ListView):
    model = Post
    template_name = 'post/all_post_list.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post/update_post.html'
    fields = ('title', 'status', 'body', 'attachment')

    def get_success_url(self):
        return reverse_lazy('user-post-list', kwargs={'pk': self.request.user.pk})


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('user-post-list', kwargs={'pk': self.request.user.pk})
