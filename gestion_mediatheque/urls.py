from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("bibliothecaire/", views.menu_bibliothecaire, name="menu_bibliothecaire"),
    path("membre/", views.menu_membre, name="menu_membre"),
    path("medias/", views.liste_medias, name="liste_medias"),
    path("membres/", views.liste_membres, name="liste_membres"),
]