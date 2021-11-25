from usuarios.models import Usuario


def listar_usuario_id(id):
    usuario = Usuario.objects.get(id=id)
    return usuario