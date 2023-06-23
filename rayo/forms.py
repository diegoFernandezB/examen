from django import forms
from .models import mecanico, cliente, administrador, Archivo

from django.forms import ModelForm

class mecanicoForm(forms.ModelForm):
    class Meta:
        model = mecanico
        exclude = ('contrasena_meca',)
        fields = ["rut_meca","nom_meca","appater_meca","apmater_meca","email_meca","fono_meca","direccion_meca"]
        labels = {'rut_meca':'Rut Mecánico',
                  'nom_meca':'Nombre',
                  'appater_meca':'Apellido Paterno',
                  'apmater_meca':'Apellido Materno',
                  'email_meca':'Correo Electrónico',
                  'fono_meca':'Teléfono',
                  'direccion_meca':'Dirección'}
        widgets = {
            'rut_meca': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'nom_meca': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'appater_meca': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'apmater_meca': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'email_meca': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'fono_meca': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'direccion_meca': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        exclude = ('contrasena_cli',)
        fields = ["rut_cli","nom_cli","appater_cli","apmater_cli","email_cli","patente","fono_cli","direccion_cli"]
        labels = {'rut_cli':'Rut Cliente',
                  'nom_cli':'Nombre',
                  'appater_cli':'Apellido Paterno',
                  'apmater_cli':'Apellido Materno',
                  'email_cli':'Correo Electrónico',
                  'patente':'Patente',
                  "fono_cli":"Teléfono",
                  'direccion_cli':'Dirección'}
        widgets = {
            'rut_cli': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'nom_cli': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'appater_cli': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'apmater_cli': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'email_cli': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'patente': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'fono_cli': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'direccion_cli': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }

class administradorForm(forms.ModelForm):
    class Meta:
        model = administrador
        exclude = ('contrasena_admin',)
        fields = ["rut_admin","nom_admin","appater_admin","apmater_admin","email_admin","fono_admin","direccion_admin"]
        labels = {'rut_admin':'Rut Mecánico',
                  'nom_admin':'Nombre',
                  'appater_admin':'Apellido Paterno',
                  'apmater_admin':'Apellido Materno',
                  'email_admin':'Correo Electronico',
                  'fono_admin':'Teléfono',
                  'direccion_admin':'Dirección'}
        widgets = {
            'rut_admin': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'nom_admin': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'appater_admin': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'apmater_admin': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'email_admin': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'fono_admin': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'direccion_admin': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        exclude = ('id_archivo',)
        fields = ["tipo_vehiculo","fecha_ingreso","tiempo_estimado","diagnostico","herramientas","descripcion","imagen"]
        labels = {'tipo_vehiculo':'Tipo Vehículo',
                  'fecha_ingreso':'Fecha de Ingreso',
                  'tiempo_estimado':'Tiempo Estimado',
                  'diagnostico':'Diagnóstico',
                  'herramientas':'Herraientas',
                  'descripcion':'Descripción',
                  'imagen':'Imagen'}
        widgets = {
            'tipo_vehiculo': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'fecha_ingreso': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'tiempo_estimado': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'diagnostico': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'herramientas': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }
