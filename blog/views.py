import os

from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.core.mail import send_mail


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Блог'}
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    extra_context = {'title': 'Блог'}

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save()
        if obj.views_count >= 100:
            sender = os.getenv('EMAIL_HOST_USER')
            to = os.getenv('EMAIL_HOST_USER')
            send_mail("Ваша статья популярна!",
                      f'Статья "{obj.title}" набрала {obj.views_count} просмотров!', sender, [to])
            return obj
        return obj


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'preview', 'is_published']
    template_name = 'blog/create_post.html'
    extra_context = {'title': 'Добавить новую статью'}


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body', 'preview', 'is_published']
    template_name = 'blog/create_post.html'
    extra_context = {'title': 'Редактировать статью'}


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    extra_context = {'title': 'Удаление статьи'}
    context_object_name = 'post'
    success_url = reverse_lazy('blog:posts_list')





