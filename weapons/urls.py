from django.urls import path

from . import views

app_name = "weapons"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("<str:weapon_id>/", views.weapon_detail, name='detail')
]
