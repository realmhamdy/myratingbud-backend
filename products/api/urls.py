from django.urls import path

from products.api import views

app_name = "api"

urlpatterns = [
    path("rate/", views.RateProductView.as_view(), name="rate_product"),
    path("compare/", views.CompareProductsView.as_view(), name="compare_products")
]
