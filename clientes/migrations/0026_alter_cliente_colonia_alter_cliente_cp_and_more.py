# Generated by Django 4.0.6 on 2022-08-18 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0025_alter_cliente_colonia_alter_cliente_cp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(choices=[('D1CIhgz', 'D1CIhgz'), ('Sn4cdh', 'Sn4cdh'), ('MVVuVSlFmOA', 'MVVuVSlFmOA'), ('XSTTmsuj050', 'XSTTmsuj050'), ('acIpHro9M6Za', 'acIpHro9M6Za'), ('VBKrwMwU9', 'VBKrwMwU9'), ('DVYhMMVqA', 'DVYhMMVqA')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cp',
            field=models.CharField(choices=[('D9IOG', 'D9IOG'), ('hvCNN', 'hvCNN'), ('btsFX', 'btsFX'), ('Go7bY', 'Go7bY'), ('QCxR3', 'QCxR3'), ('M23xa', 'M23xa'), ('Kf8QW', 'Kf8QW'), ('uPdPl', 'uPdPl'), ('bC1v3', 'bC1v3'), ('5zABZ', '5zABZ')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='municipio',
            field=models.CharField(choices=[('V33qoVtK', 'V33qoVtK'), ('9ue7oWBp5Ci4i', '9ue7oWBp5Ci4i')], default=1, max_length=150),
        ),
    ]
