from django.urls import path
from . import views

app_name = 'echo'

urlpatterns = [
    path('',views.index,name='index'),
    path('image',views.image,name='image'),
]
