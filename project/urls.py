from django.urls import path

from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('new/', views.create, name='project_new'),
    path('<int:pk>/', views.findBy, name='project_detail'),
    path('delete/<int:pk>', views.delete, name='project_delete'),
    path('', views.findAll, name='projects'),
]
