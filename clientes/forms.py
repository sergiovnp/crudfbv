from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'edad', 'dni', 'status')
        labels = {
            'nombre': _('Nombre'),
        }
        help_texts = {
            'nombre': _('Ingrese su nombre.'),
        }
        error_messages = {
            'nombre': {
                'max_length': _("Máximo 9 caracteres."),
            },
        }
        