# Generated by Django 3.1.1 on 2020-10-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201021_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='uploader_id',
            field=models.IntegerField(),
        ),
    ]
