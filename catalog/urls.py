from django.urls import path
from .views import HomeListView, ProductDetailView, ContactCreateView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactCreateView.as_view(), name='contact'),
    path('products/new/', ProductCreateView.as_view(), name='add_product'),
]
