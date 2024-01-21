from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hlavnistranka'),
	path('form', views.form, name='formular'),
]