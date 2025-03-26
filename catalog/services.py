from django.core.cache import cache
from .models import Product


def get_products(category_id):
    key = f'products_{category_id}'
    products = cache.get(key)
    if products is None:
        products = Product.objects.filter(category=category_id)
        cache.set(key, products, 60 * 15)
        if not products.exists():
            return None
    return products
