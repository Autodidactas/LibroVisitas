from django import forms
from .models import *

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
