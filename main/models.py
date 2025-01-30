from django.db import models

# Create your models
class Users(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.TextField(max_length = 100)
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title