from django.forms import ModelForm
from .models import Product, Contact
from django.core.exceptions import ValidationError

PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

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


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
