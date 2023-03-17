from django.urls import path
from plastic import views

urlpatterns = [
    path('', views.index, name='index'),
]
