from django.db import models
from django_resized import ResizedImageField
from product.models import Product, MedicalSystem


# Create your models here.
class MainSlider(models.Model):
    image_en = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/slider/",
        default="images/slider/defaults_products.WEBP",
    )
    image_en_tab = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/slider/",
        default="images/slider/defaults_products.WEBP",
    )
    image_en_mb = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/slider/",
        default="images/slider/defaults_products.WEBP",
    )
    image_ar = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/slider/",
        default="images/slider/defaults_products.WEBP",
    )
    image_ar_tab = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/slider/",
        default="images/slider/defaults_products.WEBP",
    )
    image_ar_mb = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/slider/",
        default="images/slider/defaults_products.WEBP",
    )
    en_title = models.CharField(max_length=150)
    ar_title = models.CharField(max_length=150)
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    system = models.ForeignKey(
        MedicalSystem, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    active = models.BooleanField(default=False)


class Cooldown(models.Model):
    image_en= ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/slider/",
        default="images/slider/defaults_products.WEBP",
    )
    image_ar = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/slider/",
        default="images/slider/defaults_products.WEBP",
    )
    en_offer = models.CharField(max_length=50, null=True, blank=True)
    ar_offer = models.CharField(max_length=50, null=True, blank=True)
    en_bigTitle = models.CharField(max_length=150, null=True, blank=True)
    ar_bigTitle = models.CharField(max_length=150, null=True, blank=True)
    en_description = models.CharField(max_length=50, null=True, blank=True)
    ar_description = models.CharField(max_length=50, null=True, blank=True)
    end_time = models.DateField(
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    system = models.ForeignKey(
        MedicalSystem, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    active = models.BooleanField(default=False)


class sitedata(models.Model):
    logo = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/logo/",
        default="images/logo.WEBP",
    )
    fqa_image = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/sitedata/",
        default="images/logo.WEBP",
    )
    phone_number_1 = models.CharField(max_length=50, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=75, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    map_link = models.URLField(null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    youtube = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    linkedin = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    en_about_us_footer = models.TextField(max_length=120)
    en_about_us_footer = models.TextField(max_length=120)
    en_video = models.CharField(max_length=100, null=True, blank=True)
    ar_video = models.CharField(max_length=100, null=True, blank=True)
    ar_video_image = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/sitedata/",
        default="images/logo.WEBP",
    )
    en_video_image = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/sitedata/",
        default="images/logo.WEBP",
    )


class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FQA_About(models.Model):
    ar_question = models.CharField(max_length=100)
    en_question = models.CharField(max_length=100)
    ar_answer = models.TextField()
    en_answer = models.TextField()
