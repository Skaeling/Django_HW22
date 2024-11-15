from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['pk', ]

