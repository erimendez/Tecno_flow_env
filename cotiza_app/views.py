

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Cotizacion

# Create your views here.


class CotizaBaseView(View):
    template_name = 'cotiza.html'
    model = Cotizacion
    fields = '__all__'
    success_url = reverse_lazy('cotiza:all')


class CotizaListView(CotizaBaseView,ListView):
   ...

class CotizaDetailView(CotizaBaseView,DetailView):
    template_name = "cotiza_detail.html"

class CotizaCreateView(CotizaBaseView,CreateView):
    template_name = "cotiza_create.html"
    extra_context = {
        "tipo": "Crear Cotizacion"
    }


class CotizaUpdateView(CotizaBaseView,UpdateView):
    template_name = "cotiza_create.html"
    extra_context = {
        "tipo": "Actualizar cotizacion"
    }

class CotizaDeleteView(CotizaBaseView,DeleteView):
    template_name = "cotiza_delete.html"
    extra_context = {
        "tipo": "Borrar cotizacion"
    }