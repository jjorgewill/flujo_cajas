from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages

from apps.flujo import models, forms
from apps.flujo.mixin import SecurityMixin


class ActivoDeleteView(generic.DeleteView):
    template_name = 'activo/delete_activo.html'
    model = models.Activo
    success_url = reverse_lazy('view_activo')
    #
    # def get_success_url(self):
    #     return reverse('view_activo')


class ActivoUpdateView(generic.UpdateView):
    template_name = 'activo/form_activo.html'
    form_class = forms.FrmActivo
    model = models.Activo

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_activo')


class ActivoCreateView(generic.CreateView):
    template_name = 'activo/form_activo.html'
    form_class = forms.FrmActivo
    model = models.Activo

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Su Activo se ha guardado correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Lo sentimos no se ha podido procesar la solicitud.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('view_activo')


class ActivoView(generic.ListView):
    template_name = 'activo/listar_activos.html'
    context_object_name = 'activos'
    model = models.Activo
    paginate_by = 2

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class Home(SecurityMixin, generic.TemplateView):
    template_name = 'home/login.html'