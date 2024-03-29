# Generated by Django 4.0.6 on 2022-08-11 01:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_remove_cliente_folio_conciliacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('fecha_de_pago', models.DateTimeField(default=django.utils.timezone.now)),
                ('comprobante_de_pago', models.FileField(null=True, upload_to='clientes/filesbk/')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]
