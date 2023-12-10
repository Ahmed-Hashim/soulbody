# Generated by Django 4.2.7 on 2023-12-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmsb', '0013_customer_expert_alter_whatsapp_messages_type_and_more'),
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