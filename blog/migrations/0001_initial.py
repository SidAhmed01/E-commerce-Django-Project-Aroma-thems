# Generated by Django 3.2.4 on 2021-06-29 17:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('photo_post', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_description', models.CharField(blank=True, max_length=300)),
                ('content', models.CharField(max_length=900000)),
                ('content_under', models.CharField(blank=True, max_length=500)),
                ('author', models.CharField(blank=True, max_length=300)),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.TimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
        ),
    ]