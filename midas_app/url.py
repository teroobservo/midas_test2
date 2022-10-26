from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name ='midas_app'

urlpatterns = [
    path('', views.index, name='bienvenida'),
path('persona_new/', views.persona_new, name='persona_new'),
]