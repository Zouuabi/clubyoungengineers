"""
URL configuration for youngengineers project.

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

from clubadmin.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [ 
    path('add-programme/', add_programme, name='add_programme'),
    path('add-group/', add_group, name='add_group'),
    path('', programmes, name='programmes'),
    path('groupes/', groupes, name='groupes'),
    path('enfants/', children_list, name='enfants'),
    path('presences/', presences, name='presences'),
    path('paiements/', paiements, name='paiements'),


    path('add-group/', add_group, name='add_group'),
    path('modify-group/<int:group_id>/', modify_group, name='modify_group'),
    path('delete-group/<int:group_id>/', delete_group, name='delete_group'),
    
    path('add-child/', add_child, name='add_child'),
    
]
