from config.form import AbstractForm
from case.models import Province, Regency, SubDistrict, Village

class ProvinceForm(AbstractForm):    
    class Meta:
        model = Province
        fields = "__all__"

class RegencyForm(AbstractForm):    
    class Meta:
        model = Regency
        fields = "__all__"

class SubDistrictForm(AbstractForm):    
    class Meta:
        model = SubDistrict
        fields = "__all__"

class VillageForm(AbstractForm):    
    class Meta:
        model = Village
        fields = "__all__"