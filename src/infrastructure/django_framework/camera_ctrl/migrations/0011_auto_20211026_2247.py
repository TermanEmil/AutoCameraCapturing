# Generated by Django 2.2.20 on 2021-10-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera_ctrl', '0010_alter_scheduledconfigfield_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsettings',
            name='email_subject_prefix',
            field=models.CharField(blank=True, default='[nucpcaps7b]', max_length=64),
        ),
    ]
