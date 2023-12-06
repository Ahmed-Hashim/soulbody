# Generated by Django 4.2.7 on 2023-12-06 11:39

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('crmsb', '0011_alter_whatsapp_messages_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='logo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/clients/', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='images/clients/'),
        ),
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('VIDEO', 'VIDEO'), ('IMAGE', 'IMAGE'), ('PDF', 'PDF'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('VIDEO', 'VIDEO'), ('IMAGE', 'IMAGE'), ('PDF', 'PDF'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
    ]
