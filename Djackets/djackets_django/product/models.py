from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File


class Category(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField()

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return (f'/{self.slug}/')


class Product(models.Model):
  category = models.ForeignKey(
      Category, related_name='products', on_delete=models.CASCADE())
  name = models.CharField(max_length=255)
  slug = models.SlugField()
  description = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.ImageField()
  thumbnail = models.FileField(upload_to='uploads/', blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('name',)
