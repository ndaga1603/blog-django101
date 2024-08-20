from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts/")

    def __str__(self) -> str:
        return f"{self.author.username} {self.created_at}"
        
# python manage.py makemigrations
# python manage.py migrate


