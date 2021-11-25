from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForms

# Create your views here.

def listar_usuarios(request):
    usuarios = Usuario.objects.all() #retorna todos os dados dos usuários
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForms(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
    form_usuario = UsuarioForms()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})