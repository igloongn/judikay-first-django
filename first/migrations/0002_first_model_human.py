# Generated by Django 4.0.2 on 2022-03-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='first_model',
            name='human',
            field=models.BooleanField(default=True),
        ),
    ]
