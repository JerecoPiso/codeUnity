# Generated by Django 3.1.1 on 2021-04-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_projects_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='comments',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
