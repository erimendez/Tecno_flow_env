# Documentacion del Sitio Web "Tecno Flow" #

## Integracion del Proyecto Inicial a Django y su deploy en Pythonanywhere
![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/c52c94ba-8341-480e-83cd-5209f218402e)

## Requerimientos:

### Utilizar la implementación de django views para generar las rutas y colocar los endpoints necesarios para que internamente reconozca los paths  que el proyecto requiere.
## En este punto se generaron las views, las URLs respectivas y los endpoints.

#### views.py
![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/34b63c1c-04af-485d-ba1f-dd127dcbff43)
![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/509e0e16-2e07-4e8f-b71a-bf129d6dad41)

#### urls.py
![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/daa86c8a-0814-4aff-888c-fcd49bdd90ed)
  
### Levantar los archivos estáticos que se necesitaron para la parte funcional y estética del proyecto.
##En la carpeta "static" justamente se colocaron todos las archivos estáticos (estilos CSS, scripts JS e imagenes MEDIA), se logró la funcionalidad completa acompañada de su respectiva estética.

#### static
![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/5e940db4-8712-42e7-92dc-0d3ddf82035e)

## Sintaxis jinja utilizada para la creacion de estetica del proyecto
###  Sintaxis usada para la carga de la pagina base y en el resto de las paginas .html para la carga correcta de los estilos correspondientes
```
{% extends 'base.html' %}
{% load static %}
{% block content %}
{% endblock %}
```
### Sintaxis usada para vincular imagenes 
```
"{% static '/media/img/tablet.jpg' %}"
```
### Sintaxis usada para enrutar los enlaces a las distintas paginas
```
"{% url 'tablets_page' %}"
```
### Sintaxis usada para la carga de Scripts
```
"{% static '/js/script.js' %}"
```

## Opcional-Recomendado: Generar un CRUD con los apps de django, e integrarlo con el front de django.
### Se creo las paginas para el CRUD
![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/26eb5459-6ec8-4a71-8017-c2a75550104d)
### Urls
![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/e85f1169-a47e-45e6-8b78-04ebd872d470)
### Views
![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/a4c14b52-dde4-4316-a00c-b249bfcc9cf6)

### Se agregó la página `cotización.html` donde se hizo un CRUD de reparación de celulares.

![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/61dd2824-7ab4-48b4-b4af-abb8a3fa445d)










## Opcional-Recomendado: Hacer un deploy en python anywhere.
### Posterior a la integración con Django, el agregado de un CRUD, se "subió" el proyecto a PYTHONANYWEHRE con la dirección: (https://ericamendez.pythonanywhere.com/)


## API 

https://ericamendez.pythonanywhere.com/cotiza/api-cotiza/

