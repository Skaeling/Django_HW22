from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('products/<int:pk>/', cache_page(60)(views.ProductDetailView.as_view()), name='product_detail'),
    path('contacts/', views.ContactCreateView.as_view(), name='contact'),
    path('products/new/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('ajax/product-list/', views.product_list_ajax, name='product_list_ajax'),

]
