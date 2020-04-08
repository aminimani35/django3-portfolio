# Generated by Django 3.0.5 on 2020-04-08 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200408_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='publish_date',
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
