# Generated by Django 4.0.1 on 2022-01-31 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0009_alter_pokemon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(upload_to='./pokemon/static/imagens'),
        ),
    ]
