# Generated by Django 3.1.1 on 2020-10-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='downloads',
            field=models.IntegerField(blank=True),
        ),
    ]
