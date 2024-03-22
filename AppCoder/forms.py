
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CursoFormulario(forms.Form):

    curso = forms.CharField(max_length=50, required=True)
    camada = forms.IntegerField(required=True)


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=60, required=True)
    apellido= forms.CharField(max_length=60, required=True)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50, required=True)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        # #Saca los mensajes de ayuda
        # help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail", required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)
    # password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"] 
        #Saca los mensajes de ayuda
        # help_texts = {k:"" for k in fields}
