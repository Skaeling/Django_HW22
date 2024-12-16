from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import (ContactForm, ProductForm, ProductModeratorForm,
                    ProductModeratorOwnerForm)
from .models import Category, Contact, Product
from .services import get_products


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    extra_context = {'title': 'Главная'}
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    extra_context = {'title': 'Описание товара'}


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    context_object_name = 'product'
    extra_context = {'title': 'Добавить товар'}

    def form_valid(self, form):
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = self.request.user
            product.save()
            print(f'Добавлен новый продукт: "{form.instance.name}". Владелец:"{form.instance.owner}"')

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    context_object_name = 'product'
    extra_context = {'title': 'Редактировать товар'}

    def get_form_class(self):
        product = self.get_object(queryset=None)
        if product.owner == self.request.user and self.request.user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorOwnerForm
        elif product.owner == self.request.user:
            return ProductForm
        elif self.request.user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied

    def form_valid(self, form):
        if form.is_valid():
            print(f'Отредактирован продукт: "{form.instance.name}"')

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    context_object_name = 'product'
    extra_context = {'title': 'Удалить товар'}
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user
        if not user.has_perm('catalog.can_delete_product') and user != product.owner:
            raise PermissionDenied
        return product


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    extra_context = {'title': 'Контакты'}
    template_name = 'catalog/contact.html'
    success_url = reverse_lazy('catalog:contact')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = Contact.objects.all()
        return context_data

    def form_valid(self, form):
        if form.is_valid():
            print(f'У вас новое сообщение от {form.instance.name}({form.instance.email}): {form.instance.message}')

        return super().form_valid(form)


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/categories.html"
    extra_context = {'title': 'Категории'}
    context_object_name = 'categories'

    # вариант для загрузки продуктов по категории для шаблона с обновлением всей страницы
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category_id = self.request.GET.get('category_id')
    #     context['product_list'] = get_products(category_id)
    #     return context

    # вариант кеширования продуктов для шаблона с обновлением всей страницы
    # def get_queryset(self):
    #     queryset = cache.get('products_queryset')
    #     if not queryset:
    #         queryset = super().get_queryset()
    #         cache.set('products_queryset', queryset, 60 * 15)
    #     return queryset


def product_list_ajax(request):  # ajax вариант для шаблона с обновлением только аккордеона
    category_id = request.GET.get('category_id')
    products = get_products(category_id)
    return render(request, 'catalog/partials/product_list.html', {'products': products})

