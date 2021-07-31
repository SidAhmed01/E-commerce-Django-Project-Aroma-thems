from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime 
from django.utils.text import slugify













class Product(models.Model):

     

    PROName = models.CharField(max_length=100, verbose_name=_("product name"))
    PROCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
   
    PRDDescr = models.TextField(verbose_name=_("product description"))
    PRDPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("product price"))
    PRDImage = models.ImageField(upload_to='productImage/', verbose_name=_("Imaage"), blank=True, null=True)
    PROCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("product Cost"))
    PROCreated = models.DateTimeField(verbose_name=_("time created"))
    slug = models.SlugField(('slug'), null=True, blank=True)
     #PRDStatus = models.models.ForeignKey(Product, on_delete=models.CASCADE, max_length=10,choices=STATUS, blank=True, null=True)
    def __str__(self):
        return self.PROName

    def save(self, *args,  **kwargs):
            
        self.slug = slugify(self.PROName)
        super(Product, self).save(*args,  **kwargs)

class ProductImage(models.Model):
    PROIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    PRDImage = models.ImageField(upload_to='productImage/', verbose_name=_("Imaage"))
    
    def __str__(self):
        return str(self.PROIProduct)


class Category(models.Model):
    CATName = models.CharField(max_length=50, verbose_name=("Name"))
    CATParent = models.ForeignKey('self', limit_choices_to={'CATParent__isnull': True}, verbose_name=('Main Category'), on_delete=models.CASCADE, blank=True, null=True)
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    def __str__(self):
        return str(self.CATName) 
        


class Product_Alternative(models.Model):

    PALNProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product', verbose_name=('Product'))
    PALNAlternatives = models.ManyToManyField(Product, related_name='alternative_products', verbose_name=('Alternative'))


    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Products Alternative")
    def __str__(self):
        return str(self.PALNProduct) 



class Product_Accessories(models.Model):
    
    PACCProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mainAccessory_product', verbose_name=('Product'))
    PACCAlternatives = models.ManyToManyField(Product, related_name='accessories_products', verbose_name=('Accessoire'))


    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _("Products Accessories")
    def __str__(self):
        return str(self.PACCProduct)















