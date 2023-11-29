# Generated by Django 4.2.7 on 2023-11-29 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(max_length=50)),
                ('ar_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, default='products/systems/images/defaults_products.jpg', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='products/images/systems/')),
                ('en_name', models.CharField(max_length=50)),
                ('ar_name', models.CharField(max_length=50)),
                ('en_description', models.TextField(blank=True, null=True)),
                ('ar_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, default='products/images/defaults_products.jpg', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='products/images/')),
                ('en_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ar_name', models.CharField(blank=True, max_length=100, null=True)),
                ('en_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('ar_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('currency', models.CharField(blank=True, choices=[('EGP', 'EGP')], default='EGP', max_length=5, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('best_selling', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='products.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('CURRENT', 'CURRENT'), ('EMAIL_SENT', 'EMAIL_SENT'), ('OVERDUE', 'OVERDUE'), ('PAID', 'PAID')], default='CURRENT', max_length=100)),
                ('paymentTerms', models.CharField(choices=[('14 days', '14 days'), ('30 days', '30 days'), ('60 days', '60 days')], default='14 days', max_length=100)),
                ('discount_presentage', models.IntegerField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.customer')),
                ('employeeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(related_name='products', to='products.product')),
            ],
        ),
    ]
