from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from crud.models import Usuarios

from django.contrib.auth import get_user_model

User = get_user_model()

class FormularioRegistroUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['cedula', 'username', 'password1', 'password2', 'foto']


class FormularioEditarUsuarioPersonal(UserChangeForm):
    class Meta:
        model = User
        fields = ['cedula', 'username', 'foto']


class FormularioEditarUsuarioAdmin(UserChangeForm):
    class Meta:
        model = User
        fields = ['tipo_usuario']

