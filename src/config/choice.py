from django.db.models import TextChoices

class RoleUser(TextChoices):
    ADMIN = 'admin'
    PUSKESWAN = 'puskeswan'
    USER = 'user'


class ThreadResult(TextChoices):
    OK = 'OK'
    ALREADY_RUN = 'ALREADY_RUN'
    ERROR = 'ERROR'
    INFO = 'INFO'
