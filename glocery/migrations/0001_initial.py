# Generated by Django 3.2.4 on 2021-07-01 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='recipe_category/')),
            ],
        ),
        migrations.CreateModel(
            name='Glocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='recipe_images/')),
                ('description', models.CharField(max_length=100000)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='glocery.category')),
            ],
        ),
    ]