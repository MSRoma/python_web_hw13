from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"
    
class Author(models.Model):
    fullname = models.CharField(max_length=250, null=False)
    born_date = models.CharField(max_length=250, null=False)
    born_location = models.CharField(max_length=250, null=False)
    description = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return f"{self.fullname}"

class Note(models.Model):
    description = models.TextField(max_length=1000, null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True) # тут не треба мані ту мани
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.description}"
    