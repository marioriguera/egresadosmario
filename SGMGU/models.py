# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.contrib.sessions.models import Session
from django.core.exceptions import ValidationError

class Organismo(models.Model):
    nombre=models.CharField(max_length=250)
    siglas=models.CharField(max_length=20)
    activo=models.BooleanField(default=True)
    hijode = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
         ordering=["nombre"]


class Categoria_usuario(models.Model):
    nombre=models.CharField(max_length=256)

    def __unicode__(self):
        return self.nombre

class Provincia(models.Model):
    nombre=models.CharField(max_length=250)
    siglas=models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    class Meta:
         ordering=["id"]


class Perfil_usuario(models.Model):
    usuario=models.OneToOneField(User)
    foto=models.ImageField(upload_to='uploads/img_usuarios/',blank=True, null=True)
    organismo=models.ForeignKey(Organismo)
    telefono=models.CharField(max_length=250,blank=True, null=True)
    categoria=models.ForeignKey(Categoria_usuario)
    provincia=models.ForeignKey(Provincia,blank=True, null=True)
    activo=models.BooleanField(default=True)

    def __unicode__(self):
        return self.usuario.username
    class Meta:
        verbose_name_plural="Perfiles de usuarios"
        verbose_name="Perfil de usuario"



class Notificacion(models.Model):
    emisor=models.ForeignKey(User,related_name="emisores")
    remitente=models.ForeignKey(User,related_name="remitentes")
    texto=models.TextField(blank=True,null=True)
    fecha=models.DateTimeField(auto_now_add=True)
    revisado=models.BooleanField(default=False)


class Municipio(models.Model):
    codigo_mes=models.CharField(max_length=100,blank=True,null=True)
    nombre=models.CharField(max_length=250)
    provincia=models.ForeignKey(Provincia)

    def __unicode__(self):
        return "%s"%(self.nombre)

    class Meta:
         ordering=["nombre"]



class Centro_estudio(models.Model):
    codigo_mes=models.CharField(max_length=100,blank=True,null=True)
    nombre=models.CharField(max_length=1000)
    siglas=models.CharField(max_length=20,blank=True,null=True)
    activo=models.BooleanField(default=True)
    provincia=models.ForeignKey(Provincia,blank=True,null=True)

    def __unicode__(self):
        return "%s"%(self.nombre)



class Carrera(models.Model):
    codigo_mes=models.CharField(max_length=100,blank=True,null=True)
    nombre=models.CharField(max_length=1000)
    activo=models.BooleanField(default=True)
    tipo=models.CharField(max_length=90,choices=[
        ('nm', 'Nivel Medio'),
        ('ns', 'Nivel Superior')
    ])

    def __unicode__(self):
        return self.nombre

    class Meta:
         ordering=["nombre"]
    
    def get_codigo_mes(self):
        return self.codigo_mes if self.codigo_mes else ''



class Causal_movimiento(models.Model):
     nombre=models.CharField(max_length=500)
     tipo=models.CharField(max_length=90,choices=[
        ('ml', 'Movimiento Laboral'),
        ('i', 'Inhabilitación'),
        ('f','Fluctuación')
    ])
     activo=models.BooleanField(default=True)


     class Meta:
         ordering=["nombre"]
         verbose_name_plural="Causales"

     def __unicode__(self):
        return self.nombre




class Persona(models.Model):
    nombre=models.CharField(max_length=250)

    class Meta:
          ordering=["nombre"]

    def __unicode__(self):
        return "%s"%(self.nombre)

from django.core.validators import RegexValidator
class Graduado(Persona):
    ci=models.CharField(max_length=11,blank=True,null=True,validators= [RegexValidator(
                regex='^[0-9]{2}(0[1-9]|1[0-2])(31|30|(0[1-9]|[1-2][0-9]))[0-9]{5}$',
                message='CI incorrecto',
            )])
    carrera=models.ForeignKey(Carrera,null=True,blank=True)
    anno_graduacion=models.IntegerField()
    centro_estudio=models.ForeignKey(Centro_estudio,null=True,blank=True)
    codigo_boleta=models.CharField(null=True,blank=True,max_length=250)
    imagen_boleta=models.ImageField(upload_to='uploads/img_boletas/',blank=True, null=True)
    detalle_direccion_residencia=models.CharField(max_length=500,null=True,blank=True)
    provincia_direccion_residencia=models.ForeignKey(Provincia,null=True,blank=True)
    municipio_direccion_residencia=models.ForeignKey(Municipio,null=True,blank=True)



