from django.urls import include, path

from . import views

app_name = "games"
urlpatterns = [
    path("<str:game_slug>/", views.game_detail, name="game_detail"),
    path("<str:game_slug>/weapons/", include("weapons.urls"))
]