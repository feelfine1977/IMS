from django.urls import path
from .views import inventory_list, per_product_view, add_product, update, delete, dashboard

urlpatterns = [
    path("", inventory_list, name="inventory_list"),
    path("per_product/<int:pk>", per_product_view, name="per_product"),
    path("product_update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name="delete"),
    path("add/", add_product, name="product_add"),
    path("dashboard/", dashboard, name="dashboard"),
]
