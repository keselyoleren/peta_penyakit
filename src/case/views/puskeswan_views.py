# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from config.permis import IsAuthenticated
from case.models import Puskeswan
from case.form.puskeswan_form import PuskeswanForm


class PuskeswanListView(IsAuthenticated, ListView):
    model = Puskeswan
    template_name = 'puskeswan/list.html'
    context_object_name = 'list_puskeswan'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Puskeswan'
        context['header_title'] = 'List puskeswan'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('puskeswan-create')
        return context

class PuskeswanCreateView(IsAuthenticated, CreateView):
    model = Puskeswan
    template_name = 'puskeswan/form.html'
    form_class = PuskeswanForm
    success_url = reverse_lazy('puskeswan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Puskeswan'
        context['header_title'] = 'Tambah puskeswan'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class PuskeswanUpdateView(IsAuthenticated, UpdateView):
    model = Puskeswan
    template_name = 'puskeswan/form.html'
    form_class = PuskeswanForm
    success_url = reverse_lazy('puskeswan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'puskeswan'
        context['header_title'] = 'Edit puskeswan'
        return context

class PuskeswanDeleteView(IsAuthenticated, DeleteView):
    model = Puskeswan
    template_name = 'component/delete.html'
    success_url = reverse_lazy('puskeswan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Puskeswan'
        context['header_title'] = 'Delete puskeswan'
        return context
