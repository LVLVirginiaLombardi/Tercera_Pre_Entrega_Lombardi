from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView


# from AppCoder import views


urlpatterns = [
   
    path('', inicio, name="Inicio"), 
    
    path('entregables/', entregables, name="Entregables"),
    
    
    path('cursos/', cursos, name="Cursos"),
    path('profesores', profesores, name="Profesores"),
    path('estudiantes', estudiantes, name="Estudiantes"),
    
    #path('cursoFormulario', cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  busquedaCamada, name="BusquedaCamada"),
    path('buscar/', buscar),
    path('leerProfesores', leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', editarProfesor, name="EditarProfesor"),


    path('curso/list', CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', CursoDelete.as_view(), name='Delete'),



    path('login', login_request, name = 'Login'),
    path('register', register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),

    path('editarPerfil', editarPerfil, name="EditarPerfil"),

]


