from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("week/", views.my_week, name="my_week"),
    path("day/<int:week_day_id>/note/<int:note_id>", views.my_day, name="week_day"),

]
