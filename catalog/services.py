from .models import Product


def get_products(category_id):
    products_list = Product.objects.filter(category=category_id)
    if not products_list.exists():
        return None
    return products_list


# def get_products(category_id):
#     key = f'products_{category_id}'
#     products = cache.get(key)
#
#     if products is None:
#         # Если данные не найдены в кэше, получить их из базы данных и сохранить в кэш
#         products = MyModel.objects.filter(category_id=category_id)
#         cache.set(key, products, timeout=60 * 60 * 24)  # Кешировать данные на 24 часа
#
#     return products