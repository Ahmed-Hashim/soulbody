# Generated by Django 4.2.7 on 2024-01-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmsb', '0002_customer_expert_customer_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'IMAGE'), ('VIDEO', 'VIDEO'), ('PDF', 'PDF'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'IMAGE'), ('VIDEO', 'VIDEO'), ('PDF', 'PDF'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
    ]