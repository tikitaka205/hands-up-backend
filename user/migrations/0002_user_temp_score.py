# Generated by Django 4.1.3 on 2022-12-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='temp_score',
            field=models.SmallIntegerField(default=0),
        ),
    ]