class Facultado(Persona):
     cargo=models.CharField(max_length=250,blank=True,null=True)
     activo=models.BooleanField(default=True)
     organismo=models.ForeignKey(Organismo)



class Expediente(models.Model):
    graduado=models.OneToOneField(Graduado,null=True,blank=True)
    entidad_liberacion=models.CharField(max_length=500,null=True,blank=True)
    entidad_aceptacion=models.CharField(max_length=500,null=True,blank=True)
    mun_entidad_liberacion=models.ForeignKey(Municipio,related_name="municipio_liberacion",null=True,blank=True)
    mun_entidad_aceptacion=models.ForeignKey(Municipio,related_name="municipio_aceptacion",null=True,blank=True)
    causal_movimiento=models.ForeignKey(Causal_movimiento,null=True,blank=True)
    sintesis_causal_movimiento=models.CharField(max_length=1000,blank=True,null=True)
    fecha_registro=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Expediente del graudado %s"%(self.graduado.nombre)


class Expediente_movimiento_interno(Expediente):
    aprobado_por=models.CharField(max_length=500)
    organismo=models.ForeignKey(Organismo)


class Expediente_movimiento_externo(Expediente):
    organismo_liberacion=models.ForeignKey(Organismo,related_name="organismo_liberacion")
    organismo_aceptacion=models.ForeignKey(Organismo,related_name="organismo_aceptacion")
    facultado_liberacion=models.CharField(max_length=250,null=True,blank=True)
    facultado_aceptacion=models.CharField(max_length=250,null=True,blank=True)
    comprimido=models.FileField(upload_to='uploads/adjuntos_expedientes/',null=True,blank=True)


class Expediente_rechazado(models.Model):
    expediente=models.ForeignKey(Expediente_movimiento_externo)
    fecha_rechazo=models.DateTimeField(auto_now=True)
    sintesis_rechazo=models.CharField(max_length=500)

    def __unicode__(self):
        return "Expediente del graudado %s"%(self.expediente.graduado.nombre)


class Expediente_pendiente(models.Model):
    expediente=models.ForeignKey(Expediente_movimiento_externo)
    fecha_pendiente=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Expediente del graudado %s"%(self.expediente.graduado.nombre)



class Expediente_aprobado(models.Model):
    codigo_DE_RE=models.CharField(max_length=250,null=True,blank=True)
    codigo_DE_RS=models.CharField(max_length=250,null=True,blank=True,unique_for_year=True)
    expediente=models.ForeignKey(Expediente_movimiento_externo)
    fecha_aprobado=models.DateTimeField(default=datetime.now())
    carta_expediente=models.FileField(upload_to='uploads/cartas_expedientes/',blank=True, null=True)

    def __unicode__(self):
        return "Expediente del graudado %s"%(self.expediente.graduado.nombre)


    class Meta:
        ordering=['-fecha_aprobado']


class Expediente_no_aprobado(models.Model):
    expediente=models.ForeignKey(Expediente_movimiento_externo)
    fecha_no_aprobado=models.DateTimeField(auto_now=True)
    sintesis_no_aprobado=models.CharField(max_length=500)

    def __unicode__(self):
        return "Expediente del graudado %s"%(self.expediente.graduado.nombre)


class Direccion_trabajo(models.Model):
     provincia=models.OneToOneField(Provincia)
     director=models.CharField(max_length=256,blank=True, null=True)
     sexo_director=models.CharField(max_length=30,blank=True,null=True)
     especialista=models.CharField(max_length=256,blank=True, null=True)
     correo_director=models.EmailField(blank=True, null=True)
     correo_especialista=models.EmailField(blank=True, null=True)
     activo=models.BooleanField(default=True)


     def __unicode__(self):
        return "Dirección de Trabajo de %s".decode("utf-8")%(self.provincia.nombre)


