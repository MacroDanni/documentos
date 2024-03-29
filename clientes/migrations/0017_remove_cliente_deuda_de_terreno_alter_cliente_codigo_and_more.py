# Generated by Django 4.0.6 on 2022-08-15 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='deuda_de_terreno',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022192949ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('b0UBy', 'b0UBy'), ('1iYCod', '1iYCod'), ('l0h403MPM', 'l0h403MPM'), ('2KZiy', '2KZiy'), ('r8T7RDZC', 'r8T7RDZC'), ('EiUpERFqJW', 'EiUpERFqJW')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='costo_del_terreno',
            field=models.CharField(default=0, help_text='Costo Terreno', max_length=11),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('gq5pK', 'gq5pK'), ('VtfMB', 'VtfMB'), ('DHpMQ', 'DHpMQ'), ('jUbxV', 'jUbxV'), ('Sb11j', 'Sb11j'), ('bbJDN', 'bbJDN'), ('rVdvc', 'rVdvc'), ('lEu9m', 'lEu9m'), ('ioEs9', 'ioEs9'), ('eiPsP', 'eiPsP')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('3YM90g1c', '3YM90g1c'), ('9lbPxlq64Y0PX', '9lbPxlq64Y0PX'), ('l0pmZNErhDg8kdT', 'l0pmZNErhDg8kdT'), ('DAKf2', 'DAKf2'), ('ZXAwuJCZtrzVu', 'ZXAwuJCZtrzVu')], default=1, max_length=150),
        ),
    ]
