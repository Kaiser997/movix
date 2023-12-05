from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("activacion/", views.activacion, name="activacion"),
    path("login/", views.login, name="login"),

]