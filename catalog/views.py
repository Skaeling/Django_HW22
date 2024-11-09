from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Product, Contact
from .forms import ProductForm


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        'products': products,
        'title': "Главная"
    }
    return render(request, "catalog/home.html", context)


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


def product(request, pk):
    product_pk = Product.objects.get(pk=pk)
    context = {
        'product': product_pk
    }
    return render(request, 'catalog/product.html', context)


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

