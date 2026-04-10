from django.contrib import admin
from django.db import models



from django.contrib import admin
from .models import Toldos, RopaTrabajo, ArtCamping

# 1. Personalización para el Modelo Principal (Toldos)
class ToldosAdmin(admin.ModelAdmin):
    list_display = ("cliente", "tipo_toldo", "precio")
    search_fields = ("cliente", "tipo_toldo")
    list_filter = ("tipo_toldo",)

# 2. Personalización para Ropa de Trabajo
class RopaTrabajoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "talle", "precio")
    search_fields = ("nombre",)
    list_filter = ("talle",)

# 3. Personalización para Artículos de Camping
class ArtCampingAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    search_fields = ("nombre",)

# --- REGISTRO DE TODOS LOS MODELOS ---
admin.site.register(Toldos, ToldosAdmin)
admin.site.register(RopaTrabajo, RopaTrabajoAdmin)
admin.site.register(ArtCamping, ArtCampingAdmin)
