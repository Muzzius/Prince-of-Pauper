from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # Default behaviour - Django creates primary keys for you
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=140, default="Murray Bosworth")

    class Meta:
        ordering = ['-date']

    # Returns the number of comments on a post
    @property
    def number_of_comments(self):
        return Comment.objects.filter(blog_post=self).count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    # Create a class so users can add comments to blog posts
    # Tutorial found at https://dev.to/radualexandrub/how-to-create-a-comment-section-for-your-django-blog-3egp
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)