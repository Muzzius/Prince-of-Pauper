from django.views.generic import DetailView
from .models import Comment
from .forms import CommentForm


# Create your views here.
class PostDetail(DetailView):
    """
    Creates an object as a subclass of DetailView to display posts on the website.
    """
    def get_context_data(self, **kwargs):
        """
        This method pulls the data for a post object to display it on the site.
        storing it in a dictionary

        :return: Returns the context data for a post including attached comments if there are any.
        If the user is authenticated it will also include the commentForm to allow them to leave
        a comment.
        """
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            blog_post=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        """
        This method receives the context data from the CommentForm and post it
        from within the class based PostDetail view

        :return: POSTs the new comment data to our server to be saved in our database
        """
        new_comment = Comment(body=request.POST.get('body'),
                              author=self.request.user,
                              blog_post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
