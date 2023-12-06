# Generated by Django 4.2.7 on 2023-12-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_fqa_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fqa_about',
            old_name='answer',
            new_name='ar_answer',
        ),
        migrations.RenameField(
            model_name='fqa_about',
            old_name='question',
            new_name='ar_question',
        ),
        migrations.AddField(
            model_name='fqa_about',
            name='en_answer',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fqa_about',
            name='en_question',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
