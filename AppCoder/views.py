from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *
# from typing import List

# from django.shortcuts import redirect, render, HttpResponse
# from django.http import HttpResponse
# from AppCoder.models import Curso, Profesor
# from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserRegisterForm,UserEditForm

from django.views.generic import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User


# #Para la prueba unitaria
# import string
# import random


#Para el login

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

#Decorador por defecto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# from django.views.generic.base import TemplateView


# Create your views here.

# def curso(request):

#       return render(request, "AppCoder/index.html")


def inicio(request):
      
      return render(request, "AppCoder/index.html")

# @login_required
def entregables(request):

      return render(request, "AppCoder/entregables.html")

# @login_required
def cursos(request): 
      contexto = {'cursos': Curso.objects.all().order_by("ID")}
      return render(request, "AppCoder/cursos.html", contexto)
      
# @login_required    
def cursoCreate(request):

      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) 
            if miFormulario.is_valid():   
                  curso_nombre = miFormulario.cleaned_data.get("nombre")
                  curso_camada = miFormulario.cleaned_data.get("camada")
                  curso = Curso(nombre=curso_nombre, camada=curso_camada) 
                  curso.save()
                  return redirect(reverse_lazy('cursos'))
                  # return render(request, "AppCoder/inicio.html") 

      else: 
            miFormulario = CursoFormulario() 

      return render(request, "AppCoder/curso_form.html", {"miFormulario": miFormulario})

# @login_required
def cursoUpdate(request, id_curso):
      curso = Curso.objects.get(id=id_curso)
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST)
            if miFormulario.is_valid():
                  curso.nombre = miFormulario.cleaned_data.get("nombre")
                  curso.camada = miFormulario.cleaned_data.get("camada")
                  curso.save()
                  return redirect(reverse_lazy('cursos'))
            
      else:
            miFormulario = CursoFormulario(initial={'nombre': curso.nombre, 'camada': curso.camada})
      
      return render(request, "AppCoder/curso_form.html", {"miFormulario": miFormulario})

# @login_required
def cursoDelete(request, id_curso):
      curso = Curso.objects.get(id=id_curso)
      curso.delete()
      return redirect(reverse_lazy('cursos'))        

# @login_required
def profesores(request):
      contexto = {'profesores': Profesor.objects.all().order_by("ID")}
      return render(request, "AppCoder/profesores.html", contexto)

# @login_required
def profesoresCreate(request):
      if request.method == "POST":
            miFormulario = ProfesorFormulario(request.POST)
            if miFormulario.is_valid():
                  profesor_nombre = miFormulario.cleaned_data.get("nombre")
                  profesor_apellido = miFormulario.cleaned_data.get("apellido")
                  profesor_email = miFormulario.cleaned_data.get("email")
                  profesor_profesion = miFormulario.cleaned_data.get("profesion")
                  
                  profesor = Profesor(
                        nombre=profesor_nombre, 
                        apellido=profesor_apellido, 
                        email=profesor_email, 
                        profesion=profesor_profesion) 
                  profesor.save()
                  return redirect(reverse_lazy('profesores'))
            
      else: 
            miFormulario = ProfesorFormulario() 

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

# @login_required
def profesorUpdate(request, id_profesor):
      profesor = Profesor.objects.get(id=id_profesor)
      if request.method == "POST":
            miFormulario = ProfesorFormulario(request.POST)
            if miFormulario.is_valid():
                  profesor.nombre = miFormulario.cleaned_data.get("nombre")
                  profesor.apellido = miFormulario.cleaned_data.get("apellido")
                  profesor.email = miFormulario.cleaned_data.get("email")
                  profesor.profesion = miFormulario.cleaned_data.get("profesion")
                  profesor.save()
                  return redirect(reverse_lazy('profesores'))
      
      else:
            miFormulario = ProfesorFormulario(initial= {'nombre': profesor.nombre,
                                                        'apellido': profesor.apellido,
                                                        'email': profesor.email,
                                                        'profesion': profesor.profesion
                                                        })
      
      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

# @login_required
def profesorDelete(request, id_profesor):
      profesor = Profesor.objects.get(id=id_profesor)
      profesor.delete()
      return redirect(reverse_lazy('profesores'))

      
# def estudiantes(request):

#       return render(request, "AppCoder/estudiantes.html")


# @login_required
def buscarCursos(request):
      if  request.GET["buscar"]:
            patron = request.GET["buscar"]
            cursos = Curso.objects.filter(nombre__icontains=patron)
            contexto = {"cursos": cursos}
            return render(request, "AppCoder/cursos.html", contexto)

            # #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            # camada = request.GET['camada'] 
            # cursos = Curso.objects.filter(camada__icontains=camada)
            
      contexto = {'cursos': Curso.objects.all()}
      return render(request, "AppCoder/cursos.html", contexto)  

      # else: 

	#       respuesta = "No enviaste datos"

      # #No olvidar from django.http import HttpResponse
      # #return HttpResponse(respuesta)
      # return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})



def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al menú
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})




class CursoList(ListView):

      model = Curso 
      template_name = "AppCoder/cursos_list.html"



class CursoDetalle(DetailView):

      model = Curso
      template_name = "AppCoder/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/AppCoder/curso/list"




def logout_request(request):
      logout(request)
     
      return redirect("inicio")
     

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppCoder/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})



@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
