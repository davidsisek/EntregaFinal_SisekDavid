from django.db import models
# crear usuario a partir de la clase User de Django
from django.contrib.auth.models import User
# Create your models here.

class Toldos(models.Model):
    cliente = models.CharField(max_length=50)
    tipo_toldo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.cliente} ({self.tipo_toldo})"


class RopaTrabajo(models.Model):
    nombre = models.CharField(max_length=50)
    talle = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nombre} (Talle: {self.talle})" 

class ArtCamping(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.nombre
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agregar campos adicionales al perfil de usuario
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    def __str__(self):
        return self.user.username
