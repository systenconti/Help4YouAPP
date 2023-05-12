from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path(
        "get_services/<int:profession_id>/",
        views.get_services_view,
        name="get_services",
    ),
]
