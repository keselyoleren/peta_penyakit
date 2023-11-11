# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from config.permis import IsAuthenticated
from case.models import Province
from case.form.prvince_form import ProvinceForm


class ProvinceListView(IsAuthenticated, ListView):
    model = Province
    template_name = 'province/list.html'
    context_object_name = 'list_province'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Province'
        context['header_title'] = 'List Province'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('province-create')
        return context

class ProvinceCreateView(IsAuthenticated, CreateView):
    model = Province
    template_name = 'component/form.html'
    form_class = ProvinceForm
    success_url = reverse_lazy('province-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Province'
        context['header_title'] = 'Tambah Province'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class ProvinceUpdateView(IsAuthenticated, UpdateView):
    model = Province
    template_name = 'component/form.html'
    form_class = ProvinceForm
    success_url = reverse_lazy('province-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Province'
        context['header_title'] = 'Edit Province'
        return context

class ProvinceDeleteView(IsAuthenticated, DeleteView):
    model = Province
    template_name = 'component/delete.html'
    success_url = reverse_lazy('province-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Province'
        context['header_title'] = 'Delete Province'
        return context
