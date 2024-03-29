# Generated by Django 4.2.7 on 2024-01-28 12:28

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainslider',
            old_name='image',
            new_name='image_en',
        ),
        migrations.AddField(
            model_name='mainslider',
            name='image_ar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/slider/defaults_products.WEBP', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='images/slider/'),
        ),
    ]
