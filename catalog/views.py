from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Contact


def home(request):
    products = Product.objects.reverse()[:5]
    [print(product) for product in products]
    return render(request, "catalog/home.html")


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.message = request.POST.get("message")
        contact.save()
        result = Contact.objects.all()
        print(f'Получено новое сообщение от {contact.name} ({contact.email}): {contact.message}')
        return render(request, 'catalog/contact.html', {"contact": result})
    return render(request, 'catalog/contact.html')


# return HttpResponse(f'Спасибо, {name}, ваше сообщение получено')