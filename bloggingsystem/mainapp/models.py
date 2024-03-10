from django.db import models

# Create your models here.
class BlogDetails(models.Model):
    blogtitle = models.CharField(max_length=255, **{'null': True, 'blank': True})
    BLOG_TYPES = [
        ('foodblogs', 'Food-blogs'),
        ('travelblogs', 'Travel-blogs'),
        ('petsblogs', 'Pets-blogs'),
    ]
    blogtype = models.CharField(max_length=20, choices=BLOG_TYPES, default='foodblogs')
    description = models.TextField(**{'null': True, 'blank': True})
    location = models.CharField(max_length=100, **{'null': True, 'blank': True})
    bloggerdetails = models.CharField(max_length=200, **{'null': True, 'blank': True})

    class Meta:
        db_table="BlogDetails"

