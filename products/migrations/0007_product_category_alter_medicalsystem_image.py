# Generated by Django 4.2.7 on 2023-11-28 15:12

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_medicalsystem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='products.categoies'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicalsystem',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='products/systems/images/defaults_products.jpg', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='products/images/systems/'),
        ),
    ]
