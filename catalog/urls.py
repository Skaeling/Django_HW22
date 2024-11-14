from django.urls import path
from .views import HomeListView, ProductDetailView, ContactCreateView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
]
