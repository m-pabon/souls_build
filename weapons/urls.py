from django.urls import path

from . import views

app_name = "weapons"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<str:pk>/", views.DetailView.as_view(), name="detail"),
]