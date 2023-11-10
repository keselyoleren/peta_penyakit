import email
from pyexpat import model
from unicodedata import name
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from config.choice import RoleUser
from config.models import BaseModel

# Create your models here.

class Puskeswan(BaseModel):
    name = models.CharField("Name", max_length=255)
    code = models.CharField("Code", max_length=255)
    created_by = models.ForeignKey("AccountUser", on_delete=models.CASCADE, related_name="Puskeswan")

class AccountUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField("Role", max_length=50, choices=RoleUser.choices, default=RoleUser.USER)
    puskeswan = models.ForeignKey("Puskeswan", on_delete=models.CASCADE, related_name="account_user", null=True, blank=True)



class Feedback(BaseModel):
    name = models.CharField("Name", max_length=255)
    email = models.EmailField("Email", max_length=255)
    telephone = models.CharField("Telephone", max_length=255)
    is_map_use_full = models.BooleanField("Is Map Use Full", default=True)
    is_facility_use_full = models.BooleanField("Is Facility Use Full", default=True)
    comment = models.TextField("Comment")