from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_usuarios, name='listar_usuarios'),
    path('cadastrar', cadastrar_usuario, name='cadastrar_usuario'),
]
