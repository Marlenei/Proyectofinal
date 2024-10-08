from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import * 
from django.template import loader
from .forms import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    return HttpResponse("Hola mundo")

def post_list(request):
    post_list=Post.objects.all()
    return HttpResponse(post_list)

def post_id(request, pk):
    post = Post.objects.get(id=pk)
    comentarios = Comentario.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post':post, 'comentarios':comentarios})

@login_required
def Comentar_Noticia(request):
	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_post', None)# OBTENGO LA PK
	post = Post.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(autor = usu, post = post, contenido = com)
	return redirect(reverse_lazy('post_detail', kwargs={'pk': noti}))

@login_required
def delete_comentario(request, com_id):
    comentario = get_object_or_404(Comentario, pk=com_id)
    if comentario.autor == request.user:
        comentario.delete()   
    
    return redirect('post_templates')


@login_required
def delete_posts(request, post_element_id):
    post = get_object_or_404(Post, pk=post_element_id)
    if post.autor == request.user:
        post.delete()   
    
    return redirect('post_templates')

def post_list(request):
    post_list=Post.objects.all()
    return HttpResponse(post_list)

def post_templates(request):
    post_list = Post.objects.all()
    template = loader.get_template("post_templates.html")
    context = {"post_list": post_list,}
    return HttpResponse(template.render(context, request))

@login_required
def misposteos(request):
    usu = request.user
    post_list = Post.objects.filter(autor = usu)
    template = loader.get_template("misposteos.html")
    context = {"post_list": post_list,}
    return HttpResponse(template.render(context, request))

@login_required(login_url='registro.html')
def subir_post(request):
    usu = request.user
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            post.autor_id = usu.id 
            post.save()  
    else:
        form = PostForm()

    return render(request, 'subir_post.html', {'form':PostForm})



