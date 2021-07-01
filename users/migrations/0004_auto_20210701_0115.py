# Generated by Django 3.2.4 on 2021-07-01 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glocery', '__first__'),
        ('recipe', '0002_auto_20210630_1648'),
        ('users', '0003_remove_preorderingcalender_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='preorderingcalender',
            name='glocery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='glocery.glocery'),
        ),
        migrations.AddField(
            model_name='preorderingcalender',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe'),
        ),
    ]