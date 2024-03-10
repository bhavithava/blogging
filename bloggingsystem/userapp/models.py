from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from mainapp.models import BlogDetails
class OpenBlog(models.Model):
    blog_details = models.ForeignKey(BlogDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.blogtitle} {self.blog_details}"

