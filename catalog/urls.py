from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),

]
