#cuentas/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import FormularioCambioUsuarioPers, FormularioCreacionUsuarioPers
from .models import UsuarioPers

# Register your models here.
class UsuarioPersAdmin(UserAdmin):
    add_form = FormularioCreacionUsuarioPers
    form = FormularioCambioUsuarioPers
    model = UsuarioPers
    list_display = ['email', 'username', 'edad', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('edad',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('edad',)}),
    )

admin.site.register(UsuarioPers, UsuarioPersAdmin)