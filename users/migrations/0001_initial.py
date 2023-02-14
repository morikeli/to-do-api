# Generated by Django 4.1.6 on 2023-02-14 16:31

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
            name='UserProfile',
            fields=[
                ('id', models.CharField(editable=False, max_length=18, primary_key=True, serialize=False, unique=True)),
                ('gender', models.CharField(max_length=7)),
                ('phone_no', models.CharField(max_length=14)),
                ('country', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(default='default.png', upload_to='Users-Dps/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Users Profiles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('task', models.CharField(max_length=30)),
                ('subtitle', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
                'ordering': ['-created'],
            },
        ),
    ]