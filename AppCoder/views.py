from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
      
      return render(request, "AppCoder/padre.html")


@login_required
def entregables(request):

      return render(request, "AppCoder/entregables.html")


@login_required
def cursos(request): 
      contexto = {'cursos': Curso.objects.all().order_by("id")}
      
      return render(request, "AppCoder/cursos.html", contexto)

      
@login_required    
def cursoCreate(request):

      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) 
            if miFormulario.is_valid():   
                  curso_nombre = miFormulario.cleaned_data.get("nombre")
                  curso_camada = miFormulario.cleaned_data.get("camada")
                  curso = Curso(nombre=curso_nombre, camada=curso_camada) 
                  curso.save()
                  return redirect(reverse_lazy('cursos'))

      else: 
            miFormulario = CursoFormulario() 

      return render(request, "AppCoder/curso_form.html", {"form": miFormulario})


@login_required
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
      
      return render(request, "AppCoder/curso_form.html", {"form": miFormulario})


@login_required
def cursoDelete(request, id_curso):
      curso = Curso.objects.get(id=id_curso)
      curso.delete()
      return redirect(reverse_lazy('cursos'))       
 

@login_required
def profesores(request):
      contexto = {'profesores': Profesor.objects.all().order_by("id")}
      return render(request, "AppCoder/profesores.html", contexto)


@login_required
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

      return render(request, "AppCoder/profesores.html", {"form":miFormulario})


@login_required
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
      
      return render(request, "AppCoder/profesores.html", {"form":miFormulario})

@login_required
def profesorDelete(request, id_profesor):
      profesor = Profesor.objects.get(id=id_profesor)
      profesor.delete()
      return redirect(reverse_lazy('profesores'))


@login_required
def buscarCursos(request):
      return render(request, "AppCoder/buscar.html")

@login_required
def encontrarCursos(request):
      if  request.GET["buscar"]:
            patron = request.GET["buscar"]
            cursos = Curso.objects.filter(nombre__icontains=patron)
            contexto = {"cursos": cursos}
            return render(request, "AppCoder/cursos.html", contexto)
            
      contexto = {'cursos': Curso.objects.all()}
      return render(request, "AppCoder/cursos.html", contexto)  



class EstudianteList(LoginRequiredMixin, ListView):
      model = Estudiante
      
class EstudianteCreate(LoginRequiredMixin, CreateView):
      model = Estudiante
      fields = ["nombre", "apellido", "email"]
      success_url = reverse_lazy("estudiantes")
      
class EstudianteUpdate(LoginRequiredMixin, UpdateView):
      model = Estudiante
      fields = ["nombre", "apellido", "email"]
      success_url = reverse_lazy("estudiantes")
      
class EstudianteDelete(LoginRequiredMixin, DeleteView):
      model = Estudiante
      success_url = reverse_lazy("estudiantes")
      

def login_request(request):
      if request.method == "POST":
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(request, username=usuario, password=clave)

            if user is not None:
                  login(request, user)
                  
                  return render(request, "AppCoder/padre.html")
            
            else:
                  return redirect(reverse_lazy('login'))

      else:
            miFormulario = AuthenticationForm()
                        
      return render(request, "AppCoder/login.html" ,  {'form': miFormulario} )


def register(request):
      if request.method == "POST":
            miFormulario = UserRegisterForm(request.POST)
            if miFormulario.is_valid():
                  usuario = miFormulario.cleaned_data.get("username")
                  miFormulario.save()
                  return redirect(reverse_lazy('inicio'))

      else:
            miFormulario = UserRegisterForm()     

      return render(request, "AppCoder/registro.html" ,  {"form": miFormulario})


@login_required
def editarPerfil(request):
      usuario = request.user
      if request.method == "POST":
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid():
                  user = User.objects.get(username=usuario)
                  user.email = miFormulario.cleaned_data.get("email")
                  user.first_name = miFormulario.cleaned_data.get("first_name")
                  user.last_name = miFormulario.cleaned_data.get("last_name")
                  user.save()
                  return redirect(reverse_lazy('inicio'))
            
      else: 
            miFormulario= UserEditForm(instance=usuario) 

      return render(request, "AppCoder/editarPerfil.html", {"form": miFormulario} )


# class CambiarClave(LoginRequiredMixin, PasswordChangeView):
#       template_name = "AppCoder/password_reset.html"
#       success_url = reverse_lazy("inicio")



# class CursoList(ListView):

#       model = Curso 
#       template_name = "AppCoder/cursos_list.html"



# class CursoDetalle(DetailView):

#       model = Curso
#       template_name = "AppCoder/curso_detalle.html"



# class CursoCreacion(CreateView):

#       model = Curso
#       success_url = "/AppCoder/curso/list"
#       fields = ['nombre', 'camada']


# class CursoUpdate(UpdateView):

#       model = Curso
#       success_url = "/AppCoder/curso/list"
#       fields  = ['nombre', 'camada']


# class CursoDelete(DeleteView):

#       model = Curso
#       success_url = "/AppCoder/curso/list"





# def logout_request(request):
#       logout(request)
     
#       return redirect("inicio")
     










