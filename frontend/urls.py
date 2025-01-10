from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Contoh rute ke fungsi 'home' di views
]
