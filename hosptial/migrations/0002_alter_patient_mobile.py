# Generated by Django 4.0.4 on 2022-06-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosptial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
