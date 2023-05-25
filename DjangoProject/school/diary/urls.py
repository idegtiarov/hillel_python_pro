from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("week/", views.DaysList.as_view(), name="my_week"),
    path("day/<int:pk>/", views.DayDetail.as_view(), name="week_day"),
    path("day/<int:pk>/add_note/", views.NoteFormView.as_view(), name="new_note"),
]
