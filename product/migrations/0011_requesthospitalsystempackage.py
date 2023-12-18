# Generated by Django 4.2.7 on 2023-12-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_requestclinicsystempackage_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestHospitalSystemPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('hosital', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('hospital_beds_count', models.PositiveIntegerField()),
                ('departement_count', models.PositiveIntegerField()),
                ('doctors_count', models.PositiveIntegerField()),
                ('users_count', models.PositiveIntegerField()),
                ('details', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
