# Generated by Django 3.1.1 on 2021-08-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0071_auto_20210823_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='date',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]