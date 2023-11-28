# Generated by Django 4.2.7 on 2023-11-28 15:44

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, default='home/images/slider/defaults_products.WEBP', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='home/images/slider/')),
            ],
        ),
    ]
