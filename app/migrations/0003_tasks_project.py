# Generated by Django 5.0.6 on 2024-06-01 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
    ]
