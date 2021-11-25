from django import template
import secrets


register = template.Library()

@register.filter(name='senha_randomica')
def senha_randomica(value, senha):
    senha = secrets.token_urlsafe(10)
    return senha