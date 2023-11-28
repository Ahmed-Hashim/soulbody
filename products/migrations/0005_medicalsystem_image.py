# Generated by Django 4.2.7 on 2023-11-28 15:07

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_description_medicalsystem_ar_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalsystem',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='products/images/defaults_products.jpg', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='products/images/'),
        ),
    ]
