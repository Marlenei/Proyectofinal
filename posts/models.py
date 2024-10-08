from django.db import models
from django.utils import timezone
from usuario.models import*
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Categoria (models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return self.nombre
    

class Post(models.Model):
    titulo =models.CharField(max_length=50,null=False)
    slug=models.SlugField()
    subtitulo=models.CharField(max_length=100, null=True, blank=True)
    fecha= models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True,default='Sin categoria')
    imagen = models.ImageField(upload_to='posts/', null=True)
    publicado=models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()

class Comentario(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()

