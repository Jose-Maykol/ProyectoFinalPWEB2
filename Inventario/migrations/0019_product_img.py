# Generated by Django 3.1 on 2020-08-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0018_auto_20200812_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
