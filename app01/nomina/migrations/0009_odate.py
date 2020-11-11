# Generated by Django 3.1.2 on 2020-11-11 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0008_auto_20201110_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='Estado de pago')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
    ]
