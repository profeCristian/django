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
]

#  path("sumar/<int:resultado>", views.sumar, name="sumar" ),