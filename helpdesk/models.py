from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_plural_name = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Call(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    show = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title
    