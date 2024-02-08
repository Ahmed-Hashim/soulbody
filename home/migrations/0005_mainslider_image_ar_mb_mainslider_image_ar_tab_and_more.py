# Generated by Django 4.2.7 on 2024-02-08 18:37

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_image_cooldown_image_en_cooldown_image_ar'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainslider',
            name='image_ar_mb',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/slider/defaults_products.WEBP', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='images/slider/'),
        ),
        migrations.AddField(
            model_name='mainslider',
            name='image_ar_tab',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/slider/defaults_products.WEBP', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='images/slider/'),
        ),
        migrations.AddField(
            model_name='mainslider',
            name='image_en_mb',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/slider/defaults_products.WEBP', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='images/slider/'),
        ),
        migrations.AddField(
            model_name='mainslider',
            name='image_en_tab',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/slider/defaults_products.WEBP', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='images/slider/'),
        ),
    ]