# Generated by Django 3.1.1 on 2021-09-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0075_auto_20210903_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temppdf',
            name='pdfname',
            field=models.CharField(max_length=255),
        ),
    ]
