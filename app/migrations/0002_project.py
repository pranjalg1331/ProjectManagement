# Generated by Django 5.0.6 on 2024-06-01 15:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('contributor', models.ManyToManyField(related_name='contributed_projects', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ManyToManyField(related_name='owned_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
