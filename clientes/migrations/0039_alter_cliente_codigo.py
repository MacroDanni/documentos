# Generated by Django 4.0.6 on 2022-09-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0038_alter_cliente_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(default='08092022110320ACI', max_length=100),
        ),
    ]
