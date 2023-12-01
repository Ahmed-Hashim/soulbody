from django.db import models
from django_resized import ResizedImageField
from product.models import Product,MedicalSystem
# Create your models here.
class MainSlider(models.Model):
    image=ResizedImageField(
        force_format="WEBP", quality=80, null=True, blank=True,upload_to="images/slider/",default='images/slider/defaults_products.WEBP')
    en_title=models.CharField(max_length=150)
    ar_title=models.CharField(max_length=150)
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING,null=True, blank=True)
    system=models.ForeignKey(MedicalSystem,on_delete=models.DO_NOTHING,null=True, blank=True)  
    active=models.BooleanField(default=False)
class Cooldown(models.Model):
    image=ResizedImageField(
        force_format="WEBP", quality=80, null=True, blank=True,upload_to="images/slider/",default='images/slider/defaults_products.WEBP')
    en_offer=models.CharField(max_length=50, null=True, blank=True)
    ar_offer=models.CharField(max_length=50, null=True, blank=True)
    en_bigTitle=models.CharField(max_length=150, null=True, blank=True)
    ar_bigTitle=models.CharField(max_length=150, null=True, blank=True)
    en_description=models.CharField(max_length=50, null=True, blank=True)
    ar_description=models.CharField(max_length=50, null=True, blank=True)
    end_time=models.DateField(null=True, blank=True,)
    active=models.BooleanField(default=False)
class sitedata(models.Model):
    logo=ResizedImageField(
        force_format="WEBP", quality=80, null=True, blank=True,upload_to="images/logo/",default='images/logo.WEBP')
    phone_number_1=models.CharField(max_length=50, null=True, blank=True)
    phone_number_2=models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField(max_length=75, null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    map_link=models.URLField(null=True, blank=True)
    facebook=models.CharField(max_length=50, null=True, blank=True)
    youtube=models.CharField(max_length=50, null=True, blank=True)
    twitter=models.CharField(max_length=50, null=True, blank=True)
    linkedin=models.CharField(max_length=50, null=True, blank=True)
    instagram=models.CharField(max_length=50, null=True, blank=True)
    en_about_us_footer=models.TextField(max_length=120)
    ar_about_us_footer=models.TextField(max_length=120)
    
