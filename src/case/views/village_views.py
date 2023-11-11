
# myapp/views.py

import contextlib
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from config.permis import IsAuthenticated
from case.models import SubDistrict, Village, Regency
from case.form.prvince_form import VillageForm


class VillageListView(IsAuthenticated, ListView):
    model = Village
    template_name = 'village/list.html'
    context_object_name = 'list_village'
    
    def get_queryset(self):
        if 'regency' in self.request.GET:
            with contextlib.suppress(Exception):
                return super().get_queryset().filter(sub_district_id=self.request.GET['sub_district'])
        return super().get_queryset().filter(sub_district_id=None)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_district_name'] = ''
        with contextlib.suppress(Exception):
            sub_district_name = SubDistrict.objects.filter(id=self.request.GET.get('sub_district', None)).first()
            if sub_district_name: 
                context['sub_district_name'] = sub_district_name.name
        context['header'] = 'Vlillage'
        context['header_title'] = 'List Vlillage'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('village-create')
        return context

class VillageCreateView(IsAuthenticated, CreateView):
    model = Village
    template_name = 'component/form.html'
    form_class = VillageForm
    success_url = reverse_lazy('vlillage-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Village'
        context['header_title'] = 'Tambah Vlillage'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class VillageUpdateView(IsAuthenticated, UpdateView):
    model = Village
    template_name = 'component/form.html'
    form_class = VillageForm
    success_url = reverse_lazy('vlillage-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Village'
        context['header_title'] = 'Edit Vlillage'
        return context

class VillageDeleteView(IsAuthenticated, DeleteView):
    model = Village
    template_name = 'component/delete.html'
    success_url = reverse_lazy('vlillage-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Vlillage'
        context['header_title'] = 'Delete Village'
        return context

