# Generated by Django 3.1.1 on 2021-03-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='comments',
            field=models.IntegerField(null=True),
        ),
    ]