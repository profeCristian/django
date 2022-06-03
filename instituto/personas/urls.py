from django.conf.urls import url
from django.urls import path, include
from  . import views

urlpatterns=[
    path("index", views.index, name="index" ),
    path("sumar", views.sumar, name="sumar" ),  
    path("calcularSuma", views.calcularSuma, name="calcularSuma" ),
    path("crud", views.crud, name="crud" ),
    path("controlador", views.controlador, name="controlador" ),
    path("home", views.persona_crud, name="persona_crud" ),
    path("personasAdd", views.personasAdd, name="personasAdd" ),
    path('personas_del/<str:pk>', views.personas_del, name='personas_del'),
    path('personas_edit/<str:pk>', views.personas_edit, name='personas_edit'),

    path("productos", views.productos_crud, name="productos_crud" ),
    path("productosAdd", views.productosAdd, name="productosAdd" ),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_edit/<str:pk>', views.productos_edit, name='productos_edit'),

    path('crud_alumno', views.crud_alumno, name='crud_alumno'),
    path('cargar_formulario_alumno', views.cargar_formulario_alumno, name='cargar_formulario_alumno'),
    
    path('del_alumno/<str:pk>', views.del_alumno, name='del_alumno'),
    path('editar_alumno/<str:pk>', views.editar_alumno, name='editar_alumno'),
    #path('add_alumno', views.add_alumno, name='add_alumno'),
]

