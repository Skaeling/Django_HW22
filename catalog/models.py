from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name', ]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование товара")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='photos/', default='photos/default.jpeg', verbose_name="Фотография")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    price = models.IntegerField(default='null', verbose_name='Стоимость')
    is_new = models.BooleanField(default=True, verbose_name="Новый товар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def get_absolute_url(self):
        return reverse("catalog:product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.name} {self.price}$ ({self.category}) '

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['id', ]


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(help_text='name@example.com')
    message = models.TextField(null=True, blank=True, verbose_name="Сообщение")

    def __str__(self):
        return f'Пользователь {self.name}({self.email}) отправил сообщение : {self.message}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['id', 'name', 'email', ]
