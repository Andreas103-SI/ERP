# Generated by Django 5.1.7 on 2025-03-24 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculo',
            old_name='año',
            new_name='anio',
        ),
    ]
