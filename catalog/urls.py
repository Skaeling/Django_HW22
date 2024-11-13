from django.urls import path
from . import views
from .views import HomeListView, ProductDetailView

urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),


    path('contact/', views.get_contact, name='contact'),
    path('user_product/', views.user_product, name='user_product'),

]
