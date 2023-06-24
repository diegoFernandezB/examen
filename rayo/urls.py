#from django.conf.urls import url
from django.urls import path
from. import views



urlpatterns =[
    path('index', views.index, name='index'),
    path('fichaServ', views.fichaServ, name='fichaServ'),
    path('carritoCompras', views.carritoCompras, name='carritoCompras'),
    path('CrudTrabajos', views.CrudTrabajos, name='CrudTrabajos'),
    path('fichamecas', views.fichamecas, name='fichamecas'),
    path('loguin', views.loguin, name='loguin'),
    path('login', views.login, name='login'),
    path('meca1', views.meca1, name='meca1'),
    path('meca2', views.meca2, name='meca2'),
    path('meca3', views.meca3, name='meca3'),
    path('plantillamec', views.plantillamec, name='plantillamec'),
    path('plantillaserv', views.plantillaserv, name='plantillaserv'),
    path('pll', views.pll, name='pll'),
    path('registro', views.registro, name='registro'),
    path('reserva', views.reserva, name='reserva'),
    path('trabajo1', views.trabajo1, name='trabajo1'),
    path('trabajo2', views.trabajo2, name='trabajo2'),
    path('trabajo3', views.trabajo3, name='trabajo3'),
    path('trabajo4', views.trabajo4, name='trabajo4'),
    path('trabajo5', views.trabajo5, name='trabajo5'),
    path('base', views.base, name='base'),

    path('subirArchivo', views.subirArchivo, name='subirArchivo'),
    path('subirArchivo_add', views.subirArchivo_add, name='subirArchivo_add'),
    path('subirArchivo_del/<str:id_archivo>', views.subirArchivo_del, name='subirArchivo_del'),
    path('subirArchivo_edit/<str:id_archivo>', views.subirArchivo_edit, name='subirArchivo_edit'),
    
    
    ]

