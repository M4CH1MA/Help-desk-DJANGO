from django.db import models
from django.utils import timezone

# Create your models here.
class Chamado(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())