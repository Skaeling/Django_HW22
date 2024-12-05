from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = (
            'email', 'username', 'first_name', 'last_name', 'phone_number', 'country', 'avatar', 'password1',
            'password2')
        labels = {
            'phone_number': 'Номер телефона',
            'country': 'Страна проживания',
            'avatar': 'Аватар'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Введите надежный пароль.'
        self.fields['password2'].help_text = 'Введите пароль еще раз для подтверждения.'
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number
