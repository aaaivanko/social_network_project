from django.db import models

from django.contrib.auth import get_user_model


class Post(models.Model):
    """
    Post model
    With addition methods Like, Unlike
    """
    author = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=65)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def post_like(self, user_id):
        like, _ = self.like_set.update_or_create(user_id=user_id, defaults={'was_liked': True})
        return like

    def post_unlike(self, user_id):
        like = self.like_set.filter(user_id=user_id).first()
        if like is not None:
            like.was_liked = False
            like.save()


class Like(models.Model):
    """
    Like Model
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    was_liked = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}, likes {self.post.title}'
