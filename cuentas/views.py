from django.shortcuts import render
from .forms import FormularioRegistroUsuario
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from .forms import FormularioEditarUsuarioPersonal
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth.decorators import login_required


def registrar_usuario(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            authenticate(request, username=username, password=password)
            return redirect('lista-usuarios')
    form = FormularioRegistroUsuario()
    return render(request, 'crud/crear_usuario.html', context={'form': form})

@login_required
def editar_usuario_personal(request):
    if request.method == 'POST':
        form = FormularioEditarUsuarioPersonal(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('lista-usuarios')
    form = FormularioEditarUsuarioPersonal(instance=request.user)
    return render(request, 'crud/editar_usuario.html', context={'form': form})


#@login_required
#@permission_required('usuarios_update')
def editar_usuarios_admin(request):
    pass
