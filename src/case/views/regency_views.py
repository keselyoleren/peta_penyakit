# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from config.permis import IsAuthenticated
from case.models import Province, Regency
from case.form.prvince_form import RegencyForm


class RegencyListView(IsAuthenticated, ListView):
    model = Regency
    template_name = 'regency/list.html'
    context_object_name = 'list_regency'
    
    def get_queryset(self):
        if 'province' in self.request.GET:
            return Regency.objects.filter(province_id=self.request.GET['province'])
        return super().get_queryset().filter(province_id=None)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['province_name'] = ''
        if province := Province.objects.filter(id=self.request.GET.get('province', None)).first():
            context['province_name'] = province.name
        context['header'] = 'Regency'
        context['header_title'] = 'List Regency'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('regency-create')
        return context

class RegencyCreateView(IsAuthenticated, CreateView):
    model = Regency
    template_name = 'component/form.html'
    form_class = RegencyForm
    success_url = reverse_lazy('regency-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Regency'
        context['header_title'] = 'Tambah Regency'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class RegencyUpdateView(IsAuthenticated, UpdateView):
    model = Regency
    template_name = 'component/form.html'
    form_class = RegencyForm
    success_url = reverse_lazy('regency-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Regency'
        context['header_title'] = 'Edit Regency'
        return context

class RegencyDeleteView(IsAuthenticated, DeleteView):
    model = Regency
    template_name = 'component/delete.html'
    success_url = reverse_lazy('regency-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Regency'
        context['header_title'] = 'Delete Regency'
        return context
