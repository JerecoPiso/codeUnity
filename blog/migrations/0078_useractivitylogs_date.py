# Generated by Django 3.1.1 on 2021-09-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0077_useractivitylogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivitylogs',
            name='date',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]