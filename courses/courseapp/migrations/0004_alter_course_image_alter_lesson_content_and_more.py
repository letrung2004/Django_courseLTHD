# Generated by Django 5.1.2 on 2024-10-21 08:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_tag_lesson_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='course/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(default='default content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(default=None, upload_to='course/%Y/%m'),
        ),
    ]
