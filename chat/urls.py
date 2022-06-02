from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('chat/<str:username>/', views.join_chat, name='join_chat'),
    path('chat/new/<str:username>/', views.new_message, name='new_message'),
]