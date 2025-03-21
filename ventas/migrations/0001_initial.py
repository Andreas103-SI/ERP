# Generated by Django 5.1.7 on 2025-03-21 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni_pasaporte', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contrato', models.TextField()),
                ('fecha', models.DateField()),
                ('valor_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='VentaVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.vehiculo')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta')),
            ],
            options={
                'unique_together': {('venta', 'vehiculo')},
            },
        ),
    ]
