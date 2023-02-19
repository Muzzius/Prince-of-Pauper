from django.views.generic import DetailView
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            blog_post=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'),
                              author=self.request.user,
                              blog_post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
