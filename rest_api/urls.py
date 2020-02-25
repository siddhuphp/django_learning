from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('siddhu', views.siddhu, name='siddhu'),
]