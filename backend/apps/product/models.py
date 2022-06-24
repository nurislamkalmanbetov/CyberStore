from django.db import models
from backend.apps.accounts.models import User


# Create your models here.
# PRODUCT MODELS

class Category(models.Model):
    name = models.CharField("Название", max_length=60, unique=True)
    slug = models.SlugField("Слаг", max_length=60, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2
    )
    image = models.ImageField("Фото", upload_to="product_images/")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("Активный", default=True)
    favorite = models.ManyToManyField(User, blank=True, related_name='favorite')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created']

    def __str__(self):
        return self.name


class MyLinks(models.Model):
    facebook = models.URLField('Facebook')
    twit = models.URLField('twitter')
    linkedin = models.URLField('linkedin')
    ins = models.URLField('instagram')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "мои ссылку"
        verbose_name_plural = "ссылки"
        ordering = ['-created']
        get_latest_by = ['created']

    def __str__(self):
        return self.facebook
