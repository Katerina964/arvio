from django.urls import path

from . import views


app_name = "app"
urlpatterns = [
    path("get_property_id", views.get_property_id, name="get_property_id"),
    path("get_pdf", views.get_pdf, name="get_pdf"),
]
