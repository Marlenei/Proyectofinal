from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from django.template import loader
from .forms import PostForm


def index(request):
    return HttpResponse("Hola mundo")

def post_id(request, id_post):
    response = "La persona con id: es %s"
    return HttpResponse (response % id_post)

def post_list(request):
    post_list=Post.objects.all()
    return HttpResponse(post_list)

def post_templates(request):
    post_list = Post.objects.all()
    template = loader.get_template("post_templates.html")
    context = {"post_list": post_list,}
    return HttpResponse(template.render(context, request))

def subir_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request, 'subir_post.html', {
    'form':form,
    })
