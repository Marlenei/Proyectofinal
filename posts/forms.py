from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'texto', 'categoria', 'imagen']

class ComentarioForm(forms.ModelForm):
    class Meta: 
        model = Comentario
        fields = ['contenido']