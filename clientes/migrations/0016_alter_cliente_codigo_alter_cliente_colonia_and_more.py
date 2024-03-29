# Generated by Django 4.0.6 on 2022-08-15 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0015_alter_cliente_codigo_alter_cliente_colonia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='14082022190940ACI', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('b0J2tO', 'b0J2tO'), ('OUyBPodcDunB', 'OUyBPodcDunB'), ('YOiPiCMHny6M', 'YOiPiCMHny6M'), ('7wd3Z7DmvxfA', '7wd3Z7DmvxfA'), ('hSGTlgKRA', 'hSGTlgKRA'), ('vU0dYUF3YQg', 'vU0dYUF3YQg'), ('kamEg2Cz', 'kamEg2Cz'), ('Pfsvs', 'Pfsvs'), ('c0Hhpbp', 'c0Hhpbp'), ('RcG0oB8pL6M', 'RcG0oB8pL6M'), ('s4dQF', 's4dQF'), ('36eQ882ms', '36eQ882ms'), ('ft4cXu6Doj0y', 'ft4cXu6Doj0y')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('ZBVtz', 'ZBVtz'), ('wItvv', 'wItvv'), ('34HZx', '34HZx'), ('bTEZ5', 'bTEZ5'), ('8kRnN', '8kRnN'), ('CfXWh', 'CfXWh'), ('Umw4g', 'Umw4g'), ('dIwqL', 'dIwqL'), ('VXoMh', 'VXoMh'), ('lbmiI', 'lbmiI')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('8FDJHGekCjWTSiS', '8FDJHGekCjWTSiS'), ('TIP3NEg3L', 'TIP3NEg3L'), ('747RLwD1uHywAHj', '747RLwD1uHywAHj')], default=1, max_length=150),
        ),
    ]
