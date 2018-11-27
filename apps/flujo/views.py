from django.shortcuts import render
from django.views import generic

from apps.flujo import models


class Home(generic.TemplateView):
    template_name = 'home/login.html'


class ActivoCreateView(generic.CreateView):
    template_name = 'activo/form_activo.html'



class ActivoView(generic.ListView):
    template_name = 'activo/listar_activos.html'
    context_object_name = 'activos'
    model = models.Activo
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
