from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Product, Contact
from .forms import ProductForm


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    extra_context = {'title': 'Главная'}
    paginate_by = 6


def get_contact(request):
    context = {
        'title': "Контакты"
    }
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.message = request.POST.get("message")
        contact.save()
        result = Contact.objects.all()
        context = {
            "contact": result,
            'title': "Контакты"
        }
        print(f'Получено новое сообщение от {contact.name} ({contact.email}): {contact.message}')
        return render(request, 'catalog/contact.html', context)
    return render(request, 'catalog/contact.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    extra_context = {'title': 'Описание товара'}


def user_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            print(f'Добавлен новый продукт: {new_product.name} стоимостью {new_product.price}$')
            return redirect('product', new_product.pk)
    else:
        form = ProductForm()
    return render(request, 'catalog/user_product.html', {'title': "Добавить товар", "form": form})

