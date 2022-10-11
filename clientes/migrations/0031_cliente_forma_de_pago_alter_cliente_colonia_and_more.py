# Generated by Django 4.0.6 on 2022-08-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0030_alter_cliente_colonia_alter_cliente_cp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='forma_de_pago',
            field=models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')], default='nuevo', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('uOEWuFvbq2t', 'uOEWuFvbq2t'), ('bV48YVY7qo8RC', 'bV48YVY7qo8RC'), ('MpakVRN', 'MpakVRN'), ('O5Gzt6jRXAs', 'O5Gzt6jRXAs'), ('Jb7RywaMSOGjEfj', 'Jb7RywaMSOGjEfj'), ('jWo46B1', 'jWo46B1'), ('nWHyzOQAGbHB', 'nWHyzOQAGbHB')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('LpHbu', 'LpHbu'), ('MFXXf', 'MFXXf'), ('ZXp6k', 'ZXp6k'), ('DHX49', 'DHX49'), ('oP4tf', 'oP4tf'), ('zlK9v', 'zlK9v'), ('z9tPz', 'z9tPz'), ('2iF6j', '2iF6j'), ('mWDEn', 'mWDEn'), ('Nw8W4', 'Nw8W4')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estatus_pago',
            field=models.CharField(choices=[('nuevo', 'Nuevo'), ('corriente', 'Al corriente'), ('atraso', 'Atraso'), ('pendiente', 'Pendiente'), ('disputa', 'Disputa'), ('liquidado', 'Liquidado')], default='nuevo', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('M7qCvZ1Zva5S6a4', 'M7qCvZ1Zva5S6a4'), ('PeJocFQBSg9YY', 'PeJocFQBSg9YY'), ('KWlDR4b', 'KWlDR4b'), ('g2isqBtrQj8Q', 'g2isqBtrQj8Q'), ('xCPmZnrv0', 'xCPmZnrv0')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='notificaciones',
            field=models.CharField(choices=[('recibo', 'Recibo'), ('digital', 'Digital')], default='recibo', max_length=50),
        ),
    ]