from post.models import Post
from post.views import PostListView


class LatestPostListView(PostListView):
    ordering = ['-created_time']
    template_name = 'home/home_page.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:5]
