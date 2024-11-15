from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "blog"

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('posts/create/', PostCreateView.as_view(), name="create_post"),
    path("posts/update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("posts/delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),

]