from ast import Return
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta
import qrcode
import os
 
class Pdf():
    
    def createpdf(nombre,colonia,codigo,telefono,manzana,lote,abono,id_registro_cliente,forma_de_pago):
        ruta_qrs='clientes/static/images/qrs/'
        ruta='clientes/static/images/'
        img = qrcode.make(f"{codigo}")
        f = open(f"{ruta_qrs}{codigo}.png", "wb")
        c = canvas.Canvas(f"{ruta}{codigo}.pdf", pagesize=letter)
        img.save(f)
        f.close()
        w, h = letter
       # c = canvas.Canvas(f"clientes/FilePDF/{folio}{str(id_registro_cliente)} - {str(format_fecha)}{str(id_registro_abono)}.pdf", pagesize=letter)
        now = datetime.now()
        c.drawImage(f"{ruta_qrs}{codigo}.png", 260, h - 180, width=50, height=50)

        #titulos principal
        c.drawString(250,750 , "Recibo de Pago")
        c.drawString(200,720 , "Asociacion de Colonos IlhuicaminaA.")
        #titulos datos
        c.drawString(200,690 , "RFC: ")
        c.drawString(200,670 , "Telefono: ")
        c.drawString(200,650 , "Folio: ")
        c.drawString(200,590 , "Fecha: ")
        c.drawString(200,570 , "Cobrador: ")
        c.drawString(200,550 , "Colonia: ")
        c.drawString(200,530 , "Nombre: ")
        #datos de los titulos
        c.drawString(260,690 , "")
        c.drawString(260,670 , f"{telefono}")
        
        c.drawString(260,590 , f"{now.strftime('%d-%m-%Y %H:%M')}")
        c.drawString(260,570 , f"")
        c.drawString(260,550 , f"{colonia.capitalize()}")
        c.drawString(260,530 , f"{nombre.capitalize()}")
        x = 180
        y = h - 275
        c.line(x, y, x + 270, y)
        c.drawString(220,500 , "Manzana")
        c.drawString(300,500 , "Lote")
        c.drawString(350,500 , "Monto Pagado")
        x = 180
        y = h - 300
        c.line(x, y, x + 270, y)
        c.drawString(230,480 , f"{manzana}")
        c.drawString(302,480 , f'# {lote}')
        c.drawString(370,480 , f"${abono}.00")
        c.drawString(280,450 , "Comentarios: ")
        c.rect(x, h - 450, 280, 100)
        c.drawString(200,300 , f"Forma de Pago: {forma_de_pago.capitalize()}")
        c.save()
        
        os.startfile(f"static\images\{codigo}.pdf", "print")
        
        Return


