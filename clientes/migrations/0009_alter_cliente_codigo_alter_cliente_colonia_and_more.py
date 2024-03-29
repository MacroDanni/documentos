# Generated by Django 4.0.6 on 2022-08-15 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022190230ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('fRjXdSfRUVa', 'fRjXdSfRUVa'), ('nOUaOkGOqE3KP', 'nOUaOkGOqE3KP'), ('Wa0JoKbFCVeMeu', 'Wa0JoKbFCVeMeu'), ('xtf5j', 'xtf5j'), ('OMZzibpngCmOBds', 'OMZzibpngCmOBds')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('FcHOr', 'FcHOr'), ('zqQMu', 'zqQMu'), ('hdQM7', 'hdQM7'), ('Y4VKP', 'Y4VKP'), ('5dU8y', '5dU8y'), ('txjID', 'txjID'), ('DOZqs', 'DOZqs'), ('cVFlt', 'cVFlt'), ('OPJhM', 'OPJhM'), ('jdzmc', 'jdzmc')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('bU5hlm2T6p', 'bU5hlm2T6p'), ('K590pLWEyWi', 'K590pLWEyWi'), ('nIup2f5', 'nIup2f5')], default=1, max_length=150),
        ),
    ]
