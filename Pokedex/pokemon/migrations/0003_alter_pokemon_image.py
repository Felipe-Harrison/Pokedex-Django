# Generated by Django 4.0.1 on 2022-01-31 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_alter_pokemon_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(upload_to='./imagens/'),
        ),
    ]
