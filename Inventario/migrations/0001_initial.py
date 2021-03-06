# Generated by Django 3.0.7 on 2020-07-24 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(null=True)),
                ('operation_type', models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(null=True)),
                ('cash', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('operation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Operation')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('price_in', models.FloatField(null=True)),
                ('price_out', models.FloatField(null=True)),
                ('presentation', models.CharField(choices=[('Caja', 'Caja'), ('Bolsa', 'Bolsa')], max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='operation',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Product'),
        ),
    ]
