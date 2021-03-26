from django.urls import path
from . import views
from cuentas.views import registrar_usuario
from cuentas.views import editar_usuario_personal, editar_usuarios_admin

urlpatterns = [
    path("user/", views.UsuariosListView.as_view(), name='lista-usuarios'),
    path("user/crear/", registrar_usuario, name='crear-usuario'),
    path("user/editar/", editar_usuario_personal, name='editar-usuario'),
    path("user/<int:pk>/", views.UsuariosDetailView.as_view(), name='detalle-usuario'),
    path("user/<int:pk>/editar", views.UsuariosUpdateView.as_view(), name='editar-usuario-admin'),
    path("user/<int:pk>/borrar/", views.UsuariosDeleteView.as_view(), name='borrar-usuario'),


   # path("",views.LoginView.as_view()),
    path("contacto/", views.ContactoListView.as_view(), name='lista-contactos'),
    path("crear/", views.ContactoCreateView.as_view(), name='crear-contacto'),
    path("<int:pk>/", views.ContactoDetailView.as_view(), name='detalle-contacto'),
    path("<int:pk>/editar", views.ContactoUpdateView.as_view(), name='editar-contacto'),
    path("<int:pk>/borrar/", views.ContactoDeleteView.as_view(), name='borrar-contacto'),

    #------------medidas-------------------------------------------
    path("medidas/", views.MedidasListView.as_view(), name='lista-medidas'),
    path("crear/medidas/", views.MedidasCreateView.as_view(), name='crear-medidas'),
    path("medidas/<int:pk>/", views.MedidasDetailView.as_view(), name='detalle-medidas'),
    path("<int:pk>/editar/", views.MedidasUpdateView.as_view(), name='editar-medidas'),
    path("<int:pk>/borrar/", views.MedidasDeleteView.as_view(), name='borrar-medidas'),


    #------------------------------basculas------------------
    path("basculas/", views.BasculasListView.as_view(), name='lista-basculas'),
    path("crear/basculas/", views.BasculasCreateView.as_view(), name='crear-basculas'),
    path("pesa/<int:pk>/", views.BasculasDetailView.as_view(), name='detalle-basculas'),
    path("bas/<str:pk>/editar/", views.BasculasUpdateView.as_view(), name='editar-basculas'),
    path("borrar/<int:pk>/borrar/", views.BasculasDeleteView.as_view(), name='borrar-basculas'),

    #-------------------------------------------------------
]
