# Generated by Django 3.1.2 on 2020-11-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0007_oper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oper',
            name='cut',
            field=models.DateTimeField(verbose_name='Fecha de corte:'),
        ),
    ]
