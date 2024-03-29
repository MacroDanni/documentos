# Generated by Django 4.0.6 on 2022-08-14 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022171127ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('HDseR4gh3n3xxcy', 'HDseR4gh3n3xxcy'), ('xPV5xIccY', 'xPV5xIccY'), ('coRBb0s7SbN0gVB', 'coRBb0s7SbN0gVB'), ('CzUP7NIE6W', 'CzUP7NIE6W'), ('t5zhRd69XrK', 't5zhRd69XrK'), ('VvQblR4qbet', 'VvQblR4qbet')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('foMkC', 'foMkC'), ('YFrMo', 'YFrMo'), ('F8ebU', 'F8ebU'), ('c4sin', 'c4sin'), ('HIin2', 'HIin2'), ('eIil0', 'eIil0'), ('cvsAv', 'cvsAv'), ('wgn2n', 'wgn2n'), ('2UUUP', '2UUUP'), ('HSq1v', 'HSq1v')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('5U1AaPEVoKytJq1', '5U1AaPEVoKytJq1'), ('GwXddfTyT6hn', 'GwXddfTyT6hn'), ('HEpex9U', 'HEpex9U')], default=1, max_length=150),
        ),
    ]
