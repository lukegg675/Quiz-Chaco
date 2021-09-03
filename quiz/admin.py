from django.contrib import admin
from .models import Pregunta, Respuesta, Partida,Categoria

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'autor','id_categoria')

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id_pregunta', 'opcion', 'puntaje')

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'resultado')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'descripcion')


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Partida, PartidaAdmin)
admin.site.register(Categoria, CategoriaAdmin)