class UbicacionLaboral(models.Model):

    ESTADOS_SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    boleta=models.CharField(max_length=15,blank=True,null=True)
    anno_graduado=models.IntegerField()
    centro_estudio=models.ForeignKey(Centro_estudio)
    carrera=models.ForeignKey(Carrera)
    ci=models.CharField(
        max_length=11,
        validators= [RegexValidator(regex='^[0-9]{2}(0[1-9]|1[0-2])(31|30|(0[1-9]|[1-2][0-9]))[0-9]{5}$',message='CI incorrecto',)],
        unique=True
    )
    nombre_apellidos=models.CharField(max_length=256)
    cumple_servicio_social=models.BooleanField()
    entidad=models.CharField(max_length=256)
    organismo=models.ForeignKey(Organismo)
    municipio_residencia=models.ForeignKey(Municipio,related_name="ubicacion_municipio_residencia")
    provincia_ubicacion=models.ForeignKey(Provincia,related_name="ubicacion_provincia_ubicacion")
    sexo=models.CharField(max_length=20)
    direccion_particular=models.CharField(max_length=256)
    presentado=models.BooleanField(default=True)
    fecha_registro=models.DateTimeField(auto_now_add=True)
    causa_no_presentacion=models.TextField(null=True,blank=True)
    estado_ubicacion=models.CharField(max_length=20,choices=(('desfasado','Desfasado'),('graduado','Graduado')))



    def sexo_verbose(self):
        return dict(UbicacionLaboral.ESTADOS_SEXO)[self.sexo]


    def css(self):
        if self.cumple_servicio_social:
            return "Si"
        else:
            return "No"

    def is_presentado(self):
        if self.presentado:
            return "Si"
        else:
            return "No"

    def __unicode__(self):
        return "Ubicacion de %s "%self.nombre_apellidos

    class Meta:
        ordering=["-fecha_registro"]





class GraduadoInhabilitacion(models.Model):
    nombre_apellidos=models.CharField(max_length=256)
    ci=models.CharField(max_length=11,blank=True,null=True,validators= [RegexValidator(
                regex='^[0-9]{2}(0[1-9]|1[0-2])(31|30|(0[1-9]|[1-2][0-9]))[0-9]{5}$',
                message='CI incorrecto',
            )])

    carrera=models.ForeignKey(Carrera)
    nivel_educacional=models.CharField(max_length=90,choices=[
        ('Superior', 'NS'),
        ('Medio', 'NM'),
    ])
    cumple_servicio_social=models.CharField(max_length=90,choices=[
        ('Si', 'C'),
        ('No', 'NC'),
    ])


    provincia=models.ForeignKey(Provincia)
    organismo=models.ForeignKey(Organismo)
    fecha_registrado=models.DateTimeField(auto_now_add=True)


    def c_nc(self):
        if self.cumple_servicio_social == 'Si':return "C"
        else: return "NC"

    def nm_ns(self):
        if self.nivel_educacional == 'Superior':return "NS"
        else: return "NM"




class ProcesoInhabilitacion(models.Model):
    numero_resolucion=models.IntegerField(unique_for_year=True)
    graduado=models.ForeignKey(GraduadoInhabilitacion)
    fecha=models.DateTimeField(auto_now_add=True)
    causal=models.ForeignKey(Causal_movimiento,blank=True,null=True)
    proceso=models.CharField(max_length=90,choices=[
        ('i', 'Inhabilitación'),
        ('s', 'Suspensión de la Inhabilitación'),
    ])


class DisponibilidadGraduados(models.Model):

    ESTADOS_SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    centro_estudio=models.ForeignKey(Centro_estudio)
    carrera=models.ForeignKey(Carrera)
    cumple_servicio_social=models.BooleanField()
    ci=models.CharField(max_length=11,blank=True,null=True,validators= [RegexValidator(
                regex='^[0-9]{2}(0[1-9]|1[0-2])(31|30|(0[1-9]|[1-2][0-9]))[0-9]{5}$',
                message='CI incorrecto',
            )],unique=True)
    nombre_apellidos=models.CharField(max_length=256)
    municipio_residencia=models.ForeignKey(Municipio,related_name="disponibilidad_municipio_residencia")
    sexo=models.CharField(max_length=20)
    direccion_particular=models.CharField(max_length=256)
    fecha_registro=models.DateTimeField(auto_now_add=True)


    def sexo_verbose(self):
        return dict(DisponibilidadGraduados.ESTADOS_SEXO)[self.sexo]


    def __unicode__(self):
        return self.nombre_apellidos

    class Meta:
        ordering=["-fecha_registro"]



#-----------codigo mario david--------------



class Tipo_Entidad(models.Model):
    identificador = models.CharField(primary_key = True , max_length = 250)
    nombre_tipo = models.CharField(max_length = 250)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre_tipo

    class Meta:
        ordering = ["nombre_tipo"]

class Entidad(models.Model):
    id_codigo_entidad = models.CharField(primary_key=True, max_length = 250)
    e_nombre = models.CharField(max_length = 250)
    id_organismo_s = models.ForeignKey(Organismo,blank=True,null=True)
    direccion = models.CharField(max_length = 250)
    municipio = models.ForeignKey(Municipio,blank=True,null=True)
    id_tipo = models.ForeignKey(Tipo_Entidad,blank=True,null=True)
    estado = models.BooleanField(default=True)
    est_replica = models.IntegerField(blank = True , null = True)

    def __unicode__(self):
        return self.e_nombre

    class Meta:
        ordering = ["e_nombre"]

