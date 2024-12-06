from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import CustomLoginForm
from .views import RegisterView, UserDetailView, UserUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=CustomLoginForm),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),

]
