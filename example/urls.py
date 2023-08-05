# djangotemplates/example/urls.py

from django.urls import path
from example import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('register', views.register, name='register'),
    path('selection', views.selection, name='selection'),
    path('dataset', views.dataset, name='dataset'),
]