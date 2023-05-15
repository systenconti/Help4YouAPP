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
    path("confirm/", views.confirm_view, name="confirm"),
    path("confirm/success/", views.success_view, name="success"),
    path("confirm/dismiss/", views.dismiss_view, name="dismiss"),
]
