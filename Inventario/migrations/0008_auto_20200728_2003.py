# Generated by Django 3.0.7 on 2020-07-29 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0007_auto_20200728_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Inventario.Inventory', verbose_name='Producto'),
        ),
    ]
