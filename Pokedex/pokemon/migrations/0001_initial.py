# Generated by Django 4.0.1 on 2022-01-31 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('name', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('type1', models.TextField(max_length=20)),
                ('type2', models.TextField(max_length=20)),
            ],
        ),
    ]
