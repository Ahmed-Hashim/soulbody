# Generated by Django 4.2.7 on 2023-12-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_cart_completed_cart_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, through='product.CartItem', to='product.product'),
        ),
    ]