class DemandaGraduados(models.Model):
    codigo_demanda = models.IntegerField(primary_key=True,unique=True)
    entidad = models.ForeignKey(Entidad,blank=True, null= True)
    municipio_entidad = models.ForeignKey(Municipio,blank=True, null= True)
    carrera = models.ForeignKey(Carrera,blank=True, null= True)
    organismo = models.ForeignKey(Organismo,blank=True, null= True)
    anno_realizacion = models.IntegerField(blank=True,null=True)
    anno_mas_uno = models.IntegerField(blank=True,null=True)
    anno_mas_dos = models.IntegerField(blank=True,null=True)
    anno_mas_tres = models.IntegerField(blank=True,null=True)
    anno_mas_cuatro = models.IntegerField(blank=True,null=True)
    anno_mas_cinco = models.IntegerField(blank=True,null=True)
    anno_mas_seis = models.IntegerField(blank=True,null=True)
    anno_mas_siete = models.IntegerField(blank=True,null=True)
    anno_mas_ocho = models.IntegerField(blank=True,null=True)
    anno_mas_nueve = models.IntegerField(blank=True,null=True)
    anno_mas_diez = models.IntegerField(blank=True,null=True)

class Existencia(models.Model):
    id_ocupados = models.IntegerField(primary_key=True,unique=True)
    id_organismo = models.ForeignKey(Organismo,blank=True,null=True)
    id_codigo_entidad = models.ForeignKey(Entidad,blank=True,null=True)
    id_cod_carrera = models.ForeignKey(Carrera,blank=True,null=True)
    id_municipio_ocupado = models.ForeignKey(Municipio,blank=True,null=True)
    id_tipo_plaza = models.CharField(max_length=255,choices=[
        ('CI', 'Indeterminado'),
        ('CDSS', 'Determinado en cumplimiento del servicio social'),
        ('RCCI', 'Reserva científica CI'),
        ('RCCD', 'Reserva científica CD'),
        ('DIC', 'Determinado ICRT y MINCULT')
    ])
    id_rango_edad = models.CharField(max_length=255,choices=[
        ('-31','Menores de 31 años'),
        ('31<x<50','De 31 a 50 años'),
        ('51<x<60','De 51 a 60 años'),
        ('+60','Mayores de 60 años'),
    ])
    cant_graduados = models.IntegerField(blank=True,null=True)
    ano_realizacion = models.IntegerField(blank=True,null=True)

class Fluctuacion(models.Model):
    id_organismo = models.ForeignKey(Organismo,blank=True,null=True)
    id_fluctuacion = models.IntegerField(primary_key=True,unique=True)
    id_entidad = models.ForeignKey(Entidad,blank=True,null=True)
    id_munic_entidad = models.ForeignKey(Municipio,blank=True,null=True)
    id_causal = models.ForeignKey(Causal_movimiento,blank=True,null=True)
    id_carrera = models.ForeignKey(Carrera,blank=True,null=True)
    cantidad = models.IntegerField(blank=True,null=True)
    anno_realizacion = models.IntegerField(blank=True,null=True)



#---------------------------------------------

class CategoriaIndicacion(models.Model):
   nombre=models.CharField(max_length=256)

   def __unicode__(self):return self.nombre

class Indicacion(models.Model):
    titulo=models.CharField(max_length=256)
    categoria=models.ForeignKey(CategoriaIndicacion)
    texto=models.TextField()
    autor=models.ForeignKey(User)
    fecha_registro=models.DateTimeField(auto_now_add=True)
    fichero=models.FileField(upload_to='uploads/archivos_indicaciones/',blank=True, null=True)


    def get_nombre_fichero(self):
        if self.fichero:
            return self.fichero.name.split("/")[-1]
        else: return None

    class Meta:
        ordering=["-fecha_registro"]
        verbose_name_plural="Indicaciones"
        verbose_name="Indicacion"


@receiver(post_save)
def limpiar_cache0(sender, instance, created, **kwargs):
        if created:
             if sender != Session:
                cache.clear()

@receiver(post_save)
def limpiar_cache1(sender, instance, **kwargs):
       if sender != Session:
            cache.clear()

@receiver(post_delete)
def limpiar_cache2(sender, **kwargs):
        if sender != Session:
          cache.clear()

@receiver(post_save, sender=User)
def actualizar_perfil(sender, instance, **kwargs):
        #instance.perfil_usuario.save()
        pass