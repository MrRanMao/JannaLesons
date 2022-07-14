from django.db import models

class Post(models.Model):

    title = models.CharField('Title', max_length=50)
    slug = models.CharField('Slug', max_length=100, default=None, blank=True, null=True)
    text = models.TextField()
    publish_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

