from django.shortcuts import render
from .models import Product, Contact


def home(request):
    products = Product.objects.all()[:6]
    context = {
        'products': products,
        'title': "Главная"
    }
    [print(product) for product in products]
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
        print(f'Получено новое сообщение от {contact.name} ({contact.email}): {contact.message}')
        return render(request, 'catalog/contact.html', {"contact": result})
    return render(request, 'catalog/contact.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)

