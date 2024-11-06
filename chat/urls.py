from django.urls import path

from chat import views

urlpatterns = [
    path("<int:id>/", views.chat, name="chat"),
    path("<int:id1>/<int:id2>/", views.chat_new, name="chat_new"),
    path("<int:id>/<int:id1>/<int:id2>/", views.chat_mod, name="chat_mod"),
    path('logout/', views.logout_view, name='logout'),
]