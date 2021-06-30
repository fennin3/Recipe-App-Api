# Generated by Django 3.2.4 on 2021-06-30 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='category/')),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='recipe_images/')),
                ('no_of_consumers', models.IntegerField(default=1)),
                ('nutritional_details', models.CharField(max_length=100000)),
                ('min_duration', models.IntegerField()),
                ('max_duration', models.IntegerField()),
                ('attribution', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100000)),
                ('ingredient', models.CharField(max_length=100000)),
                ('allergies', models.CharField(max_length=100000)),
                ('total_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=2)),
                ('total_raters', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=2)),
                ('vid_instruction', models.FileField(upload_to='video_instructions/')),
                ('text_instruction', models.CharField(max_length=100000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipe.category')),
                ('reviews', models.ManyToManyField(blank=True, null=True, to='recipe.Review')),
                ('tips_from_chef', models.ManyToManyField(blank=True, null=True, to='recipe.Tip')),
            ],
        ),
    ]
