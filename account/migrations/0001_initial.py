# Generated by Django 4.2.7 on 2023-12-28 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(blank=True, max_length=20, null=True)),
                ('fullname', models.CharField(blank=True, max_length=150, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/profile/default-profile.jpg', force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[1920, 1080], upload_to='images/profile/')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('country', models.CharField(blank=True, choices=[('Algeria', 'Algeria'), ('Bahrain', 'Bahrain'), ('Comoros', 'Comoros'), ('Djibouti', 'Djibouti'), ('Egypt', 'Egypt'), ('Iraq', 'Iraq'), ('Jordan', 'Jordan'), ('Kuwait', 'Kuwait'), ('Lebanon', 'Lebanon'), ('Libya', 'Libya'), ('Mauritania', 'Mauritania'), ('Morocco', 'Morocco'), ('Oman', 'Oman'), ('Saudi Arabia', 'Saudi Arabia'), ('Sudan', 'Sudan'), ('Syria', 'Syria'), ('Tunisia', 'Tunisia'), ('United Arab Emirates', 'United Arab Emirates'), ('Yemen', 'Yemen')], max_length=25, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=150, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=150, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=150, null=True)),
                ('skype_url', models.CharField(blank=True, max_length=150, null=True)),
                ('access_token', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('online_status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
