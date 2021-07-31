from django.db import models
from taggit.managers import TaggableManager
from datetime import datetime
from django.utils.text import slugify


    
    
    
    
class Category(models.Model):
        
    name = models.CharField(max_length=50)
    photo_Category = models.ImageField(upload_to='photosblogCategory', null=True, blank=True)
    content_category = models.TextField(max_length=100, null=True, blank=True)
    slug = models.SlugField(('slug'), null=True, blank=True)
    def __str__(self):
        return self.name

    def save(self, *args,  **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,  **kwargs)




class Post(models.Model):
    #post content
    title = models.CharField(max_length=250)       
    photo_post = models.ImageField(upload_to='photosblog', null=True, blank=True)
    photo_secondary = models.ImageField(upload_to='photosblog', null=True, blank=True)
    photo_final = models.ImageField(upload_to='photosblog', null=True, blank=True)
    content = models.TextField()
    photo_description = models.TextField(max_length=300, null=True, blank=True)
    content_under = models.TextField(max_length=500, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created  = models.TimeField(default=datetime.now)
    slug = models.SlugField( ('slug'), null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    tags = TaggableManager()
    
    #author content
    author  = models.CharField(max_length=300, blank=True)
    author_description  = models.CharField(max_length=150, blank=True)
    photo_author = models.ImageField(upload_to='photosblog', null=True, blank=True)

    def save(self, *args,  **kwargs):
            
        self.slug = slugify(self.title)
        super(Post, self).save(*args,  **kwargs)



    def __str__(self):
        return self.title