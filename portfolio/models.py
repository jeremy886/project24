from django.db import models
from django.utils import timezone

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)