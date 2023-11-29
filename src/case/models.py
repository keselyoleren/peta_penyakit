from unicodedata import name
from django.db import models

from config.models import BaseModel
from manage_users.models import Puskeswan   

# Create your models here.
class Province(BaseModel):
    name = models.CharField("Name", max_length=255)

    def __str__(self) -> str:
        return self.name

class Regency(BaseModel):
    name = models.CharField("Name", max_length=255)
    province = models.ForeignKey("Province", on_delete=models.CASCADE, related_name="regency")

    def __str__(self) -> str:
        return self.name

class SubDistrict(BaseModel):
    name = models.CharField("Name", max_length=255)
    regency = models.ForeignKey("Regency", on_delete=models.CASCADE, related_name="sub_district")
    
    def __str__(self) -> str:
        return self.name

class Village(BaseModel):
    name = models.CharField("Name", max_length=255)
    sub_district = models.ForeignKey("SubDistrict", on_delete=models.CASCADE, related_name="village")
    kode_pos = models.CharField("Kode Pos", max_length=255)
    longitude = models.CharField("Longitude", max_length=255, blank=True, null=True)
    latitude = models.CharField("Latitude", max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Disease(BaseModel):
    name = models.CharField("Name", max_length=255)

    def __str__(self) -> str:
        return self.name


class Case(BaseModel):
    address = models.CharField("Aalamat", max_length=255)
    village = models.ForeignKey("Village", on_delete=models.CASCADE, blank=True, null=True)
    animal = models.CharField("Animal", max_length=255)
    diseases = models.ForeignKey("Disease", on_delete=models.CASCADE, blank=True, null=True)
    date_discovered = models.DateTimeField("Date Discovered")
    longitude = models.CharField("Longitude", max_length=255, blank=True, null=True)
    latitude = models.CharField("Latitude", max_length=255, blank=True, null=True)
    total_case = models.IntegerField("Total Case")

    def __str__(self) -> str:
        return self.address


