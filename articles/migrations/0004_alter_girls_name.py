# Generated by Django 5.1.6 on 2025-02-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_girls_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girls',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Имя'),
        ),
    ]
