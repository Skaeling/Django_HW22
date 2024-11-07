from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Contact, Category


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'products': products,
        'title': "Главная"
    }
    # [print(product) for product in products]
    return render(request, "catalog/home.html", {"page_obj": page_obj, 'products': products, 'title': "Главная"})


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
        print(f'Получено новое сообщение от {contact.name} ({contact.email}): {contact.message}')
        return render(request, 'catalog/contact.html', {"contact": result})
    return render(request, 'catalog/contact.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)


def user_product(request):
    context = {
        'title': "Добавить новый продукт"
    }
    if request.method == 'POST':
        user_product = Product()
        user_product.name = request.POST.get("name")
        user_product.description = request.POST.get("description")
        user_product.image = request.POST.get("image")
        user_product.category = Category(request.POST.get("category"))
        user_product.price = request.POST.get("price")
        user_product.save()
        result = Product.objects.all()
        return render(request, 'catalog/home.html', {"products": result})
    return render(request, 'catalog/user_product.html', context)

