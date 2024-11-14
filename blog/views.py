from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Блог'}
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    extra_context = {'title': 'Блог'}


# class CreatePostView(CreateView):
#     model = Post
#     template_name = 'blog/create_post.html'
#     context_object_name = 'post'
