from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, HTML, Submit
from django.forms import ModelForm
from .models import Product, Contact
from django.core.exceptions import ValidationError
from config.settings import PROHIBITED_WORDS, VALID_IMAGE_EXTENSIONS


def valid_url_extension(url, extension_list=None):
    if extension_list is None:
        extension_list = VALID_IMAGE_EXTENSIONS
    return any([url.endswith(e) for e in extension_list])


class CustomForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get('image'):
            self.fields['image'].help_text = 'Изображение размером не более 5 мб'
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset('', *self.fields, css_class='form-control border-info', style='font-size: 18px;'),
            Row(
                Column(HTML('<a class="btn btn-info form-group" href="javascript: history.back()">Назад</a>')),
                Column(Submit('submit', '{% if object %}Сохранить{% else %}Создать{% endif %}', css_class='btn btn-info form-group')),
                css_class='col-12 mt-2 d-flex justify-content-center text-center'
            )
        )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in PROHIBITED_WORDS:
            if word in name.lower():
                raise ValidationError(f'Использовано запрещенное слово "{word}"! Введите другое название.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in PROHIBITED_WORDS:
            if word in description.lower():
                raise ValidationError(f'Использовано запрещенное слово "{word}"! Откорректируйте описание.')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        elif price == 0:
            raise ValidationError('Цена не может быть равна нулю')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        # Если продукт редактируется, и новое изображение не загружают
        if not isinstance(image, str):
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Файл превышает допустимый размер ( > 5mb )")
            # Если продукт редактируется, и загружают новое изображение
            if hasattr(image, 'url'):
                if not valid_url_extension(image.url):
                    raise ValidationError(
                        "Неподходящий формат файла. Выберите из списка разрешенных: (.jpg/.jpeg/.png)")
            # Если создается новый продукт и изображение загружают
            elif not valid_url_extension(image.image.format.lower()):
                raise ValidationError("Неподходящий формат файла. Выберите из списка разрешенных: (.jpg/.jpeg/.png)")
            return image
        else:
            return image


class ProductForm(CustomForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'is_published', 'owner')


class ProductModeratorOwnerForm(CustomForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'owner')


class ProductModeratorForm(CustomForm):
    class Meta:
        model = Product
        fields = ('is_published', )


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
