from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('', inicio, name="inicio"), 
    
    
    path('entregables/', entregables, name="entregables"),
    
    
    path('cursos/', cursos, name="cursos"),
    path('curso_create/', cursoCreate, name="curso_create"),
    path('curso_update/<id_curso>/', cursoUpdate, name="curso_update"),
    path('curso_delete/<id_curso>/', cursoDelete, name="curso_delete"),
    
    
    path('profesores', profesores, name="profesores"),
    path('profesores_create', profesoresCreate, name="profesores_create"),
    path('profesor_update/<id_profesor>/', profesorUpdate, name="profesor_update"),
    path('profesor_delete/<id_profesor>/', profesorDelete, name="profesor_delete"),
    
    
    path('estudiantes/', EstudianteList.as_view(), name="estudiantes"),
    path('estudiante_create/', EstudianteCreate.as_view(), name="estudiante_create"),
    path('estudiante_update/<int:pk>/', EstudianteUpdate.as_view(), name="estudiante_update"),
    path('estudiante_delete/<int:pk>/', EstudianteDelete.as_view(), name="estudiante_delete"),
    
    
    path('buscar_cursos/', buscarCursos, name="buscar_cursos"),
    path('encontrar_cursos/', encontrarCursos, name="encontrar_cursos"),
    
    
    path('login/', login_request, name = "login"),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name = "logout"),
    path('register/', register, name = "register"),
    
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    # path('<int:pk>/password/', CambiarClave.as_view(), name="password_reset"),
    
    #path('cursoFormulario', cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  busquedaCamada, name="BusquedaCamada"),
   
    # path('leerProfesores', leerProfesores, name="LeerProfesores"),
    # path('eliminarProfesor/<profesor_nombre>/', eliminarProfesor, name="EliminarProfesor"),
    # path('editarProfesor/<profesor_nombre>/', editarProfesor, name="EditarProfesor"),


    # path('curso/list', CursoList.as_view(), name='List'),
    # path(r'^(?P<pk>\d+)$', CursoDetalle.as_view(), name='Detail'),
    # path(r'^nuevo$', CursoCreacion.as_view(), name='New'),
    # path(r'^editar/(?P<pk>\d+)$', CursoUpdate.as_view(), name='Edit'),
    # path(r'^borrar/(?P<pk>\d+)$', CursoDelete.as_view(), name='Delete'),
]


