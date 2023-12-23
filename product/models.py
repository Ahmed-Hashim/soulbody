from decimal import Decimal
from django.db import models
from crmsb.models import Customer, Note
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from datetime import timedelta, date
from django_resized import ResizedImageField
from taggit.managers import TaggableManager
from django.conf import settings

# Create your models here.


class Categories(models.Model):
    en_name = models.CharField(max_length=50)
    ar_name = models.CharField(max_length=50)

    def __str__(self):
        return self.en_name


class Product(models.Model):
    CURRENCY = [("EGP", "EGP")]
    category = models.ForeignKey(
        Categories, on_delete=models.DO_NOTHING, related_name="products"
    )
    image = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="products/images/",
        default="products/images/defaults_products.jpg",
    )

    en_name = models.CharField(max_length=100, null=True, blank=True)
    ar_name = models.CharField(max_length=100, null=True, blank=True)
    en_description = models.TextField(max_length=1000, null=True, blank=True)
    ar_description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=100,
        decimal_places=2,
    )
    old_price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=100,
        decimal_places=2,
    )
    currency = models.CharField(
        choices=CURRENCY, default="EGP", max_length=5, null=True, blank=True
    )
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    best_selling = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.en_name, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify("{} {}".format(self.en_name, self.uniqueId))

        self.slug = slugify("{} {}".format(self.en_name, self.uniqueId))
        super(Product, self).save(*args, **kwargs)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="CartItem")


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Invoice(models.Model):
    STATUS = [
        ("CURRENT", "CURRENT"),
        ("EMAIL_SENT", "EMAIL_SENT"),
        ("OVERDUE", "OVERDUE"),
        ("PAID", "PAID"),
    ]
    TERMS = [
        ("14 days", "14 days"),
        ("30 days", "30 days"),
        ("60 days", "60 days"),
    ]
    # RELATED fields
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employeeid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Invoice Data fields
    note = models.TextField(max_length=1000)
    status = models.CharField(max_length=100, choices=STATUS, default="CURRENT")
    products = models.ManyToManyField(Product, related_name="products")
    paymentTerms = models.CharField(choices=TERMS, default="14 days", max_length=100)
    discount_presentage = models.IntegerField(blank=True, null=True)
    # cost_tax
    # cost

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.customerid, self.uniqueId)

    def get_absolute_url(self):
        return reverse("invoice-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split("-")[4]
            self.slug = slugify("{} {}".format(self.customerid, self.uniqueId))

        self.slug = slugify("{} {}".format(self.customerid, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)


class MedicalSystem(models.Model):
    image = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="products/images/systems/",
        default="products/systems/images/defaults_products.jpg",
    )
    en_name = models.CharField(max_length=50)
    ar_name = models.CharField(max_length=50)
    en_description = models.TextField(null=True, blank=True)
    ar_description = models.TextField(null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.en_name


class System_FQA(models.Model):
    system = models.ForeignKey(MedicalSystem, on_delete=models.CASCADE)
    ar_question = models.CharField(max_length=100)
    en_question = models.CharField(max_length=100)
    ar_answer = models.TextField()
    en_answer = models.TextField()

    def __str__(self):
        return self.system.en_name


class RequestClinicSystemPackage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    clinic_count = models.PositiveIntegerField()
    departement_count = models.PositiveIntegerField()
    doctors_count = models.PositiveIntegerField()
    users_count = models.PositiveIntegerField()
    details = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(
            self.name, self.phone_number, self.clinic_count, self.date
        )


class RequestHospitalSystemPackage(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    hosbital = models.CharField(max_length=120, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    hospital_beds_count = models.PositiveIntegerField(blank=False, null=False)
    departement_count = models.PositiveIntegerField(blank=False, null=False)
    doctors_count = models.PositiveIntegerField(blank=False, null=False)
    users_count = models.PositiveIntegerField(blank=False, null=False)
    details = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
