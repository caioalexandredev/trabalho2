"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('api/galileu/procedimento_pericial/<int:id>/', views.procedimento_pericial, name='procedimento_pericial'),
    path('api/word/gerar_documento_teste/', views.gerar_arquivo_word_teste, name='gerar_documento_teste'),
    path('modelo/criar/', views.minha_pagina, name='minha_pagina'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]