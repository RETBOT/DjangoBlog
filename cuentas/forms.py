#cuentas/froms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioPers

class FormularioCreacionUsuarioPers(UserCreationForm):
    class Meta(UserCreationForm):
        model = UsuarioPers
        fields = ('username','email','edad',)

class FormularioCambioUsuarioPers(UserChangeForm):
    class Meta:
        model = UsuarioPers
        fields = ('username','email','edad',)

