from config.form import AbstractForm
from case.models import Puskeswan, SubDistrict
from django import forms
from django.contrib.admin.widgets import (
    FilteredSelectMultiple,
    AutocompleteSelect,
)


class PuskeswanForm(AbstractForm):    
    wilayah_pelayanan = forms.ModelMultipleChoiceField(
            queryset=SubDistrict.objects.all(), 
            widget=FilteredSelectMultiple("Kecamatan", is_stacked=False),
            required=False
        )
    class Meta:
        model = Puskeswan
        fields = "__all__"

    class Media:
        css = {
            'all': ('/static/jazzmin/css/main.css',),
        }
        js = ('/admin/jsi18n',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        