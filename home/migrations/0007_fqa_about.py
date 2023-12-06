# Generated by Django 4.2.7 on 2023-12-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_fqa_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='FQA_About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ar_question', models.CharField(max_length=100)),
                ('en_question', models.CharField(max_length=100)),
                ('ar_answer', models.TextField()),
                ('en_answer', models.TextField()),
            ],
        ),
    ]
