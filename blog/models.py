from django.db import models



class Blog(models.Model):
    title = models.CharField('عنوان',max_length=200)
    description = models.TextField ('متن نوشته ',max_length=350)
    image =  models.ImageField('تصویر',upload_to='blog/images')
    url = models.URLField('لینک',blank=True)
    p_date = models.DateField("تاریخ",auto_now=True)


    def __str__(self):
        return self.title
    

# Create your models here.
