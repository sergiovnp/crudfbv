# Generated by Django 2.1.1 on 2018-09-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=9, verbose_name='Nombre'),
        ),
    ]