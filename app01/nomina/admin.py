from django.contrib import admin
from .models import Direction, Task, Employee, Oper
# Register your models here.

admin.site.register(Direction)
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(Oper)