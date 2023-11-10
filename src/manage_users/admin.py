from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import AccountUser, Feedback, Puskeswan

# Register your models here.
@admin.register(AccountUser)
class UserAdmin(BaseUserAdmin):
    list_display = ('username','email','role', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role')}),
        (_('Personal info'), {'fields': (
            'first_name', 
            'last_name', 
            'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )


@admin.register(Puskeswan)
class PushkeswannAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_by')

@admin.register(Feedback)
class FeedbackAdminView(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone', 'is_map_use_full', 'is_facility_use_full')
