from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import RopaTrabajo
from .forms import RopaTrabajoFormulario, BusquedaRopaTrabajo
from .models import Avatar
from .models import Toldos
from .forms import ToldosFormulario

from .models import ArtCamping
from .forms import ArtCampingFormulario
from .forms import RegistroUsuarioForm
from .forms import EditProfileForm
from .forms import AvatarForm
from django.contrib.auth import views as auth_views
# * Ejemplo de CARGA DE TEMPLATE MANUAL

@login_required
def inicio(request):
    template = loader.get_template("user/inicio.html")
    return HttpResponse(template.render())


def probando_template(request):
    contexto = {
        "nom": "Juan",
        "ap": "Perez",
        "notas": [10, 7, 3, 9],
    }
    return render(request, "user/probando.html", contexto)

#########################################
# Vistas basadas en FUNCIONES
def ropaTrabajo(request):
    ropaTrabajo= RopaTrabajo.objects.all()
    contexto = {"ropaTrabajo":ropaTrabajo}    
    return render(request, "user/RopaTrabajo.html", contexto)

def toldo(request):
    toldos= Toldos.objects.all()
    contexto = {"toldos":toldos}    
    return render(request, "user/Toldos.html", contexto)

def artc(request):
    articulo= ArtCamping.objects.all()
    contexto = {"articulo":articulo}    
    return render(request, "user/ArtCamping.html", contexto)

########################################################





def ropaTrabajoFormulario(request):
    if request.method == "POST":
        form = RopaTrabajoFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            talle = form.cleaned_data["talle"]
            precio = form.cleaned_data["precio"]

            ropa = RopaTrabajo(nombre=nombre, talle=talle,precio=precio)
            ropa.save()
            return render(request, "user/RopaTrabajo_exito.html")
    else:
        form = RopaTrabajoFormulario()
    return render(request, "user/RopaTrabajo_formulario.html", {"form": form})

def toldoFormulario(request):
    if request.method == "POST":
        form = ToldosFormulario(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data["cliente"]
            tipo_toldo = form.cleaned_data["tipo_toldo"]
            precio = form.cleaned_data["precio"]

            told = Toldos(cliente=cliente, tipo_toldo=tipo_toldo,precio=precio)
            told.save()
            return render(request, "user/Toldos_exito.html")
    else:
        form = ToldosFormulario()
    return render(request, "user/Toldos_formulario.html", {"form": form})

def artcFormulario(request):
    if request.method == "POST":
        form = ArtCampingFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            precio = form.cleaned_data["precio"]

            art = ArtCamping(nombre=nombre, precio=precio)
            art.save()
            return render(request, "user/ArtCamping_exito.html")
    else:
        form = ArtCampingFormulario()
    return render(request, "user/ArtCamping_formulario.html", {"form": form})


def buscarRopaTrabajo(request):
    if request.method == "GET":
        form = BusquedaRopaTrabajo(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            resultados = RopaTrabajo.objects.filter(nombre=nombre)
            return render(
                request,
                "user/resultados_busqueda.html",
                {"resultados": resultados, "form": form},
            )
    else:
        form = BusquedaRopaTrabajo()
    return render(request, "user/buscar_RopaTrabajo.html", {"form": form})

####################################   Vistas basadas en CLASES  ###################


class ToldoList(LoginRequiredMixin, ListView):
    model = Toldos
    template_name = "user/leer_toldos.html"
    context_object_name = "toldos"


class ToldoCrear(LoginRequiredMixin, CreateView):
    model = Toldos
    fields = ["cliente", "tipo_toldo", "precio"]
    template_name = "user/toldos_form.html"
    success_url = reverse_lazy("toldos_list")


class ToldoEditar(LoginRequiredMixin, UpdateView):
    model = Toldos
    fields = ["cliente", "tipo_toldo", "precio"]
    template_name = "user/editar_toldos.html"
    success_url = reverse_lazy("toldos_list")


class ToldoBorrar(LoginRequiredMixin, DeleteView):
    model = Toldos
    template_name = "user/toldos_confirm_delete.html"
    success_url = reverse_lazy("toldos_list")

class ToldoDetalle(LoginRequiredMixin, DetailView):
    model = Toldos
    template_name = "user/toldos_detalle.html"

############################ 

class ArtCampingList(LoginRequiredMixin, ListView):
    model = ArtCamping
    template_name = "user/leer_ArtCamping.html"
    context_object_name = "ArtCamping"


class ArtCampingCrear(LoginRequiredMixin, CreateView):
    model = ArtCamping
    fields = ["nombre", "precio"]
    template_name = "user/ArtCamping_form.html"
    success_url = reverse_lazy("ArtCamping_list")


class ArtCampingEditar(LoginRequiredMixin, UpdateView):
    model = ArtCamping
    fields = ["nombre" , "precio"]
    template_name = "user/editar_ArtCamping.html"
    success_url = reverse_lazy("ArtCamping_list")


class ArtCampingBorrar(LoginRequiredMixin, DeleteView):
    model = ArtCamping
    template_name = "user/ArtCamping_confirm_delete.html"
    success_url = reverse_lazy("ArtCamping_list")

class ArtCampingDetalle(LoginRequiredMixin, DetailView):
    model = ArtCamping
    template_name = "user/ArtCamping_detalle.html"





def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form})


# -- CODE - Parte III ---
def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print(f"ERRORES DEL FORMULARIO: {form.errors}") 
    else:
        form = RegistroUsuarioForm()
    return render(request, "user/register.html", {"form": form})

# user/views.py
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect

def logout_view(request):
    django_logout(request)
    return redirect('inicio') 

@login_required
def editarPerfil(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "user/editar_perfil.html", {"form": form})


# clase final - 04 creacion de la vista para gestionar avatares
@login_required
def upload_avatar(request):
    avatar, _ = Avatar.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = AvatarForm(instance=avatar)
    return render(request, "user/upload_avatar.html", {"form": form, "avatar": avatar})

@login_required
def about(request):
    return render(request, "user/about.html")