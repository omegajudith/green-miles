# Generated by Django 3.0 on 2019-12-03 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email adress')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, max_length=30, null=True, upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_verified', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
