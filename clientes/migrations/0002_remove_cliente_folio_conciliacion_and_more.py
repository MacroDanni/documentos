# Generated by Django 4.0.6 on 2022-08-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='folio_conciliacion',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cantidad_en_conciliacion',
            field=models.CharField(default=0, help_text='Cantidad en Conciliacion', max_length=10),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='10082022205432ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('j1IXVdUeaUU2iZn', 'j1IXVdUeaUU2iZn'), ('WqDnFP7', 'WqDnFP7'), ('K63AacMV', 'K63AacMV'), ('ajMfDUD', 'ajMfDUD'), ('9uvmXwx', '9uvmXwx'), ('pnFtYG746OEW', 'pnFtYG746OEW'), ('5iJv69nuQhkO', '5iJv69nuQhkO')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('qvndi', 'qvndi'), ('Btbzx', 'Btbzx'), ('6JD4E', '6JD4E'), ('rqE5y', 'rqE5y'), ('puLuO', 'puLuO'), ('qkbEy', 'qkbEy'), ('Zwpk2', 'Zwpk2'), ('fLO5F', 'fLO5F'), ('yCNiN', 'yCNiN'), ('AHm7R', 'AHm7R')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('vJNDKQlGOeK5l2', 'vJNDKQlGOeK5l2'), ('AxGYs', 'AxGYs'), ('V0itkK', 'V0itkK'), ('0KmIS', '0KmIS')], default=1, max_length=150),
        ),
    ]
