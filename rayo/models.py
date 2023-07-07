from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import EmailValidator, MinLengthValidator
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.

class cliente (models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=10)
    nom_cli = models.CharField(blank=False, null=False, max_length=20)
    appater_cli = models.CharField(blank=False, null=False,max_length=20)
    apmater_cli = models.CharField(blank=False,null=False,max_length=20)
    email_cli = models.EmailField(blank=False,null=False,unique=True,validators=[EmailValidator(), MinLengthValidator(8)])
    contrasena_cli = models.CharField(blank=False,null=False,max_length=100)
    def set_password(self, raw_password):
        self.contrasena_cli = make_password(raw_password)        
    def check_password(self, raw_password):
        return check_password(raw_password, self.contrasena_cli)
    patente = models.CharField(blank=False, null=False, max_length=6)
    fono_cli = models.IntegerField(blank=False, null=False,)
    direccion_cli = models.CharField(blank=False,null=False,max_length=250)
    def __str__(self):
        return str(self.nom_cli)+" "+str(self.appater_cli)+ " "+ str(self.apmater_cli)    

class mecanico(models.Model):
    rut_meca = models.CharField(primary_key=True, max_length=10)
    nom_meca = models.CharField(blank=False, null=False, max_length=20)
    appater_meca = models.CharField(blank=False, null=False,max_length=20)
    apmater_meca = models.CharField(blank=False,null=False,max_length=20)
    email_meca = models.EmailField(blank=False,null=False,unique=True,validators=[EmailValidator(), MinLengthValidator(8)])
    contrasena_meca = models.CharField(blank=False,null=False,max_length=100)
    def set_password(self, raw_password):
        self.contrasena_meca = make_password(raw_password)        
    def check_password(self, raw_password):
        return check_password(raw_password, self.contrasena_meca)
    fono_meca = models.IntegerField(blank=False, null=False,)
    direccion_meca = models.CharField(blank=False,null=False,max_length=250)
    def __str__(self):
        return str(self.nom_meca)+" "+str(self.appater_meca)+ " "+ str(self.apmater_meca) 

class administrador(models.Model):
    rut_admin = models.CharField(primary_key=True, max_length=10)
    nom_admin = models.CharField(blank=False, null=False, max_length=20)
    appater_admin = models.CharField(blank=False, null=False,max_length=20)
    apmater_admin = models.CharField(blank=False,null=False,max_length=20)
    email_admin = models.EmailField(blank=False,null=False,unique=True,validators=[EmailValidator(), MinLengthValidator(8)])
    contrasena_admin = models.CharField(blank=False,null=False,max_length=100)
    def set_password(self, raw_password):
        self.contrasena_admin = make_password(raw_password)        
    def check_password(self, raw_password):
        return check_password(raw_password, self.contrasena_admin)
    fono_admin = models.IntegerField(blank=False, null=False,)
    direccion_admin = models.CharField(blank=False,null=False,max_length=250)
    def __str__(self):
        return str(self.nom_admin)+" "+str(self.appater_admin)+ " "+ str(self.apmater_admin)
    
class Archivo (models.Model):
    id_archivo = models.AutoField(primary_key=True, unique=True, blank=True)
    rut_meca = models.ForeignKey('mecanico', on_delete=models.CASCADE)
    tipo_vehiculo = models.CharField(blank=False,null=False,max_length=20)
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    tiempo_estimado = models.CharField(blank=False,null=False,max_length=20)
    diagnostico = models.CharField(blank=False,null=False,max_length=20)
    herramientas = models.CharField(blank=False,null=False,max_length=20)
    descripcion = models.CharField(blank=False,null=False,max_length=20)
    imagen = models.ImageField(upload_to='archivos', null=True)
    def __str__(self):
        return str(self.id_archivo)

class Categoria (models.Model):
    id_categoria = models.AutoField(primary_key=True,unique=True,)
    nombre_cat = models.CharField(blank=False,null=False,max_length=20)
    estado = models.BooleanField()
    def __str__(self):
        return str(self.nombre_cat)

class palabraClave (models.Model):
    id_palabras = models.AutoField(primary_key=True, unique=True)
    palabra = models.CharField(blank=False,null=False, max_length=20)
    categorias = models.ManyToManyField('Categoria')
    def __str__(self):
        return str(self.palabra)
    
    
