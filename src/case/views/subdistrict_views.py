
# myapp/views.py

import contextlib
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from config.permis import IsAuthenticated
from case.models import Province, Regency, SubDistrict, SubDistrict
from case.form.prvince_form import SubDistrictForm


class SubDistrictListView(IsAuthenticated, ListView):
    model = SubDistrict
    template_name = 'subdistrict/list.html'
    context_object_name = 'list_subdistrict'
    paginate_by = 100
    
    def get_queryset(self):
        if 'regency' in self.request.GET:
            try:
                return super().get_queryset().filter(regency_id=self.request.GET['regency'])
            except:
                pass
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regency_name'] = ''
        with contextlib.suppress(Exception):
            regency = Regency.objects.filter(id=self.request.GET.get('regency', None)).first()
            if regency:
                context['regency_name'] = regency.name
        context['header'] = 'Sub District'
        context['header_title'] = 'List Sub District'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('subdistrict-create')
        return context

class SubDistrictCreateView(IsAuthenticated, CreateView):
    model = SubDistrict
    template_name = 'subdistrict/form.html'
    form_class = SubDistrictForm
    success_url = reverse_lazy('subdistrict-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'SubDistrict'
        context['header_title'] = 'Tambah Sub District'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class SubDistrictUpdateView(IsAuthenticated, UpdateView):
    model = SubDistrict
    template_name = 'subdistrict/form.html'
    form_class = SubDistrictForm
    success_url = reverse_lazy('subdistrict-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'SubDistrict'
        context['header_title'] = 'Edit Sub District'
        return context

class SubDistrictDeleteView(IsAuthenticated, DeleteView):
    model = SubDistrict
    template_name = 'component/delete.html'
    success_url = reverse_lazy('subdistrict-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Sub District'
        context['header_title'] = 'Delete Sub District'
        return context

