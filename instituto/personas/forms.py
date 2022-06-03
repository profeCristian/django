from django import forms
from .models import Persona, Genero, Alumno


class Alumno(forms.ModelForm):
    #use_required_attribute = False  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto'].required = False


    class Meta:
        model = Alumno
        fields = '__all__'