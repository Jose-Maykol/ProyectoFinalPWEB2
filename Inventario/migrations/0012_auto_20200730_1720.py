# Generated by Django 3.0.7 on 2020-07-30 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0011_auto_20200730_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio unitario'),
        ),
    ]
