# Generated by Django 3.2.4 on 2021-07-02 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0006_auto_20210702_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='total_rating',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=1, default=0.0, max_digits=1)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='all_ratings',
            field=models.ManyToManyField(blank=True, null=True, to='recipe.Rating'),
        ),
    ]