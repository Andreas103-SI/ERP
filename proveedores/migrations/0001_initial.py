# Generated by Django 5.0.2 on 2025-03-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
            ],
        ),
    ]
