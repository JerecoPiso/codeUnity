# Generated by Django 3.1.1 on 1980-01-01 14:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_remove_developers_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='developers',
            name='photo',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='developers',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]