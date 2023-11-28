from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    imagelink = models.URLField(max_length=250)
    design_link = models.ImageField(
        null=True, blank=True, upload_to="images/designs/")
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name="posts")
    published = models.BooleanField(default='False')
    design = models.BooleanField(default='False')

    class Meta:
        ordering = ('id',)


class Category (models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    imagelink = models.URLField(max_length=250)
    design_link = models.ImageField(
        null=True, blank=True, upload_to="images/designs/")
    message = models.TextField(max_length=1000)
    date_to_publish = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    schedule = models.BooleanField(default='False')
    published = models.BooleanField(default='False')
    timezone = models.CharField(max_length=150, null=True, blank=True)
    access_token = models.CharField(max_length=250, null=True, blank=True)
    scheduled_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_to_publish',)


class PublishedPost(models.Model):
    link = models.URLField(null=True, blank=True, max_length=250)
    message = models.TextField(max_length=1000)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name="pubposts")
    published_date = models.DateTimeField(null=True, blank=True)
    scheduled_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    fblink = models.URLField(max_length=100, null=True, blank=True)
    fb_post_id = models.CharField(max_length=40, null=True, blank=True)
    like_count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        ordering = ('-published_date',)

    def thumbnail(self):
        return self.link


class AlmazadiProducts(models.Model):
    add_title = models.CharField(null=True, blank=True, max_length=500)
    imagelink = models.URLField(null=True, blank=True, max_length=250)
    add_link = models.URLField(
        null=True, blank=True, max_length=250, unique=True)
    edit_link = models.URLField(null=True, blank=True, max_length=250)
    owner = models.CharField(null=True, blank=True, max_length=150)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    created_post = models.BooleanField(default=False)

    def __str__(self):
        return f"id={self.id}**({self.add_title})**({self.owner})**({self.category})"


class Comment(models.Model):
    post_id = models.ForeignKey(
        PublishedPost, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    comment_id = models.CharField(
        null=True, blank=True, max_length=100, unique=True)
    comment_by = models.CharField(null=True, blank=True, max_length=200)
    comment_by_profile = models.CharField(
        null=True, blank=True, max_length=200)
    comment = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"Post_ID={self.post_id.fb_post_id}**({self.comment})"


class Share(models.Model):
    post_id = models.ForeignKey(
        PublishedPost, null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Post_ID={self.post_id.fb_post_id}**( likes count ={self.count})"


class Quotes(models.Model):
    LANG = (
        ("AR", "AR"),
        ("EN", "EN")
    )
    quote = models.TextField(max_length=1000)
    lang = models.CharField(max_length=2, choices=LANG, default="AR")
