from django.db import models



class Post(models.Model):
    title = models.CharField('عنوان',max_length=100)
    description = models.CharField('متن نوشته ',max_length=200)
    image =  models.ImageField('تصویر',upload_to='blog/images')
    url = models.URLField('لینک',blank=True)

# Create your models here.
