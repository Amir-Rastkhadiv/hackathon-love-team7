# Generated by Django 3.2 on 2022-02-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottles', '0003_alter_reply_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='body',
            field=models.CharField(max_length=100),
        ),
    ]