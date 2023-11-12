# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from case.form.case_form import CaseForm

from config.permis import IsAuthenticated
from case.models import Case



class CaseListView(IsAuthenticated, ListView):
    model = Case
    template_name = 'case/list.html'
    context_object_name = 'list_case'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Case'
        context['header_title'] = 'List Case'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('case-create')
        return context

class CaseCreateView(IsAuthenticated, CreateView):
    model = Case
    template_name = 'case/form.html'
    form_class = CaseForm
    success_url = reverse_lazy('case-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Case'
        context['header_title'] = 'Tambah Case'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class CaseUpdateView(IsAuthenticated, UpdateView):
    model = Case
    template_name = 'case/form.html'
    form_class = CaseForm
    success_url = reverse_lazy('case-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Case'
        context['header_title'] = 'Edit Case'
        return context

class CaseDeleteView(IsAuthenticated, DeleteView):
    model = Case
    template_name = 'component/delete.html'
    success_url = reverse_lazy('case-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Case'
        context['header_title'] = 'Delete Case'
        return context
