from django.db import models
import datetime
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  #SEO friendly
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

