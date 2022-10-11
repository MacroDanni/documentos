import asyncio
import os
from datetime import datetime, timedelta
from email.headerregistry import ContentTypeHeader
from importlib.resources import Package
from logging import PlaceHolder
from msilib.schema import Class
from multiprocessing.connection import Client
from pickle import TRUE
from typing_extensions import Required
from urllib import request

from django import forms
from django.contrib import admin, sessions
from django.contrib.admin.models import ADDITION, LogEntry
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_exempt
from numpy import save
from pyexpat import model

from .choises import choises
from .createPDF import Pdf
from .funciones import Punto
import win32print
import win32api
import time

#format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
now =datetime.now()
format = now.strftime('%d%m%Y%H%M%S')+'ACI'



class Pago(models.Model):
     
    
    create = models.DateTimeField(auto_now_add=True) 
    update = models.DateTimeField(auto_now=True)
    fecha_de_pago = models.DateTimeField(auto_now_add=True)
    comprobante_de_pago=models.FileField(upload_to="static/images/",null=True)
    nombre_cliente_pago=models.CharField(max_length=100,null=True)
    codigo=models.CharField(max_length=30,null=True)
    estatus_pago2=models.CharField(max_length=10, default='nuevo')
    abono_cliente= models.CharField(max_length=11,null=True)
    
    
   
    class Meta():
        ordering = ('-fecha_de_pago',)
        
    @csrf_exempt
    
    def __srt__(self):
               
        return self.nombre_cliente_pago
    
    def comprobante_de_pago_(self):
        return format_html('<a href="{0}" target="_blank"> <img src="/static/images/file-earmark-pdf-fill.svg">  Recibo </a>'.format(self.comprobante_de_pago.url)) 
    
    def abono_cliente_(self):
       return format_html(f'<span><strong>$ </strong>{self.abono_cliente}</span>') 
    

