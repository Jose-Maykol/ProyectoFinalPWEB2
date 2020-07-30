# Generated by Django 3.0.7 on 2020-07-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0020_locaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metodos_envio',
            fields=[
                ('id_metodo', models.AutoField(primary_key=True, serialize=False)),
                ('metodo_envio', models.CharField(max_length=255, null=True, verbose_name='Metodo del envio')),
            ],
            options={
                'verbose_name': 'Metodo_envio',
                'verbose_name_plural': 'Metodos_envios',
                'ordering': ['metodo_envio'],
            },
        ),
        migrations.AlterField(
            model_name='locaciones',
            name='desc_loc',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripción de la localizacion'),
        ),
    ]
