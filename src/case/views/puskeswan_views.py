# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from config.choice import RoleUser

from config.permis import IsAuthenticated, IsPuskeswan
from case.models import Puskeswan
from case.form.puskeswan_form import PuskeswanForm


class PuskeswanListView(IsPuskeswan, ListView):
    model = Puskeswan
    template_name = 'puskeswan/list.html'
    context_object_name = 'list_puskeswan'

    def get_queryset(self):
        if self.request.user.role == RoleUser.PUSKESWAN:
            return super().get_queryset().filter(created_by=self.request.user)
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Puskeswan'
        context['header_title'] = 'List puskeswan'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('puskeswan-create')
        return context

class PuskeswanCreateView(IsPuskeswan, CreateView):
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

class PuskeswanUpdateView(IsPuskeswan, UpdateView):
    model = Puskeswan
    template_name = 'puskeswan/form.html'
    form_class = PuskeswanForm
    success_url = reverse_lazy('puskeswan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'puskeswan'
        context['header_title'] = 'Edit puskeswan'
        return context

class PuskeswanDeleteView(IsPuskeswan, DeleteView):
    model = Puskeswan
    template_name = 'component/delete.html'
    success_url = reverse_lazy('puskeswan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Puskeswan'
        context['header_title'] = 'Delete puskeswan'
        return context
