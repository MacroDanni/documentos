from msilib.schema import Class
from turtle import title
from webbrowser import get
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from .models import Cliente,Pago


admin.site.site_header="Asoc. de Colonos IlhuicaminaA."
admin.site.site_title="Portal ACI"
class PostAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente','estatus_pago_',
                    'manzana','numero_lote','m2_lote','costo_del_terreno_','deuda_de_terreno_','a_cuenta_de_terreno_'
                    ,'notificaciones','forma_de_pago','abono_pago',)
    readonly_fields= ('deuda_de_terreno','a_cuenta_de_terreno','abono_pago','fecha_de_entrega','forma_de_pago','estatus_pago','codigo','notificaciones',)
    search_fields =('nombre_cliente','codigo',)
    list_editable=('forma_de_pago','notificaciones','abono_pago',)
    #autocomplete_fields = ['municipio']

    #list_display_links = ('nombre_cliente','estatus_pago')
    #list_filter= ('estatus_pago',)
    list_per_page =10
    


    def get_actions(self, request):
            actions = super(PostAdmin, self).get_actions(request)
            if 'delete_selected' in actions:
                del actions['delete_selected']
            return actions
  
 
class PagoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente_pago','codigo','comprobante_de_pago_','fecha_de_pago','abono_cliente')
    list_display_links = ('comprobante_de_pago_','nombre_cliente_pago',)
    readonly_fields= ('nombre_cliente_pago','codigo','comprobante_de_pago_','fecha_de_pago','estatus_pago2',)
    search_fields =('nombre_cliente_pago','codigo',)
    empty_value_display = '---'
    list_per_page =15
 
   
    def has_add_permission(self, request, obj=None): 
        return False

    def get_actions(self, request):
        actions = super(PagoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
  
    
    
    
admin.site.index_title = 'Panel de control del sitio'
admin.site.register(Cliente,PostAdmin)
admin.site.register(Pago,PagoAdmin) 




    
   