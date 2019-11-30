from django.contrib import admin
from .models import Companiess
from .models import Employees

# Register your models here.
class CompaniessAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'img', 'website')


admin.site.register(Companiess, CompaniessAdmin)


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'email', 'phone')


admin.site.register(Employees, EmployeesAdmin)