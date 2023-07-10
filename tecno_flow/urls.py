"""
URL configuration for tecno_flow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from .views import ProductosmotoPage, ListadosucursalesPage, ProductossamsungPage, TecnoViewPage, ContactoPage, SucursalesPage, TabletsPage, CotizacionPage, GraciasPage, ImpresorasPage, MonitoresPage, NotePage, PregFrecPage, ProductosPage, PromocionesPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",TecnoViewPage.as_view(), name = "landing_page"),
    path("contacto",ContactoPage.as_view(), name = "contacto_page" ),
    path("sucursales",SucursalesPage.as_view(), name = "sucursales_page" ),
    path("tablets",TabletsPage.as_view(), name = "tablets_page" ),
    path("cotizacion",CotizacionPage.as_view(), name = "cotizacion_page" ),
    path("gracias",GraciasPage.as_view(), name = "gracias_page" ),
    path("impresoras",ImpresorasPage.as_view(), name = "impresoras_page" ),
    path("monitores",MonitoresPage.as_view(), name = "monitores_page" ),
    path("preguntasfrecuentes",PregFrecPage.as_view(), name = "preguntasfrecuentes_page" ),
    path("productos",ProductosPage.as_view(), name = "productos_page" ),
    path("promociones",PromocionesPage.as_view(), name = "promociones_page" ),
    path("note",NotePage.as_view(), name = "note_page" ),
    path("cotiza/", include("cotiza_app.urls")),
    path("productosmoto",ProductosmotoPage.as_view(), name = "productosmoto_page" ),
    path("productossamsung",ProductossamsungPage.as_view(), name = "productossamsung_page" ),
    path("listadoSucursales",ListadosucursalesPage.as_view(), name = "listadosucursales_page" ),
]







