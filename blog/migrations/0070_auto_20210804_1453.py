# Generated by Django 3.1.1 on 2021-08-04 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0069_auto_20210804_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developers',
            name='country',
        ),
        migrations.RemoveField(
            model_name='developers',
            name='countryAbbr',
        ),
        migrations.RemoveField(
            model_name='developers',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='developers',
            name='resume',
        ),
    ]
