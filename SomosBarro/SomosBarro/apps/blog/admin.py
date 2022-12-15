from django.contrib import admin
from .models import Categorias, Noticia, Comentarios
# Register your models here.
admin.site.register(Categorias, admin.ModelAdmin)
admin.site.register(Noticia, admin.ModelAdmin)
admin.site.register(Comentarios, admin.ModelAdmin)