from django.urls import path
from .views import DescartadoresListCreateView, DescartadoresRetrieveUpdateDestroyView

urlpatterns = [
    path('', DescartadoresListCreateView.as_view(), name='descartadores-list-create'),
    path('<int:pk>/', DescartadoresRetrieveUpdateDestroyView.as_view(), name='descartadores-retrieve-update-destroy'),
]
