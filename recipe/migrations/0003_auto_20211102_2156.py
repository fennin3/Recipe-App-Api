# Generated by Django 3.2.4 on 2021-11-02 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='images/recipe_category/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/recipe_images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='vid_instruction',
            field=models.FileField(blank=True, null=True, upload_to='videos/video_instructions/'),
        ),
        migrations.CreateModel(
            name='TipImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/tip_images/')),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='recipe.tip')),
            ],
        ),
    ]