class Cliente(models.Model): 
   
    author=models.ForeignKey(User, related_name='blog_post',on_delete=models.CASCADE,default=User)
    nombre_cliente=models.CharField(max_length=100,help_text='Ingresa el Nombre del Comprador',)
    telefono = models.CharField(max_length=10,help_text='Telefono o Celular',)
    municipio = models.CharField(max_length=350,choices=choises.municipio_por_estado,default='Puebla')
    cp=models.CharField(max_length=6,help_text='Ingresa Codigo Postal',blank=True)
    colonia=models.CharField(max_length=100,help_text='Ingresa la Colonia',blank=True)
    # cp = models.CharField(max_length=350,choices=tuple(Punto.get_cp_municipio()))
    #colonia = models.CharField(max_length=200,choices=tuple(Punto.get_colonia_por_cp()))
    manzana = models.IntegerField(help_text='Ingresa la manzana',default=0,blank=True)
    numero_lote = models.IntegerField(help_text='Ingresa numero de lote',default=0,blank=True)
    m2_lote = models.CharField(max_length=5,default=None,blank=True)
    costo_del_terreno = models.IntegerField(help_text='Costo Terreno',default=0,blank=True)
    deuda_de_terreno = models.IntegerField(default=0,blank=True)
    a_cuenta_de_terreno = models.IntegerField(default=0,blank=True)
    compromiso_de_pago = models.IntegerField(help_text='Compromiso Pago',default=0,blank=True)
    cantidad_en_conciliacion = models.IntegerField(help_text='Cantidad en Conciliacion',default=0,blank=True)
    estatus_pago = models.CharField(max_length=50,choices=choises.status_pago, default='nuevo')
    notificaciones = models.CharField(max_length=50,choices=choises.status_notificacion, default='recibo',)
    fecha_de_revision = models.DateTimeField(default=timezone.now)
    fecha_de_entrega = models.DateTimeField(default=timezone.now)
    abono_pago = models.IntegerField(default=0)
    forma_de_pago= models.CharField (max_length=50,choices=choises.forma_pago, default='efectivo')
    codigo = models.CharField(max_length=100,default=format)
    create = models.DateTimeField(auto_now_add=True) 
    update = models.DateTimeField(auto_now=True)
    

       
    
    def save(self,*args,**kwargs): 
        self.nombre_cliente=self.nombre_cliente.capitalize()
        #se valida si el motno es mayor a 0 y que  el abono sea menor que la deuda 
        if int(self.abono_pago) > 0 and int(self.abono_pago)< int(self.deuda_de_terreno):
                    now = datetime.now()
                    format_fecha = now.strftime('%d%m%Y%H%M%S')
                    codigo='ACI'+str(self.id)+str(format_fecha)

              
                    #Se crea el PDF para el recibo impreso
                    Pdf.createpdf(f'{self.nombre_cliente}',f'{self.colonia}',f'{codigo}',f'{self.telefono}',f'{self.manzana}',f'{self.numero_lote}',f'{self.abono_pago}',f'{self.id}',f'{self.forma_de_pago}')  
                    #se inserta el pago y la url del pago en la BD          
                    pago= Pago.objects.create(nombre_cliente_pago=self.nombre_cliente,comprobante_de_pago=f'/static/images/{codigo}.pdf',codigo=codigo,abono_cliente=self.abono_pago)
                    #se manda a impresion el documento generado
                    
                   
                    #win32api.ShellExecute(0,'print','C:\proyectos\entornoPY\Scripts\principal\clientes\static\images\{codigo}.pdf',None,'.',1)
            
                   
                    
                    
                    self.estatus_pago='corriente'
                    #Se abona en abtomatico antes del save
                    self.a_cuenta_de_terreno=self.a_cuenta_de_terreno+self.abono_pago
                    
                    self.deuda_de_terreno=self.deuda_de_terreno-self.abono_pago
                    self.abono_pago=0
                                        
        if self.abono_pago>self.deuda_de_terreno: 
                        self.abono_pago=0
                        
        if self.abono_pago == self.deuda_de_terreno and self.estatus_pago=='corriente':
                    self.deuda_de_terreno=self.deuda_de_terreno-self.abono_pago
                    self.abono_pago=0
                    self.estatus_pago='liquidado' 
            
        if self.estatus_pago=='nuevo':
            self.deuda_de_terreno=self.costo_del_terreno    
        #r= Pago(comprobante_de_pago=self.codigo,cliente_id=self.id,nombre_cliente=self.nombre_cliente)
        #r.save
            
        super(Cliente,self).save(*args,**kwargs)
        
        #if self.estatus_pago=='corriente':
          #  time.sleep(1)
           
       
          #  os.startfile(f"C:\proyectos\entornoPY\Scripts\principal\clientes\static\images\{codigo}.pdf", "print")
                  
                  
    #debe de ser igual que el modelo 
    class Meta():
        ordering = ('estatus_pago',)
    @csrf_exempt
    def __srt__(self):
         
        return self.id 
        
    #C:\proyectos\entornoPY\Scripts\principal\clientes\static\images\ACI210102022163103.pdf
    def estatus_pago_(self):
        if self.estatus_pago =='atraso' or self.estatus_pago =='pendiente' or self.estatus_pago =='disputa':
            return format_html('<span style="color:#dc3545;"><strong>{0}</strong></span>'.format(self.estatus_pago.capitalize())) 
        else:
            return format_html('<span style="color:#198754;"><strong>{0}</strong></span>'.format(self.estatus_pago.capitalize()))
    
    def costo_del_terreno_(self):
        
        return format_html(f'<span><strong>$ </strong>{self.costo_del_terreno:,}</span>') 

    def deuda_de_terreno_(self):
        
        return format_html(f'<span><strong>$ </strong>{self.deuda_de_terreno:,}</span>') 

    def a_cuenta_de_terreno_(self):
        return format_html(f'<span><strong>$ </strong>{self.a_cuenta_de_terreno:,}</span>') 
        
   