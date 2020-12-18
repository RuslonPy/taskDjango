from django.db import models
from django.utils import timezone
from django.conf import settings


class Author(models.Model):
  name = models.CharField(max_length=255)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="some string")
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
      return self.name

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="some string")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title