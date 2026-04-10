from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import logout as django_logout
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("probando/", views.probando_template, name="probando"),
    path("RopaTrabajo/", views.ropaTrabajo, name="RopaTrabajo"),
    path("RopaTrabajoFormulario/",views.ropaTrabajoFormulario, name="RopaTrabajoFormulario"),
    path("Toldos/", views.toldo, name="Toldos"),
    path("ToldosFormulario/",views.toldoFormulario, name="ToldosFormulario"),
    path("ArtCamping/", views.artc, name="ArtCamping"),
    path("ArtCampingFormulario/",views.artcFormulario, name="ArtCampingFormulario"),
    path("BuscarRopaTrabajo/",views.buscarRopaTrabajo, name="buscarRopaTrabajo"),
 ####################################   TOLDOS ####################################  
# Lista de Toldos
    path('toldos/lista/', views.ToldoList.as_view(), name='toldos_list'),
    
    # Detalle (El "Leer más") - IMPORTANTE el <int:pk>
    path('toldos/detalle/<int:pk>/', views.ToldoDetalle.as_view(), name='toldos_detalle'),
    
    # Crear
    path('toldos/crear/', views.ToldoCrear.as_view(), name='toldos_crear'),
    
    # Editar - También necesita el ID (<int:pk>)
    path('toldos/editar/<int:pk>/', views.ToldoEditar.as_view(), name='toldos_editar'),
    
    # Borrar - También necesita el ID (<int:pk>)
    path('toldos/borrar/<int:pk>/', views.ToldoBorrar.as_view(), name='toldos_borrar'),

####################################  ARTICULOS CAMPING #################################### 

# Lista de ArtCamping
    path('ArtCamping/lista/', views.ArtCampingList.as_view(), name='ArtCamping_list'),
    
    # Detalle 
    path('ArtCamping/detalle/<int:pk>/', views.ArtCampingDetalle.as_view(), name='ArtCamping_detalle'),
    
    # Crear
    path('ArtCamping/crear/', views.ArtCampingCrear.as_view(), name='ArtCamping_crear'),
    
    # Editar - 
    path('ArtCamping/editar/<int:pk>/', views.ArtCampingEditar.as_view(), name='ArtCamping_editar'),
    
    # Borrar 
    path('ArtCamping/borrar/<int:pk>/', views.ArtCampingBorrar.as_view(), name='ArtCamping_borrar'),


####################################   LOGINs #################################### 
   
path("login/", views.login_request, name="login"),
path("register/", views.register, name="register"),
path("logout/", views.logout_view, name="logout"),
########################## PERFIL ###########

path("editarPerfil/", views.editarPerfil, name="EditarPerfil"),
    # clase final - 04 creacion de la url para cargar avatar
path("upload-avatar/", views.upload_avatar, name="upload_avatar"),

path("about/", views.about, name="about"),
]