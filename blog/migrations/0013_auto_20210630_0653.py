# Generated by Django 3.2.4 on 2021-06-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_description',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_final',
            field=models.ImageField(blank=True, null=True, upload_to='photosblog'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_secondary',
            field=models.ImageField(blank=True, null=True, upload_to='photosblog'),
        ),
    ]