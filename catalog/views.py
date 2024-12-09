from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Product, Contact
from .forms import ProductForm, ProductModeratorForm, ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    extra_context = {'title': 'Главная'}
    paginate_by = 6


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
            print(f'В категорию "{form.instance.category}" добавлен новый продукт: "{form.instance.name}"')

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    context_object_name = 'product'
    extra_context = {'title': 'Редактировать товар'}

    def form_valid(self, form):
        if form.is_valid():
            print(f'Отредактирован продукт: "{form.instance.name}"')

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        return ProductForm
#     raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    context_object_name = 'product'
    extra_context = {'title': 'Удалить товар'}
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user
        if not user.has_perm('catalog.can_delete_product'):
            raise PermissionDenied
                # HttpResponseForbidden('Недостаточно прав для выполнения удаления')
        return product
