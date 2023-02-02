from django.urls import path

from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('post/new/', views.create, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('download', views.download_document, name='download_document'),
]
