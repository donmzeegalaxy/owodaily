from django.db import models

from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField 
from django.urls import reverse




class Blog(models.Model):
    
    thumbnail = models.ImageField()
    title = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(config_name='awe')

    slug = models.SlugField(blank=True, null=False)
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'slug':self.slug
        })


class Newsletter(models.Model):
    email = models.EmailField()
    time  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    