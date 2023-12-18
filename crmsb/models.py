from email.policy import default
from random import choices
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from crmsb.fields import NonStrippingTextField
from django_resized import ResizedImageField
from django.conf import settings

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

TITLE = (
    ("MR", "MR"),
    ("MRS", "MRS"),
)

# Create your models here.


class Customer(models.Model):
    STATUS = (
        ("Prospect", "Prospect"),
        ("Email Sent", "Email Sent"),
        ("Active", "Active"),
        ("Expired", "Expired"),
        ("Suspended", "Suspended"),
    )
    logo = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/clients/",
        default="images/clients/",
    )
    title = models.CharField(max_length=25, choices=TITLE, null=True, blank=True)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    middle_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    lead_referral_source = models.CharField(max_length=120, blank=True, null=True)
    industry = models.ForeignKey(
        "Industry",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="industry_type",
    )
    company = models.CharField(max_length=120, blank=False, null=False)
    address = models.CharField(max_length=190, null=True, blank=True)
    street = models.CharField(max_length=190, null=True, blank=True)
    land_phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=120, null=True, blank=True)
    website = models.CharField(max_length=190, null=True, blank=True)
    Situation = models.CharField(
        null=True, blank=True, choices=STATUS, default="Prospect", max_length=100
    )
    # status= models.ForeignKey('Status',on_delete=models.SET_NULL,null=True,blank=True,related_name='status_type')
    background_info = models.TextField(max_length=500, null=True, blank=True)
    last_contact_date = models.DateTimeField(null=True, blank=True)
    facebook_url = models.CharField(max_length=150, null=True, blank=True)
    instagram_url = models.CharField(max_length=150, null=True, blank=True)
    twitter_url = models.CharField(max_length=150, null=True, blank=True)
    linkedin_url = models.CharField(max_length=150, null=True, blank=True)
    skype_url = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(("slug"), blank=True, null=True)

    def __str__(self):
        return self.company

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.company)
        super(Customer, self).save(*args, **kwargs)

    expert = models.BooleanField(default=False)


class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    position = models.CharField(max_length=50)

    def __str__(self):
        return str(self.company)


class Industry(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Status(models.Model):
    type = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.type)


class Note(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    notes = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]


class Customer_Email(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    file_upload = models.FileField(null=True, blank=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.company, self.subject)


TYPES = {("TEXT", "TEXT"), ("IMAGE", "IMAGE"), ("PDF", "PDF"), ("VIDEO", "VIDEO")}
LANG = (
    ("AR", "AR"),
    ("EN", "EN"),
    ("FR", "FR"),
)


class Whatsapp_Template(models.Model):
    title = models.CharField(max_length=25)
    type = models.CharField(choices=TYPES, default="TEXT", max_length=10)
    message = NonStrippingTextField(max_length=1000)
    file_upload = models.FileField(
        null=True, blank=True, upload_to="whatsapp_templates/"
    )
    language = models.CharField(choices=LANG, max_length=2, null=True, blank=True)
    template_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)


class Whatsapp_Messages(models.Model):
    company = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="whatappmsg"
    )
    type = models.CharField(choices=TYPES, default="TEXT", max_length=10)
    message = models.TextField(max_length=1000)
    file_upload = models.FileField(
        null=True, blank=True, upload_to="whatsapp_templates/"
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date}-{self.company}"


class Testimonials(models.Model):
    image = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="home/images/testimonials/",
        default="home/images/testimonials/defaults_testimonials.WEBP",
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="testimonials"
    )
    name = models.CharField(max_length=50)
    jobtitle = models.CharField(max_length=50)
    comment = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}-{self.customer.company}-{self.jobtitle}"
