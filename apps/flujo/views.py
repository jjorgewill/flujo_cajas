from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages

from apps.flujo import models, forms
from apps.flujo.filters import ActivoFilter
from apps.flujo.mixin import SecurityMixin
from mail_templated import send_mail

from flujo_cajas.settings import EMAIL_HOST_USER


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
        email = 'correo@gmail.com'
        send_mail('emails/activo.tpl', {'nombre':'Jorge','edad':78}, EMAIL_HOST_USER, [email])
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


class ActivoView(SecurityMixin, generic.ListView):
    template_name = 'activo/listar_activos.html'
    context_object_name = 'activos'
    model = models.Activo
    paginate_by = 2
    filter = None

    def get_queryset(self, **kwargs):
        filter = ActivoFilter(self.request.GET, queryset=super().get_queryset())
        self.filter = filter
        return filter.qs.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['frm_filter'] = self.filter.form
        pk = self.kwargs.get("pk")
        context['frm_activo'] = forms.FrmActivo(self.request.POST or None,
                                                instance=models.Activo.objects.filter(pk=pk).first())
        return context


class Home(SecurityMixin, generic.TemplateView):
    template_name = 'home/login.html'