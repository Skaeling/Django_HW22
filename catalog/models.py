from django.db import models


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
    name = models.CharField(max_length=150, verbose_name="Товар")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фотография")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    price = models.IntegerField(default='null', verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.name} {self.price}$ ({self.category}) '

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name', ]


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
