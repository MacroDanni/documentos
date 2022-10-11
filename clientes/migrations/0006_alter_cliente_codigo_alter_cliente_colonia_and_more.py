# Generated by Django 4.0.6 on 2022-08-14 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022171247ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('8BDRMZdRmCgMwJm', '8BDRMZdRmCgMwJm'), ('ttC2k3rVx', 'ttC2k3rVx'), ('nA5A7RIqWdz', 'nA5A7RIqWdz'), ('fYwiInofaRYqHBx', 'fYwiInofaRYqHBx'), ('73tjfz7ywGbxl', '73tjfz7ywGbxl'), ('nwOehs2rIcWve', 'nwOehs2rIcWve'), ('T7YcIQL', 'T7YcIQL'), ('lcg0VTHOvq36Ts', 'lcg0VTHOvq36Ts')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('geqS2', 'geqS2'), ('kUQOE', 'kUQOE'), ('dBtvc', 'dBtvc'), ('zhDK4', 'zhDK4'), ('U37Gn', 'U37Gn'), ('S59SP', 'S59SP'), ('6selz', '6selz'), ('9FPMx', '9FPMx'), ('Rudqa', 'Rudqa'), ('qIZ2b', 'qIZ2b')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('hzXX2HWmok5', 'hzXX2HWmok5'), ('qkHUl', 'qkHUl'), ('0wGuYFEayfuzgZi', '0wGuYFEayfuzgZi'), ('9OF5TRhNL23', '9OF5TRhNL23')], default=1, max_length=150),
        ),
    ]