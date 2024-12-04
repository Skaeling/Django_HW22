from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from config.settings import DEFAULT_FROM_EMAIL
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация нового пользователя'}
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в Deep Blue Store'
        message = "Благодарим за регистрацию!"
        from_email = DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
