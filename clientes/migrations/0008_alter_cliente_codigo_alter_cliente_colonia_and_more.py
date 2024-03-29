# Generated by Django 4.0.6 on 2022-08-15 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022190223ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('URW0PJ7PYPO', 'URW0PJ7PYPO'), ('bR9Czq9vy78', 'bR9Czq9vy78'), ('xDz8XSOU', 'xDz8XSOU'), ('8J5zrajmOlE3Ha9', '8J5zrajmOlE3Ha9'), ('gDnl1NruF8s', 'gDnl1NruF8s'), ('w1vrydUaYVw', 'w1vrydUaYVw'), ('QB1BORb0KMrhdO0', 'QB1BORb0KMrhdO0'), ('jBPRW', 'jBPRW'), ('Z9uIMt9l', 'Z9uIMt9l'), ('oH25w4', 'oH25w4')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('LCYoa', 'LCYoa'), ('VT9Kl', 'VT9Kl'), ('zQtV9', 'zQtV9'), ('v1Y4m', 'v1Y4m'), ('IoezH', 'IoezH'), ('AbjMT', 'AbjMT'), ('0EoqR', '0EoqR'), ('MU6ap', 'MU6ap'), ('7A6co', '7A6co'), ('OPddW', 'OPddW')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('mzAqJTPRi', 'mzAqJTPRi'), ('OAYGpI', 'OAYGpI')], default=1, max_length=150),
        ),
    ]
