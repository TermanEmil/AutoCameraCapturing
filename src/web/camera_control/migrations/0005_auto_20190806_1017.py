# Generated by Django 2.2.3 on 2019-08-06 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera_control', '0004_auto_20190806_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crontimelapse',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 7, 10, 17, 3, 153371)),
        ),
    ]
