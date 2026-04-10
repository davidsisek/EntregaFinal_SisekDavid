from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar

# Formulario para agregar un nuevo curso
class RopaTrabajoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre del artículo")
    talle = forms.CharField(max_length=50, label="Talle")
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")

# Formulario para agregar un nuevo curso
class ToldosFormulario(forms.Form):
    cliente = forms.CharField(max_length=50,label="Nombre del cliente")
    tipo_toldo = forms.CharField(max_length=50, label="Tipo de Toldo")
    precio = forms.DecimalField(max_digits=10, decimal_places=2,label="Precio")

class ArtCampingFormulario(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre del artículo")
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")

# Formulario de búsqueda de cursos por camada
class BusquedaRopaTrabajo(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre del artículo")

############## Parte Nueva ###############

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

# clase final - 04 uso de UserChangeForm
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
        labels = {
            "email": "Correo Electronico",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }


# clase final - 05 creacion del formulario de avatar
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]
