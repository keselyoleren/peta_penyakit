from config.form import AbstractForm
from case.models import Case, Village
from django import forms

class CaseForm(AbstractForm):    
    class Meta:
        model = Case
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance', None)
        villigae_init_form = [('', '---------')]
        if instance:
            villigae_init_form = [(instance.village.id, instance.village.name)]
        


        self.fields['village'].widget = forms.Select(
            attrs={
                'id': 'id_village',
                'class':'form-control',                
            },
            choices=villigae_init_form
        )
       