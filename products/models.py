from decimal import Decimal
from django.db import models
from crm.models import Customer, Note
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from datetime import timedelta, date
from django_resized import ResizedImageField
# Create your models here.

class Categoies(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CURRENCY=[
    ("EGP","EGP")
    ]
    image=ResizedImageField(
        force_format="WEBP", quality=80, null=True, blank=True,upload_to="products/images/",default='products/images/defaults_products.jpg')
    name=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(max_length=1000,null=True,blank=True)
    price=models.DecimalField(null=True,blank=True,max_digits=100, decimal_places=2,)
    currency=models.CharField(choices=CURRENCY,default="EGP",max_length=5,null=True,blank=True)
    uniqueId =models.CharField(null=True,blank=True,max_length=100)
    slug=models.SlugField(max_length=500,unique=True,null=True,blank=True)


    def __str__(self):
        return '{} {}'.format(self.name,self.uniqueId)

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))
        super(Product, self).save(*args, **kwargs)


class Invoice(models.Model):
    STATUS=[
    ('CURRENT', 'CURRENT'),
    ('EMAIL_SENT', 'EMAIL_SENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
]
    TERMS = [
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]
    #RELATED fields
    customerid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    employeeid=models.ForeignKey(User,on_delete=models.CASCADE)
    #Invoice Data fields
    note=models.TextField(max_length=1000)
    status=models.CharField(max_length=100,choices=STATUS,default='CURRENT')
    products=models.ManyToManyField(Product,related_name='products')
    paymentTerms = models.CharField(choices=TERMS, default='14 days', max_length=100)
    discount_presentage=models.IntegerField(blank=True, null=True)
    #cost_tax
    #cost

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.customerid, self.uniqueId)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.customerid, self.uniqueId))          
        

        self.slug = slugify('{} {}'.format(self.customerid, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)


