# Generated by Django 3.1.1 on 1980-01-01 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_19800101_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]