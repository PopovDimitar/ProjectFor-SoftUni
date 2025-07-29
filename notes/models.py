from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    subject = models.CharField(max_length=50)
    tags = models.CharField(max_length=200, help_text="Comma-separated tags")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.title
