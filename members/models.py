from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from .timezones import TIMEZONES
from django_resized import ResizedImageField
from django.db.models import UniqueConstraint

# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
COUNTIERS = (
    ('Algeria', 'Algeria'),
    ('Bahrain', 'Bahrain'),
    ('Comoros', 'Comoros'),
    ('Djibouti', 'Djibouti'),
    ('Egypt', 'Egypt'),
    ('Iraq', 'Iraq'),
    ('Jordan', 'Jordan'),
    ('Kuwait', 'Kuwait'),
    ('Lebanon', 'Lebanon'),
    ('Libya', 'Libya'),
    ('Mauritania', 'Mauritania'),
    ('Morocco', 'Morocco'),
    ('Oman', 'Oman'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Sudan', 'Sudan'),
    ('Syria', 'Syria'),
    ('Tunisia', 'Tunisia'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('Yemen', 'Yemen'),
)
TIMEZONES = TIMEZONES


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, unique=True)
    fullname = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = ResizedImageField(
        force_format="WEBP", quality=80, null=True, blank=True, upload_to="images/profile/", default='images/profile/default-profile.jpg')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER, null=True, blank=True)
    country = models.CharField(
        max_length=25, choices=COUNTIERS, null=True, blank=True)
    timezone = models.CharField(
        max_length=100, choices=TIMEZONES, null=True, blank=True)
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
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Chat(models.Model):
    user1 = models.ForeignKey(
        Profile, related_name="user1_chats", on_delete=models.DO_NOTHING)
    user2 = models.ForeignKey(
        Profile, related_name="user2_chats", on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user1', 'user2'],
                name='unique_chat_between_users'
            )
        ]

    def __str__(self):
        return f"Chat between {self.user1} and {self.user2}"


class Messege(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)


class ChatNotification(models.Model):
    chat = models.ForeignKey(Messege, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.user.username


class AppDownLoad(models.Model):
    device_ip = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=30)
    regoin = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    deviceType = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "App Download"
        verbose_name_plural = "App Downloads"

