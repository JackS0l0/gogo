# Generated by Django 5.1.6 on 2025-02-11 12:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='girls',
            name='desc',
            field=ckeditor.fields.RichTextField(default='none', verbose_name='Описание'),
        ),
    ]
