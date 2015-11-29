from django.contrib import admin
from .models import Pais, Ciudad, Lenguaje

# Register your models here.

class CiudadInline(admin.TabularInline):
    model = Ciudad
    extra = 0

class LenguajeInline(admin.TabularInline):
    model = Lenguaje
    extra = 0

class AdminPais(admin.ModelAdmin):
    fieldsets = [
        ('Informacion General',{'fields':['Codigo', 'Nombre', 'Continente']}),
        ('Informacion Adicional',{'fields':['Region', 'Area', 'Independence'], 'classes':['collapse']}),
    ]
    inlines = [CiudadInline, LenguajeInline]
    list_display = ('Nombre', 'Codigo')
    list_filter = ['Nombre']

admin.site.register(Pais, AdminPais)

