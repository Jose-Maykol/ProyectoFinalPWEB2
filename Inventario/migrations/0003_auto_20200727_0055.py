# Generated by Django 3.0.7 on 2020-07-27 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_auto_20200727_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='id',
            new_name='id_producto',
        ),
    ]
