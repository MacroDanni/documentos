from django.contrib import admin
#from .models import Pago
# Register your models here.
'''
class PostPago(admin.ModelAdmin):
    list_display = ('nombre_cliente_pago','fecha_de_pago','comprobante_de_pago','estatus_pago')
    readonly_fields= ('nombre_cliente_pago','fecha_de_pago','comprobante_de_pago','estatus_pago',)
    search_fields =('nombre_cliente_pago','codigo',)
    
    list_per_page =10

admin.site.register(PostPago)

 '''