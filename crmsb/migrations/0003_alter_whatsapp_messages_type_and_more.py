# Generated by Django 4.2.7 on 2023-12-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmsb', '0002_alter_whatsapp_messages_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapp_messages',
            name='type',
            field=models.CharField(choices=[('PDF', 'PDF'), ('VIDEO', 'VIDEO'), ('IMAGE', 'IMAGE'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
        migrations.AlterField(
            model_name='whatsapp_template',
            name='type',
            field=models.CharField(choices=[('PDF', 'PDF'), ('VIDEO', 'VIDEO'), ('IMAGE', 'IMAGE'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
    ]