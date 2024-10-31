from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f'{self.name}({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name', ]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Продукт")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='photos/', verbose_name="Фотография")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(default='null', verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.name} {self.category} {self.price})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name', ]
