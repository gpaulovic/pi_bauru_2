from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.UsuariosListView.as_view(), name='usuarios-list'),
    path('usuarios/<int:pk>/', views.UsuariosDetailView.as_view(), name='usuarios-detail'),
]