![image](https://github.com/erimendez/Tecno_flow_env/assets/129424045/e62ad50c-3f70-4cc3-bdaf-978e4085e2a8)
















## Descripcion
Tecno Flow es un sitio dedicado a la venta de productos tecnologicos tanto para uso hogareño como de oficina.
Cuenta con varias paginas con diversos productos (celulares, notebooks, tablets, monitores e impresoras) y sus descripciones, ademas de un formulario de consulta.

## Estructura del proyecto

#Tecno_flow_env
-
#Carpeta templates
- *Bloque/*: Carpeta que contiene paginas html anexas del sitio web.
- *base.html*: Página base.
- *index.html*: Página de inicio del sitio web.

#Carpeta templates/Bloque

- *index.html*: Página de inicio del sitio web.
- *preg_Frec.html*: Página de las preguntas frecuentes.
- *contacto.html*: Página de contacto con el cliente.
- *gracias.html*: Página de agradecimiento por la compra.
- *impresoras.html*: Página del producto impresora.
- *monitores.html*: Página del producto monitor.
- *note.html*: Página del producto notebook.
- *sucursales.html*: Página de las sucursales del fisicas.
- *tablets.html*: Página del producto tablet.
- *promociones.html*: Página de medios de pago.
- *cotización.hmtl*: Página de cotización de reparaciones.
- *productossamsung.hmtl*: Página del producto celular.
- *productosmoto.hmtl*: Página del producto celular.

#Carpeta static/*: contiene los arhivos

- *css/*: Carpeta que contiene los estilos del sitio web.

- *js/*: Carpeta que contiene los archivos javascript/jason del sitio web.

- *media*: Carpeta que contiene archivos visuales para el sitio web.

## Archivo `index.html`
Este archivo contiene la pagina de inicio del sitio web, donde los usuario(clientes) pueden comprar y visualizar los productos tecnologicos a la venta. Ademas de promociones y ofertas.

## Archivo `base.html`
Este archivo contiene la base o plantilla que emplea las bibliotecas estáticas de JavaScript, Bootstrap.

## Archivo `preg_Frec.html`
Este archivo contiene las repuestas a las preguntas frecuentes hechas por los clientes en el momento de la compra o postventa; ademas de las gtias de los productos.

## Archivo `contacto.html`
Este archivo contiene el formulario de contacto que el usuario(cliente)puede completar para elevar un comentario/sugerencia o reclamo.

## Archivo `gracias.html`
Este archivo contiene un texto de agradecimiento por la compra.

## Archivo `impresoras.html`
Este archivo contiene infomacion sobre las impresoras en venta, ademas de sus descripciones y sus valores comerciales correspondientes.

## Archivo `monitores.html`
Este archivo contiene infomacion sobre los monitores en venta, ademas de sus descripciones y sus valores comerciales correspondientes.

## Archivo `note.html`
Este archivo contiene infomacion sobre las notebooks en venta, ademas de sus descripciones y sus valores comerciales correspondiente.

## Archivo `productossamguns.html`
Este archivo contiene infomacion sobre los celulares en venta de la marca "samsung ", ademas de sus descripciones y sus valores comerciales correspondiente.

## Archivo `productosmoto.html`
Este archivo contiene infomacion sobre los celulares en venta de la marca "Motorola", ademas de sus descripciones y sus valores comerciales correspondiente.

## Archivo `sucursales.html`
Este archivo contiene informacion y ubicacion fisica de las sucursales de la empresa en cuestion.

## Archivo `tablets.html`
Este archivo contiene infomacion sobre las tablets en venta, ademas de sus descripciones y sus valores comerciales 
correspondiente.

## Archivo `promociones.html`
Este archivo contiene infomacion sobre las promociones vigentes en los medios de pagos correspondientes.

## Archivo `cotización.html`
Este archivo contiene un CRUD sobre las reparaciones solicitadas.

## Carpeta Css
- *style.css*: Contiene los estilos generales del sitio web.
- *pf.css*: Contiene los estilos específicos para la página `preg_Frec.html`.
- *style_contacto.css*: Contiene los estilos específicos para la página `contacto.html`.
- *productos.css*: Contiene los estilos específicos para la páginas `impresoras.html`, `monitores.html`,`note.html`, `tablets.html`, `productossamsung.html`, `productosmoto.html`.
- *sucursales.css*: Contiene los estilos específicos para la página `sucursales.html`.

## Carpeta Js
- *all.min.js*: Es el archivo que contiene  el codigo javascript para visualizar los iconos la pagina especifica `sucursales.html`.
- *contacto.js*: Es el archivo que contiene  el codigo javascript para validar el ingreso de datos de la pagina especifica `contacto.html`.
- *script.js*:  Es el archivo que contiene  el codigo  javascript para visualizar e insertar en el DOM del "slider" del `index.html` los campos de la base de datos.
- *slider.js*:  Es el archivo que contiene  el codigo  javascript para controlar los botones de navegacion del "slider" de la pagina `index.html`.
- *sucursales.js*:  Es el archivo que contiene  el codigo  javascript para visualizar e insertar en el DOM de la pagina `sucursales.html` las sucursales y localidades. Asi como tambien lo datos de la geolocalizacion de las mismas.

## Carpeta media/img
Carpeta que contiene las imagenes en formato png/jpg del sitio web.

## Carpeta media
- *listado_de_sucursales.pdf*: Es el archivo que contiene la informacion en formato PDF de las sucursales fisicas del sitio web. 

## Carpeta Bloque
- *listadoSucursales.html*: Archivo que contiene el codigo html y estilo para la presentacion del archivo PDF.
- *preg_Frec.html*: Página de las preguntas frecuentes.
- *contacto.html*: Página de contacto con el cliente.
- *gracias.html*: Página de agradecimiento por la compra.
- *impresoras.html*: Página del producto impresora.
- *monitores.html*: Página del producto monitor.
- *note.html*: Página del producto notebook.
- *productossamsung.html*: Página del producto celular Samsung.
- *productossmoto.html*: Página del producto celular Motorola.
- *sucursales.html*: Página de las sucursales del fisicas.
- *tablets.html*: Página del producto tablet.
- *promociones.html*: Página de medios de pago.
- *cotización.hmtl*: Páginade cotización de reparaciones.

## Dependencias y Bibliotecas

- [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) v5.1.0: Una biblioteca de CSS y JavaScript utilizada para el diseño y la interactividad especificamente para la pagina `contacto.html`.

- [Leaflet API](https://leafletjs.com/download.html)Leaflet 1.9.4: Una biblioteca JavaScript de código abierto para mapas interactivos utilizada espeficamente en la pagina `sucurales.html`. 

- [OpenSteetMap ](https://www.openstreetmap.org/) Proyecto colaborativo para crear mapas editables y libres, utlizada espeficamente en la pagina `sucurales.html`. 

## API 
- [Sheetdb.io API](https://sheetdb.io/) SheetDB es una herramienta que converte una hoja de cálculo de Google en una API JSON. Nos permite conectar con nuestra tabla que contiene los datos utilizados en el sitio web. Utilizada en la pagina `index.html`.

- [API Formsubmit](https://formsubmit.co/) API Formsubmit herramienta para el envio de correo electronico desde el formulario de la la página `contacto.html`. 

## Compatibilidad y Requisitos
- Navegadores compatibles: Google Chrome (última versión), Mozilla Firefox (última versión), Safari (última versión).


## Integrantes del proyecto y detalle del trabajo realizado

>"Individualmente somos una gota,
      juntos formamos un océano"
                   Ryunosuke Satoro

- En general el aporte de todos para buscar info, imagenes y correciones en general, tips a lo largo del proyecto.
- Aprendimos a trabajar con GitHub en equipo.
- Destacar la comunicación y el trabajo en equipo.

- Erica Mendez (https://github.com/erimendez)
    * Maquetacion y creacion de la paginas `index.html`, `productos.html`, `gracias.html`, `monitores.html`, `promociones.html`, `tablets.html`, `impresoras.html`. 
    * Creacion y modificacion de estilo `style.css`, `productos.css`
    * Conexion de Api Rest.
    * Creacion de archivos Javascript `nav_footer.js`, `script.js`, `seccion.js`, `seccioncelus.js` y `slider.js`.
    * Separacion del codigo en las paginas `header.html` y `footer.html` para poder repetirse en todas las demas paginas del sitio.
    * Creacion del archivo Readme.md.
    * Creacion de Logo, banner publicitario, tira de imagenes.
    * Edicion de imagenes.

- Lorena Dominguez     (https://github.com/primerapruebagithub)
    * Maquetacion y creacion de las paginas `preg_Frec.html`, `note.html`y `footer.html`.
    * Creacion y modificacion de estilo `pf.css` y `style.css`
    * Creacion del Favicon.
    * Eleccion de tipografia.
    * Busqueda de imagenes para creacion de contenido. 
    
- Manuel Saquilan (https://github.com/ManuelSaquilan)
    * Maquetacion y creacion de las paginas `contacto.html` y  `header.html`.
    * Creacion y modificacion de estilo `style.css`.
    * Creacion del archivo `contacto.js`.
    * Creacion del menu "hamburguesa" y su responsividad. 
    * Creacion de la funcionalidad y validacion para llenar el formulario de `contacto.html` y recibir un mail de respuesta. Utilizando Api Formsubmit.
       
- Mirta Veron (https://github.com/mirtaveron)
    * Maquetacion y creacion de las paginas `sucursales.html`,  `listadoSucursales.html`.
    * Creacion y modificacion de estilo `style.css`, `pf.css` y `sucursales.css`
    * Creacion de los 3 puntos de corte de responsividad (media queries) solicitados en el trabajo practico. 
    * Creacion del archivo `sucursales.js`. 
    * Geolocalizacion de sucursales en la pagina `sucursales.html` utilizando api externa. 


    
