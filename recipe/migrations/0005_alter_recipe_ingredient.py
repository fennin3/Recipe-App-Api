# Generated by Django 3.2.4 on 2021-11-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20211103_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredient',
            field=models.CharField(max_length=100000),
        ),
    ]
