from django.db import models
# Create your models here.

class Direction(models.Model):
    street_name=models.CharField(max_length=50,verbose_name='Nombre de la calle.')
    house_number=models.PositiveIntegerField(verbose_name='Numero de casa.')
    reference=models.CharField(max_length=100,verbose_name='Referencia.')

    def __str__(self):
        return self.street_name

    class Meta:
        verbose_name='Dirección'
        verbose_name_plural='Direcciones'


class Task(models.Model):
    operation=models.CharField(max_length=50,verbose_name='Puesto que desempeña.')
    price=models.PositiveIntegerField(verbose_name='Sueldo por día.')
    working_day=models.PositiveIntegerField(verbose_name='Dias laborados.')
    

    def __str__(self):
        return self.operation

    class Meta:
        verbose_name='Puesto'
        verbose_name_plural='Puestos'


class Employee(models.Model):
    name=models.CharField(max_length=50,verbose_name='Nombre.')
    surname=models.CharField(max_length=100,verbose_name='Apellidos.')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Puesto')
    direction_id = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Dirección')
    phone=models.CharField(max_length=13,verbose_name='Numero de telefono.')

    def __str__(self):
        return "{0}--{1}".format(self.name, self.task_id)

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'


class Oper(models.Model):
    ingre=models.PositiveIntegerField(verbose_name='Ingresos')
    gast=models.PositiveIntegerField(verbose_name='Gastos')
    cut=models.DateTimeField(verbose_name='Fecha de corte:')

    def __str__(self):
        return "{0}--{1}--{2}".format(self.ingre, self.gast, self.cut)

    class Meta:
        verbose_name='Otro'
        verbose_name_plural='Otras'