
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView,FormView

from django.contrib.auth.forms import AuthenticationForm

from .models import Contacto
from .models import Usuarios
from .models import Medidas
from .models import Basculas


class ContactoListView(ListView):
    model = Contacto
    template_name = "crud/lista_contactos.html"
    # paginate_by = 20


class ContactoDetailView(DetailView):
    model = Contacto
    template_name = "crud/detalle_contacto.html"


class ContactoCreateView(CreateView):
    model = Contacto
    fields = ['id_contacto', 'nombre', 'apellidos', 'movil', 'correo', 'telefono', 'Titulo']
    template_name = "crud/crear_contacto.html"
    success_url = reverse_lazy("lista-contactos")



class ContactoDeleteView(DeleteView):
    model = Contacto
    success_url = reverse_lazy("lista-contactos")
    template_name = 'crud/contacto_confirm_delete.html'


class ContactoUpdateView(UpdateView):
    model = Contacto
    template_name = "crud/editar_contacto.html"
    fields = '__all__'
    success_url = reverse_lazy("lista-contactos")



# ------------------------------------------------MEDIDAS------------------------------------------------------




class MedidasListView(ListView):
    model = Medidas
    template_name = "crud/lista_medidas.html"
    paginate_by = 3



class MedidasDetailView(DetailView):
    model = Medidas
    template_name = "crud/detalle_medidas.html"

class MedidasCreateView(CreateView):
    model = Medidas
    fields = ['id', 'logn_vigas_logn', 'altura_vigas_logn', 'ancho_vigas_logn', 'long_vigas_trans', 'altura_vigas_trans', 'ancho_vigas_trans', 'altura_zapatas_viga_long', 'long_puntos_apoyo', 'altura_zapatas', 'ancho_zapatas', 'largo_zapatas', 'distancia_zapatas', 'altura_obra_civil']
    template_name = "crud/crear_medidas.html"
    success_url = reverse_lazy("lista-medidas")


class MedidasDeleteView(DeleteView):
    model = Medidas
    success_url = reverse_lazy("lista-medidas")
    template_name = 'crud/medidas_confirm_delete.html'



class MedidasUpdateView(UpdateView):
    model = Medidas
    template_name = "crud/editar-medidas.html"
    fields = '__all__'
    success_url = reverse_lazy("lista-medidas")

#--------------------------------------Basculas-----------------------


class BasculasListView(ListView):
    model = Basculas
    template_name = "crud/lista_basculas.html"
    paginate_by = 3


class BasculasDetailView(DetailView):
    model = Basculas
    template_name = "crud/detalle_basculas.html"


class BasculasCreateView(CreateView):
    model = Basculas
    fields = ['cod_bascula', 'descripcion', 'tipos_basculas', 'longitud', 'marca', 'id_plano', 'id_tecnologia', 'longitud_basculas', 'caracteristicas_basculas']
    template_name = "crud/crear_basculas.html"
    success_url = reverse_lazy("lista-basculas")


class BasculasDeleteView(DeleteView):
    model = Basculas
    success_url = reverse_lazy("lista-basculas")
    template_name = 'crud/basculas_confirm_delete.html'


class BasculasUpdateView(UpdateView):
    model = Basculas
    template_name = "crud/editar-basculas.html"
    fields = '__all__'
    success_url = reverse_lazy("lista-basculas")





















#-----------------------------Usuarios_-----------------------------------

class UsuariosListView(ListView):
    model = Usuarios
    template_name = "crud/lista_usuarios.html"
    context_object_name = 'usuarios'
    paginate_by = 3


class UsuariosDetailView(DetailView):
    model = Usuarios
    template_name = "crud/detalle_usuario.html"

#
# class UsuariosCreateView(CreateView):
#     model = Usuarios
#     fields = ['cedula', 'username', 'first_name', 'last_name', 'cargo', 'tipo_usuario', 'foto', 'password']
#     template_name = "crud/crear_usuario.html"
#     success_url = reverse_lazy("lista-usuarios")
#

class UsuariosDeleteView(DeleteView):
    model = Usuarios
    success_url = reverse_lazy("lista-usuarios")
    template_name = 'crud/usuario_confirm_delete.html'


class UsuariosUpdateView(UpdateView):
    model = Usuarios
    template_name = "crud/editar_usuario.html"
    fields = '__all__'
    success_url = reverse_lazy("lista-usuarios")

#---------------------------Clientes----------------------------------------------------------

# Login


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "crud/login.html"
    success_url = reverse_lazy("/user/")
