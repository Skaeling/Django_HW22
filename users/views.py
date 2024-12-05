from django.contrib import messages
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from config.settings import DEFAULT_FROM_EMAIL

from .forms import CustomUpdateForm, CustomUserCreationForm
from .models import User


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация нового пользователя'}
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        messages.success(self.request, "Регистрация прошла успешно!")
        return redirect(self.success_url)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в Deep Blue Store'
        message = "Благодарим за регистрацию!"
        from_email = DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'
    extra_context = {'title': 'Мой профиль'}


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = CustomUpdateForm
    template_name = 'users/register.html'
    context_object_name = 'user'
    success_message = "Профиль успешно обновлен!"
    extra_context = {'title': 'Редактировать профиль'}

    def get_success_url(self, **kwargs):
        return reverse("users:user_detail", kwargs={'pk': self.object.pk})
