from django.urls import path

from djangoProject2.article import views

urlpatterns = [
    path('', views.index),
]
