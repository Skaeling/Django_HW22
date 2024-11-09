from django.forms import ModelForm
from .models import Category, Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]
