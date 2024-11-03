from django.urls import path

from chat import views

urlpatterns = [
    path("<int:id>/", views.chat),
    path('logout/', views.logout_view, name='logout'),
]