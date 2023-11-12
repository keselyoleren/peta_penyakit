# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from config.permis import IsAuthenticated, IsPuskeswan
from case.models import Disease
from case.form.diseases_form import DiseaseForm


class DiseaseListView(IsPuskeswan, ListView):
    model = Disease
    template_name = 'disease/list.html'
    context_object_name = 'list_disease'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Disease'
        context['header_title'] = 'List Disease'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('disease-create')
        return context

class DiseaseCreateView(IsPuskeswan, CreateView):
    model = Disease
    template_name = 'component/form.html'
    form_class = DiseaseForm
    success_url = reverse_lazy('disease-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Disease'
        context['header_title'] = 'Tambah Disease'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class DiseaseUpdateView(IsPuskeswan, UpdateView):
    model = Disease
    template_name = 'component/form.html'
    form_class = DiseaseForm
    success_url = reverse_lazy('disease-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Disease'
        context['header_title'] = 'Edit Disease'
        return context

class DiseaseDeleteView(IsPuskeswan, DeleteView):
    model = Disease
    template_name = 'component/delete.html'
    success_url = reverse_lazy('disease-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Disease'
        context['header_title'] = 'Delete Disease'
        return context
