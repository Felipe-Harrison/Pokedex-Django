# Generated by Django 4.0.1 on 2022-02-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0013_pokemon_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image_name',
            field=models.TextField(default=None, max_length=50),
        ),
    ]
