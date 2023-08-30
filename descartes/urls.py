from django.urls import path
from .views import (
    DescartesListCreateView,
    DescartesRetrieveUpdateDestroyView,
    save,
    update,
    delete,
)

app_name = "descartes"

urlpatterns = [
    path("", DescartesListCreateView.as_view(), name="home-descartes"),
    path("save/", save, name="save-descartes"),
    path("editar/<int:pk>/", DescartesRetrieveUpdateDestroyView.as_view(), name="editar-descartes"),
    path("update/<int:id>/", update, name="update-descartes"),
    path("delete/<int:id>/", delete, name="delete-descartes"),
]
