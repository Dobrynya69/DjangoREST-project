# Generated by Django 4.1.4 on 2022-12-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageAPI', '0002_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='text',
            new_name='title',
        ),
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
