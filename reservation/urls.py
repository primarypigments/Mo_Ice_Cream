from . import views
from django.urls import path


urlpatterns = [
    path("", views.reservation_page, name="reservation_page"),
    path(
        "edit_reservation/<int:id>/",
        views.edit_reservation,
        name="edit_reservation"
    ),
    path(
        "delete_reservation/<int:id>/",
        views.delete_reservation,
        name="delete_reservation"
    ),
    path(
        "profile/",
        views.profile,
        name="profile"
    ),
]
