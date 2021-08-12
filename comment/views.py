from django.urls import reverse_lazy
from django.views.generic import CreateView

from comment.models import Comment


class CreateCommentView(CreateView):
    model = Comment
    fields = ('text',)
    template_name = 'comment/add_comment.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
