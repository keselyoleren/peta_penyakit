# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from case.form.case_form import CaseForm

from config.permis import IsPublicAuth
from manage_users.models import AccountUser, Feedback, Puskeswan



class FeedbackListView(IsPublicAuth, ListView):
    model = Feedback
    template_name = 'feedback/list.html'
    context_object_name = 'list_feedback'

    def get_queryset(self):
        puskeswan = self.request.user.puskeswan
        if puskeswan:
            user = AccountUser.objects.filter(puskeswan=puskeswan)
            return super().get_queryset().filter(sub_district__in=puskeswan.wilayah_pelayanan.all())
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Feedback'
        context['header_title'] = 'List Feedback'
        return context

