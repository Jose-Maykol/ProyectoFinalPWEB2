# Generated by Django 3.1 on 2020-08-06 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventario', '0011_auto_20200806_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='Inventario.product', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='Inventario.entry'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='Inventario.inventory', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='user_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Nombre del cliente'),
        ),
    ]
