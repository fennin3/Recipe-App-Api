# Generated by Django 3.2.4 on 2021-06-30 04:01

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Profile_pic/')),
                ('phone', models.CharField(max_length=16)),
                ('language', models.CharField(default='en', max_length=10)),
                ('points', models.IntegerField(default=0)),
                ('notifications', models.BooleanField(default=False)),
                ('email_news', models.BooleanField(default=False)),
                ('special_offers', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('momo_name', models.CharField(blank=True, max_length=255, null=True)),
                ('momo_number', models.CharField(blank=True, max_length=16, null=True)),
                ('holder_name', models.CharField(blank=True, max_length=255, null=True)),
                ('card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('exp_month', models.IntegerField(blank=True, null=True)),
                ('exp_year', models.IntegerField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments_methods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('recipient_name', models.CharField(max_length=500)),
                ('recipient_phone', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=1000)),
                ('town', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('instruction', models.CharField(max_length=10000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='more_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
