from django.contrib import admin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    fields = ('titulo', 'slug', 'subtitulo', 'texto', 'categoria', 'imagen', 'autor')
    prepopulated_fields= {'slug' : ('titulo',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)
admin.site.register(Comentario)