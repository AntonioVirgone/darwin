from django.urls import path

from . import views

urlpatterns = [
    path('', views.findAll, name='findAll'),
    path('create', views.create, name='create'),
]
