# Generated by Django 3.0.7 on 2020-07-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0004_auto_20200727_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_compras',
            fields=[
                ('id_detalle_compra', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_orden', models.IntegerField(verbose_name='Cantidad de orden')),
                ('cantidad_recibida', models.IntegerField(verbose_name='Cantidad recibida')),
            ],
            options={
                'verbose_name': 'Detalle_compra',
                'verbose_name_plural': 'Detalle_compras',
                'ordering': ['id_detalle_compra'],
            },
        ),
        migrations.CreateModel(
            name='Historia_mov',
            fields=[
                ('id_inv_hist', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_mov', models.CharField(choices=[('ENTRADA', 'ENTRADA'), ('SALIDA', 'SALIDA')], max_length=25, verbose_name='Tipo de movimiento')),
                ('cant_mov', models.IntegerField(verbose_name='Cantidad de movimiento')),
                ('fecha_mov', models.DateField(auto_now=True, verbose_name='Fecha de movimiento')),
                ('hora_mov', models.DateTimeField(auto_now=True, verbose_name='Hora de movimiento')),
                ('lote', models.CharField(max_length=255, null=True, verbose_name='Código del lote del producto')),
                ('caducidad', models.DateField(verbose_name='Fecha de caducidad')),
            ],
            options={
                'verbose_name': 'Historia_mov',
                'verbose_name_plural': 'Historias_mov',
                'ordering': ['fecha_mov'],
            },
        ),
        migrations.CreateModel(
            name='Locaciones',
            fields=[
                ('id_loc', models.AutoField(primary_key=True, serialize=False)),
                ('cod_loc', models.CharField(max_length=15, verbose_name='Codigo de la localizacion')),
                ('desc_loc', models.CharField(max_length=150, null=True, verbose_name='Descripción de la localizacion')),
                ('isla', models.CharField(max_length=15, null=True, verbose_name='Codigo de isla de almacen')),
                ('seccion', models.CharField(max_length=15, null=True, verbose_name='Codigo de sección')),
                ('nivel', models.CharField(max_length=15, null=True, verbose_name='Codigo de nivel')),
                ('contenedor', models.CharField(max_length=15, null=True, verbose_name='Codigo de contenedor')),
                ('capacidad', models.IntegerField(null=True, verbose_name='Capacidad del contenedor')),
            ],
            options={
                'verbose_name': 'Locacion',
                'verbose_name_plural': 'Locaciones',
                'ordering': ['cod_loc'],
            },
        ),
        migrations.CreateModel(
            name='Ordenes_compra',
            fields=[
                ('id_orden_compra', models.AutoField(primary_key=True, serialize=False)),
                ('numero_compra', models.CharField(max_length=255, null=True, verbose_name='Numero de la compra')),
                ('descripción_compra', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion de la compra')),
                ('fecha_orden', models.DateField(verbose_name='Fecha de orden')),
                ('fecha_embarque', models.DateField(verbose_name='Fecha de embarque')),
                ('fecha_requerida', models.DateField(verbose_name='Fecha requerida')),
                ('fecha_promesa', models.DateField(verbose_name='Fecha promesa')),
            ],
            options={
                'verbose_name': 'Orden_compra',
                'verbose_name_plural': 'Ordenes_compra',
                'ordering': ['id_orden_compra'],
            },
        ),
    ]