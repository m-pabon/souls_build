from django.urls import path

from . import views

app_name = "games"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:game_slug>", views.game_detail, name="games")  # new URL pattern
]