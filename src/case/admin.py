from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Province)
class AdminProvince(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Regency)
class AdminRegency(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(SubDistrict)
class AdminSubDistrict(admin.ModelAdmin):
    list_display = ["name", "puskeswan"]

@admin.register(Village)
class AdminVillage(admin.ModelAdmin):
    list_display = ["name", "kode_pos", "longitude", "latitude"]

@admin.register(Disease)
class AdminDisease(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Case)
class AdminCase(admin.ModelAdmin):
    list_display = ["address", "date_discovered", "animal", "village", "diseases", "longitude", "latitude", "total_case"]