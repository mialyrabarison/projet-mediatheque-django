from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("bibliothecaire/", views.menu_bibliothecaire, name="menu_bibliothecaire"),
    path("membre/", views.menu_membre, name="menu_membre"),
    path("medias/", views.liste_medias, name="liste_medias"),
    path("membres/", views.liste_membres, name="liste_membres"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("bibliothecaire/", views.menu_bibliothecaire, name="menu_bibliothecaire"),
    path("membre/", views.menu_membre, name="menu_membre"),
    path("medias/", views.liste_medias, name="liste_medias"),
    path("membres/", views.liste_membres, name="liste_membres"),

    # nouvelles routes CRUD membres
    path("membres-page/", views.liste_membres_page, name="liste_membres_page"),
    path("membres/ajouter/", views.ajouter_membre, name="ajouter_membre"),
    path("membres/modifier/<int:membre_id>/", views.modifier_membre, name="modifier_membre"),
    path("membres/supprimer/<int:membre_id>/", views.supprimer_membre, name="supprimer_membre"),
]
