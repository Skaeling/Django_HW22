from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.get_contact, name='contact'),
    path('product/<int:pk>/', views.product, name='product'),
    path('user_product/', views.user_product, name='user_product'),

]
