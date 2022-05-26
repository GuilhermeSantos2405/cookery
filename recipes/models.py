from django.contrib.auth.models import User
from django.db import models
from stdimage import StdImageField


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)

    preparation_time = models.IntegerField()
    servings = models.IntegerField()
    ingredients = models.TextField()
    method_preparation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, blank=True)
    image = StdImageField(upload_to='path/to/img',
                          variations={'variation_image':
                                      {'width': 370, 'height': 217}})

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Recipe')
        verbose_name_plural = ('Recipes')
