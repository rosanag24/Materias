from django import forms
from django.core.validators import RegexValidator
from postgrado.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RegistrarMatForm(forms.Form):
    nombreMateria = forms.CharField(label='Nombre de la materia', max_length=60)
    codigoMateria = forms.CharField(label='Código de la materia', max_length=7,
                    validators=[RegexValidator('^[a-z]{2}-[0-9]{4}$',
                    message="Formato de código incorrecto")])
    unidadesCredito = forms.IntegerField(label='Unidades de crédito',
                       max_value=16,min_value=1)
    area = forms.CharField(label='Área', max_length=60)
    programaPertenece = forms.CharField(label='Programa al que pertenece')
    departamento = forms.IntegerField(label='Departamento')

    def clean_codigoMateria(self):
        codigoMateria = self.cleaned_data['codigoMateria']
        if Asignatura.objects.filter(codigoMateria=codigoMateria).count() > 0:
            raise ValidationError(_('La materia ya existe'), code='mat_exist')
        return codigoMateria


