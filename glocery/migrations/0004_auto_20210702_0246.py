# Generated by Django 3.2.4 on 2021-07-02 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('glocery', '0003_alter_glocery_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='GloceryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='glocery_category/')),
            ],
        ),
        migrations.CreateModel(
            name='SavedGlocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_saved', models.DateTimeField(auto_now_add=True)),
                ('glocery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glocery_saves', to='glocery.glocery')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_gloceries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='glocery',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gloceries', to='glocery.glocerycategory'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]