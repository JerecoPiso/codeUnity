# Generated by Django 3.1.1 on 2021-04-01 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210402_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.language'),
        ),
    ]