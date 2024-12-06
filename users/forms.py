from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.core.exceptions import ValidationError

from .models import User


class CustomUserCreationForm(UserCreationForm):
    usable_password = None
    fields_group = {'main': (
        'email', 'username', 'first_name', 'last_name', 'phone_number', 'country', 'avatar', 'password1',
        'password2'),
    }

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
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = 'Введите пароль еще раз для подтверждения.'
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset('', *self.fields_group['main'], css_class='form-control border-info', style='font-size: 13px;'),
            Div(Submit('submit', '{% if object %}Сохранить{% else %}Зарегистрироваться{% endif %}',
                       css_class='btn btn-lg btn-info'),
                css_class='col-12 mt-2 text-center'),
        )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if not isinstance(avatar, str):
            if avatar.size > 5 * 1024 * 1024:
                raise ValidationError("Файл превышает допустимый размер ( > 5mb )")
            return avatar
        else:
            return avatar


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('username', css_class='form-control border-info'),
            Field('password', css_class='form-control border-info'),
            Div(Submit('submit', 'Войти', css_class='btn btn-lg btn-info'), css_class='col-12 mt-3 text-center'),
        )


class CustomUpdateForm(UserChangeForm, CustomUserCreationForm):
    password = None

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'country', 'avatar',)
        labels = {
            'phone_number': 'Номер телефона',
            'country': 'Страна проживания',
            'avatar': 'Аватар'
        }


