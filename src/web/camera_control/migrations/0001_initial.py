# Generated by Django 2.2.3 on 2019-08-06 08:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronTimelapse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='My schedule', max_length=64)),
                ('storage_dir', models.CharField(default='~/Pictures/', max_length=256)),
                ('filename_pattern', models.CharField(default='capture', max_length=256)),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 7, 8, 25, 46, 402418))),
                ('year', models.CharField(default='*', max_length=128)),
                ('month', models.CharField(default='*', max_length=128)),
                ('day', models.CharField(default='*', max_length=256)),
                ('week', models.CharField(default='*', max_length=256)),
                ('day_of_week', models.CharField(default='*', max_length=256)),
                ('hour', models.CharField(default='*', max_length=128)),
                ('minute', models.CharField(default='*', max_length=128)),
                ('second', models.CharField(default='*', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='FavField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='camera_control.Profile')),
            ],
        ),
    ]
