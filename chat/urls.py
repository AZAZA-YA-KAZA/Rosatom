from django.urls import path

from chat import views

urlpatterns = [
    path("<int:id>/", views.chat, name="chat"),
    path("<int:id1>/<int:id2>/", views.chat_new, name="chat_new"),
    path('logout/', views.logout_view, name='logout'),
]