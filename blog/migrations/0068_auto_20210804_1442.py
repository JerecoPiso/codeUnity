# Generated by Django 3.1.1 on 2021-08-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0067_auto_20210730_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='developers',
            name='country',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='developers',
            name='countryAbbr',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='developers',
            name='rate',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='developers',
            name='resume',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='users_device',
            name='total_users',
            field=models.IntegerField(),
        ),
    ]
