from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8000/polls/
    path('', views.index, name='index'),
    # ex: localhost:8000/app/sumar/5/2/
    path('sumar/<int:n1>/<int:n2>/', views.suma, name='sumar'),
    # ex: localhost:8000/app/restar/5/2/
    path('restar/<int:n1>/<int:n2>/', views.resta, name='restar'),
    # ex: localhost:8000/app/multiplicar/5/2/
    path('multiplicar/<int:n1>/<int:n2>/', views.multiplicacion, name='multiplicar'),
]