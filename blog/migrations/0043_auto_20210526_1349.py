# Generated by Django 3.1.1 on 2021-05-26 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_questions_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionTags',
        ),
        migrations.AddField(
            model_name='questions',
            name='tags',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]