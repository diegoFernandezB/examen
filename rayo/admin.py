from django.contrib import admin
from .models import cliente, administrador, mecanico, Archivo

# Register your models here.
admin.site.register(cliente)
admin.site.register(administrador)
admin.site.register(mecanico)
admin.site.register(Archivo)