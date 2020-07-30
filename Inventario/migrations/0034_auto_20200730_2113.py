# Generated by Django 3.0.7 on 2020-07-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0033_auto_20200730_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenes_compra',
            name='fecha_embarque',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de embarque'),
        ),
        migrations.AddField(
            model_name='ordenes_compra',
            name='fecha_orden',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de orden'),
        ),
        migrations.AddField(
            model_name='ordenes_compra',
            name='fecha_promesa',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha promesa'),
        ),
        migrations.AddField(
            model_name='ordenes_compra',
            name='fecha_requerida',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha requerida'),
        ),
    ]
