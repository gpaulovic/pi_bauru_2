from django.urls import path
from .views import (
    EcopontosListCreateView,
    EcopontosRetrieveUpdateDestroyView,
    create_ecoponto,
    ecopontos_detail,
)

app_name = "ecopontos"

urlpatterns = [
    path("", EcopontosListCreateView.as_view(), name="home-ecopontos"),
    path("create/", create_ecoponto, name="create-ecopontos"),
    path("detail/<int:pk>/", ecopontos_detail, name="detail-ecopontos"),
    path("detail/update/<int:pk>/", EcopontosRetrieveUpdateDestroyView.as_view(), name="update-ecopontos"),
]
