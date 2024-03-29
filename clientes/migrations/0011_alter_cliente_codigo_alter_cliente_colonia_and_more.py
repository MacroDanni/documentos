# Generated by Django 4.0.6 on 2022-08-15 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022190250ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('GabO04Y1lh', 'GabO04Y1lh'), ('UkG03hQbNggUh0O', 'UkG03hQbNggUh0O'), ('fxW2iYwsiykRPm2', 'fxW2iYwsiykRPm2'), ('KsrNx481YFLe', 'KsrNx481YFLe'), ('zH77BWRxh1TvEcv', 'zH77BWRxh1TvEcv'), ('LQbIJ', 'LQbIJ'), ('eW0ZpUKfIpids', 'eW0ZpUKfIpids'), ('TQfRPBSPTWYwddl', 'TQfRPBSPTWYwddl'), ('t8DkZI2d5Nb', 't8DkZI2d5Nb')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('F4UMM', 'F4UMM'), ('hi7h1', 'hi7h1'), ('qG1yN', 'qG1yN'), ('YWFj5', 'YWFj5'), ('ywLW3', 'ywLW3'), ('JDicC', 'JDicC'), ('pJMN4', 'pJMN4'), ('rjtTr', 'rjtTr'), ('ojUTj', 'ojUTj'), ('f9Mpy', 'f9Mpy')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('3NykZ6L2k', '3NykZ6L2k'), ('bWWxSwFWPX', 'bWWxSwFWPX'), ('ITzVkijYU', 'ITzVkijYU')], default=1, max_length=150),
        ),
    ]
