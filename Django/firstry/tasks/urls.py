from django.urls import path
from . import views

#Esto es obligatorio para que django pueda encontrar las urls de la app
urlpatterns = [
  path('', views.home, name='home'),
]