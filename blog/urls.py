from django.urls import path
from .views import PostListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name="post_detail"),

]