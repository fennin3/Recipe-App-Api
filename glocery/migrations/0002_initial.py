# Generated by Django 3.2.4 on 2021-11-02 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('glocery', '0001_initial'),
        ('recipe', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='savedglocery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_gloceries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='glocery',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gloceries', to='glocery.glocerycategory'),
        ),
        migrations.AddField(
            model_name='glocery',
            name='reviews',
            field=models.ManyToManyField(blank=True, null=True, to='recipe.Review'),
        ),
    ]
