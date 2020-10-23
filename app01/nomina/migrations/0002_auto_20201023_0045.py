# Generated by Django 3.1.2 on 2020-10-23 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=50, verbose_name='Puesto que desempeña.')),
                ('price', models.IntegerField(verbose_name='Sueldo por día.')),
                ('working_day', models.IntegerField(verbose_name='Dias laborados.')),
            ],
            options={
                'verbose_name': 'Puesto',
                'verbose_name_plural': 'Puestos',
            },
        ),
        migrations.AlterModelOptions(
            name='direction',
            options={'verbose_name': 'Dirección', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterField(
            model_name='direction',
            name='house_number',
            field=models.IntegerField(verbose_name='Numero de casa.'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='street_name',
            field=models.CharField(max_length=50, verbose_name='Nombre de la calle.'),
        ),
    ]
