# Generated by Django 3.1 on 2020-08-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0016_remove_line_have_sub_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Precio total'),
        ),
    ]
