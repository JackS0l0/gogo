# Generated by Django 5.1.6 on 2025-02-11 12:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_girls_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='girls',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
