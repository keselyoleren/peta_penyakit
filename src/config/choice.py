from django.db.models import TextChoices

class RoleUser(TextChoices):
    ADMIN = 'admin'
    PUSKESWAN = 'puskeswan'
    USER = 'user'
