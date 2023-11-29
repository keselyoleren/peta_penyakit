import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from config.choice import RoleUser
from config.models import BaseModel

# Create your models here.

class Puskeswan(BaseModel):
    name = models.CharField("Name", max_length=255)
    code = models.CharField("Code", max_length=255)
    wilayah_pelayanan = models.ManyToManyField('case.SubDistrict', related_name="puskeswan", blank=True)
    created_by = models.ForeignKey("AccountUser", on_delete=models.CASCADE, related_name="Puskeswan")

    def __str__(self) -> str:
        return self.name

class AccountUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField("Role", max_length=50, choices=RoleUser.choices, default=RoleUser.USER)
    puskeswan = models.ForeignKey("Puskeswan", on_delete=models.CASCADE, related_name="account_user", null=True, blank=True)

    def __str__(self) -> str:
        return self.username

class Feedback(BaseModel):
    name = models.CharField("Name", max_length=255)
    email = models.EmailField("Email", max_length=255)
    telephone = models.CharField("Telephone", max_length=255)
    is_map_use_full = models.BooleanField("Is Map Use Full", default=True)
    is_facility_use_full = models.BooleanField("Is Facility Use Full", default=True)
    comment = models.TextField("Comment")
    sub_district = models.ForeignKey("case.SubDistrict", on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey("AccountUser", on_delete=models.CASCADE, related_name="feedback", blank=True, null=True)

    def __str__(self) -> str:
        return self.name