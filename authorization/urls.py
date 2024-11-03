from django.urls import path

from authorization import views

urlpatterns = [
    path('', views.authotiz)
]