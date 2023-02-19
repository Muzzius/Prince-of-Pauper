from django.views.generic import ListView
from django.urls import path
from .models import Post
from . import views

app_name = 'blog'
urlpatterns = [
    path('',
         ListView.as_view(
             queryset=
             Post.objects.all().order_by("-date")[:25],
             template_name="blog.html"
         ), name="blog"
         ),

    path('<int:pk>/',
         views.PostDetail.as_view(
             model=Post,
             template_name="post.html"
         ), name="post"
         ),
]
