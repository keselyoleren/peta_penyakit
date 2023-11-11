from config.form import AbstractForm
from case.models import Disease

class DiseaseForm(AbstractForm):    
    class Meta:
        model = Disease
        fields = "__all__"