from django.views.generic import TemplateView


class TecnoViewPage(TemplateView):
    template_name = "index.html"
    extra_content = {
        'titulo_pagina' : "Inicio"
    }

class ContactoPage(TemplateView):
    template_name = "Bloque/contacto.html"

class SucursalesPage(TemplateView):
    template_name = "Bloque/sucursales.html"

class TabletsPage(TemplateView):
    template_name = "Bloque/tablets.html"

class CotizacionPage(TemplateView):
    template_name = "Bloque/cotizacion.html"


class GraciasPage(TemplateView):
    template_name = "Bloque/gracias.html"

class ImpresorasPage(TemplateView):
    template_name = "Bloque/impresoras.html"

class MonitoresPage(TemplateView):
    template_name = "Bloque/monitores.html"
    
class NotePage(TemplateView):
    template_name = "Bloque/note.html"

class PregFrecPage(TemplateView):
    template_name = "Bloque/preg_Frec.html"
    

class ProductosPage(TemplateView):
    template_name = "Bloque/productos.html"

class PromocionesPage(TemplateView):
    template_name = "Bloque/promociones.html"
