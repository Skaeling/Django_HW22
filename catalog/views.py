from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "students/home.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'Получено новое сообщение от {name} {email}: {message}')
        return HttpResponse(f'Спасибо, {name}, ваше сообщение получено')
    return render(request, 'students/contact.html')
