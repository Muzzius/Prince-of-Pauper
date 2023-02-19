from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """
    This class is used to create posts for the articles section of the site

    :param title: The title of the post
    :param body: The main body of text for a post
    :param date: The date the post was added, defaults to the current date
    :param author: The creator of a post, currently defaults to my name
    """
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
        """
        This allows us to track the number of comments attached to a post

        :return: The number of comments attached to a post

        :rtype: int
        """
        return Comment.objects.filter(blog_post=self).count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    This class is used to create comments for the articles section of the site

    :param blog_post: The post object the comment is attached to
    :param author: The author of the comment, taken from their username
    :param body: The body of the comment
    :param date_posted: The date the comment was added, defaults to the current date
    """
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