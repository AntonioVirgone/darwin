from django.urls import path

from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('all', views.findAll, name='findAll'),
]
