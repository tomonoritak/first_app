from django.db import models

class Post(models.Model):
  memo = models.TextField(blank=True)