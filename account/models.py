from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.utils.text import slugify
from django.db.models.signals import post_save

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)
COUNTIERS = (
    ("Algeria", "Algeria"),
    ("Bahrain", "Bahrain"),
    ("Comoros", "Comoros"),
    ("Djibouti", "Djibouti"),
    ("Egypt", "Egypt"),
    ("Iraq", "Iraq"),
    ("Jordan", "Jordan"),
    ("Kuwait", "Kuwait"),
    ("Lebanon", "Lebanon"),
    ("Libya", "Libya"),
    ("Mauritania", "Mauritania"),
    ("Morocco", "Morocco"),
    ("Oman", "Oman"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("Sudan", "Sudan"),
    ("Syria", "Syria"),
    ("Tunisia", "Tunisia"),
    ("United Arab Emirates", "United Arab Emirates"),
    ("Yemen", "Yemen"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, unique=True)
    jobtitle = models.CharField(max_length=20, null=True, blank=True)
    fullname = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = ResizedImageField(
        force_format="WEBP",
        quality=80,
        null=True,
        blank=True,
        upload_to="images/profile/",
        default="images/profile/default-profile.jpg",
    )
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    country = models.CharField(max_length=25, choices=COUNTIERS, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    facebook_url = models.CharField(max_length=150, null=True, blank=True)
    instagram_url = models.CharField(max_length=150, null=True, blank=True)
    twitter_url = models.CharField(max_length=150, null=True, blank=True)
    linkedin_url = models.CharField(max_length=150, null=True, blank=True)
    skype_url = models.CharField(max_length=150, null=True, blank=True)
    access_token = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(("slug"), blank=True, null=True)
    online_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


def create_profile(sender, **kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])


post_save.connect(create_profile, sender=User)
