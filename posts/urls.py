from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name = "home"),
        path("<int:id_post>", views.post_id, name="post_id"),
        path("post_list", views.post_list, name="post_list"),
        path("post_templates", views.post_templates, name="post_templates"),
        path("subir_post", views.subir_post, name="subir_post"),
]