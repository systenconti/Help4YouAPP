from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path(
        "get_services/<int:profession_id>/",
        views.get_services_view,
        name="get_services",
    ),
    path("services/", views.services_view, name="services"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
]
