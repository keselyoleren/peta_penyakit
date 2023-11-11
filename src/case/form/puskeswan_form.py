from config.form import AbstractForm
from case.models import Puskeswan

class PuskeswanForm(AbstractForm):    
    class Meta:
        model = Puskeswan
        fields = "__all__"