from django.urls import path

from drogasil.views import search

urlpatterns = [
    path("search/", view=search, name="search"),
]
