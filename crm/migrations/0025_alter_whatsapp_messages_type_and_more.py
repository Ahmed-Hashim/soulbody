# Generated by Django 4.2.7 on 2023-11-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_alter_whatsapp_messages_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'IMAGE'), ('TEXT', 'TEXT'), ('VIDEO', 'VIDEO'), ('PDF', 'PDF')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'IMAGE'), ('TEXT', 'TEXT'), ('VIDEO', 'VIDEO'), ('PDF', 'PDF')], default='TEXT', max_length=10),
        ),
    ]
