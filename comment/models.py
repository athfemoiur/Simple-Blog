from django.db import models
from lib.models import BaseModel
from post.models import Post
from user.models import User


class Comment(BaseModel):
    text = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"({self.user} , {self.post}) --> {self.post}"
