# Generated by Django 3.1.1 on 2021-06-15 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0053_users_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_device',
            name='total_users',
            field=models.IntegerField(default=0, verbose_name=0),
            preserve_default=False,
        ),
    ]
