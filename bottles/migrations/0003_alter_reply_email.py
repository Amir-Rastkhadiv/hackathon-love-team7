# Generated by Django 3.2 on 2022-02-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottles', '0002_auto_20220226_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]