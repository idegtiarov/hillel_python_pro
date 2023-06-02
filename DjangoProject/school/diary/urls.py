from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.RegisterCreateView.as_view(), name='register'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout, name="logout"),
    path("week/", views.DaysList.as_view(), name="my_week"),
    path("day/<int:pk>/", views.my_day, name="week_day"),
    path("day/<int:pk>/add_note/", views.NoteFormView.as_view(), name="new_note"),
]
